

# Create your views here.
from django.http import JsonResponse
from django.shortcuts import render,HttpResponse,redirect
from .forms import DataForm,userForm
from .models import Patient,Doctor
from django.shortcuts import render, redirect,get_object_or_404
from .forms import DataForm, DataFormNew


def adminpage(request):
    return render(request, 'hosapp/adminpage.html')
def entry(request):
    return render(request, 'hosapp/entry.html')
def patientpage(request):
    return render(request, 'hosapp/patientpage.html')

def docviewpres(request):
    data=Doctor.objects.all()
    return render(request,'hosapp/docviewpres.html',{'datas':data})

def patientviewpres(request):
    data=Doctor.objects.all()
    return render(request,'hosapp/patientviewpres.html',{'datas':data})




def doctorpage(request):
    return render(request, 'hosapp/doctorpage.html')


def patiententrypage(request):
    return render(request, 'hosapp/patiententrypage.html')


def docuploadpres(request):
    
    doctor_form = DataFormNew()
    return render(request, 'hosapp/docuploadpres.html', { 'doctor_form': doctor_form})






def newpatient(request):
    form = DataForm()
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'hosapp/newpatient.html', {'form': form})

def patientedit(request):
    data=Patient.objects.all()
    return render(request,'hosapp/patientedit.html',{'datas':data})

def docviewpnt(request):
    data=Patient.objects.all()
    return render(request,'hosapp/docviewpnt.html',{'datas':data})

def viewdoctorupload(request):
    data=Doctor.objects.all()
    return render(request,'hosapp/viewdoctorupload.html',{'datas':data})

def viewpatientdetails(request):
    data=Patient.objects.all()
    return render(request,'hosapp/viewpatientdetails.html',{'datas':data})


def save(request):
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            form.save()
            form=DataForm()
            data_value=Patient.objects.all()
            return render(request,'hosapp/patientedit.html',{'datas':data_value})
        else:
             return render(request,'hosapp/newpatient.html',{'form':form})
        
    else:
         return render(request,'hosapp/newpatient.html',{'form':form})
    
def update(request,pk=None):
     if request.method == 'POST':
        if pk is not None:
            instance = userForm.objects.get(pk=pk)
            form=DataForm(request.POST,instance=instance)
            if form.is_valid():
                form.save()
                return redirect('patientedit')
            else:
                return render(request,'hosapp/newpatient.html',{'form':form})
        else:
            return redirect('patientedit')
     else:
        return render(request,'hosapp/newpatient.html',{'form':form})
     
def delete(request,id):
    Patient.objects.filter(id = id).delete()
    return redirect(patientedit)

def edit(request,id):
    instance = get_object_or_404(Patient,id=id)
    form = DataForm(instance=instance)
    return render(request,'hosapp/newpatient.html',{'form':form,'instance':instance})


def savenew(request):
    if request.method == 'POST':
        form = DataFormNew(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            form=DataFormNew()
            data_value=Doctor.objects.all()
            return render(request,'hosapp/docviewpres.html',{'datas':data_value})
        else:
             return render(request,'hosapp/docuploadpres.html',{'form':form})
        
    else:
         return render(request,'hosapp/docuploadpres.html',{'form':form})
    


def updatenew(request,pk=None):
     if request.method == 'POST':
        if pk is not None:
            instance = Doctor.objects.get(pk=pk)
            form=DataFormNew(request.POST,instance=instance)
            if form.is_valid():
                form.save()
                return redirect(docviewpres)
            else:
                return render(request,'hosapp/docuploadpres.html',{'form':form})
        else:
            return redirect(docviewpres)
     else:
        return render(request,'hosapp/docuploadpres.html',{'form':form})
     


















     



def deletenew(request,id):
    Doctor.objects.filter(id = id).delete()
    return redirect(docviewpres)

def editnew(request,id):
    instance = get_object_or_404(Doctor,id=id)
    form = DataFormNew(instance=instance)
    return render(request,'hosapp/docuploadpres.html',{'form':form,'instance':instance})

            


def docuploadpres(request):
    form = DataFormNew()
    if request.method == 'POST':
        form = DataFormNew(request.POST)
        if form.is_valid():
           form.save()
    return render(request, 'hosapp/docuploadpres.html', {'form': form})
    