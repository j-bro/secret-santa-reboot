from django.contrib import admin

from .models import Exchange, PersonGroup, GiftList, Draw

# Register your models here.

admin.site.register(Exchange)
admin.site.register(PersonGroup)
admin.site.register(GiftList)
admin.site.register(Draw)
