from django.contrib import admin

# Register your models here.
from . models import AboutFives, Training, SupportTheClub, Sponsors, Donors

admin.site.register(AboutFives)
admin.site.register(Training)
admin.site.register(SupportTheClub)
admin.site.register(Sponsors)
admin.site.register(Donors)
