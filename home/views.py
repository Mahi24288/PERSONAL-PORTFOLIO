from django.shortcuts import render
from home.models import Contact

# Create your views here.
def home(request):
    context = {'name': 'mahesh', 'course': 'django'}
    return render(request, 'home.html', context)
    # return HttpResponse("this is my home page(/) ")


def about(request):
    return render(request, 'about.html')
    # return HttpResponse("this is my about page(/about)")


def contact(request):
    if request.method == "POST":
        # print("this is post")
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
        # print(name, email, phone, concern)
        ins = Contact( name=name, email=email, phone=phone, desc=desc)
        ins.save()
        print("the value is stored in db")
    return render(request, 'contact.html')
    # return HttpResponse("this is my contact page(/contact)")


def project(request):
    return render(request, 'project.html')
    # return HttpResponse("this is my projects(/project)")
