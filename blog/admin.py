from django.contrib import admin
from blog.models import Post

# Register your models here.

# @admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # date_hierarchy = 'created_date'
    # list_display = ('title','counted_views',
    #                 'status','published_date')
    # empty_value_display = '__empty__'
    # fields = ('title',)
    # list_filter = ('status','published_date')
    # ordering=['-created_date']
    # search_fields = ['title','content']
    pass

admin.site.register(Post,PostAdmin)
