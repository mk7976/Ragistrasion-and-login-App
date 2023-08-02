from django.shortcuts import render, redirect
from .models import User


# Create your views here
def Ragisterpage(request):
    return render(request, 'ragister.html')


def Ragister(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        user = User.objects.filter(Email=email)
        print(user)

        if user:
            msg = "You Are Already Ragistered"
            return render(request, 'ragister.html', {'msg': msg})

        else:
            if confirm_password == password:
                if len(password) == 8 and password.isalnum():
                    user1 = User.objects.create(Username=username, Email=email,
                                                Password=password, Confirm_password=confirm_password)
                    return render(request, 'login.html')
                else:
                    msg = " Make strong Password from Numbers and Alphabet With 8 Character length"
                    return render(request, 'ragister.html', {'msg': msg})

            else:
                msg = "Confirm Password and Password Does Not Match"
                return render(request, 'ragister.html', {'msg': msg})


def Loginpage(request):
    return render(request, 'login.html')


def Login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(Username=username)
        print(user)
        if len(user) > 0:
            user1 = User.objects.get(Username=username)
            if user1.Password == password:
                return render(request, 'home.html', {'username': username})

            else:
                return render(request, 'login.html', {'msg': " Password does not match"})


        else:
            return render(request, 'login.html', {'msg': "You Are Not Registered"})

# mac
# mah12345
