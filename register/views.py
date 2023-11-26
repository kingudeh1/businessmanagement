from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Person  # Import your Person model

def index(request):
    if request.method == 'POST':
        surname = request.POST.get('surname')
        middlename = request.POST.get('middlename')
        lastname = request.POST.get('lastname')
        faculty = request.POST.get('faculty')
        department = request.POST.get('department')
        sex = request.POST.get('sex')
        matric_number = request.POST.get('matric_number')
        level = request.POST.get('level')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        # Create a new Person object and save it to the database
        person = Person(
            surname=surname,
            middlename=middlename,
            lastname=lastname,
            faculty=faculty,
            department=department,
            sex=sex,
            matric_number=matric_number,
            level=level,
            email=email,
            phone=phone
        )
        person.save()
        messages.success(request, 'Babalola has confirmed your form,don`t register twice thank you.')


        # Redirect to a success page or any other page after successful submission
        return redirect('/')  # Change '/success/' to your desired URL

    return render(request, 'index.html')  # Replace 'your_template.html' with your actual template name
