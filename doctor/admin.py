from django.contrib import admin
from .models import Tempstorage


# FOR APPOINTMENT
class TempAdmin(admin.ModelAdmin):
    # ordering = ('-date',)
    list_display = ( 'id', 'image' )

    fieldsets = (
        (None, {'fields': ('image',)}),
    )
    

admin.site.register(Tempstorage, TempAdmin)