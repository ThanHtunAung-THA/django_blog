from django.contrib import admin
from blog.models import CategoryModel
from blog.models import PostModel
# Register your models here.
admin.site.register(CategoryModel)
admin.site.register(PostModel)