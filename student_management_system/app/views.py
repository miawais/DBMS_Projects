from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from app.models import Customer
from django.views import View

    # Create your views here.
    # def home(request):
    #     return render(request, 'signup_or_login.html')

class Signup(View):
    def get(self, request):
        return render(request, 'signup_or_login.html')
        
    def post(self, request):
        postData = request.POST
        name = postData.get('name')
        email = postData.get('email')
        password = postData.get('password')

        print("\n\n\n", name, email, password, "\n\n\n")
                
        error_message = None
                
        values = {"name" : name,
                    "email" : email,
                    "password" : password}
        customer = Customer(name = name,
                                email = email,
                                password = password)
        error_message = self.validations(customer)
                # saving
        if not error_message:
            customer.password = make_password(customer.password)
            customer.register()
            print("\n\n\ncustomer saved\n\n\n")
            return redirect('signup_or_login')
        else:
            return render(request, 'signup_or_login.html', {'error':error_message, 'values':values})
            

    def validations(self, customer):
            # Form validations 
        error_message = None
        if not customer.name:
            error_message = "Name Reguired!!"
        elif len(customer.name)<=2:
            error_message = "Name must be longer than or equal to 2 characters!!"
        elif not customer.email:
            error_message = "Email Reguired!!"
        elif len(customer.email)<=2:
            error_message = "Email must be longer than or equal to 2 characters!!"
        elif customer.isExists():
            error_message="This Email already exists! Please try another one.."
        elif not customer.password:
            error_message = "Password is required!"
        elif len(customer.password)<=10:
            error_message =" Password should have at least 10 characteres."
            
        return error_message 



class Login(View):
        # return_url = None
    def get(self, request):
            # Login.return_url = request.GET.get('return_url')
        return render(request, 'signup_or_login.html')
    def post(self, request):
            # return login(request)
        email = request.POST.get('email')
        password = request.POST.get('password')
        error_message = None
        customer = Customer.get_customer_by_email(email)
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer_id'] = customer.id
                request.session['customer_email'] = customer.email
                    # if Login.return_url:
                    #     return HttpResponseRedirect(Login.return_url)
                    # else:
                    #     Login.return_url = None
                    #     return redirect('homepage')
                return redirect('home') 
            else:
                error_message = "Invalid email or password"
        else:
            error_message="Invalid Email or Password!"
            
        return render(request, 'signup_or_login.html', {'error':error_message})
            # print(email, password)
            
            
            
def logout(request):
    request.session.clear()
    return redirect('signup_or_login')



class home(View):
    def get(self, request):
        return render(request, 'index.html')