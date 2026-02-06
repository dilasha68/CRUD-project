from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import BlogModel

@admin . register ( BlogModel )
class BlogModelAdmin ( admin . ModelAdmin ) :
    list_display = ('title ', 'author ', ' last_updated ', ' date_of_post ')
    list_filter = (' date_of_post ', 'author ')
    search_fields = ('title ', 'author')