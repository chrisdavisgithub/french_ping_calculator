"""Urls for french_ping_calculator"""
from django.conf import settings
from django.contrib import admin
from django.conf.urls import url
from django.conf.urls import include
from django.conf.urls import patterns

from calculator.views import PingCalculatorView

urlpatterns = patterns('',
    url(r'^$', PingCalculatorView.as_view(), name='home'),
)
