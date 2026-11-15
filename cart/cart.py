import json
from main.models import Product, CustomerDeliveryInfo



class Cart:
    def __init__(self, request):
        self.session = request.session
        self.request = request

        cart = self.session.get('session_key')

        if 'session_key' not in self.session:
            cart = self.session['session_key'] = {}

        self.cart = cart

    def _save_cart(self):
        self.session.modified = True

        if self.request.user.is_authenticated:
            CustomerDeliveryInfo.objects.filter(
                user_id=self.request.user.id
            ).update(
                shopping_cart=json.dumps(self.cart)
            )

    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = str(quantity)

        if product_id not in self.cart:
            self.cart[product_id] = int(product_qty)

        self._save_cart()

    def db_add(self, product, quantity):
        product_id = str(product)
        product_qty = str(quantity)

        if product_id not in self.cart:
            self.cart[product_id] = int(product_qty)

        self._save_cart()

    def delete(self, product):
        product_id = str(product)

        if product_id in self.cart:
            del self.cart[product_id]

        self._save_cart()

    def __len__(self):
        return len(self.cart)

    def get_prods(self):
        product_ids = self.cart.keys()

        products = Product.objects.filter(
            id__in=product_ids
        )

        return products

    def get_quants(self):
        return self.cart

    def get_total(self):
        product_ids = self.cart.keys()

        products = Product.objects.filter(
            id__in=product_ids
        ).only(
            'id',
            'price',
            'sale_price',
            'is_sale'
        )

        total = 0

        for product in products:
            quantity = self.cart.get(str(product.id), 0)

            if product.is_sale:
                total += product.sale_price * quantity
            else:
                total += product.price * quantity

        return total