from django.contrib import admin
from .models import Member, Ladies, Rescue
from .utils import send_sms

class ChurchMemberAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'phone', 'department', 'date_added')

    def save_model(self, request, obj, form, change):
        if not change:  # New member
            super().save_model(request, obj, form, change)
            message = f"Welcome {obj.firstname} {obj.lastname} to our church community!"
            send_sms(obj.phone, message)
        else:
            super().save_model(request, obj, form, change)

admin.site.register(Member, ChurchMemberAdmin)


class LadiesMemberAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'phone', 'date_added')

    def save_model(self, request, obj, form, change):
        if not change:  # New member
            super().save_model(request, obj, form, change)
            message = f"Welcome {obj.firstname} {obj.lastname} to our church community!"
            send_sms(obj.phone, message)
        else:
            super().save_model(request, obj, form, change)

admin.site.register(Ladies, LadiesMemberAdmin)


class RescueMemberAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'phone', 'date_added')

    def save_model(self, request, obj, form, change):
        if not change:  # New member
            super().save_model(request, obj, form, change)
            message = f"Welcome {obj.firstname} {obj.lastname} to our church community!"
            send_sms(obj.phone, message)
        else:
            super().save_model(request, obj, form, change)

admin.site.register(Rescue, RescueMemberAdmin)