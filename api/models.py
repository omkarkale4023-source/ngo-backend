from django.db import models

class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name


class Donation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    amount = models.IntegerField()
    purpose = models.CharField(max_length=100)
    donation_type = models.CharField(max_length=50)
    payment_mode = models.CharField(max_length=50)
    anonymous = models.BooleanField(default=False)
    donated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class LoginActivity(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=100, default="")
    login_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
