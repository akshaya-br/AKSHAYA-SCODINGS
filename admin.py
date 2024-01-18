from django.contrib import admin


from .models import *
# Register your models here.





admin.site.register(Tenant_Register)
admin.site.register(Owner_Register)
admin.site.register(Add_properties)

admin.site.register(Message)