# coding:utf-8
from django.db import models
from django.utils.html import format_html

# Create your models here.

#添加admin商品管理模块
class Article(models.Model):  


    usert = models.CharField(u'用户名',  max_length=256)
    category = models.CharField(u'类目', max_length=256)
    title = models.CharField(u'标题', max_length=256)
    data1 = models.CharField(u'编码', max_length=256, blank=True, null=True)
    data2 = models.CharField(u'状态', max_length=256, blank=True, null=True)
    data3 = models.CharField(u'技术', max_length=256, blank=True, null=True)


    content = models.TextField(u'内容', blank=True, null=True)

    pub_date = models.DateTimeField(u'发表时间', auto_now_add=True, editable=True, blank=True, null=True)
    update_time = models.DateTimeField(u'更新时间', auto_now=True, blank=True, null=True)


    def image_data(self):
        return format_html(
            '<img src="../../../media/{}" width="90px"/>',
            self.img,

        )
    image_data.short_description = u'相片'



    def __str__(self):  # 在Python3中用 __str__ 代替 __unicode__
        return self.title

    class Meta:
        # db_table = ''
        # managed = True
        verbose_name = '所有信息'
        verbose_name_plural = '所有信息'


class DataLatest(models.Model):  


    usert = models.CharField(u'用户名',  max_length=256)
    category = models.CharField(u'类目', max_length=256)
    title = models.CharField(u'标题', max_length=256)
    data1 = models.CharField(u'编码', max_length=256, blank=True, null=True)
    data2 = models.CharField(u'状态', max_length=256, blank=True, null=True)
    data3 = models.CharField(u'CMS', max_length=256, blank=True, null=True)

    img2 = models.ImageField(u'相片2', upload_to='imgs/', blank=True, null=True)
    content = models.TextField(u'内容', blank=True, null=True)

    pub_date = models.DateTimeField(u'发表时间', auto_now_add=True, editable=True, blank=True, null=True)
    update_time = models.DateTimeField(u'更新时间', auto_now=True, blank=True, null=True)


    def image_data(self):
        return format_html(
            '<img src="../../../media/{}" width="90px"/>',
            self.img,

        )
    image_data.short_description = u'相片'

    def __str__(self):  # 在Python3中用 __str__ 代替 __unicode__
        return self.title

    class Meta:
        # db_table = ''
        # managed = True
        verbose_name = '最新信息'
        verbose_name_plural = '最新信息'