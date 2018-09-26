from django.db import models

# Create your models here.

class BookName(models.Model):
    title = models.CharField(verbose_name='标题',max_length=50)
    body = models.TextField(verbose_name='文章')
    author = models.CharField(verbose_name='作者',default='sing',max_length=50)
    slug = models.SlugField(verbose_name='索引后缀',unique=True)
    created_time = models.DateTimeField(verbose_name='创建时间',auto_now_add=True)
    update_time = models.DateTimeField(verbose_name='修改时间',auto_now=True)
    class Meta:
        verbose_name = '书名'
        verbose_name_plural = '图书馆'
        ordering = ['-created_time']

    # 使对象在后台显示更友善
    def __str__(self):
        return self.title

class Book(models.Model):
    # 章节级别
    BODY_LEVEL = (
        (1,'一级章节'),
        (2,'二级章节'),
        (3,'三级章节'),
        (4,'一级小节'),
        (5,'二级小节'),
        (6,'三级小节'),
    )

    title = models.CharField(verbose_name='标题',max_length=50)
    body = models.TextField(verbose_name='文章')
    slug = models.SlugField(verbose_name='索引后缀',unique=True)
    body_level = models.IntegerField(choices=BODY_LEVEL,verbose_name='级别')
    body_page = models.IntegerField(verbose_name='页码顺序',help_text='用于自定义章节的顺序')
    body_parent = models.ForeignKey('self',blank=True,null=True,blank=True,verbose_name='所属章节')
    bookname = models.ForeignKey(BookName,verbose_name='所属书名')
    created_time = models.DateTimeField(verbose_name='创建时间',auto_now_add=True)
    update_time = models.DateTimeField(verbose_name='修改时间',auto_now=True)
    class Meta:
        verbose_name = '章节'
        verbose_name_plural = '章节列表'
        ordering = ['body_page']

    # 使对象在后台显示更友善
    def __str__(self):
        return self.title
