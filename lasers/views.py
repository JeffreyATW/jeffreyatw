import datetime
import time
from django.contrib.sessions.models import Session
from django.http import HttpResponse
from django.utils import simplejson

def _get_coords():
    coords = []
    # Query database for all sessions
    sessions = Session.objects.all()
    # Set latest_update to 0 for starters
    latest_update = 0
    for session in sessions:
        # Get object from encoded session data
        decoded_session = session.get_decoded()
        # Check if this is a lasers-specific session
        if decoded_session.get('lasers', False):
            # Check for an expired or misconfigured session
            if session.expire_date < datetime.datetime.now() or \
               decoded_session.get('x', None) == None:
                session.delete()
            else:
                # After iterating through all sessions, latest_update will be
                # correct
                if decoded_session.get('updated', 0) > latest_update:
                    latest_update = decoded_session.get('updated', 0)
                # Add the session key to the coordinate data so the DOM knows
                # which sessions are active and doesn't have to be rebuilt
                decoded_session['session_key'] = session.session_key
                coords.append(decoded_session)
    # Sort coords by last updated.
    coords.sort(key=lambda coord: coord['updated'], reverse=True)
    # Truncate to 10 users.
    coords = coords[:10]
    return (coords, latest_update)

def coords(request):
    # Store this session as a lasers-specific session
    request.session['lasers'] = True
    # Stuff to do only if receiving new coords
    if request.method == 'POST':
        request.session['x'] = request.POST.get('x', 0)
        request.session['y'] = request.POST.get('y', 0)
        request.session['r'] = request.POST.get('r', 0)
        request.session['g'] = request.POST.get('g', 0)
        request.session['b'] = request.POST.get('b', 0)
        request.session['name'] = request.POST.get('name', None)
        # Update the time this session was updated
        request.session['updated'] = time.time()
    # Get a list of coords of all active sessions
    # Also get the timestamp of the latest update
    coords, latest_update = _get_coords()
    # Set this session to expire in 100 seconds
    request.session.set_expiry(100)
    # Always send new data back when receiving new coords
    if request.method == 'POST':
        data = simplejson.dumps(coords) 
    if request.method == 'GET':
        # If latest update hasn't been set or there is a newer update than the
        # last time this session sent or received data
        if (latest_update == 0 or latest_update > request.session.get( \
            'updated', time.time())):
            data = simplejson.dumps(coords)
            # Set this session's updated time to the latest update so we know
            # it's up to date
            request.session['updated'] = latest_update
        # If there isn't a newer update, don't send anything
        else:
            data = {}
    return HttpResponse(data)
