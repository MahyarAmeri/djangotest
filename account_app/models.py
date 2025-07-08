# from django.db import models
# from django.contrib.auth.models import User
# import secrets
# # Create your models here.
#
# class Device(models.Model):
#     name = models.CharField(max_length=100)
#     serial_number = models.CharField(max_length=12, unique=True)
#     status_door = models.BooleanField(default=False)
#     token = models.CharField(max_length=100, unique=True, blank=True, null=True)
#     def __str__(self):
#         return self.name
#     def save(self, *args, **kwargs):
#         if not self.token:
#             self.token = secrets.token_hex(32)
#             super().save(*args, **kwargs)
#
#
# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     devices = models.ManyToManyField(Device, blank=True, null=True)
#
#
# class Command(models.Model):
#     profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
#     device = models.ForeignKey(Device, on_delete=models.CASCADE)
#     lock_door = models.BooleanField(default=False)
#     created = models.DateTimeField(auto_now_add=True)


