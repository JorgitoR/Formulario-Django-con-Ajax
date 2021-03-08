# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Post (models.Model):
    titulo             = models.CharField(max_length=50)
    descripcion = models.TextField()

    def __str__(self):
        return self.titulo