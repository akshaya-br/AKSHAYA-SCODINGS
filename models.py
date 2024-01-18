from django.contrib.auth.models import User
from django.db import models
# Create your models here.


class Tenant_Register(models.Model):
    Tenant=models.ForeignKey(User,on_delete=models.CASCADE)
    Username=models.CharField(max_length=50,null=True)
    First_name=models.CharField(max_length=50,null=True)
    Email_id=models.EmailField(null=True)
    Tenant_type=models.CharField(max_length=50,null=True)
    Address=models.CharField(max_length=100,null=True)
    Document_proof=models.ImageField(null=True)
    Contact=models.CharField(max_length=10,null=True)
    Location=models.CharField(max_length=100,null=True)
    Password=models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.Username
    

class Owner_Register(models.Model):
    Owner=models.ForeignKey(User,on_delete=models.CASCADE)
    Username=models.CharField(max_length=50,null=True)
    First_name=models.CharField(max_length=50,null=True)
    Email_id=models.EmailField(null=True)
    Owner_type=models.CharField(max_length=50,null=True)
    Address=models.CharField(max_length=100,null=True)
    Document_proof=models.ImageField(null=True)
    Contact=models.CharField(max_length=10,null=True)
    Location=models.CharField(max_length=100,null=True)
    Password=models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.Username
    
    
class Add_properties(models.Model):
    user=models.ForeignKey(Owner_Register,on_delete=models.CASCADE)
    Property_title=models.CharField(max_length=1000,null=True)
    Property_description=models.CharField(max_length=1000,null=True)
    Property_type=models.CharField(max_length=100,null=True)
    Property_location=models.CharField(max_length=50,null=True)
    Property_area=models.CharField(max_length=50,null=True)
    Property_size=models.CharField(max_length=50,null=True)
    Property_rent_price=models.CharField(max_length=100,null=True)
    Property_features=models.CharField(max_length=100,null=True)
    Property_image=models.ImageField(null=True)
    def __str__(self):
        return self.Property_type
    
    
class Message(models.Model):
    Tenant_message=models.ForeignKey(Tenant_Register,on_delete=models.CASCADE)
    Owners_message=models.ForeignKey(Owner_Register,on_delete=models.CASCADE)

    Owner_name=models.CharField(max_length=100,null=True)
    Property_type=models.CharField(max_length=100,null=True)
    Name_of_the_user=models.CharField(max_length=100,null=True)
    Location=models.CharField(max_length=100,null=True)
    Owner_Messages=models.CharField(max_length=1000,null=True)
    Ownerreply=models.CharField(max_length=500,default='waiting for admin reply')
    def __str__(self):
        return self.Owner_name
    
    
    