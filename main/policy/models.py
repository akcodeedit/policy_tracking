from django.contrib.auth.models import User
from django.db import models

# status_type={
# ("claimed","claimed"),
# ("rejected","rejected"),
# ("pending","pending")
# }
class Policy(models.Model):
    name = models.CharField(max_length=255)
    account_no = models.IntegerField()
    date = models.DateField()
    customer_id = models.IntegerField()
    branch = models.IntegerField()
    mobile = models.IntegerField()
    adhar_sub = models.IntegerField()
    adhar_nom = models.IntegerField()
    insured_name = models.CharField(max_length=255)
    nom_account = models.IntegerField()
    nom_name = models.CharField(max_length=255)
    bank = models.IntegerField()
    status = models.CharField(max_length=50)
    photo = models.FileField(upload_to='static/img')


