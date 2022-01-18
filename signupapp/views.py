from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages

def signup(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        fname = request.POST['fname']
        lname = request.POST['lname']
        mail = request.POST['mail']
        passd = request.POST['passd']
        cpassd = request.POST['cpassd']
        
        #password validation
        if passd == cpassd:
            if User.objects.filter(username = uname).exists():
                #Username already exist
                print("Username already exist")
                messages.debug(request,"Username Already Taken")
                return redirect('signuppage')
            else:
                if User.objects.filter(email = mail).exists():
                    #Email Already exist
                    print("Email already exist")
                    messages.debug(request,"Email Already Taken")
                    return redirect('signuppage')
                else:
                    user = User(username = uname, first_name = fname,
                                last_name = lname, email = mail, 
                                password = passd)
                    messages.success(request,"User Successfully Added")            
                    user.save()
                    return redirect('loginpage')

        else:
            #Password Does not Match
            print("Passwords doesnot match")
            messages.debug(request,"Password Doesnot Match")
            return redirect('signuppage')
    else:
        return render(request,'signupapp/signup.html')