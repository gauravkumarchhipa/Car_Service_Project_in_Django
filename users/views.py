from asyncio.windows_events import NULL
from audioop import add
import datetime
from email import message
from pyexpat.errors import messages
from tabnanny import check
from telnetlib import STATUS
from urllib.request import Request
from xmlrpc.client import DateTime
from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from platformdirs import user_data_dir
from django.core.mail import send_mail
import users
from .models import Customers, Mechanic, Add_Service, Services_req, request_assign, add_car_service, service_payment, Membership, ContactUs
from django.contrib.auth.hashers import make_password
# from .forms import addservice
# Create your views here.


def index(request):
    return render(request, 'index.html')


def home(request):
    return render(request, 'admin/admindash.html')


def customerpanel(request):
    return render(request, 'users/customerdash.html')


def mechanicpanel(request):
    # id = request.user.id
    # service_data = Services_req.objects.filter(
    #     Mechanic_id=request.user.id, Status=2)
    Mech_id = Mechanic.objects.get(
        userId_id=request.user.id)
    service_data = Services_req.objects.filter(Mechanic_id=Mech_id, Status=2)
    # return render(request, 'mechanic/Mechnice_request.html', {'Request': service_data})
    return render(request, 'mechanic/mechanicdash.html', {'Request': service_data})


def adminpanel(request):
    return render(request, 'admin/dashboard.html')


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_superuser == True:
                login(request, user)
                return redirect('adminpanel')
            if user.is_staff == True:
                login(request, user)
                return redirect('mechanicpanel')
            login(request, user)
            return redirect('customerpanel')
        else:
            return redirect('login')
    return render(request, 'users/customerlogin.html')


def signup(request):
    if request.method == "POST":
        uname = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['eml']
        password = request.POST['pass']
        dob = request.POST['dob']
        gender = request.POST['fm']
        mnumber = request.POST['mno']
        user = User.objects.create(username=uname, email=email, first_name=fname,
                                   last_name=lname, password=make_password(password))
        c = Customers(userId=user, Gender=gender, mobile_no=mnumber, dob=dob)
        c.save()
        user.save()
        return redirect('login')
    return render(request, 'users/customersignup.html')


def Mec_signup(request):
    if request.method == "POST":
        uname = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['eml']
        password = request.POST['pass']
        dob = request.POST['mdob']
        skill = request.POST['skill']
        gender = request.POST['fm']
        city = request.POST['city']
        area = request.POST['area']
        mnumber = request.POST['mno']
        salary = request.POST['salary']
        user = User.objects.create(username=uname, email=email, first_name=fname,
                                   last_name=lname, password=make_password(password), is_staff=1)
        m = Mechanic(userId=user, mobile=mnumber,
                     skill=skill, Gender=gender, salary=salary, dob=dob, city=city, area=area)
        user.save()
        m.save()

        return render(request, 'mechanic/mechanicsignup.html')
    return render(request, 'mechanic/mechanicsignup.html')


def logout_user(request):
    logout(request)
    return redirect('/')

# def index(request):
#     return render(request,'home.html')


# changepassword with old password
def user_change_pass(request, uname):
    if request.method == 'POST':
        opass = request.POST.get('old_password')
        user = authenticate(request, username=uname, password=opass)
        if user:
            u = User.objects.get(username=uname)
            npass = request.POST.get('new_password1')
            u.password = make_password(npass)
            u.save()
            return redirect('login')
        else:
            return redirect('customerpanel')
    return render(request, 'changepass.html')

# userprofile manage
# def user_profile(request):
#   if request.user.is_authenticated:
#     if request.method=="POST":
#        fm=EditUserProfileForm(request.POST,instance=request.user)
#        if fm.is_valid():
#           messages.success(request,'Profile is updated')
#           fm.save()
#     else:
#         fm=EditUserProfileForm(instance=request.user)
#         return render(request,'profile.html',{'name':request.user,'form':fm})
#   else:
#      return HttpResponseRedirect('/login/')


# servicecode

def fuel_services(request):
    return render(request, 'fuel.html')


def picup_drop(request):
    return render(request, 'picup_drop.html')


# def carservices(request):
#     s1 = Add_Service.objects.all()
#     if request.method == 'POST':
#         service_id = request.POST.get('service')
#         service_name = Add_Service.objects.get(id=service_id)
#         userId = Customers.objects.get(userId_id=request.POST['uid'])
#         serv_name = service_name.id
#         c_com = request.POST['ccompany']
#         cmodel = request.POST['cmodel']
#         cnumber = request.POST['cnumber']
#         city = request.POST['city']
#         area = request.POST['area']
#         mobile = request.POST['mobile']
#         fuel = request.POST['fuel_s']
#         add = request.POST['address']
#         pd_date = request.POST['date']
#         time = request.POST['time']

