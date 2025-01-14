from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages  # Message framework
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Vehicle, Customer


from datetime import datetime


# email
from django.core.mail import send_mail,EmailMessage
from django.template.loader import render_to_string
# Home View
@login_required(login_url='log_in')
def home(request):
    customer = None
    customer_email = None

    if request.user.is_authenticated:
        try:
            customer = Customer.objects.get(user=request.user)
            customer_email = customer.customer_email
            messages.success(request, "Welcome aboard!")
        except Customer.DoesNotExist:
            pass

    vehicles = Vehicle.objects.all()
    context = {
        'greeting': f"Welcome, {request.user.first_name or request.user.username}!",
        'vehicles': vehicles,
        'customer': customer,
        'customer_email': customer_email
    }
    return render(request, 'main/home.html', context)

# Customer Views
@login_required(login_url='log_in')
def previous_rentals(request):
    return render(request, 'customerView/prev_rentals.html')

@login_required(login_url='log_in')
def current_orders(request):
    vehicle_name = request.GET.get('vehicle_name', '')
    data = Customer.objects.all()
    return render(request, 'customerView/current_orders.html',{'data':data})

# Authentication Views
def register(request):
    if request.method == "POST":
        data = request.POST
        required_fields = ['fname', 'lname', 'username', 'email', 'password', 'confirm-password']
        if not all(field in data and data[field].strip() for field in required_fields):
            messages.error(request, "All fields are required.")
            return render(request, 'authenticate/register.html')

        f_name = data['fname']
        l_name = data['lname']
        username = data['username']
        email = data['email']
        password = data["password"]
        confirm_password = data["confirm-password"]

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return redirect('register')

        if password == confirm_password:
            try:
                validate_password(password)
                User.objects.create_user(
                    first_name=f_name,
                    last_name=l_name,
                    email=email,
                    username=username,
                    password=password
                )
                messages.success(request, "Your account has been registered.")
                return redirect('log_in')
            except ValidationError as e:
                for error in e.messages:
                    messages.error(request, error)
                return redirect('register')
        else:
            messages.error(request, "Password and confirm password do not match.")
            return redirect('register')

    return render(request, 'authenticate/register.html')

def log_in(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username or not password:
            messages.error(request, "Both username and password are required.")
            return redirect('log_in')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully.")
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('log_in')

    return render(request, 'authenticate/login.html')

def log_out(request):
    logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect('log_in')


def showdetails(request):
    return render(request,'customerView/showdetails.html')




def update(request,id):
    data = Customer.objects.get(id = id)
    if request.method == 'POST':
        name = request.POST['customer_firstname']
        add = request.POST['customer_address']
        email = request.POST['customer_email']
        mob = request.POST['customer_mobileno']

        data = Customer.objects.get(id=id)
        data.customer_firstname = name
        data.customer_address = add
        data.customer_email = email
        data.customer_mobileno = mob
        
        data.save()
        return redirect('current_orders')
    return render(request,'customerView/update.html',{'data':data})

def delete_data(request,ida):
    data = Customer.objects.get(id=ida)
    data.is_delete = True
    data.save()
    return redirect('current_orders')

@login_required(login_url='log_in')
def order(request):
    vehicle_name = request.GET.get('vehicle_name', '')
    if request.method == "POST":
        data = request.POST
        try:
            # Extract and process form data
            fname = data['fname']
            lname = data['lname']
            address = data['address']
            email = data['email']
            DOB = datetime.strptime(data['DOB'], '%Y-%m-%d').date()
            mob = data['mob']
            license = request.FILES['license']
            order_take_day = datetime.strptime(data['order_take_day'], '%Y-%m-%d').date()
            order_return_day = datetime.strptime(data['order_return_day'], '%Y-%m-%d').date()

            # Validate age
            current_date = datetime.now().date()
            age = current_date.year - DOB.year
            if (current_date.month, current_date.day) < (DOB.month, DOB.day):
                age -= 1

            if age < 0 or age > 100:
                messages.error(request, "Age should be between 0 and 100.")
                return redirect('order')

            # Validate order dates
            if order_take_day >= order_return_day:
                messages.error(request, "Order return day must be after the order take day.")
                return redirect('order')

            # Save customer data
            custo = Customer(
                customer_firstname=fname,
                customer_lastname=lname,
                customer_address=address,
                customer_email=email,
                customer_dob=DOB,
                customer_mobileno=mob,
                customer_license=license,
                order_take_day=order_take_day,
                order_return_day=order_return_day,
            )
            custo.full_clean()
            custo.save()

            # Send email confirmation
            subject = "Order Confirmation"
            message = render_to_string('customerView/msg.html', {'name': fname, 'date': current_date})
            from_email = 'red445992@gmail.com'
            recipient_list = [email]
            msg_email = EmailMessage(subject, message, from_email, recipient_list)
            msg_email.send(fail_silently=True)

            messages.success(request, "Order placed successfully!")
            return redirect('order') 
        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
            return redirect('order')

    return render(request, "customerView/order.html", {'vehicle_name': vehicle_name})