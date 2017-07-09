from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.forms import TextInput, Textarea
from django.db import models

from .models import Profile
from .models import Answer
from .models import Code

class UserCodeAdmin(admin.ModelAdmin):
    list_display = ('user','date','code','confirmed')

admin.site.register(Code, UserCodeAdmin)

class UserAnswerAdmin(admin.ModelAdmin):
    list_display = ('user','pub_date','answer_text','prize')
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'style':'width: 500px'})},
    }

admin.site.register(Answer, UserAnswerAdmin)




class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'get_points','get_vouchers','get_premium')
    list_select_related = ('profile', )

    def get_points(self, instance):
        return instance.profile.points
    get_points.short_description = 'Points'

    def get_vouchers(self, instance):
        return instance.profile.vouchers
    get_vouchers.short_description = 'Vouchers'

    def get_premium(self, instance):
        return instance.profile.premium
    get_premium.short_description = 'Premium'

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
