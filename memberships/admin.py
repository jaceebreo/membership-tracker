from django.contrib import admin
from django.contrib.auth.models import User
from .models import Role, StaffProfile, Member, Invoice, Billing

admin.site.register(Role)
admin.site.register(StaffProfile)
admin.site.register(Member)
admin.site.register(Invoice)
admin.site.register(Billing)
