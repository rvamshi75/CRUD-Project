from django.shortcuts import render , HttpResponseRedirect
from .forms import StudentRegistration
from myapp.models import User
# Create your views here.
def add_show(request):
    if request.method=='POST':
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pw=fm.cleaned_data['password']
            reg=User(name=nm,email=em,password=pw)
            reg.save()
            return HttpResponseRedirect('/')

    else:
        fm=StudentRegistration()
    stud = User.objects.all()
    return render(request,'addandshow.html',{'form':fm,'stud':stud})
# to edit data
def update_data(request, id):
    if request.method =='POST':
        pi=User.objects.get(pk=id)
        fm=StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi=User.objects.get(pk=id)
        fm=StudentRegistration(instance=pi)
    return render(request,'update.html',{'form':fm})



# To delete the data
def delete_data(request, id):
    if request.method =='POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
