from django.db import models


# Create your models here.

class USER(models.Model):
    name = models.CharField(max_length=16)
    e_mail = models.CharField
    reg_date = models.DateField
    last_login_time = models.DateTimeField


class ARTICLE(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField
    author_id = models.ForeignKey(USER)
    read_count = models.IntegerField
    keyword = models.CharField
    update_time = models.DateTimeField
    del_flag = models.BooleanField


class COMMENT(models.Model):
    content = models.CharField
    article_id = models.ForeignKey(ARTICLE)
    reply_id = models.IntegerField
    del_flag = models.BooleanField
