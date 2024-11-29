from django.shortcuts import render, redirect


from .utils import send_sms

from .models import Member
from django.conf import settings
from django.http import JsonResponse



# Create your views here.
def index(request):
    if request.method == "POST":
        title = request.POST['title']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        middlename = request.POST['middlename']
        dob = request.POST['dob']
        location = request.POST['location']
        email = request.POST['email']
        phone = request.POST['phone']
        marital_status = request.POST['marital_status']
        membership_status = request.POST['membership_status']
        consent_participate = request.POST['consent_participate']
        consent_data = request.POST['consent_data']
        
        member = Member(title=title, firstname=firstname, lastname=lastname, middle_name=middlename, date_of_birth=dob, location=location, email=email, phone=phone, marital_status=marital_status, membership_status=membership_status, consent_participate=consent_participate, consent_data=consent_data)
        member.save()

        phone_number = member.phone
        message = f"welcome {member.firstname} {member.lastname} to our church community!"
        
        response = send_sms(phone_number, message)
        print(response)
        
        return redirect('message_sent')

    return render(request, "members/index.html")
        
        
def message_sent(request):
    return render(request, "members/message_sent.html")