#         car_service = Services_req(car_company=c_com, car_model=cmodel, car_number=cnumber, city=city, area=area, Mobile_Number=mobile, Fuel=fuel,
#                                    Address=add, pd_date=pd_date, pd_time=time, userId=userId, Service_id=serv_name)
#         car_service.save()

  #  return render(request, 'Users/Service_request.html', {'service': s1})

def carservices(request):
    s1 = Add_Service.objects.filter(active=1)

    if request.method == 'POST':
        service_id = request.POST.get('service')
        service_name = Add_Service.objects.get(id=service_id)
        userId = Customers.objects.get(userId_id=request.POST['uid'])
        serv_name = service_name.id
        c_com = request.POST['ccompany']
        cmodel = request.POST['cmodel']
        cnumber = request.POST['cnumber']
        city = request.POST['city']
        area = request.POST['area']
        mobile = request.POST['mobile']
        fuel = request.POST['fuel_s']
        add = request.POST['address']
        pd_date = request.POST['date']
        time = request.POST['time']
        fliter = int(request.POST['Liter'])
        charge = NULL

        try:
            membership = Membership.objects.get(userId=userId.id)
        except Membership.DoesNotExist:
            membership = None

        if(service_id == '2'):
            if membership != None:
                charge = NULL
            else:
                charge = int(service_name.service_charge)
        if(fuel != ''):
            if(fuel == 'Petrol'):
                charge = int(service_name.Petrol)*fliter

            else:
                charge = int(service_name.Diesel)*fliter

        demo = request.POST.get('pd_service').split(",")
        if(demo != "['']"):
            for c in demo:
                if(c == 'washing'):
                    charge = 100
                if(c == 'engine_oil'):
                    charge += 200
                if(c == 'oil_filter'):
                    charge += 300
                if(c == 'breakes'):
                    charge += 200
                if(c == 'Battery'):
                    charge += 500

        pd_service = demo

        car_service = Services_req(car_company=c_com, car_model=cmodel, car_number=cnumber, city=city, area=area, Mobile_Number=mobile, Fuel=fuel,
                                   fuel_liter=fliter, charge=charge, Address=add, pd_date=pd_date, pd_time=time, pd_service=pd_service, userId=userId, Service_id=serv_name)
        car_service.save()
    return render(request, 'users/Service_request.html', {'service': s1})


# Add And Show Service Function
def add_show(request):
    s1 = Add_Service.objects.all()
    if request.method == 'POST':
        ser_name = request.POST['ser_name']
        ser_charge = request.POST['ser_charge']
        ser_desc = request.POST['ser_desc']
        ser_active = request.POST.get('chk_btn')
        service = Add_Service(service_name=ser_name, service_charge=ser_charge,
                              service_desc=ser_desc, active=ser_active)
        service.save()
    return render(request, 'admin/add&show.html', {'service': s1})

# Edit Service Function


def updatedata(request, id):
    s1 = Add_Service.objects.get(id=id)
    if request.method == 'POST':
        s1.service_name = request.POST['ser_name']
        s1.service_charge = request.POST['ser_charge']
        s1.service_desc = request.POST['ser_desc']
        # if(request.POST['petrol']):
        #     s1.Petrol = request.POST['petrol']
        # if(request.POST['Diesel']):
        #     s1.Diesel = request.POST['Diesel']
        s = request.POST.get('status')
        if s == 'on':
            s = True
        else:
            s = False
        s1.active = s
        s1.save()
    return render(request, 'admin/updateservice.html', {'s1': s1})


# Delete Service Function

def deletedata(request, id):
    if request.method == 'POST':
        pi = Add_Service.objects.get(id=id)
        pi.delete()
        return redirect('add_show')


def user_manage(request):
    cust = Customers.objects.all()
    return render(request, 'admin/user_manage.html', {'all_cust': cust})


# userupdate_admin

def admin_usermanage(request, id):
    cust = Customers.objects.get(userId_id=id)
    userdata = User.objects.get(id=id)
    if request.method == 'POST':
        userdata.username = request.POST['username']
        userdata.first_name = request.POST['fname']
        userdata.last_name = request.POST['lname']
        userdata.email = request.POST['email']
        cust.mobile_no = request.POST['mobile']
        userdata.save()
        cust.save()
        return redirect('user_manage')
    return render(request, 'admin/update_userform.html', {'s1': cust})

# userdelete_admin


def admin_user_delete(request, id):
    if request.method == 'POST':
        user_c = Customers.objects.get(userId_id=id)
        user_u = User.objects.get(id=id)
        user_c.delete()
        user_u.delete()
        return redirect('user_manage')


