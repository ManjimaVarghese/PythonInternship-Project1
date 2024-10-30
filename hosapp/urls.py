from django.urls import path
from .import views

urlpatterns = [
  
     
     path('', views.entry, name = 'entry'),
     path('adminpage', views.adminpage, name = 'adminpage'),
     path('newpatient', views.newpatient, name = 'newpatient'),
     path('viewpatientdetails', views.viewpatientdetails, name = 'viewpatientdetails'),
     path('viewdoctorupload', views.viewdoctorupload, name = 'viewdoctorupload'),
     path('patiententrypage', views.patiententrypage, name = 'patiententrypage'),
     path('docuploadpres', views.docuploadpres, name = 'docuploadpres'),
     path('docviewpres/', views.docviewpres, name = 'docviewpres'),
     path('patientviewpres/', views.patientviewpres, name = 'patientviewpres'),
     path('docviewpnt/',views.docviewpnt,name='docviewpnt'),
     path('doctorpage', views.doctorpage, name = 'doctorpage'),
     path('patientpage', views.patientpage, name = 'patientpage'),
     path('patientedit/',views.patientedit,name='patientedit'),
     path('save/',views.save,name='save'),
     path('delete/<int:id>/',views.delete,name='lete'),
     path('edit/<int:id>/',views.edit,name='edit'),
     path('update/<int:pk>',views.update,name='update'),
     path('savenew/',views.savenew,name='savenew'),
     path('updatenew/<int:pk>',views.updatenew,name='updatenew'),
     path('deletenew/<int:id>/',views.deletenew,name='deletenew'),
     path('editnew/<int:id>/',views.editnew,name='editnew'),


]