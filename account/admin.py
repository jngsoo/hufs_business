from django.contrib import admin


from .models import Users
from .models import Origin_users
# Register your models here.

admin.site.register(Users)
admin.site.register(Origin_users)