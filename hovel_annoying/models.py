# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from hovel_annoying.model_utils import FilePathGenerator


class TempArchiveBase(models.Model):
    """Temporary archive for batch uploading and processing files"""

    STATUS_PENDING = 'pending'
    STATUS_PROCESSING = 'processing'
    STATUS_SUCCESS = 'success'
    STATUS_ERROR = 'error'
    STATUSES = ((STATUS_PENDING, 'Ожидает обработки'),
                (STATUS_PROCESSING, 'В процессе обработки'),
                (STATUS_SUCCESS, 'Успешно обработан'),
                (STATUS_ERROR, 'Ошибка при обработке'))

    status = models.CharField(verbose_name='статус', max_length=50,
                              choices=STATUSES, default=STATUS_PENDING)
    status_verbose = models.TextField(verbose_name='подробный статус',
                                      blank=True)
    archive = models.FileField(verbose_name='файл архива', blank=True,
                               upload_to=FilePathGenerator(
                                   to='temp_archives/'))
    load_user = models.ForeignKey(settings.AUTH_USER_MODEL,
                                  on_delete=models.CASCADE,
                                  verbose_name='кто загрузил',
                                  blank=True, null=True)
    load_datetime = models.DateTimeField(verbose_name='дата и время загрузки',
                                         blank=True, null=True)

    class Meta:
        abstract = True
        verbose_name = 'временный архив'
        verbose_name_plural = 'временные архивы'
