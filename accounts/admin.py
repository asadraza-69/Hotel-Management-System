from django.contrib import admin

from .models import *

# Register your models here.
@admin.register(User)
class UserAdmin(admin.Admin):
    list_display = ("username", "email", "first_name", "last_name", "is_staff")
    
admin.site.register(UserProfile)

admin.site.register(Restaurant)
admin.site.register(RestaurantBranch)

admin.site.register(Delivery)
admin.site.register(DeliveryMan)
admin.site.register(Payment)
admin.site.register(Order)
admin.site.register(OrderPackageList)
