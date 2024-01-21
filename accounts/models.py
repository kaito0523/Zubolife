from django.db import models
from django.contrib.auth.models import PermissionsMixin,UserManager
from django.contrib.auth.base_user import AbstractBaseUser,BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.contrib.auth.validators import UnicodeUsernameValidator
from app.models import Recipe



"""書かないとcreatesuperuserできない"""
class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError('The given username must be set')
        username = self.model.normalize_username(username)
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, password, **extra_fields)



"""お気に入り機能追加済みユーザー"""
class CustomUser(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _('username'),
        max_length=10,
        unique=True,
        help_text=_('Required. 10 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    name = models.CharField(_('name'), max_length=10, blank=True)

    favorite_recipe = models.ManyToManyField(Recipe, verbose_name='お気に入りの場所', blank=True)

    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'username'

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        name = '%s %s' % (self.name)
        return name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.name
