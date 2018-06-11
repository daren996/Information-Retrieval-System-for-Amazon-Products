# Create your models here.

from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
    email = models.EmailField()

    def __unicode__(self):
        return self.name


class Tag(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class Product(models.Model):
    P_id = models.IntegerField(null=False)
    title = models.TextField(null=False)
    url = models.URLField(null=False)
    photo = models.URLField(null=True)
    category = models.TextField(null=True)
    price = models.CharField(max_length=20, null=True)
    star = models.CharField(max_length=20, null=True)
    description = models.TextField(null=True)
    details = models.TextField(null=True)

    def __unicode__(self):
        return self.P_id


class User_1(models.Model):
    Email = models.IntegerField(null=False)

    Sex = models.IntegerField(null=True)
    first_name_1 = models.TextField(null=False)
    last_name_1 = models.TextField(null=False)

    Password = models.CharField(max_length=20, null=True)
    Years = models.IntegerField(null=False)
    Month = models.IntegerField(null=False)
    days = models.IntegerField(null=False)

    first_name_2 = models.TextField(null=False)
    last_name_2 = models.TextField(null=False)
    company = models.TextField(null=False)
    Adress = models.TextField(null=False)
    Adress_line_2 = models.TextField(null=False)
    city = models.CharField(max_length=20, null=True)
    state = models.CharField(max_length=20, null=True)
    Zip = models.CharField(max_length=20, null=True)
    country = models.CharField(max_length=20, null=True)
    aditionalInfo = models.TextField(null=False)
    phone = models.IntegerField(null=False)
    mobile = models.IntegerField(null=False)

    def __unicode__(self):
        return self.Email


class UserProd(models.Model):
    Email = models.IntegerField(null=False)
    Item = models.TextField(null=True)

    def __unicode__(self):
        return self.Email
