from django.db.models import (
    Model, 
    CharField, 
    OneToOneField, 
    DateField,
    DecimalField,
    ManyToManyField,
    BooleanField, 
    EmailField, 
    ForeignKey, 
    UUIDField,
    SET_NULL,
    CASCADE
)
from django.contrib.auth.models import User 
import uuid



PAYMENT_METHODS = [
    ('BANK_TRANSFER', 'Bank Transfer'),
    ('CASH', 'Cash'),
    ('GCASH', 'G-Cash'),
    ('QR_PAYMENT', 'QR Payment'),
]

class Role(Model):
    role_name = CharField(verbose_name='Role Name', max_length=64)
    description = CharField(blank=True, null=True)
        
    
    
class Member(Model):
    email = EmailField(verbose_name="Email")
    first_name = CharField(verbose_name="First Name", max_length=128)
    last_name = CharField(verbose_name="Last Name", max_length=128)
    birthdate = DateField(verbose_name="Birth Date")
    phone_number = CharField(verbose_name="Phone number", max_length=15, blank=True)
    is_active = BooleanField(verbose_name="Is Active?", default=True)
    qr_code_key = UUIDField(default=uuid.uuid4, editable=False, unique=True)
    role = ManyToManyField(Role)
    # Todo:
    # Create a property/attribute to verify if user has up to date payment


class Invoice(Model):
    invoice_num = CharField(verbose_name='Invoice Number', max_length=128)
    member = ForeignKey(Member,  related_name='related_member_invoices', on_delete=SET_NULL, null=True, blank=True)
    payment_date = DateField(verbose_name="Payment Date",)
    payment_method = CharField(verbose_name="Payment Method", max_length=15, choices=PAYMENT_METHODS, default='CASH')
    payment_amount = DecimalField(verbose_name='Payment Amount', decimal_places=2, max_digits=5)


class Billing(Model):
    member = ForeignKey(Member, related_name='related_member_billings', on_delete=SET_NULL,  null=True, blank=True )
    billing_date = DateField(verbose_name="Billing Date")
    start_date = DateField(verbose_name='Biling Start Date')
    end_date = DateField(verbose_name='Biling End Date')
    invoice = ForeignKey(Invoice, related_name='related_invoice_billings', on_delete=SET_NULL,  null=True, blank=True)


class StaffProfile(Model):
    user = OneToOneField(User, on_delete=CASCADE)
    roles = ManyToManyField(Role)