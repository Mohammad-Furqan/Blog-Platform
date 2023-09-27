from django.contrib import admin
from blog.models import *
# Register your models here.
class BlogPostAdmin(admin.ModelAdmin):
  list_display = ("title", "author",'content',)

class UserProfileAdmin(admin.ModelAdmin):
  list_display=('user','profile_picture','bio')


admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(BlogPost,BlogPostAdmin)


