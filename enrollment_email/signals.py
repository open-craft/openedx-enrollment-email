# -*- coding: utf-8 -*-
"""
Signals to detect enrollments.
"""

import logging
from django.dispatch import receiver

from student.models import ENROLL_STATUS_CHANGE, EnrollStatusChange

LOGGER = logging.getLogger(__name__)

@receiver(ENROLL_STATUS_CHANGE)
def send_email_to_staff_on_student_enrollment(sender, event=None, user=None, **kwargs):  # pylint: disable=unused-argument
    """
    """

    print(event)
    raise NotImplementedError("Continue porting code from https://github.com/edx/edx-platform/pull/16669 and transform it into a plugin")
    if event == EnrollStatusChange.enroll:
        raise NotImplementedError("enrolling")
