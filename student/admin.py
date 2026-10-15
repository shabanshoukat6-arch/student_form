from django.contrib import admin
from student.models import Profile
# Register your models here.

@admin.register(Profile)
class Profilemodel(admin.ModelAdmin):

    list_display = [
            'Name',
            'Date_Of_Birth',
            'Gender',
            'Locality',
            'City',
            'Pin',
            'Choose_Your_State',
            'Mobile',
            'Email',
            'Job_City',
            'profile_image',
            'my_file'
        ]
 