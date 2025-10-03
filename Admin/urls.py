from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_view, name="Admin Login"),
    path("adminlogo/", views.Logo_List, name="Admin Logo"),
    path("adminlifestyle/", views.Life_Style_List, name="Admin Life Style"),
    path("adminphisicaleducation/", views.Phisical_Education_List, name="Admin Phisical Education"),
    path("adminrhetorical/", views.Rhetorical_List, name="Admin Rhetorical"),





    path("adminstudent/", views.Student_List, name="Admin Student"),
    path('adminstudent/delete/<int:contact_id>/', views.delete_Student_List, name='delete_Student_List'),


    path("adminteacher/", views.Teacher_List, name="Admin Teacher"),
    path('adminteacher/delete/<int:contact_id>/', views.delete_Teacher_List, name='delete_Teacher_List'),




    path("admincontact", views.Contact_List, name="Admin Contact"),
    path('adminlogo/delete/<int:contact_id>/', views.delete_Logo_List, name='delete_contact_Logo'),
    path('adminrhetorical/delete/<int:contact_id>/', views.delete_Rhetorical_List, name='delete_contact_Rhetorical'),
    path('adminlifestyle/delete/<int:contact_id>/', views.delete_Life_Style_List, name='delete_contact_Life_Style'),
    path('adminphisicaleducation/delete/<int:contact_id>/', views.delete_Phisical_Education_List, name='delete_contact_Phisical_Education'),
    path('admincontact/delete/<int:contact_id>/', views.delete_Contact_List, name='delete_contact'),
]
