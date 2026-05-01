from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
import random
from product_app.models import *
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

def signin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully signed In")
            return redirect('home')
        else:
            messages.error(request, "Invalid credentials, Try again")
            return redirect('signin')
    return render(request, "signin.html")

def signup(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('pass')
        confirm_password = request.POST.get('cpass')
        print(f"Form password: {password}")
        
        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect('signup')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exist, Try another!")
            return redirect('signup')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exist, Try another!")
            return redirect('signup')
        
        otp = random.randint(10000, 99999)
        
        request.session['otp'] = otp
        request.session['temp_password'] = password
        
        request.session['registration_data'] = {
            'username':username,
            'fname':fname,
            'lname':lname,
            'email':email,
        }
        
        send_mail(
            'Your OTP Code',
            f'Your Ecommerce Website OTP is: {otp}',
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )
        messages.success(request, "OTP has been sent to your email.")
        return redirect('verify_otp')
        
    return render(request, "signup.html")

def verify_otp(request):
    session_otp = request.session.get("otp")
    registration_data = request.session.get('registration_data')
    temp_password = request.session.get("temp_password")
    if request.method == "POST":
        entered_otp = request.POST.get('otp')
        if str(entered_otp) == str(session_otp):
            
            user = User.objects.create(
                username=registration_data['username'],
                first_name=registration_data['fname'],
                last_name=registration_data['lname'],
                email=registration_data['email'],
            )
            user.set_password(temp_password)
            user.save()
            
            del request.session['otp']
            del request.session['registration_data']
            
            messages.success(request, "Your Account has been created successfully!")
            return redirect('signin')
        else:
            messages.error(request, "Invalid OTP! Please try again")
            return redirect('verify_otp')
              
    return render(request, "verifyotp.html")

def logout_view(request):
    logout(request)
    return render(request, "signin.html")


def home(request):
    data = {}
    category = request.GET.get('category')
    if category:
        all_products = Product.objects.filter(category=category)
    else:
        all_products = Product.objects.all()

    data = {
        'all_products':all_products
    }
    return render(request, "index.html", data)

def shop(request):
    products = Product.objects.all()
    product_per_page = Paginator(products, 1) # first parameter is used for "What to display" and 2nd parameter is used how much items you want to display per page
    page_number = request.GET.get('page')
    final_product = product_per_page.get_page(page_number)
    
    return render(request, "shop.html", {'final_product':final_product})

@login_required(login_url="/signin/")
def cart(request):
    data = {}
    
    cart_item = Cart.objects.filter(user=request.user)
    total_cost = sum(item.total_price() for item in cart_item)
    
    data = {
        'cart_item': cart_item, 
        'total_cost':total_cost,
    }
    
    return render(request, "cart.html", data)

@csrf_exempt
@login_required(login_url="/signin/")
def add_to_cart(request, product_id):
    qty = request.GET.get('quantity', '1')
    qty = int(qty)
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += qty
    else:
        cart_item.quantity = qty
    cart_item.save()
    return redirect('cart')

@login_required
def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(Cart, id=cart_item_id, user=request.user)
    cart_item.delete()
    return redirect('cart')
@login_required(login_url="/signin/")
def checkout_view(request):
    data = {}
    user = request.user
    cart_items = Cart.objects.filter(user=user)
    total_price = sum(item.total_price() for item in cart_items)
    
    if request.method == "POST":  
        checkout = Checkout(
            user=user, 
            total_price=total_price,
            first_name = request.POST.get('fname'),
            last_name = request.POST.get('lname'),
            email = request.POST.get('email'),
            mobile = request.POST.get('mobile'),
            address_line1 = request.POST.get('address1'),
            address_line2 = request.POST.get('address2'),
            country = request.POST.get('country'),
            city = request.POST.get('city'),
            state = request.POST.get('state'),
            zip_code = request.POST.get('zipcode'),
            )
        checkout.save()
        cart_items.delete()
        messages.success(request, "Order placed successfully")

    data = {
        'cart_items':cart_items,
        'total_price':total_price,
    }
    return render(request, "checkout.html", data)

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        send_mail(
            subject,
            message,
            email,
            [config('EMAIL_HOST_USER')],
            fail_silently=False,
        )
        messages.success(request, "Email Sent Successfully")

    return render(request, "contact.html")

def details(request, product_ref):
    product = get_object_or_404(Product, product_slug=product_ref)
    
    return render(request, "detail.html", {'product':product})

