from django.contrib import admin

from listings.models import Band, Listing

class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'year_formed', 'genre', 'biography') # liste les champs que nous voulons sur l'affichage de la liste

class ListingAdmin(admin.ModelAdmin):
    list_display = ('title','description', 'sold', 'year', 'type', 'band')

admin.site.register(Band, BandAdmin)
admin.site.register(Listing, ListingAdmin)
