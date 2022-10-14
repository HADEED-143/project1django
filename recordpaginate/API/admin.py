from django.contrib import admin

# Register your models here.
from . models import cases , labs, quarantine, sqliteseq, summery, vaccine

admin.site.register(cases)
admin.site.register(labs)
admin.site.register(quarantine)
admin.site.register(sqliteseq)
admin.site.register(summery)
admin.site.register(vaccine)