from django.shortcuts import render,redirect
from .models import*
from django.contrib.auth.models import auth,User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
# Create your views here.

def index(request):
    return render(request,'index.html')

def tenant_register(request):
    if request.method=='POST':
        user_names=request.POST['usernames']
        first_name=request.POST['firstname']
        email_id=request.POST['email_id']
        tenant_type=request.POST['tenantType']
        address=request.POST['address']
        
        document_proof=request.FILES['img_proof']
        contact_number=request.POST['contact']
        locations=request.POST['location']
        
        passwords=request.POST['password']
        confirm_password=request.POST['c_password']
        # user_approved=request.POST['user_appointment']

        if passwords==confirm_password:  
            user=None
            if User.objects.filter(username=user_names).exists():
                user=User.objects.get(username=user_names)
                if Tenant_Register.objects.filter(Tenant=user).exists():
                    print("already exists")
                    return render(request,'tenant/tenant_registration.html',{'key1':"EMAIL ID ALREADY EXISTS"})
            else:
                User.objects.create_user(username=user_names,password=passwords,email=email_id).save()
                user=User.objects.get(username=user_names)
            if user:
                if Tenant_Register.objects.filter(Username=user_names).exists():
                    print("uname already exists")
                    return render(request,'tenant/tenant_registration.html',{'key1':"EMAIL ID ALREADY EXISTS"})
                else:
                    user_save=Tenant_Register(Tenant=user,Username=user_names,First_name=first_name,Email_id=email_id,Tenant_type=tenant_type,Address=address,Document_proof=document_proof,Location=locations,Contact=contact_number,Password=passwords)
                    user_save.save()
                    print("saved")
                    return redirect(tenant_login)
                    # return render(request,'user_registration.html',{'key2':"SUCCESSFULLY SAVED"})
        else:
            return render(request,'tenant/tenant_registration.html',{'key1':'PASSWORD DOES NOT MATCH'})
    else:
        return render(request,'tenant/tenant_registration.html')
    return render(request,'tenant/tenant_registration.html')    

def tenant_homepage(request):
    return render(request,'tenant/tenant_homepage.html')

def tenant_login(request):
    if request.method=='POST':
        username=request.POST['user_name']
        password=request.POST['password']
        if Tenant_Register.objects.filter(Username=username,Password=password).exists():
            use=auth.authenticate(username=username,password=password)
            if use is not None:
                auth.login(request,use)
                print("successfully login")
                return redirect(tenant_homepage)
            else:
                print("invalid login")
                return render(request,'tenant/tenant_login.html',{'key':'INVALID USER'})
        else:
            print("username not found")
            return render(request,'tenant/tenant_login.html',{'key':'PASSWORD DOESNOT MATCH'})

    return render(request,'tenant/tenant_login.html')

def tenant_profile(request):
    username=request.user
    n=Tenant_Register.objects.filter(Tenant=username).all()
    di={'view':n}
    return render(request,'tenant/tenant_profile.html',di)
def tenant_profile_update(request,upd):
    updates=Tenant_Register.objects.get(id=upd)
    if request.method=="POST":
        updates.First_name=request.POST['firstname']
        updates.Email_id=request.POST['email']
        updates.Address=request.POST['address']
        updates.Contact=request.POST['contact']
        updates.Location=request.POST['location']
        updates.Document_proof=request.FILES['img_proof']
        updates.save()
        
        return redirect(tenant_profile)
    return render(request,'tenant/tenant_profile_update.html',{'updates':updates})

def view_properties(request):
    b=request.user
    u=Tenant_Register.objects.get(Tenant=request.user)
    print(u.Username)

    info_view=Add_properties.objects.filter(Property_location=u.Location)
    dii={'view':info_view}
    return render(request,'tenant/view_properties.html',dii)

def tenant_change_password(request):
    valu=Tenant_Register.objects.get(Tenant=request.user)
    var=User.objects.get(id=valu.Tenant.id)
    if request.method == 'POST':
        valu.Password=request.POST['new_password']
        valu.save()
        pwd=request.POST['new_password']
        var.set_password(pwd)
        var.save()
        return redirect(tenant_login)
    return render(request,'tenant/tenant_change_password.html')

def tenantlogout(request):
    logout(request)
    return redirect(tenant_login)

def tenant_search_properties(request):
    if request.method=="POST":
        search_properities=request.POST['search_property']
        v=Add_properties.objects.filter(Property_type=search_properities)
        dictn={'view':v}
        return render(request,'tenant/view_properties.html',dictn)
    
def property_views1(request,pk):
    b=Add_properties.objects.filter(id=pk)
    return render(request,'tenant/view_properties1.html',{'key':b})
    
def tenant_message(request,pk):
    user=Tenant_Register.objects.get(Tenant=request.user)
    ownr=Owner_Register.objects.get(id=pk)
    comp=Message.objects.filter(Tenant_message=user)
    context={
        'key1':user,
        'key2':ownr,
        'key3':comp
    }
    if request.method=="POST":
        owner_name=request.POST['ownerName']
        property_type=request.POST['propertyType']
        name_of_user=request.POST['userName']
        location=request.POST['location']
        messages=request.POST['message']
        Message(Tenant_message=user,Owner_name=owner_name,Property_type=property_type,Name_of_the_user=name_of_user,Location=location,Owner_Messages=messages).save()
        comp=Message.objects.filter(Tenant_message=user)
        context={
            'key1':user,
            'key2':ownr,
            'key3':comp
        }
        return render(request,'tenant/message_to_owner.html',context)
    return render(request,'tenant/message_to_owner.html',context)   
    

