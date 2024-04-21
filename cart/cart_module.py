from product.models import Product

CART_SESSION_ID = "cart"


class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(CART_SESSION_ID)
        if not cart:
            cart = self.session[CART_SESSION_ID] = {}
        self.cart = cart

    def uniqe_id_generator(self, id, color, size):
        resualt = f"{id}+{color}+{size}"
        return resualt

    def __iter__(self):
        cart = self.cart.copy()
        for iteam in cart.values():
            iteam["product"] = Product.objects.get(id=int(iteam["id"]))
            iteam["total"] = int(iteam['quantity']) * int(iteam['price'])
            yield iteam

    def add(self, product, size, color, quantity):
        print(product.price)
        uniqe = self.uniqe_id_generator(product.id, color, size)
        if uniqe not in self.cart:
            self.cart[uniqe] = {'quantity': 0, 'price': str(product.price), "color": color, "size": size,
                                "id": str(product.id)}
        self.cart[uniqe]['quantity'] += int(quantity)
        self.session.modified = True
