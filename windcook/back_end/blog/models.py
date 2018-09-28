from django.db import models

# 标签
class BlogTag(models.Model):
    name = models.CharField(max_length=64,verbose_name='标签名')
    slug = models.SlugField(unique=True,verbose_name='标签索引')
    body = models.TextField(verbose_name='简介')
    class Meta:
        verbose_name = '标签'
        verbose_name_plural = '标签列表'
        ordering = ['id']       # 排序，按id排序

    # 使对象在后台显示更友善
    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(verbose_name='标题',max_length=50)
    body = models.TextField(verbose_name='文章')
    author = models.CharField(verbose_name='作者',default='sing',max_length=50)
    created_time = models.DateTimeField(verbose_name='创建时间',auto_now_add=True)
    update_time = models.DateTimeField(verbose_name='修改时间',auto_now=True)
    slug = models.SlugField(verbose_name='后缀',unique=True)
    blog_tag = models.ManyToManyField(BlogTag,verbose_name='博客标签',related_name='blog_card')


    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        ordering = ['-created_time']

    # 使对象在后台显示更友善
    def __str__(self):
        return self.title
    # 分页
    def get_pre(self):# 上一页
        return Blog.objects.filter(id__lt=self.id).order_by('-id').first()

    def get_next(self):#下一页
        return Blog.objects.filter(id__gt=self.id).order_by('id').first()
