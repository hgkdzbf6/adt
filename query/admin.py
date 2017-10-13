# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from query.models import SystemCommonSensitiveWords
from query.models import SystemClause
from query.models import SystemImage
from query.models import SystemUserSimple

# Register your models here.
admin.site.register(SystemCommonSensitiveWords)
admin.site.register(SystemClause)
admin.site.register(SystemImage)
admin.site.register(SystemUserSimple)