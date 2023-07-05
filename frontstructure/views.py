from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .forms import SignUpForm
from .models import Profile

# connect models and templates.
def home(request):
    return render(request, 'frontstructure/home.html', {})
def contact(request):
    return render(request, 'contact/contact.html', {})

def update_user_data(user):
    Profile.objects.update_or_create(user=user, defaults={'mob': user.profile.mob},)
def signup_views(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            # load the profile instance created by the signal
            user.save()
            raw_password = form.cleaned_data.get('password1')

            # login user after signing up
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)

            # redirect user to home page
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup/signup.html', {'form': form})

def login_views(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Replace 'home' with the desired URL name after successful login
    else:
        form = AuthenticationForm()
    return render(request, 'login/login.html', {'form': form})
