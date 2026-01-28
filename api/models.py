from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Donation(models.Model):
    PURPOSE_CHOICES = [
        ("Education", "Education"),
        ("Healthcare", "Healthcare"),
        ("Women Empowerment", "Women Empowerment"),
        ("General", "General"),
    ]

    DONATION_TYPE_CHOICES = [
        ("One Time", "One Time"),
        ("Monthly", "Monthly"),
    ]

    PAYMENT_MODE_CHOICES = [
        ("UPI", "UPI"),
        ("Card", "Card"),
        ("Net Banking", "Net Banking"),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    amount = models.PositiveIntegerField()
    purpose = models.CharField(max_length=50, choices=PURPOSE_CHOICES, default="General")
    donation_type = models.CharField(max_length=50, choices=DONATION_TYPE_CHOICES, default="One Time")
    payment_mode = models.CharField(max_length=50, choices=PAYMENT_MODE_CHOICES, default="UPI")
    anonymous = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.amount}"


class LoginActivity(models.Model):
    email = models.EmailField()
    login_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
