from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


# Create your models here.

# 采用继承方式扩展用户信息
class USER(AbstractUser):
    avatar = models.ImageField(upload_to='avatar/%Y/%m', default='avatar/default.png')
    QQ = models.CharField(max_length=20, blank=True, null=True)
    mobile = models.CharField(max_length=11, blank=True, unique=True, null=True)

    # 备注
    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class CATEGORY(models.Model):
    category_name = models.CharField(max_length=10, verbose_name='分类名')

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.category_name


class ARTICLE(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField(max_length=2000, null=True, blank=True)
    author = models.ForeignKey(USER)
    read_count = models.IntegerField(default=0)
    keyword = models.CharField(max_length=100, null=True, blank=True)
    update_time = models.DateTimeField(default=timezone.now())
    del_flag = models.BooleanField
    category = models.ForeignKey(CATEGORY,default=1)

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class COMMENT(models.Model):
    content = models.CharField(max_length=200, null=True, blank=True)
    article = models.ForeignKey(ARTICLE)
    parent = models.ForeignKey('self', blank=True, null=True)
    del_flag = models.BooleanField(default=False)

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name
