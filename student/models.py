from django.db import models


class StudentRegister(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    name = models.CharField(max_length=40)
    email_id = models.EmailField(max_length=254, unique=True)
    mobile_number = models.CharField(max_length=40)
    age = models.CharField(max_length=10, null=True)
    gender = models.CharField(max_length=10, null=True, choices=GENDER_CHOICES)
    address = models.TextField(null=True)
    photo = models.ImageField(upload_to='uploads/', null=True, blank=True)

    previous_class = models.CharField(max_length=20, null=True)
    session_year = models.CharField(max_length=20, null=True)
    current_class = models.CharField(max_length=20, null=True)
    current_session_year = models.CharField(max_length=20, null=True)

    class Meta:
        db_table = "studentRegister"

    def __str__(self):
        return '{} {} '.format(self.name, self.email_id)