from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import *

# admin.site.register(Log)
admin.site.register(Log, SimpleHistoryAdmin)
