# -*- coding: utf-8 -*-
"""
enrollment_email Django application initialization.
"""

from __future__ import absolute_import, unicode_literals

from django.apps import AppConfig


class EnrollmentEmailAppConfig(AppConfig):
    """
    Configuration for the enrollment_email Django application.
    """

    name = 'enrollment_email'
    plugin_app = {}

    def ready(self):
        from . import signals
