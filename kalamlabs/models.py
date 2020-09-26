
# Create your models here.

from django.db import models


# Create your models here.
class KalamRegistration(models.Model):

    email = models.EmailField(max_length=25, unique=True,default='NA')
    school = models.CharField(max_length=25,default='unknown')
    name = models.CharField(max_length=255,default='anonymous')
    slot = models.CharField(max_length=100,default='00:00')
    date = models.CharField(max_length=100,default='000000')
    mobile = models.CharField(max_length=10, default='0000000000',unique=True)
    order_id = models.CharField(max_length=255,default='nor ordered',unique=True)
    payment = models.BooleanField(default=False)
    payment_amount = models.CharField(max_length=10,default=0)
    payment_id = models.CharField(max_length=255,default='',unique=True)
    signature = models.CharField(max_length=255,default='',unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name','school','mobile','payment','payment_id']

    def __str__(self):
        return self.name


class BookAFreeTrial(models.Model):
    email = models.EmailField(max_length=25, unique=True, default='NA')
    school = models.CharField(max_length=25, default='unknown')
    name = models.CharField(max_length=255, default='anonymous')
    slot = models.CharField(max_length=100, default='00:00')
    date = models.CharField(max_length=100, default='000000')
    mobile = models.CharField(max_length=10, default='0000000000', unique=True)

    def __str__(self):
        return self.name

class GeTInTouch(models.Model):
    email = models.EmailField(max_length=25, unique=True, default='NA')

    def __str__(self):
        return self.email
