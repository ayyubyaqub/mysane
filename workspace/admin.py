from django.contrib import admin

from workspace.models import resume, work_space
from workspace.models import work_space_tag
# Register your models here.
admin.site.register(work_space_tag)
admin.site.register(work_space)
admin.site.register(resume)