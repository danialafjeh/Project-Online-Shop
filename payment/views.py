from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db import transaction
from cart.cart import Cart
from main.models import CustomerDeliveryInfo
from .models import Order, OrderItem



def create_order(request):
    if request.method == 'POST':

        if request.user.is_authenticated:
            cart = Cart(request)

            cart_products = cart.get_prods()
            quantity = cart.get_quants()

            delivery_info = CustomerDeliveryInfo.objects.get(
                user_id=request.user.id
            )

            user = request.user

            with transaction.atomic():

                total = 0

                new_order = Order.objects.create(
                    user=user,
                    full_name=delivery_info.full_name,
                    phone=delivery_info.phone,
                    email=user.email,
                    delivery_address=delivery_info.address,
                    amount_paid=0
                )

                for product in cart_products:

                    product_quantity = quantity.get(
                        str(product.id)
                    )

                    if product_quantity is None:
                        continue

                    if product.is_sale:
                        price = product.sale_price
                    else:
                        price = product.price

                    total += price * product_quantity

                    OrderItem.objects.create(
                        order=new_order,
                        user=user,
                        products=product,
                        quantity=product_quantity,
                        price=price
                    )

                new_order.amount_paid = total
                new_order.save(update_fields=['amount_paid'])

                CustomerDeliveryInfo.objects.filter(
                    user_id=user.id
                ).update(
                    shopping_cart=""
                )

            # Session خارج از تراکنش دیتابیس است؛
            # بنابراین فقط بعد از موفقیت تراکنش پاک می‌شود.
            for key in list(request.session.keys()):
                if key == 'session_key':
                    del request.session[key]

            messages.success(request, ('سفارش شما با موفقیت ثبت شد و در انتطار پرداخت است'))
            messages.success(request, ('از بخش "پیگیری سفارشات من" در حساب کاربری خود اقدام به پرداخت مبلغ نمایید'))

            return redirect('home')

        else:
            messages.error(request, ('ابتدا وارد حساب خود شوید'))

            return redirect('home')

    else:
        messages.error(request, ('دسترسی به این صفحه امکان پذیر نمی باشد'))

        return redirect('home')


def orders_tracking(request):
    if request.user.is_authenticated:

        active_orders = Order.objects.filter(
            user_id=request.user.id
        ).exclude(
            status__in=['canceled', 'Delivered']
        )

        canceled_orders = Order.objects.filter(
            user_id=request.user.id,
            status='canceled'
        )

        delivered_orders = Order.objects.filter(
            user_id=request.user.id,
            status='Delivered'
        )

        info = {
            'active_orders': active_orders,
            'canceled_orders': canceled_orders,
            'delivered_orders': delivered_orders
        }

        return render(request, 'orders_tracking.html', info)

    else:
        messages.error(request, ('ابتدا باید وارد حساب کاربری خود شوید'))

        return redirect('home')


def cancel_order(request, order_id):
    if request.user.is_authenticated:

        order = get_object_or_404(
            Order,
            id=order_id,
            user=request.user
        )

        order.status = 'canceled'
        order.save()

        messages.success(request, ('سفارش شما با موفقیت لغو گردید'))

        return redirect('orders_tracking')

    else:
        messages.error(request, ('دسترسی به این صفحه مجاز نمی باشد'))

        return redirect('home')


def order_details(request, pk):
    if request.user.is_authenticated:

        order = get_object_or_404(
            Order,
            id=pk,
            user=request.user
        )

        order_items = OrderItem.objects.filter(
            order_id=pk
        ).select_related(
            'products'
        )

        info = {
            'order': order,
            'order_items': order_items
        }

        return render(request, 'order_details.html', info)

    else:
        messages.error(request, ('ابتدا باید وارد حساب کاربری خود شوید'))

        return redirect('home')