from django.db import models


class Member(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True, default="")
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100,  blank=True, null=True, default="")
    date_of_birth = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=100,  blank=True, null=True, default="")
    phone = models.CharField(max_length=15, unique=True)
    email = models.EmailField(null=True, blank=True)
    marital_status = models.CharField(max_length=100, blank=True, null=True)
    membership_status = models.CharField(max_length=100, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    consent_participate = models.CharField(max_length=100, blank=True, null=True, default="False")
    consent_data = models.CharField(max_length=100, blank=True, null=True, default="False")
    
    class Meta:
        verbose_name_plural = "Members"
        ordering = ["-firstname"]
        
    def __str__(self):
        return f"{self.firstname} {self.lastname}"