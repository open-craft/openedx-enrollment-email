# -*- coding: utf-8 -*-
"""
ACE message types related to staff notifications of enrollments.
"""

from openedx.core.djangoapps.ace_common.message import BaseMessageType


class Enrolled(BaseMessageType):
    """
    A message to staff after a student enrolls into a course.
    """
    APP_LABEL = 'enrollment_email'

    def __init__(self, *args, **kwargs):
        super(Enrolled, self).__init__(*args, **kwargs)
        self.options['transactional'] = True  # pylint: disable=unsupported-assignment-operation
