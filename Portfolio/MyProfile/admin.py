from django.contrib import admin

# Register your models here.
from .models import Language,Basic_Information,Education

admin.site.register(Language)
admin.site.register(Basic_Information)
admin.site.register(Education)