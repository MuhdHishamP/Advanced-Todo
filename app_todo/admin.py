from django.contrib import admin
from .models import tag,TodoDetails


class TodoDetailsAdmin(admin.ModelAdmin):
    filter_horizontal = ('tag',)
    list_filter = ('status','due_date',)
    readonly_fields = ('timestamp',)
    fieldsets = (('Primary Information',{'fields':('title','description')}),
                 ('Secondary Information',{'fields':('due_date','status','tag','timestamp')}),)
    
class tagAdmin(admin.ModelAdmin):
    search_fields = ('tag_name',)

# Register your models here.
admin.site.register(tag,tagAdmin)
admin.site.register(TodoDetails,TodoDetailsAdmin)

