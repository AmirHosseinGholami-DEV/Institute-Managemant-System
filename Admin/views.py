# Import necessary modules and models
from Logo.models import Logo_Database
from Rhetorical.models import Rhetorical_Database
from LifeStyle.models import Life_Style_Database
from MentalHealth.models import Mental_Health_Database
from Messages.models import Contact_Database
from .models import Student_Database
from Teacher.models import Teacher
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import DatabaseForm, TeacherForm
from django.contrib.auth.decorators import login_required


# View to display and handle the student list
@login_required  # Ensure only logged-in users can access this view
def Student_List(request):
    if request.method == 'POST':
        # If the form is submitted, process the data
        form = DatabaseForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('Admin Student')  # Redirect to the student list page
    else:
        form = DatabaseForm()  # Display an empty form for GET requests

    # Retrieve all student records from the database
    contacts = Student_Database.objects.all()
    return render(request, 'Admin/Student.html', {'contacts': contacts, 'form': form})


# View to delete a student record
@login_required
def delete_Student_List(request, contact_id):
    # Retrieve the student record or return a 404 error if not found
    contact = get_object_or_404(Student_Database, id=contact_id)
    contact.delete()  # Delete the record
    return HttpResponseRedirect(reverse('Admin Student'))  # Redirect to the student list page


# View to display the logo list
@login_required
def Logo_List(request):
    # Retrieve all logo records from the database
    contacts = Logo_Database.objects.all()
    return render(request, 'Admin/Logo.html', {'contacts': contacts})


# View to delete a logo record
@login_required
def delete_Logo_List(request, contact_id):
    # Retrieve the logo record or return a 404 error if not found
    contact = get_object_or_404(Logo_Database, id=contact_id)
    contact.delete()  # Delete the record
    return HttpResponseRedirect(reverse('Admin Logo'))  # Redirect to the logo list page


# View to display the rhetorical list
@login_required
def Rhetorical_List(request):
    # Retrieve all rhetorical records from the database
    contacts = Rhetorical_Database.objects.all()
    return render(request, 'Admin/Rhetorical.html', {'contacts': contacts})


# View to delete a rhetorical record
@login_required
def delete_Rhetorical_List(request, contact_id):
    # Retrieve the rhetorical record or return a 404 error if not found
    contact = get_object_or_404(Rhetorical_Database, id=contact_id)
    contact.delete()  # Delete the record
    return HttpResponseRedirect(reverse('Admin Rhetorical'))  # Redirect to the rhetorical list page


# View to display the lifestyle list
@login_required
def Life_Style_List(request):
    # Retrieve all lifestyle records from the database
    contacts = Life_Style_Database.objects.all()
    return render(request, 'Admin/Life Style.html', {'contacts': contacts})


# View to delete a lifestyle record
@login_required
def delete_Life_Style_List(request, contact_id):
    # Retrieve the lifestyle record or return a 404 error if not found
    contact = get_object_or_404(Life_Style_Database, id=contact_id)
    contact.delete()  # Delete the record
    return HttpResponseRedirect(reverse('Admin Life Style'))  # Redirect to the lifestyle list page


# View to display the physical education list
@login_required
def Phisical_Education_List(request):
    # Retrieve all mental health records (used for physical education) from the database
    contacts = Mental_Health_Database.objects.all()
    return render(request, 'Admin/Phisical Education.html', {'contacts': contacts})


# View to delete a physical education record
@login_required
def delete_Phisical_Education_List(request, contact_id):
    # Retrieve the mental health record or return a 404 error if not found
    contact = get_object_or_404(Mental_Health_Database, id=contact_id)
    contact.delete()  # Delete the record
    return HttpResponseRedirect(reverse('Admin Phisical Education'))  # Redirect to the physical education list page


# View to display the contact list
@login_required
def Contact_List(request):
    # Retrieve all contact records from the database
    contacts = Contact_Database.objects.all()
    return render(request, 'Admin/Cantact.html', {'contacts': contacts})


# View to delete a contact record
@login_required
def delete_Contact_List(request, contact_id):
    # Retrieve the contact record or return a 404 error if not found
    contact = get_object_or_404(Contact_Database, id=contact_id)
    contact.delete()  # Delete the record
    return HttpResponseRedirect(reverse('Admin Contact'))  # Redirect to the contact list page


# View to display and handle the teacher list
@login_required
def Teacher_List(request):
    if request.method == 'POST':
        # If the form is submitted, process the data
        form = TeacherForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('Admin Teacher')  # Redirect to the teacher list page
    else:
        form = TeacherForm()  # Display an empty form for GET requests

    # Retrieve all teacher records from the database
    contacts = Teacher.objects.all()
    return render(request, 'Admin/Teacher.html', {'contacts': contacts, 'form': form})


# View to delete a teacher record
@login_required
def delete_Teacher_List(request, contact_id):
    # Retrieve the teacher record or return a 404 error if not found
    contact = get_object_or_404(Teacher, id=contact_id)
    contact.delete()  # Delete the record
    return HttpResponseRedirect(reverse('Admin Teacher'))  # Redirect to the teacher list page


# View to handle user login
def login_view(request):
    if request.method == 'POST':
        # If the form is submitted, process the data
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Authenticate the user
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)  # Log the user in
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("Admin Logo")  # Redirect to the admin logo page
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()  # Display an empty form for GET requests

    return render(request, "Admin/Login.html", {"form": form})