from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    COUNTRY_CHOISE = [
        ("UZB", "UZBEKISTAN"),
        ("KAZ", "KAZAKHSTAN"),
        ("KGZ", "KIRGYIZSTAN"),
    ]
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address1 = models.CharField(max_length=250,  blank=True, null=True)
    address2 = models.CharField(max_length=250,  blank=True, null=True)
    country = models.CharField(max_length=3, choices=COUNTRY_CHOISE, default="UZB")
    city = models.CharField(max_length=50,  blank=True, null=True)
    state = models.CharField(max_length=50,  blank=True, null=True)
    zipcode = models.CharField(max_length=50,  blank=True, null=True)

    # USERNAME_FIELD = "email"
    # REQUIRED_FIELDS = []
    
class Category(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="images/", blank=True, null=True)

    def __str__(self):
        return self.title
    
class SubCategory(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="images/", blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title
    