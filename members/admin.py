from django.contrib import admin
from .models import Member
from .utils import send_sms

class ChurchMemberAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'phone', 'date_added')

    def save_model(self, request, obj, form, change):
        if not change:  # New member
            super().save_model(request, obj, form, change)
            message = f"Welcome {obj.firstname} {obj.lastname} to our church community!"
            send_sms(obj.phone, message)
        else:
            super().save_model(request, obj, form, change)

admin.site.register(Member, ChurchMemberAdmin)
