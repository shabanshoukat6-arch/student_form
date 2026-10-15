from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

def Enter_Pin(value):
    if len(str(value))!=6:
        return ValidationError('The Pin code must be exactly 6 digits.')

US_STATES = [
    ('Alabama', 'Alabama'),
    ('Alaska', 'Alaska'),
    ('Arizona', 'Arizona'),
    ('Arkansas', 'Arkansas'),
    ('California', 'California'),
    ('Colorado', 'Colorado'),
    ('Connecticut', 'Connecticut'),
    ('Delaware', 'Delaware'),
    ('Florida', 'Florida'),
    ('Georgia', 'Georgia'),
    ('Hawaii', 'Hawaii'),
    ('Idaho', 'Idaho'),
    ('Illinois', 'Illinois'),
    ('Indiana', 'Indiana'),
    ('Iowa', 'Iowa'),
    ('Kansas', 'Kansas'),
    ('Kentucky', 'Kentucky'),
    ('Louisiana', 'Louisiana'),
    ('Maine', 'Maine'),
    ('Maryland', 'Maryland'),
    ('Massachusetts', 'Massachusetts'),
    ('Michigan', 'Michigan'),
    ('Minnesota', 'Minnesota'),
    ('Mississippi', 'Mississippi'),
    ('Missouri', 'Missouri'),
    ('Montana', 'Montana'),
    ('Nebraska', 'Nebraska'),
    ('Nevada', 'Nevada'),
    ('New Hampshire', 'New Hampshire'),
    ('New Jersey', 'New Jersey'),
    ('New Mexico', 'New Mexico'),
    ('New York', 'New York'),
    ('North Carolina', 'North Carolina'),
    ('North Dakota', 'North Dakota'),
    ('Ohio', 'Ohio'),
    ('Oklahoma', 'Oklahoma'),
    ('Oregon', 'Oregon'),
    ('Pennsylvania', 'Pennsylvania'),
    ('Rhode Island', 'Rhode Island'),
    ('South Carolina', 'South Carolina'),
    ('South Dakota', 'South Dakota'),
    ('Tennessee', 'Tennessee'),
    ('Texas', 'Texas'),
    ('Utah', 'Utah'),
    ('Vermont', 'Vermont'),
    ('Virginia', 'Virginia'),
    ('Washington', 'Washington'),
    ('West Virginia', 'West Virginia'),
    ('Wisconsin', 'Wisconsin'),
    ('Wyoming', 'Wyoming'),
]
# Create your models here.
class Profile(models.Model):

    Name = models.CharField(max_length=100)

    Date_Of_Birth = models.DateField(auto_now=False,auto_now_add=False)


    Gender = models.CharField(max_length=1)

    Locality = models.CharField(max_length=100)

    City= models.CharField(max_length=100)

    Pin = models.PositiveIntegerField(validators=[Enter_Pin],
                                      help_text='Enter 6 Digit Pin Code')
    
    Choose_Your_State = models.CharField(choices = US_STATES,max_length=100)
     
    Mobile  = models.CharField(max_length=10,
    validators= [RegexValidator(regex=r'^\d{10}$')],
    help_text='Enter 10_digit mobile number')
    
    Email = models.EmailField()

    Job_City = models.CharField(max_length=50)

    profile_image = models.ImageField(upload_to='profileimg',
    blank=True)
    
    my_file = models.FileField(upload_to='doc',blank=True)
