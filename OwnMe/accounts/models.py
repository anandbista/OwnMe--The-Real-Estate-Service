from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse

 
class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=255, null=True,
                                  verbose_name=_("Firstname"))
    last_name = models.CharField(max_length=255, null=True,
                                 verbose_name=_("Lastname"))
    username = None
    phone = models.CharField(max_length=20, null=True,
                             verbose_name=_("Phone"))
    address = models.ForeignKey('core.Address', null=True, blank=True,
                                on_delete=models.DO_NOTHING,
                                verbose_name=_("Address"))
    email = models.EmailField(unique=True, verbose_name=_("Email"))

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse('profile', args=[str(self.id)])

    def get_groups(self):
        return [group.name for group in self.groups.all()]
    get_groups.short_description = _("Groups")



        
        
