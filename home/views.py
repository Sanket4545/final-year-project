from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

# Create your views here.

def home(request):
    # return  HttpResponse("This is business....")
    return render(request,'home.html')

def assesment(request):
    # return  HttpResponse("This is business....")
    return render(request,'assesment.html')

def instructions(request):
    return render(request,'instructions.html')

def test(request):
    return render(request,'test.html')

def test_4(request):
    return render(request,'test_4.html')



def signup(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        if password1!=password2:
            message = "Password does not match"  
            data = {
            'message': message
            # Other context data
        }
            return render(request,'signup.html',data)
            
        else:
            my_user=User.objects.create_user(username,email, password1)
            my_user.save()
            return redirect('login')

    return render(request,'signup.html')


def loginpage(request):
    if request.method=='POST':
        email=request.POST.get('email')
        # username=request.POST.get('username')
        password1=request.POST.get('password')

        my_user=authenticate(request,username=email, password=password1)
        # print(my_user)
        if my_user is not None:
            login(request,my_user)
            print("Hey welcome")
            print(my_user.username)
            print(my_user.id)
            request.session['user_id'] = my_user.id
            request.session['username'] = my_user.username
            user_id = request.session.get('user_id')
            username = request.session.get('username')
            # print("your id is: ")
            # print(user_id)
            # print(username)
            return render(request,'user.html',{'user_id': user_id, 'username': username})
        else:
            print("error")
            message1 = "Email Id and password not match please enter right email id and password or create account"  
            data = {
            'message1': message1
            # Other context data
        }
            return render(request,'login.html',data) 
    
        # return redirect('home')
    return render(request,'login.html')


# def session_man(request):
#     # Retrieve user-specific data from session
#     user_id = request.session.get('user_id')
#     username = request.session.get('username')
#     print("your id is: ")
#     print(user_id)
#     print(username)
#     return render(request, 'home.html', {'user_id': user_id, 'username': username})

def about(request):
    return  HttpResponse("This is about....")

def services(request):
    return  HttpResponse("This is services....")
