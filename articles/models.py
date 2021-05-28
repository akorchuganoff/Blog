from django.db import models
from django.db.models.fields import CharField, TextField, URLField, DateTimeField, IntegerField
import django


# Create your models here.
class Article(models.Model):
    header_on_main_page = CharField("Header_on_main_page", max_length=200)
    description_on_main_page = CharField("description_on_main_page", max_length=200)
    Title = CharField("title", max_length=200)
    Header_on_article_page = CharField("Header_on_article_page", max_length=200)
    Text_of_article = TextField("Text_of_article")
    github_url = URLField("github_url")
    date_of_pub = DateTimeField(auto_now_add=True)
    TopImage = models.ImageField(null=True)

    def __str__(self):
        return self.Header_on_article_page


    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"


class Paragraph(models.Model):
    image = models.ImageField(upload_to='gallery', null=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='paragraphs')
    paragraph = TextField("Text of paragraph")
    numder = IntegerField("Number of paragraph")

    class Meta:
        verbose_name = "Параграф"
        verbose_name_plural = "Параграфы"
