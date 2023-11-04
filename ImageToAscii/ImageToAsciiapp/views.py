from django.shortcuts import render
from django.http import HttpResponse,FileResponse
from ascii_magic import AsciiArt
from html2image import *
import os

def home(request):
    return render(request,'home.html')
def download(request):
    img=request.FILES.get('img')
    t=request.POST.get('t')
    if img:
        art=AsciiArt.from_image(img)
        art.to_html_file('file.html',char=t)
        with open('file.html', 'rb') as html_file:
            response = HttpResponse(html_file.read(), content_type='text/html')
            response['Content-Disposition'] = 'attachment; filename="ascii.html"'
        return response
        

   
    