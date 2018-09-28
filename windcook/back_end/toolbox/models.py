from django.db import models

# 网站信息
class MySiteData(models.Model):
    logo = models.CharField(max_length=30,verbose_name='网站标题')
    introduction = models.CharField(max_length=64,verbose_name='网站简介')
    source_of_power = models.CharField(max_length=64,verbose_name='网站作者和网站框架')
    approval_number = models.CharField(max_length=64,verbose_name='网站审批号')

    class Meta:
        verbose_name = '网站信息'
        verbose_name_plural = verbose_name
        ordering = ['id']

    # 使对象在后台显示更友善
    def __str__(self):
        return self.logo

# 个人空间
class SpaceLink(models.Model):
    name = models.CharField(max_length=64,verbose_name='链接名称')
    link = models.URLField(verbose_name='友链地址', help_text='请填写http或https开头的完整形式地址')

    class Meta:
        verbose_name = '个人链接'
        verbose_name_plural = '个人空间链接列表'
        ordering = ['id']  # 排序，按id排序

    # 使对象在后台显示更友善
    def __str__(self):
        return self.name


# 友情链接
class FriendLink(models.Model):
    name = models.CharField(max_length=64,verbose_name='链接名称')
    link = models.URLField(verbose_name='友链地址', help_text='请填写http或https开头的完整形式地址')

    class Meta:
        verbose_name = '友情链接'
        verbose_name_plural = '友情链接列表'
        ordering = ['id']  # 排序，按id排序

    # 使对象在后台显示更友善
    def __str__(self):
        return self.name

# 书籍链接
class BookLink(models.Model):
    name = models.CharField(max_length=64,verbose_name='链接名称')
    link = models.URLField('书籍链接', help_text='请填写http或https开头的完整形式地址')

    class Meta:
        verbose_name = '书籍'
        verbose_name_plural = '书籍链接列表'
        ordering = ['id']  # 排序，按id排序

    # 使对象在后台显示更友善
    def __str__(self):
        return self.name

# 首页公告

class Home(models.Model):
    title = models.CharField(verbose_name='标题',max_length=50)
    body = models.TextField(verbose_name='文章')
    author = models.CharField(verbose_name='作者',default='sing',max_length=50)
    created_time = models.DateTimeField(verbose_name='创建时间',auto_now_add=True)
    update_time = models.DateTimeField(verbose_name='修改时间',auto_now=True)


    class Meta:
        verbose_name = '公告和首页信息'
        verbose_name_plural = verbose_name
        ordering = ['-created_time']

    # 使对象在后台显示更友善
    def __str__(self):
        return self.title

class About(models.Model):
    title = models.CharField(verbose_name='标题',max_length=50)
    body = models.TextField(verbose_name='文章')
    author = models.CharField(verbose_name='作者',default='sing',max_length=50)
    created_time = models.DateTimeField(verbose_name='创建时间',auto_now_add=True)
    update_time = models.DateTimeField(verbose_name='修改时间',auto_now=True)



    class Meta:
        verbose_name = '关于页面内容'
        verbose_name_plural = verbose_name
        ordering = ['-created_time']

    # 使对象在后台显示更友善
    def __str__(self):
        return self.title

class GitBookLink(models.Model):
    name = models.CharField(max_length=64,verbose_name='链接名称')
    link = models.URLField('书籍链接', help_text='请填写http或https开头的完整形式地址')
    book_status = models.CharField(verbose_name='状态',default='未完成',max_length=50)
    class Meta:
        verbose_name = '书籍'
        verbose_name_plural = 'GitBook链接列表'
        ordering = ['id']  # 排序，按id排序

    # 使对象在后台显示更友善
    def __str__(self):
        return self.name
