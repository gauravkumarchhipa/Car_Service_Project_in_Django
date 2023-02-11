from django.contrib import admin

# Register your models here.
from users. models import Customers, Mechanic, Add_Service, Services_req, request_assign, add_car_service, service_payment, Membership, ContactUs
admin.site.register(Customers)
admin.site.register(Mechanic)
admin.site.register(Add_Service)
admin.site.register(Services_req)
admin.site.register(request_assign)
admin.site.register(add_car_service)
admin.site.register(service_payment)
admin.site.register(Membership)
admin.site.register(ContactUs)
