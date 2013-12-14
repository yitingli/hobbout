import re

from django.core import validators
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
from django.db import models
from django.db.models import Q
from django.utils import timezone
from django.utils.http import urlquote
from django.utils.translation import ugettext_lazy as _

from albums.models import Album


class TingUserManager(BaseUserManager):

    def create_user(self, email, username, password=None, **extra_fields):
        now = timezone.now()
        if not email:
            raise ValueError('The given email must be set')
        if not username:
            raise ValueError('The given username must be set')
        email = TingUserManager.normalize_email(email)
        user = self.model(email=email, username=username,
                          is_staff=False, is_active=True, is_superuser=False,
                          last_login=now, date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        album = Album(owner=user, name="MicroBlog", is_public=False,\
                      description="Used as default album for microblog images")
        album.save()
        return user

    def create_superuser(self, email, username, password, **extra_fields):
        user = self.create_user(email, username, password, **extra_fields)
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class TingUser(PermissionsMixin, AbstractBaseUser):

    username = models.CharField(_('username'), max_length=30, unique=True,
        help_text=_('Required. 30 characters or fewer. Letters, numbers and '
                    '@/./+/-/_ characters'),
        validators=[
            validators.RegexValidator(re.compile(u'^(?!_)(?!.*?_$)[a-zA-Z0-9_\u4e00-\u9fa5]+$'), _('Enter a valid username.'), 'invalid')]
        )

    first_name = models.CharField(_('first name'), max_length=30, default='Your', blank=True)
    last_name = models.CharField(_('last name'), max_length=30, default='Name', blank=True)
    email = models.EmailField(_('email address'))
    birth_date = models.DateField(_('birth date'), null=True, blank=True)

    """
        Note: TextField is a longtext field in database, in MySQL
        TINYTEXT    L + 1 bytes, where L < 28
        TEXT        L + 2 bytes, where L < 216
        MEDIUMTEXT  L + 3 bytes, where L < 224
        LONGTEXT    L + 4 bytes, where L < 232
        So a longtext will use one more byte than mediumtext to store the same text.
        There is a bit more information in the Data Type Storage Requirements section of the manual
        and some more in the The BLOB and TEXT Types section.
        There's no practical difference between the four TEXT types.
    """
    description = models.TextField(_('description'), default='Detailed description', blank=True)

    is_staff = models.BooleanField(_('staff status'), default=False,
        help_text=_('Designates whether the user can log into this admin '
                    'site.'))
    is_active = models.BooleanField(_('active'), default=True,
        help_text=_('Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    avatar = models.ForeignKey('mediabox.MediaImage', null=True, blank=True, on_delete=models.SET_NULL)
    brief_description = models.CharField(_('brief_description'), max_length=180, default='Brief description', blank=True)

    registration_status = models.CharField(_('registration status'), max_length=1, default='T')

    objects = TingUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', ]

    def __unicode__(self):
        return self.username

    def get_absolute_url(self):
        return "/users/%s/" % urlquote(self.username)

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        "Returns the short name for the user."
        return self.first_name

    def email_user(self, subject, message, from_email=None):
        """
        Sends an email to this TingUser.
        """
        send_mail(subject, message, from_email, [self.email])

    def set_registration_complete(self):
        self.registration_status = 'T'

    def get_avatar(self, geometry, crop='center'):
        if self.avatar:
            return self.avatar.get_image(geometry, crop)
        else:
            return None

    def get_avatar_url(self, geometry, crop='center'):
        if self.avatar:
            return self.avatar.get_image(geometry, crop).url
        else:
            return settings.DEFAULT_AVATAR_LOCATION + geometry + '.jpg'

    def get_albums(self, max_id, size=settings.PAGE_SIZE['ALBUM'], public=True):
        criteria = Q(owner=self)
        if public:
            criteria = criteria & Q(is_public=True)
        else:
            criteria = criteria & Q(is_public=False)
        if max_id:
            criteria = criteria & Q(pk__lt=max_id)
        return Album.objects.filter(criteria).order_by('-rank')[:size]
