from django.urls import path
from . import views

urlpatterns = [
  
   
    path('create-firm/', views.CreateFirm.as_view()),
    path('create-client/', views.CreateClient.as_view()),
    path('create-prestation/', views.CreatePresta.as_view()),
    path('create-bill/', views.CreateBill.as_view()),


    path('edit-firm/', views.MyFirm.as_view()),
    path('my-bills/', views.MyBills.as_view()),
    path('bill/<int:pk>/',views.BillDetailView.as_view()),
    path('delete/<int:pk>/',views.BillDetailView.as_view()),
    path('edit-bill/<int:pk>/',views.BillDetailView.as_view()) 

]