from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth import logout as django_logout

from .models import Contact, Withdraw, Transaction, Support, Profile


# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        contact = Contact(name=name, email=email, message=message)

        contact.save()
        # return redirect('contacts')

    return render(request, 'contact.html')

def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard.html')
    else:
        return redirect('login')


def deposit(request):
    if request.user.is_authenticated:
        return render(request, 'deposit.html')
    else:
        return redirect('login')

def transaction(request):
    if request.user.is_authenticated:
        invests = Transaction.objects.filter(user=request.user)
        # invests = invests2.order_by('sn')
        context = {
        'invests': invests
        }

        return render(request, 'transaction.html', context)

    else:
        return redirect('login')

# Investment 
def investment(request):
    if request.method == 'POST':
        username = request.POST['username']
        deposit_type = request.POST['deposit_type']
        amount = request.POST['amount']


        if int(amount) > request.user.balance.available_balance:
            messages.error(request, 'Insuffient Balance. Fund Your Account')
            return render(request, 'investment.html')

        newTransaction = Transaction(amount=amount, deposit_type=deposit_type, name = username, user = request.user)
        newTransaction.save()
        
        messages.success(request, 'Investment Started')
        return render(request, 'investment.html')
    
    return render(request, 'investment.html')




def notification(request):
    if request.user.is_authenticated:
        return render(request, 'notification.html')
    else:
        return redirect('login')

def support(request):
    if request.method == 'POST':
        username = request.POST['username']
        title = request.POST['title']
        message = request.POST['message']

        contact = Support(username=username, title=title, message=message)
        contact.save()

        messages.success(request, 'Your Ticket have been submitted. You will receive a response from our support team shortly')
        # return render(request, 'support-ticket.html')
    return render(request, 'support-ticket.html')


def referrals(request):
    if request.user.is_authenticated:
        return render(request, 'referrals.html')
    else:
        return redirect('login')

def profile(request):
    if request.method == 'POST':
        wallet = request.POST['wallet']
        address = request.POST['address']
        country = request.POST['country']
        phone = request.POST['phone']
        username = request.POST['username']

        support = Profile(username=username, address=address, country=country, wallet=wallet, phone=phone)

        support.save()
        
    return render(request, 'profile.html')


def forgot(request):
    return render(request, 'forgot.html')

def signin(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard.html')
    else:
        if request.method == 'POST':
            username = request.POST['email']
            password = request.POST['password']
            
            user = auth.authenticate(username=username, password=password)
            
            if user is not None:
                auth.login(request, user)
				# messages.success(request, 'You are now logged in')
                return redirect('dashboard')
            else:
                messages.error(request, 'Invalid Credentials')
                return redirect('signin')
        else:
            return render(request, 'signin.html')

def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        if password == password2:
			#Check email
            if User.objects.filter(username=username).exists():
                messages.error(request, 'It seems you are already registered signin')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name)
                user.save()
                
                subject = "Welcome to FX Pro Investment"
                message = f'Hello {username}, thank you for signing up to our platform'
                from_email = settings.EMAIL_HOST_USER
                to = [username]

                html_message = render_to_string('email.html', {'first_name': first_name})
                message = EmailMessage(subject, html_message, from_email, [to])
                message.content_subtype = 'html'
                # message.send()

                messages.success(request, 'You are now registered and can log in')
                return redirect('signin')
        else:
            messages.error(request, "Passwords do not Match")
            return redirect ('signup')
    else:
        return render(request, 'signup.html')

# def logout(request):
# 	if request.method == 'POST':
# 		auth.logout(request)
# 		return redirect ('signin')

def logout(request):
    django_logout(request)
    return redirect('index')

def withdraw(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            return render(request, 'withdraw.html')


        if request.method == 'POST':
            if hasattr(request.user, 'balance'):
                amount = request.POST['amount']
                wallet = request.POST['wallet']
                method = request.POST['method']
                username = request.POST['username']

                print(amount)

                if int(amount) > request.user.balance.available_balance:
                    messages.error(request, 'Insufficient Balance')
                    return redirect('withdraw')
                

                withdraw = Withdraw(amount=amount, wallet=wallet, username=username, method=method)

                withdraw.save()

                messages.success(request, 'Withdrawal Processing')
                return render(request, 'withdraw.html')
            else:
                messages.error(request, 'You Have not funded your account')
                return redirect('withdraw')
    else:
        return redirect('login')
