from django.contrib import admin
from .models import CategoryModel , ArticleModel

# Register your models here.
def true( modeladmin , request , queryset):
    row = queryset.update(status=True)
    message = 'فعال شد'
    modeladmin.message_user(request,'{} دسته بندی {}'.format(row,message))
true.short_description = 'فعال کردن دسته بندیهای انتخاب شده'

def false( modeladmin , request , queryset):
    row = queryset.update(status=False)
    message = 'غیرفعال شد'
    modeladmin.message_user(request,'{} دسته بندی {}'.format(row,message))
false.short_description = 'غیرفعال کردن دسته بندیهای انتخاب شده'
class Category(admin.ModelAdmin):
    list_display = ('parent','title','slug','position','status')
    list_filter = (['status'])
    search_fields = ('title','status')
    prepulated_fields = {'slug':('title',)}
    actions = [true,false]
admin.site.register(CategoryModel,Category)

def publishe( modeladmin , request , queryset):
    row = queryset.update(status='publish')
    message = 'منتشر شد'
    modeladmin.message_user(request,'{} مقاله {}'.format(row,message))
publishe.short_description = 'منتشر کردن مقاله های انتخاب شده'

def drafte( modeladmin , request , queryset):
    row = queryset.update(status='draft')
    message = 'پیش نویس شد'
    modeladmin.message_user(request,'{} مقاله {}'.format(row,message))
drafte.short_description = 'پیش نویس کردن مقاله های انتخاب شده'
class Article(admin.ModelAdmin):
    list_display = ('auth','title','picture','slug','publish','status','category_list')
    list_filter = ('publish','status')
    search_fields = ('title','slug')
    prepulated_fields = {'slug':('title',)}
    actions = [publishe,drafte]
admin.site.register(ArticleModel,Article)