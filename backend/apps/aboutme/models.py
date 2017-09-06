# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class AboutMe(models.Model):
    version = models.CharField(max_length=6, default='v0.0.0')
    resume = models.FileField(null=True, blank=True)
    summary = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'About Me'
        verbose_name_plural = 'About Mes'
