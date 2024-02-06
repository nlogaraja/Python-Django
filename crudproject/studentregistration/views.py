from django.shortcuts import render,redirect
from studentregistration.models import Register

# Create your views here.
def home(request):
    query=Register.objects.all()
    print(query)
    context={"data":query}
    return render(request,"home.html",context)

def register(request):
    if request.method=="POST":
        fullname=request.POST.get('fullname')
        email=request.POST.get('email')
        age=request.POST.get('age')
        course=request.POST.get('course')
        print(fullname,email,age,course)
        query = Register(name=fullname,email=email, age=age, course=course)
        query.save()
    
    query=Register.objects.all()
    
    context={"data":query}    
    return render(request,"home.html",context)

#update function
def update(request,id):
    if request.method=="POST":
        fullname=request.POST.get('fullname')
        email=request.POST.get('email')
        age=request.POST.get('age')
        course=request.POST.get('course')
        edit=Register.objects.get(id=id)
        edit.name=fullname
        edit.email=email
        edit.age = age
        edit.course=course
        edit.save()
        return redirect("/")

    data=Register.objects.get(id=id)
    context={"data":data}
    return render(request,"update.html",context)

#delete function
def deletedata(request,id):
    data=Register.objects.get(id=id)
    data.delete()
    return redirect("/")
