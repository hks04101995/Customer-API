from django.db import models
from django.contrib.auth.models import PermissionsMixin,AbstractBaseUser,BaseUserManager
from django.utils.translation import ugettext_lazy as _
# Create your models here.

class ResPartnerManager(BaseUserManager):
    def create_user(self, name, image, password, address, address2, is_company, vat_number, parent ):
        if not email:
            raise ValueError("User must have an email address")
        email = self.normalize_email(email)
        user = self.model(name, image, address, address2, is_company, vat_number, parent)
        user.set_password(password)
        user.save(using = self._db)
        return user


class ResPartner(AbstractBaseUser):
    email =  models.EmailField(_('Email'),max_length=200,unique=True)
    image = models.ImageField(_('Image'), blank=True)
    name = models.CharField(_("Name"),max_length=200)
    address = models.CharField(_('Address'), blank=True)
    password = models.CharField(_("Password"),max_length=200)
    address = models.CharField(_('Address2'),max_length=200, blank=True)
    is_company = models.BooleanField(_('Company'), default=False)
    vat_number = models.CharField(_('Vat Number'),max_length=200, blank=True)
    parent = models.ForeignKey('self', models.SET_NULL,null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email','name']

    def __str__(self):
        return self.name
