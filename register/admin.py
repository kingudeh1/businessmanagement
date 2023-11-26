from django.contrib import admin
from .models import Person
import csv
from django.http import HttpResponse





def export_as_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="people_data.csv"'

    writer = csv.writer(response)
    headers = ['surname', 'middlename', 'lastname', 'faculty', 'department','sex', 'matric_number', 'level', 'email', 'phone',]
    writer.writerow(headers)

    for person in queryset:
        row = [person.surname, person.middlename, person.lastname, person.faculty, person.department, person.sex, person.matric_number, person.level, person.email, person.phone,]
        writer.writerow(row)

    return response

export_as_csv.short_description = 'Export selected as CSV'

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('surname', 'middlename', 'lastname', 'faculty', 'department','sex', 'matric_number', 'level', 'email', 'phone',)
    actions = [export_as_csv]