def panding_request(request):
    Request = Services_req.objects.filter(Status=1)
    return render(request, 'admin/Panding_request.html', {'Request': Request})


def Assign_Mechanic(request, id):
    service_data = Services_req.objects.get(id=id)
    Mechanic_data = Mechanic.objects.filter(status=1, area=service_data.area)
    if request.method == 'POST':
        srequest = request.POST['service_id']
        userId = request.POST['uid']
        Mec_id = request.POST['Mechanic_assign']
        srequest_id = Services_req.objects.get(id=srequest)
        userId_id = Customers.objects.get(userId_id=userId)
        Mechanic_id = Mechanic.objects.get(userId_id=Mec_id)
        Mechanic_id.status = False
        Mechanic_id.save()
        srequest_id.Status = 2
        srequest_id.Mechanic = Mechanic_id
        srequest_id.save()

        email_from = settings.EMAIL_HOST
        subject = "Assign Mechanic"
        message = f'Your mechanic detai\n Mechanic Name:-{Mechanic_id.userId.first_name}\n Mechanic Mobile Number:-{Mechanic_id.mobile}\n Mechanic Email:-{Mechanic_id.userId.email}'
        # send_mail(subject, message, email_from, [userId_id.userId.email])
        return redirect('panding_request')

    return render(request, 'admin/Assign_Mechanic.html', {'Request': service_data, 'Mechanic_data': Mechanic_data})


def request_status(request, id):
    customer_data = Customers.objects.get(userId_id=id)
    sreq_data = Services_req.objects.filter(
        userId=customer_data.id).order_by('-id')
    try:
        membership = Membership.objects.filter(userId=customer_data.id)
    except Membership.DoesNotExist:
        membership = False

    # if sreq_data.Fuel
    #    if i.Fuel == 'Petrol' or i.Fuel == 'Diesel':
    #         i.charge | add: i.Service.service_charge
    #     else:
    #         i.Service.service_charge

    # service_data = request_assign.objects.filter(
    #     userId=customer_data.id)
    return render(request, 'users/request_status.html', {'sreq': sreq_data, 'member': membership})

# user_edit


def update_userprofile(request, id):
    cust = Customers.objects.get(userId_id=id)
    userdata = User.objects.get(id=id)
    try:
        membership = Membership.objects.get(userId_id=cust.id)
    except Membership.DoesNotExist:
        membership = False
    if request.method == 'POST':
        userdata.username = request.POST.get('username')
        userdata.first_name = request.POST.get('fname')
        userdata.last_name = request.POST.get('lname')
        userdata.email = request.POST.get('email')
        cust.mobile_no = request.POST.get('mobile')
        cust.dob = request.POST.get('dob')
        userdata.save()
        cust.save()
        return redirect('customerpanel')
    return render(request, 'users/Edit_profile.html', {'s1': cust, 'member': membership})

# mechanic
# update mechanic profile


def update_mechanic_profile(request, id):
    mech = Mechanic.objects.get(userId_id=id)
    userdata = User.objects.get(id=id)
    if request.method == 'POST':
        userdata.username = request.POST.get('username')
        userdata.first_name = request.POST.get('fname')
        userdata.last_name = request.POST.get('lname')
        userdata.email = request.POST.get('email')
        mech.mobile_no = request.POST.get('mobile')
        # mech.dob = request.POST.get('dob')
        mech.skill = request.POST.get('skill')
        userdata.save()
        mech.save()
        return redirect('mechanicpanel')
    return render(request, 'mechanic/Edit_Mech_profile.html', {'s1': mech})


# mechnic

def Mechnic_request(request, id):
    Mech_id = Mechanic.objects.get(userId_id=id)
    service_data = Services_req.objects.filter(Mechanic_id=Mech_id, Status=2)
    return render(request, 'mechanic/Mechnice_request.html', {'Request': service_data})


def MechRequest_fullview(request, id):
    service_data = Services_req.objects.get(id=id)
    cser = add_car_service.objects.filter(Srequest=service_data.id)
    charge = 0
    for c in cser:
        if(c.service_charge != ''):
            charge += int(c.service_charge)

    if request.method == 'POST':
        sid = request.POST.get('service_id')
        uid = request.POST.get('uid')
        charge = request.POST.get('service_charge')
        service_data = Services_req.objects.get(id=sid)
        cser = add_car_service.objects.filter(Srequest=service_data.id)
        service_data.Status = 3
        service_data.save()
        # return render(request, 'mechanic/Generated_Bill.html', {'Request': service_data, 'charge': charge, 'cser': cser})

    return render(request, 'mechanic/MechRequest_fullview.html', {'Request': service_data, 'charge': charge, 'cser': cser})


