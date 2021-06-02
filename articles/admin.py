from django.contrib import admin
from .models import Article
from .models import Paragraph

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("Title", "date_of_pub")
    ordering = ('-date_of_pub',)

class ParagraphAdmin(admin.ModelAdmin):
    list_display = ("article", "number")
    list_filter = ("article",)
    ordering = ('number',)


admin.site.register(Article, ArticleAdmin)
admin.site.register(Paragraph, ParagraphAdmin)