from django.http import HttpResponse, Http404
from django.shortcuts import redirect, render_to_response
from django.template import RequestContext
from django.utils import timezone
from django.core.urlresolvers import reverse
import json, os, datetime, operator

from forms import UploadFileForm
from content.settings import IMAGE_ROOT, DISPLAY_ROOT, URL_ROOT

def get_context(request):
    ctxt = RequestContext(request)
    ctxt['content_root'] = URL_ROOT
    return ctxt

class image():
    def __init__(self, url, name, md_change):
        self.url = url
        self.name = name
        self.md_change = md_change

def show(filepath):
    stat = os.stat(filepath)
    print "\n%s" % filepath
    print "last modified on:",
    print datetime.datetime.fromtimestamp(stat.st_mtime)
    print "last metadata change on:"
    print datetime.datetime.fromtimestamp(stat.st_ctime)

def image_urls():
    '''returns urls of all images in the
    gallery in reverse chronological order (not yet ordered)
    This should probably be cached'''
    filenames = os.listdir(IMAGE_ROOT)
    images = []
    for name in filenames:
        md_change = os.stat(IMAGE_ROOT+name).st_ctime
        url = DISPLAY_ROOT + name
        images.append( image(url, name, md_change) )
    images.sort(key=operator.attrgetter('md_change'), reverse=True)
    return images


def check(request):
    if not request.user.is_active:
        print "user not logged in"
        raise Http404

def main(request, template="gallery/display.html"):
    check(request)
    ctxt = get_context(request)
    ctxt['images'] = image_urls()
    return render_to_response(template, ctxt)

def selector(request):
    return main(request, "gallery/select.html")


# File upload stuff

def handle_uploaded_file(f, location):
    destination = open(location, 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()

def upload_file(request):
    ctxt = get_context(request)
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            location = IMAGE_ROOT + request.POST['name']
            handle_uploaded_file(request.FILES['file'], location)
            return redirect('../')
    else:
        form = UploadFileForm()
    ctxt['form'] = form
    return render_to_response('gallery/upload.html', ctxt)

def success(request):
    return redirect(reverse(main))
