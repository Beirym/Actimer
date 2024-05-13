from .models import Session

from actimer.ip import getIP

import datetime


def is_auth(request) -> int:
    '''Checks the session for communication with an authorized employee.

    If the request contains a session_id that is associated with an authorized
    by an employee, the employee_id will be returned. Otherwise, no.'''

    session_id = request.session.get('session_id')
    if session_id:
        try:
            session = Session.objects.select_related('user').get(pk=session_id)

            if session.ip == getIP(request) \
                and (datetime.date.today() - session.authDate.date()).days < 7:
                return session.user
            else:
                Session.objects.delete(pk=session_id)
        except Session.DoesNotExist:
            return