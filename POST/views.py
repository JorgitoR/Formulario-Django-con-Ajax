# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import JsonResponse
from .models import Post

def crear_post(request):
    posts = Post.objects.all()
    response_data = {}

    if request.POST.get('action') == 'post':
        titulo = request.POST.get('titulo')
        descripcion = request.POST.get('descripcion')

        response_data['titulo'] = titulo
        response_data['descripcion'] = descripcion

        Post.objects.create(
            titulo = titulo,
            descripcion = descripcion,
            )
        return JsonResponse(response_data)

    return render(request, 'crear_post.html', {'posts':posts})