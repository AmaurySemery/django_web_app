from django.contrib import admin

from listings.models import Band

class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'year_formed', 'genre', 'biography') # liste les champs que nous voulons sur l'affichage de la liste

admin.site.register(Band, BandAdmin)