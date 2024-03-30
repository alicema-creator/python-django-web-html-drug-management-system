from django.contrib import admin
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import time
import openpyxl

#from .models import Article
from .models import Article
from .models import DataLatest


# Register your models here.

#admin.site.register(Article)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id','category', 'usert', 'title', 'data1', 'data2','data3',  'pub_date', 'update_time',)


    search_fields = ('category',)



    print("articleheadimg")

    actions = ['export_excel', 'custom_button']

    def export_excel(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        cn_name = ['id','category','usert', 'title',  'data1', 'data2','data3',  'pub_date', 'update_time',]
        #field_names = ['quyu', 'Akcs', 'Akcj', 'Bkcs', 'Bkcj', 'Ckcs', 'Ckcj', 'kc_date', 'note']

        today_time = time.strftime('%Y%m%d%H%M%S', time.localtime())
        filename = f'{str(meta)[7:]}' + '_' + f'{today_time}'

        response = HttpResponse(content_type='application/msexcel')
        response['Content-Disposition'] = f'attachment; filename={filename}.xlsx'
        wb = openpyxl.Workbook()
        ws = wb.active
        # ws.append(field_names)
        ws.append(cn_name)  # 写入中文表头
        for obj in queryset:
            for field in field_names:
                data = [f'{getattr(obj, field)}' for field in field_names]
            row = ws.append(data)
        wb.save(response)
        self.message_user(request, f"{request.user.username}导出库存数据<{filename}.xlsx>")
        return response


    export_excel.type = 'success'

    export_excel.short_description = '导出数据'


    #wangEditor引入
    class Media:  # 通过此方法将js文件插入到页面中
        js = (
            'admin/js/vendor/jquery/jquery.min.js',  # Django自带的jQuery
            # 通过CDN的方法引入wangeditor的js文件
            'https://cdn.jsdelivr.net/npm/wangeditor@latest/dist/wangEditor.min.js',
            'js/wang_editor_config.js'  # wangeditor主要的配置文件
        )
    # wangEditor引入结束



class DataLatestAdmin(admin.ModelAdmin):
    list_display = ('id','category', 'usert', 'title', 'data1', 'data2','data3',  'pub_date', 'update_time',)


    search_fields = ('category',)



    print("articleheadimg")

    actions = ['export_excel', 'custom_button']


    def export_excel(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        cn_name = ['id','category','usert', 'title', 'image_data', 'pub_date', 'update_time',]
        #field_names = ['quyu', 'Akcs', 'Akcj', 'Bkcs', 'Bkcj', 'Ckcs', 'Ckcj', 'kc_date', 'note']

        today_time = time.strftime('%Y%m%d%H%M%S', time.localtime())
        filename = f'{str(meta)[7:]}' + '_' + f'{today_time}'

        response = HttpResponse(content_type='application/msexcel')
        response['Content-Disposition'] = f'attachment; filename={filename}.xlsx'
        wb = openpyxl.Workbook()
        ws = wb.active
        # ws.append(field_names)
        ws.append(cn_name)  # 写入中文表头
        for obj in queryset:
            for field in field_names:
                data = [f'{getattr(obj, field)}' for field in field_names]
            row = ws.append(data)
        wb.save(response)
        self.message_user(request, f"{request.user.username}导出库存数据<{filename}.xlsx>")
        return response


    # 指定element-ui的按钮类型，参考https://element.eleme.cn/#/zh-CN/component/button
    export_excel.type = 'success'
    #custom_button.type = 'success'
    # 给按钮追加自定义的文字颜色
    # custom_button.style = 'color:red;'
    # 显示的文本，与django admin一致
    export_excel.short_description = '导出数据'
    #custom_button.short_description = '测试按钮2'








admin.site.register(Article, ArticleAdmin)
admin.site.register(DataLatest, DataLatestAdmin)


# 页面标题
admin.site.site_title="后台管理系统"
# 登录页导航条和首页导航条标题
admin.site.site_header="后台管理"
admin.site.index_title = "后台首页"






