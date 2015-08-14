# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response
from django import forms
from django.template import RequestContext
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
## gmapi
import simplejson as json

@login_required
def bump_map(request):
    return render_to_response('bump_hunter/bump_map.html',  # 使用するテンプレート
                              context_instance=RequestContext(request))  # その他標準のコンテキスト