# owner
def owner_register(request):
    if request.method=='POST':
        user_names=request.POST['usernames']
        first_name=request.POST['firstname']
        email_id=request.POST['email_id']
        owner_type=request.POST['ownerType']
        address=request.POST['address']
        
        document_proof=request.FILES['img_proof']
        contact_number=request.POST['contact']
        locations=request.POST['location']
        passwords=request.POST['password']
        confirm_password=request.POST['c_password']
        if passwords==confirm_password:  
            user=None
            if User.objects.filter(username=user_names).exists():
                user=User.objects.get(username=user_names)
                if Owner_Register.objects.filter(Owner=user).exists():
                    print("already exists")
                    return render(request,'owner/owner_registration.html',{'key1':"USERNAME ALREADY EXISTS"})
            else:
                User.objects.create_user(username=user_names,password=passwords,email=email_id).save()
                user=User.objects.get(username=user_names)
            if user:
                if Owner_Register.objects.filter(Username=user_names).exists():
                    print("uname already exists")
                    return render(request,'owner/owner_registration.html',{'key1':"USERNAME ALREADY EXISTS"})
                else:
                    user_save=Owner_Register(Owner=user,Username=user_names,First_name=first_name,Email_id=email_id,Owner_type=owner_type,Address=address,Document_proof=document_proof,Contact=contact_number,Location=locations,Password=passwords)
                    user_save.save()
                    print("saved")
                    return redirect(owner_login)
                    # return render(request,'user_registration.html',{'key2':"SUCCESSFULLY SAVED"})
        else:
            return render(request,'owner/owner_registration.html',{'key1':'PASSWORD DOES NOT MATCH'})
    else:
        return render(request,'owner/owner_registration.html')
    return render(request,'owner/owner_registration.html')   

def owner_homepage(request):
    return render(request,'owner/owner_homepage.html')

 
def owner_login(request):
    if request.method=='POST':
        username=request.POST['user_name']
        password=request.POST['password']
        if Owner_Register.objects.filter(Username=username,Password=password).exists():
            use=auth.authenticate(username=username,password=password)
            if use is not None:
                auth.login(request,use)
                print("successfully login")
                return redirect(owner_homepage)
            else:
                print("invalid login")
                return render(request,'owner/owner_login.html',{'key':'INVALID USER'})
        else:
            print("username not found")
            return render(request,'owner/owner_login.html',{'key':'PASSWORD DOESNOT MATCH'})

    return render(request,'owner/owner_login.html')

def add_property(request):
    print(request.user)
    users=Owner_Register.objects.get(Owner=request.user)
    print(users)
    if request.method=="POST":
        property_title=request.POST['title']
        property_description=request.POST['description']
        property_type=request.POST['type']
        property_location=request.POST['location']
        property_area=request.POST['area']
        property_size=request.POST['size']
        rent_price=request.POST['rentPrice']
        property_features=request.POST['features']
        image=request.FILES['images']
        properties=Add_properties(user=users,Property_title=property_title,Property_description=property_description,Property_type=property_type,Property_location=property_location,Property_area=property_area,Property_size=property_size,Property_rent_price=rent_price,Property_features=property_features,Property_image=image)
        properties.save()
        return render(request,'owner/add_property.html',{"key":'SUCCESSFULLY ENTERED'})
    return render(request,'owner/add_property.html')

def owner_profile(request):
    username=request.user
    n=Owner_Register.objects.filter(Owner=username).all()
    di={'view':n}
    return render(request,'owner/view_profile.html',di)
def profile_update(request,up):
    updates=Owner_Register.objects.get(id=up)
    if request.method=="POST":
        updates.First_name=request.POST['firstname']
        updates.Email_id=request.POST['email']
        updates.Address=request.POST['address']
        updates.Contact=request.POST['contact']
        updates.Location=request.POST['location']
        updates.Document_proof=request.FILES['img_proof']
        updates.save()
        
        return redirect(owner_profile)
    return render(request,'owner/update_profile.html',{'updates':updates})

def owner_view_properties(request):
    owner=request.user
    u=Owner_Register.objects.get(Owner=request.user)
    print(u.Username)

    views=Add_properties.objects.filter(Property_location=u.Location)
    dii={'view':views}
    return render(request,'owner/owner_view_property.html',dii)


def change_password(request):
    valu=Owner_Register.objects.get(Owner=request.user)
    var=User.objects.get(id=valu.Owner.id)
    if request.method == 'POST':
        valu.Password=request.POST['new_password']
        valu.save()
        pwd=request.POST['new_password']
        var.set_password(pwd)
        var.save()
        return redirect(owner_login)
    return render(request,'owner/change_password.html')

def message_view(request):
    print(request.user)
    user=User.objects.get(username=request.user)
    a=Owner_Register.objects.get(Owner=user)
    print(a.Username)
    views=Message.objects.filter(Owners_message=a)
    di={'view':views}
    return render(request,'owner/view_messages.html',di)


    
def ownerlogout(request):
    logout(request)
    return redirect(owner_login)

