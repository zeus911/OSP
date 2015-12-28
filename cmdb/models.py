# -*- coding: utf-8 -*-
from django.db import models


class Update(models.Model):
    user_name = models.CharField(max_length=32, verbose_name=u'用户名')
    date = models.DateTimeField(verbose_name=u'更新时间')
    status = models.IntegerField(default=0, verbose_name=u'发布状态')
    update_project = models.CharField(max_length=100, null=True)
    file_path = models.FileField(upload_to='./upload/')
    old_file_path = models.CharField(max_length=100, verbose_name=u'上次备份', null=True)
    is_gray = models.BooleanField(default=0)
    desc = models.CharField(max_length=100, null=True, verbose_name=u'更新描述')

