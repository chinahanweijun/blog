from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

'''null：如果为True，Django将用NULL来在数据库中存储空值。默认值是False。
   blank:如果为True，该字段允许不填，默认为False
   choices:由二项元组构成的一个可迭代对象（例如，列表或元组），用来给字段提供选择项。如果设置了choices，默认的表单将是一个选择框而不是标准的文本框，而且这个选择框的选项就是choices中的选项。
   default:字段的默认值。可以是一个值或者可调用对象
   help_text:表单部件额外显示的帮助内容。
   primary_key:如果为True，那么这个字段就是模型的主键。
   unique:如果该值设置为True，这个数据字段在整张表中必须是唯一的
'''
class User(AbstractUser):
    # 用户
    avatar = models.ImageField(
        upload_to='avatar/%Y/%m', default='avatar/default.png',
        max_length=186, blank=True, null=True, verbose_name='头像')
    phone = models.CharField(max_length=11, blank=True, null=True,
                             unique=True, verbose_name='手机号码')

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name
        ordering = ['-id', 'username']

    def __str__(self):
        return self.username

class Category():
    # 文章分类
    name = models.CharField(max_length=25, verbose_name='分类名称')
    idnex = models.IntegerField(default=999, verbose_name='排序')

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name
        ordering = ['index', 'id']

    def __str__(self):
        return  self.name


class Article(models.Model):
# 文章模型
    title = models.CharField(max_length=50, verbose_name='标题')
    content = models.TextField(verbose_name='内容')
    desc = models.CharField(max_length=50, verbose_name='描述')
    click_count = models.IntegerField(default=0, verbose_name='点击数')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    uid = models.ForeignKey(User, verbose_name='用户')
    category = models.ForeignKey(Category, blank=True, verbose_name='分类')

    tag = models.ManyToManyField(Tag, verbose_name='标签')

    objects = ArticleManage()
    # 文章模型中加入自定义的管理器

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        ordering = ['create_date','click_count']

    def __str__(self):
        return self.title


class ArticleManage(models.Model):
    # 自定义一个数据处理方法
    def distinct_date(self):
        distinct_date_list = []
        date_list = self.values('create_date')
        for date in date_list:
            # 转换日期格式
            date = date['create_date'].strftime('%Y/%m文档存档')
            if date not in distinct_date_list:
                distinct_date_list.append(date)
        return distinct_date_list


class Tag(models.Modle):
    # 创建Tag标签
    name = models.CharField(max_length=30, verbose_name="标签")


    class Meta:
        # 后台admin显示
        verbose_name = '标签'
        verbose_name_plural = verbose_name
        orfering = ['id']

    def __str__(self):
    # 调用时返回自身的一些属性
        return self.name



