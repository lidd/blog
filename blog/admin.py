from django.contrib import admin
# from blog.models import ARTICLE
# from blog.models import COMMENT

# Register your models here.
from blog.models import ARTICLE, USER, COMMENT, CATEGORY


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name',)


class ArticleAdmin(admin.ModelAdmin):
    class Media:
        js = ('/static/simditor-2.3.6/scripts/jquery.min.js',
              '/static/simditor-2.3.6/scripts/module.js',
              '/static/simditor-2.3.6/scripts/hotkeys.js',
              '/static/simditor-2.3.6/scripts/uploader.js',
              '/static/simditor-2.3.6/scripts/simditor.js',)
        css = {
            "all": ('/static/simditor-2.3.6/styles/simditor.css',)
        }

    exclude = ('update_time', 'read_count',)
    list_display = ('title', 'author', 'update_time', 'category',)



class UserAdmin(admin.ModelAdmin):
    exclude = ('last_login',)


class CommentAdmin(admin.ModelAdmin):
    exclude = ('parent',)


admin.site.register(ARTICLE, ArticleAdmin)
admin.site.register(USER, UserAdmin)
admin.site.register(COMMENT, CommentAdmin)
admin.site.register(CATEGORY, CategoryAdmin)
