from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from .models import UserAccount

class AdminUser(UserAdmin):
  list_display = ('email', 'username', 'role', 'is_admin')
  search_fields = ('email', 'username', 'role', 'email')
  readonly_fields = ('date_joined', 'last_login')

  filter_horizontal = ()
  list_filter = ()
  fieldsets = ()

admin.site.register(UserAccount, AdminUser)
