# -*- coding: utf-8 -*-
"""
Signals to detect enrollments.
"""

import logging
from edx_ace import ace
from edx_ace.recipient import Recipient
from django.contrib.sites.models import Site
from django.dispatch import receiver
from message_types import Enrolled
from openedx.core.djangoapps.ace_common.template_context import get_base_template_context
from student.models import ENROLL_STATUS_CHANGE, EnrollStatusChange

LOGGER = logging.getLogger(__name__)

@receiver(ENROLL_STATUS_CHANGE)
def send_email_to_staff_on_student_enrollment(sender, event=None, user=None, **kwargs):  # pylint: disable=unused-argument
    """
    Sends an e-mail to staff after a new enrollment.
    """
    if event == EnrollStatusChange.enroll:
        course_id = kwargs['course_id'].to_deprecated_string()
        LOGGER.debug('Sending enrollment notification (user %i, %course %s)', user.id, course_id)
        site = Site.objects.get_current()
        message_context = get_base_template_context(site)
        message_context.update({
            'username': user.username,
            'user_full_name': user.profile.name if hasattr(user, 'profile') else None,
            'course_id': course_id
        }),

        message = Enrolled().personalize(
            recipient=Recipient(username='', email_address='…@….com'),  # FIXME define a setting and set it
            language=None,  # FIXME
            user_context=message_context,
        )

        ace.send(message)
    raise NotImplementedError("Continue portings code from https://github.com/edx/edx-platform/pull/16669 and transform it into a plugin")
