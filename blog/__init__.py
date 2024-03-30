import pymysql
pymysql.install_as_MySQLdb()

#修改后台Blog App名称
from os import path
from django.apps import AppConfig

VERBOSE_APP_NAME = "YOUR VERBOSE APP NAME HERE"

def get_current_app_name(file):
    return path.dirname(file).replace('\\', '/').split('/')[-1]

class AppVerboseNameConfig(AppConfig):
    name = get_current_app_name(__file__)
    verbose_name = u'项目管理'

default_app_config = get_current_app_name(__file__) + '.__init__.AppVerboseNameConfig'
#修改后台Blog App名称结束

