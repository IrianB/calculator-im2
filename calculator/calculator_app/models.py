from django.db import models

class Donor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    blood_type = models.CharField(max_length=3)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.blood_type})"
