from django.db import models
from django.utils import timezone
from account.models import User
from django.utils.html import format_html

# Create your models here.
class CategoryModel(models.Model):
    parent = models.ForeignKey('self',blank=True,default=None,null=True,on_delete=models.SET_NULL,related_name='parents',verbose_name='دسته بندی')
    title = models.CharField(max_length=300,verbose_name='عنوان')
    slug = models.SlugField(unique=True,max_length=200,verbose_name='آدرس')
    position = models.IntegerField(verbose_name='پوزیشن')
    status = models.BooleanField(default=True,verbose_name='وظعیت')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندیها'
        ordering = ['parent__id','position']

class ArticleModel(models.Model):
    auth = models.ForeignKey(User,null=True,on_delete=models.SET_NULL,related_name='author',verbose_name='نویسنده')
    title = models.CharField(max_length=300,verbose_name='عنوان')
    slug = models.SlugField(unique=True,max_length=200,verbose_name='آدرس')
    category = models.ManyToManyField(CategoryModel,related_name='children',verbose_name='دسته بندی')
    description = models.TextField(verbose_name='محتوا')
    thumbnail = models.ImageField(verbose_name='تصاویر')
    create = models.DateTimeField(verbose_name='زمان ساخت')
    publish = models.DateTimeField(default=timezone.now,verbose_name='زمان انتشار')
    update = models.DateTimeField(verbose_name='بروز رسانی در')
    STATUS = (
        ('publish','منتشر شد'),
        ('draft','پیش نویس'),
        ('lock','در انتظار تعیین وظعیت'),
        ('back','رد شد!!'),
    )
    status = models.CharField(max_length=30,choices=STATUS,verbose_name='وظعیت')

    def __str__(self):
        return self.title

    def category_list(self):
        return " ,".join([cat.title for cat in self.category.all()])
    category_list.short_description = 'دسته بندی'

    def picture(self):
        return format_html('<img width=75 style=border-radius:15px height=100 src={}>'.format(self.thumbnail.url))
    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'
        ordering = ['publish']