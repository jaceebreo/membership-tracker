from django.contrib.admin import ModelAdmin
from django.contrib import admin
from .models import StaffProfile, StaffRole, Member, MembershipType, Invoice, Billing, GymBranch


class BillingAdmin(ModelAdmin):
    list_display = ("id", "member", "billing_date", "start_date",
                    "end_date", "invoice__payment_amount")


class MemberAdmin(ModelAdmin):
    list_display = ("id", "email", "first_name", "last_name", "is_active")


class MembershipTypeAdmin(ModelAdmin):
    list_display = ("id", "name", "description")


class RoleAdmin(ModelAdmin):
    list_display = ("id", "role_name",)
    ordering = ("id",)


class InvoiceAdmin(ModelAdmin):
    list_display = ("invoice_num", "member", "payment_date")


class StaffProfileAdmin(ModelAdmin):
    list_display = ("user",)


class StaffRoleAdmin(ModelAdmin):
    list_display = ("role_name",)


# admin.site.register(Role, RoleAdmin)
admin.site.register(StaffRole, StaffRoleAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(MembershipType, MembershipTypeAdmin)
admin.site.register(Billing, BillingAdmin)
admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(StaffProfile, StaffProfileAdmin)
admin.site.register(GymBranch)
