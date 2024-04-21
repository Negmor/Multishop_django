


CART_SESSION_ID="cart"

class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(CART_SESSION_ID)
        if not cart:
            cart = self.session[CART_SESSION_ID] = {}
        self.cart = cart

    def uniqe_id_generator(self, id, size, color):
        resualt = f"{id}+{color}+{size}"
        return resualt

    def add(self, proudct ,size , color , quantity):
        uniqe = self.uniqe_id_generator(proudct.id,size,color)
        if uniqe not in self.cart:
            self.cart[uniqe] = {'quantity': 0, 'price': str(proudct.price),"color": color ,"size":size, "id":proudct.id}
        self.cart[uniqe]['quantity'] += quantity
        self.session.modified = True
        self.save()


    """def __iter__(self):
        variant_ids = self.cart.keys()
        products = Variants.objects.filter(id__in=variant_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(variant.id)]['variant'] = variant"""





