# Create your models here.

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    points = models.SmallIntegerField(default=0)
    vouchers = models.SmallIntegerField(default=0)
    premium = models.BooleanField(default=False)

    def exchanchePointsToVouchers(self, vouchers):
        self.points -= vouchers * 100
        self.vouchers += vouchers
        self.save()

    def exchangeVoucherToAnswer(self):
        self.vouchers -= 1
        self.save()




@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=500)
    pub_date = models.DateTimeField(auto_now_add=True)

class Code(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=20)
    confirmed = models.BooleanField(default=False, blank=True)
    date = models.DateTimeField(auto_now_add=True)