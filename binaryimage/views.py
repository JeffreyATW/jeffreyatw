import base64
from django.shortcuts import render_to_response

def index(request):
    return render_to_response('binaryimage/index.html')

def ascii(request):
    expose = {}
    if request.method == "POST":
        try:
            file = request.FILES['file']
            if file.content_type == "image/gif" or \
               file.content_type == "image/png" or \
               file.content_type == "image/vnd.microsoft.icon" or \
               file.content_type == "image/x-icon":
                expose['content_type'] = file.content_type
                if file.size <= (1024 * 1024):
                    expose['data'] = base64.encodestring(file.read()).replace("\n","\"+\n\"")
                else:
                    expose['error'] = "Please upload a file 1MB or smaller."
            else:
                expose['error'] = "Please upload a GIF, PNG, or ICO image. (You uploaded %s)" % file.content_type
        except KeyError:
            expose['error'] = "Please choose a file."
    else:
        expose['error'] = "Please submit a form."
    try:
        expose['error']
        return render_to_response('binaryimage/index.html', expose)
    except KeyError:
        return render_to_response('binaryimage/ascii.html', expose)

def binary(request):
    expose = {}
    if request.method == "POST":
        try:
            expose['ascii'] = request.POST['text']
        except KeyError:
            expose['error'] = "Please enter some text."
    else:
        expose['error'] = "Please submit a form."
    try:
        expose['error']
        return render_to_response('binaryimage/index.html', expose)
    except KeyError:
        return render_to_response('binaryimage/binary.html', expose)