def Bill_Generate(request):
    return render(request, 'mechanic/Generated_Bill.html')


def add_car_ser(request):
    if request.method == 'POST':
        service_data = Services_req.objects.get(id=request.POST.get('sid'))
        Srequ = service_data.id
        userId = service_data.userId
        service_name = request.POST.get('as')
        service_charge = request.POST.get('ac')
        addc_service = add_car_service(
            Srequest_id=Srequ, userId=userId, service_name=service_name, service_charge=service_charge)
        addc_service.save()
    return redirect('MechRequest_fullview', id=service_data.id)


def bill_generat(request):
    mech = Mechanic.objects.get(userId=request.user.id)
    mech_service_detail = Services_req.objects.filter(
        Mechanic_id=mech.id).order_by('-id')
    if request.method == 'POST':
        sid = request.POST.get('service_id')
        service_data = Services_req.objects.get(id=sid)
        service_data.Status = 3
        service_data.save()
    return render(request, 'mechanic/mech_payment_detail.html', {'payment': mech_service_detail})


# managemech
def mechanic_manage(request):
    mech = Mechanic.objects.all()
    return render(request, 'admin/mechanic_manage.html', {'all_mech': mech})


def admin_mechanicmanage(request, id):
    s1 = Mechanic.objects.get(userId=id)
    userdata = User.objects.get(id=id)
    if request.method == 'POST':

        userdata.username = request.POST['uname']
        userdata.first_name = request.POST['fname']
        userdata.last_name = request.POST['lname']
        userdata.email = request.POST['email']
        s1.mobile = request.POST['mno']
        # s1.dob=request.POST['dob']
        s1.skill = request.POST['skill']

        s = request.POST.get('status')

        if s == 'on':
            s = True
        else:
            s = False

        s1.status = s
        userdata.save()
        s1.save()
        return redirect('mechanic_manage')
    return render(request, 'admin/updatemechanic.html', {'s1': s1})


def admin_delete_mec(request, id):
    if request.method == 'POST':
        mech = Mechanic.objects.get(userId=id)
        user_u = User.objects.get(id=id)
        mech.delete()
        user_u.delete()
        return redirect('mechanic_manage')
    return render(request, 'admin/mechanic_manage.html')


def makepayment(request, id):
    charge = ""
    cser = ''
    service_data = Services_req.objects.get(id=id)
    try:
        membership = Membership.objects.get(userId=service_data.userId_id)
    except Membership.DoesNotExist:
        membership = None

    if membership != None:
        charge = service_data.charge
    else:
        if service_data.Service_id == 2:
            cser = add_car_service.objects.filter(Srequest=service_data.id)
            charge = int(service_data.charge)
            for c in cser:
                if(c.service_charge != ''):
                    charge += int(c.service_charge)

        elif service_data.Service_id == 3:
            charge = int(service_data.charge) + \
                int(service_data.Service.service_charge)

        elif service_data.Service_id == 5:
            charge = int(service_data.charge) + \
                int(service_data.Service.service_charge)

        else:
            charge = ""

    if request.method == 'POST':
        uid = request.POST['uid']
        userId = Customers.objects.get(id=uid)
        payment = service_payment(
            Srequest_id=service_data.id, userId=userId, service_charge=charge)
        payment.save()
        service_data.Status = 4
        service_data.save()

    return render(request, 'users/View_bill.html', {'s1': service_data, 'charge': charge, 'added_service': cser})


def membership(request, id):
    if request.method == 'POST':
        userId = id
        uid = Customers.objects.get(userId_id=userId)
        pay = 500
        sdate = datetime.datetime.now()
        edate = datetime.datetime.now() + datetime.timedelta(90)
        ms = Membership(userId=uid, pay=pay, startdate=sdate, enddate=edate)
        ms.save()
        return redirect('customerpanel')


def Payment_detail(request, id):
    uid = Customers.objects.get(userId=id)
    service_data = Services_req.objects.filter(userId=uid.id, Status=4)
    # try:
    #     charge = service_payment.objects.filter(Srequest=service_data)
    # except service_payment.DoesNotExist:
    #     charge = None

    return render(request, 'users/Payment_detail.html', {'service': service_data})


def Contact(request):
    id = request.user.id
    uid = Customers.objects.get(userId=id)
    if request.method == "POST":
        fname = request.POST['fname']
        email = request.POST['email']
        number = request.POST['number']
        msg = request.POST['msgname']

        contact = ContactUs(userId=uid, name=fname,
                            email=email, number=number, msg=msg)
        contact.save()
    return redirect('customerpanel')


def all_reqshow_admin(request):
    service_data = Services_req.objects.filter()
    return render(request, 'admin/all_reqshow.html', {'Request': service_data})
