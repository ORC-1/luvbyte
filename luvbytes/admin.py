from django.contrib import admin
from . models import sms, tips, voice, simple_log
# Register your models here.

admin.site.register(sms)
admin.site.register(simple_log)
