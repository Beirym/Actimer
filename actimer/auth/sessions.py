from .models import Session

from actimer.ip import getIP

import uuid


def createSession(request, user) -> None:
    session = Session.objects.create(
        id=str(uuid.uuid4()),
        user=user, 
        ip=getIP(request)
    )
    saveUserDataInSessions(request, session, user)


def saveUserDataInSessions(request, session, user) -> None:
    request.session['session_id'] = session.id

    request.session['user'] = {
        'id': user.id,
        'email': user.email,
        'timezone': user.timezone,
    }
    request.session.save()