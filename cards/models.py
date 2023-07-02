from django.db import models
from CardGenerator.settings import AUTH_USER_MODEL

# Create your models here.
class Detail(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    role = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    companyname = models.CharField(max_length=100)
    companyemail = models.EmailField()
    companycontact = models.CharField(max_length=100)
    companylogo = models.ImageField(upload_to='images/')
    website = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    
    created_at = models.DateTimeField(auto_now_add=True)
    created_for = models.ForeignKey(AUTH_USER_MODEL,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name + " " + self.companyname