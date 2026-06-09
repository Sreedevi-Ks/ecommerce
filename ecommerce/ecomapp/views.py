from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User
from .models import Product
from .models import Cart
from .models import Order
from django.core.paginator import Paginator
def home(request):
    return render(request,'home.html')
def login(request):
    if request.method == "POST":

        email = request.POST.get('email')

        password = request.POST.get('password')
        if email == "admin@gmail.com" and password == "admin":
            request.session['admin'] = email

            return HttpResponse("""

                <script>

                    alert("Admin Login Successful");

                    window.location.href='/adminhome/';

                </script>

            """)

        try:

            user = User.objects.get(
                email=email,
                password=password
            )
            request.session['user'] = user.email

            return HttpResponse("""

                <script>

                    alert("Login Successful");

                    window.location.href='/userindex/';

                </script>

            """)

        except:

            return render(request, 'login.html', {
                'error': 'Invalid Email or Password'
            })
    return render(request,'login.html')
def register(request):
    return render(request,'register.html')
def ecomregister(request):
    if request.method == "POST":

        email = request.POST.get('email')

        password = request.POST.get('password')

        confirm_password = request.POST.get('confirm_password')
        if password == confirm_password:
            User.objects.create(
                email=email,
                password=password
            )
            return HttpResponse("""

                <script>

                    alert("Registration Successful");

                    window.location.href='/login/';

                </script>

            """)
        else:
            return render(request, 'register.html', {
                'error': 'Password does not match'
            })

    return redirect('register')
def userindex(request):
    if 'user' not in request.session:
        return redirect('login')
    return render(request,'userindex.html')

def adminhome(request):
    if 'admin' not in request.session:
        return redirect('login')
    return render(request,'adminhome.html')
def products(request):
    if 'user' not in request.session:

        return redirect('login')

    all_products = Product.objects.all()

    paginator = Paginator(all_products, 4)

    page_number = request.GET.get('page')

    page_obj = paginator.get_page(page_number)

    return render(request, 'products.html', {
        'page_obj': page_obj
    })
def cart(request):

    if 'user' not in request.session:

        return redirect('login')

    user_email = request.session['user']

    user = User.objects.get(email=user_email)

    cart_items = Cart.objects.filter(user=user)

    grand_total = 0

    for item in cart_items:

        item.total = item.product.price * item.quantity

        grand_total += item.total

    return render(request, 'cart.html', {

        'cart_items': cart_items,

        'grand_total': grand_total
    })
def addtocart(request, id):
    if 'user' not in request.session:

        return HttpResponse("""

            <script>

                alert('Please Login First');

                window.location.href='/login/';

            </script>

        """)
    user_email = request.session['user']

    user = User.objects.get(email=user_email)

    product = Product.objects.get(id=id)

    try:

        cart_item = Cart.objects.get(
            user=user,
            product=product
        )

        cart_item.quantity += 1

        cart_item.total_amount = (
            cart_item.quantity * product.price
        )

        cart_item.save()
    except:
        Cart.objects.create(

            user=user,

            product=product,

            quantity=1,

            total_amount=product.price
        )

    return HttpResponse("""

        <script>

            alert('Product Added Successfully');

            window.location.href='/products/';

        </script>

    """)

def profile(request):
    if 'user' not in request.session:

        return redirect('login')

    user_email = request.session['user']

    user = User.objects.get(email=user_email)

    return render(request, 'profile.html', {

        'user': user
    })
def addproduct(request):

    return render(request,'addproduct.html')


def saveproduct(request):

    if request.method == "POST":

        name = request.POST.get('name')

        price = request.POST.get('price')

        description = request.POST.get('description')

        image = request.POST.get('image')

        Product.objects.create(

            name=name,
            price=price,
            description=description,
            image=image
        )

        return HttpResponse("""

            <script>

                alert("Product Added Successfully");

                window.location.href='/addproduct/';

            </script>

        """)
def logout(request):

    request.session.flush()

    return HttpResponse("""

        <script>

            alert("Logout Successful");

            window.location.href='/';

        </script>

    """)
def adminproducts(request):

    if 'admin' not in request.session:

        return redirect('login')

    products = Product.objects.all()
    paginator = Paginator(products, 4)

    page_number = request.GET.get('page')

    page_obj = paginator.get_page(page_number)

    return render(request, 'adminproducts.html', {

        'page_obj': page_obj
    })
def deleteproduct(request, id):

    if 'admin' not in request.session:

        return redirect('login')



    product = Product.objects.get(id=id)

    product.delete()

    return HttpResponse("""

        <script>

            alert('Product Deleted Successfully');

            window.location.href='/adminproducts/';

        </script>

    """)
def checkout(request):

    if 'user' not in request.session:

        return redirect('login')

    payment_method = request.POST.get('payment')

    user_email = request.session['user']

    user = User.objects.get(email=user_email)

    cart_items = Cart.objects.filter(user=user)

    for item in cart_items:

        Order.objects.create(

            user=user,

            product=item.product,

            quantity=item.quantity,

            total=item.product.price * item.quantity,
            status="Placed",
            payment_method=payment_method
        )

    cart_items.delete()

    return HttpResponse("""

        <script>

            alert('Payment Successful & Order Placed');

            window.location.href='/orders/';

        </script>

    """)
def orders(request):


    if 'user' not in request.session:

        return redirect('login')



    user_email = request.session['user']

    user = User.objects.get(email=user_email)

    

    user_orders = Order.objects.filter(user=user)

    return render(request, 'orders.html', {

        'orders': user_orders
    })
def paymentpage(request):

    if 'user' not in request.session:

        return redirect('login')

    return render(request, 'payment.html')
def increase_quantity(request, id):

    cart_item = Cart.objects.get(id=id)

    cart_item.quantity += 1
    cart_item.total_amount = cart_item.quantity * cart_item.product.price

    cart_item.save()

    return redirect('cart')


def decrease_quantity(request, id):

    cart_item = Cart.objects.get(id=id)

    if cart_item.quantity > 1:

        cart_item.quantity -= 1
        cart_item.total_amount = cart_item.quantity * cart_item.product.price

        cart_item.save()

    return redirect('cart')
def remove_cart(request, id):

    
    item = Cart.objects.get(id=id)


    item.delete()


    return redirect('cart')
def adminorders(request):

    if 'admin' not in request.session:
        return redirect('login')

    orders = Order.objects.all()

    return render(request, 'adminorders.html', {
        'orders': orders
    })