from django.db import models
from django.db.models.fields import CharField, TextField, URLField, DateTimeField, IntegerField


# Create your models here.
class Article(models.Model):
    header_on_main_page = CharField("Header_on_main_page", max_length=100)
    description_on_main_page = CharField("description_on_main_page", max_length=150)
    Title = CharField("title", max_length=200)
    Header_on_article_page = CharField("Header_on_article_page", max_length=200)
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
    number = IntegerField("Number of paragraph", null=True)

    class Meta:
        verbose_name = "Параграф"
        verbose_name_plural = "Параграфы"
        unique_together = ("number", "article")
