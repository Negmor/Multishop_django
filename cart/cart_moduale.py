


CART_SESSION_ID="cart"

class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(CART_SESSION_ID)
        if not cart:
            cart = self.session[CART_SESSION_ID] = {}
        self.cart = cart

    def __iter__(self):
        variant_ids = self.cart.keys()
        products = Variants.objects.filter(id__in=variant_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(variant.id)]['variant'] = variant

    def add(self, variant, quantity):
        variant_id = str(variant.id)
        if variant_id not in self.cart:
            self.cart[variant_id] = {'quantity': 0, 'price': str(variant.price)}
        self.cart[variant_id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session.modified = True


# add to cart
def cart_add(request, variant_id):
    cart = Cart(request)
    variant = get_object_or_404(Variant, id=variant_id)
    form = CartAddForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(variant=variant, quantity=cd['quantity'])
    return redirect('cart:details')