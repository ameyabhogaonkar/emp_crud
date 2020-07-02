from django.shortcuts import render

# Create your views here.

def register(request):

    if request.method == 'POST':
        firstname=request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

    return render(request,'register.html')


