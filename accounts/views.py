from django.shortcuts import render
from django.contrib.auth import get_user_model, login, logout, authenticate
from django.shortcuts import redirect

User = get_user_model()

# Create your views here.
def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        status = request.POST.get('status')
        if password == password2:
            user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name, role=status)
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'accounts/signup.html')
    return render(request, 'accounts/signup.html')


def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('index')
        
    return render(request, 'accounts/login.html')

def logout_user(request):
    logout(request)
    return redirect('index')
   
def profile(request):
    return render(request, 'accounts/profile.html')
