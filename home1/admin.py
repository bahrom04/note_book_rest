from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Categories)
admin.site.register(Authors)
admin.site.register(Posts)
admin.site.register(ResentlyPosteds)
admin.site.register(Popular)
admin.site.register(Featured)
admin.site.register(TopAuthors)
admin.site.register(TodaysUpdates)

