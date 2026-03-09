from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin


admin.site.register(Student)
admin.site.register(Branches)
admin.site.register(Subjects)
admin.site.register(Notices)
admin.site.register(SubjectCombination)
admin.site.register(Results)
admin.site.register(GetResults)

