from django.contrib import admin
# from blog.models import ARTICLE
# from blog.models import COMMENT

# Register your models here.
from blog.models import ARTICLE, USER, COMMENT


class ArticleAdmin(admin.ModelAdmin):
    exclude = ('update_time', 'read_count',)


class UserAdmin(admin.ModelAdmin):
    exclude = ('last_login',)


class CommentAdmin(admin.ModelAdmin):
    exclude = ('parent',)


admin.site.register(ARTICLE,ArticleAdmin)
admin.site.register(USER,UserAdmin)
admin.site.register(COMMENT,CommentAdmin)
