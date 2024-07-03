import os

from django.http import HttpResponse
from .services import  get_college_list, get_college_logo, crawl_college_data

# /college
def getCollegeInfo(request):
    return get_college_list(request)

# /college/crawler
def crawlCollegeData(request):
    return crawl_college_data(request)
# /college/logo/filename
def getCollegeLogo(request,filename):
    return get_college_logo(request,filename)

def getCollegeLogo(request,filename):
    path = os.path.dirname(os.path.abspath(__file__))
    imagepath = path + "\\static\\" + filename
    image_data = open(imagepath, "rb").read()
    return HttpResponse(image_data, content_type="image/png")