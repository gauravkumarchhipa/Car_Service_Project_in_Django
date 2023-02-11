"""carservice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib.auth.views import PasswordChangeForm
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('customerpanel/', views.customerpanel, name="customerpanel"),
    path('mechanicpanel', views.mechanicpanel, name="mechanicpanel"),
    path('adminpanel/', views.adminpanel, name="adminpanel"),
    path('home/', views.home, name="home"),
    path('signup/', views.signup, name="signup"),
    path('login/', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('mec_signup/', views.Mec_signup, name="Mec_signup"),
    path('changepass/<str:uname>', views.user_change_pass, name="changepass"),
    path('fuel_services/', views.fuel_services, name="fuel_services"),
    path('picup_drop/', views.picup_drop, name="picup_drop"),
    path('carservices/', views.carservices, name="carservices"),
    # path('AddServices/',views.add_services,name="add_services"),
    # adminmanage
    path('add_show/', views.add_show, name="add_show"),
    path('del/<str:id>', views.deletedata, name="deletedata"),
    path('updatedata/<int:id>', views.updatedata, name="updatedata"),
    path('user_manage/', views.user_manage, name="user_manage"),
    path('admin_usermanage/<int:id>',
         views.admin_usermanage, name="admin_usermanage"),
    path('admin_user_delete/<str:id>',
         views.admin_user_delete, name="admin_user_delete"),

    # mechanic
    path('mechanic_manage/', views.mechanic_manage, name="mechanic_manage"),
    path('admin_mechanicmanage/<int:id>',
         views.admin_mechanicmanage, name="admin_mechanicmanage"),
    path('admin_delete_mec/<int:id>',
         views.admin_delete_mec, name="admin_delete_mec"),
    path('bill_generat', views.bill_generat, name="bill_generat"),
    path('makepayment/<int:id>', views.makepayment, name="makepayment"),
    path('membership/<int:id>', views.membership, name="membership"),
    path('Payment_detail/<int:id>', views.Payment_detail, name="Payment_detail"),
    path('ContactUs', views.Contact, name="ContactUs"),

    # service_request
    # path('service_request/', views.service_request, name="service_request"),
    path('panding_request/', views.panding_request, name="panding_request"),
    path('Assign_Mechanic/<int:id>', views.Assign_Mechanic, name="Assign_Mechanic"),
    path('request_status/<str:id>', views.request_status, name="request_status"),


    # mechanic
    path('update_userprofile/<int:id>/',
         views.update_userprofile, name="update_userprofile"),
    path('update_mechanic_profilee/<int:id>/',
         views.update_mechanic_profile, name="update_mechanic_profile"),
    path('Mechnic_request/<int:id>',
         views.Mechnic_request, name="Mechnic_request"),
    path('MechRequest_fullview/<str:id>',
         views.MechRequest_fullview, name="MechRequest_fullview"),
    path('Bill_Generate', views.Bill_Generate, name="Bill_Generate"),
    path('add_car_ser', views.add_car_ser, name="add_car_ser"),


    # admin
    path('all_reqshow_admin', views.all_reqshow_admin, name="all_reqshow_admin"),


    # path('profile/',views.user_profile,name='profile'),

    path('reset_password/', auth_views.PasswordResetView.as_view(
        template_name="forgotpassword.html"), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(
        template_name="mailsent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name="changepassword.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name="users/customerlogin.html"), name="password_reset_complete"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
