from django.contrib import admin

# Register your models here.
from .models import Language,Basic_Information,Education,Project

admin.site.register(Language)
admin.site.register(Basic_Information)
admin.site.register(Education)
admin.site.register(Project)