from django.contrib import admin
from .models import *

admin.site.register(Category)
admin.site.register(PdCategory)
admin.site.register(Perk)
admin.site.register(UserPerk)