from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError("Email must be fill")
        email = self.normalize_email(email=email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **kwargs):
        kwargs.setdefault("is_staff", True)
        kwargs.setdefault("is_superuser", True)

        if kwargs.get("is_staff") is not True:
            raise ValueError("Supperuser must be True is_staff")
        
        if kwargs.get("is_superuser") is not True:
            raise ValueError("Supperuser must be True is_superuser")
        
        return self.create_user(email=email,password=password, **kwargs)


class CustomUser(AbstractUser):
    COUNTRY_CHOISE = [
        ("UZB", "UZBEKISTAN"),
        ("KAZ", "KAZAKHSTAN"),
        ("KGZ", "KIRGYIZSTAN"),
    ]
    username = None
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

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    
class Category(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="images/", blank=True, null=True)

    def get_photo(self):
        try:
            return self.image.url
        except:
            return "data:image/png;base64,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"
    

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
    

    
class SubCategory(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="images/", blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "SubCategory"
        verbose_name_plural = "SubCategories"

class Offer(models.Model):
    title = models.CharField(max_length=100)
    percent = models.IntegerField(default=10)
    image = image = models.ImageField(upload_to="images/", blank=True, null=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Offer"
        verbose_name_plural = "Offers"


class Product(models.Model):
    SIZE_CHOISE = [
        ("XS", "EXTRA_SMALL"),
        ("S", "SMALL"),
        ("M", "MEDIUM"),
        ("L", "LARGE"),
        ("XL", "EXTRA LARGE"),
    ]
    title = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    sale = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    description = models.TextField(default="The description is not available")
    size = models.CharField(max_length=2, choices=SIZE_CHOISE, default="M")
    color = models.CharField(max_length=30, blank=True, null=True)
    info = models.TextField(default="The information is not available")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default=10)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def get_first_photo(self):
        if self.photos:
            try:
                return self.photos.first().image.url

            except:
                return "data:image/png;base64,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"    
            
            else:
                return "data:image/png;base64,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"
class Gallery(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="photos")
    image = models.ImageField(upload_to="images/")

    class Meta:
        verbose_name = "Photo"
        verbose_name_plural = "Photos"

class Partner(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to="images/", blank=True, null=True)
    
