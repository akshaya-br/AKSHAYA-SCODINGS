from django.urls import path
from .import views

urlpatterns = [
    
    path('',views.index),
    path('tenant_register',views.tenant_register),
    path('tenant_login',views.tenant_login),
    path('tenant_homepage',views.tenant_homepage),
    path('tenant_profile',views.tenant_profile),
    path('tenant_profile_update<str:upd>',views.tenant_profile_update,name='tenantprofile_update'),
    path('view_properties',views.view_properties),
    path('tenant_change_password',views.tenant_change_password),
    path('tenant_logout',views.tenantlogout),
    path('tenant_search_properties',views.tenant_search_properties),
    path('property_views1',views.property_views1),
    path('property_view1<str:pk>',views.property_views1,name='property_detail'),
    path('tenant_messages<str:pk>',views.tenant_message,name='send_message'),
    
    # owner
    path('owner_register',views.owner_register),
    path('owner_login',views.owner_login),
    path('owner_homepage',views.owner_homepage),
    
    path('add_property',views.add_property),
    path('owner_profile',views.owner_profile),
    path('profile_update<str:up>',views.profile_update,name='ownerprofile_update'),
    path('owner_view_properties',views.owner_view_properties),
    path('owner_change_password',views.change_password),
    path('owner_logout',views.ownerlogout),
    path('message_view',views.message_view),
]
