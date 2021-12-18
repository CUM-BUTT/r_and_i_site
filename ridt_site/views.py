from PIL import Image
from PIL.JpegImagePlugin import JpegImageFile
from django.core.files.base import ContentFile
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.

def RidtMain(request):
    return render(request, 'main/home.html')


def UrlInput(request,):
    url = request.POST.get('url', '')
    return render(request, 'main/builder.html', context={'url': url})


def Constructor(request,):
    url = request.POST.get('url', '')
    app_name = request.POST.get('app_name', '')
    app_id = request.POST.get('app_id', '')
    image = request.FILES['image']

    image: JpegImageFile = Image.open(image)
    image.save(open('cat.jpeg', 'wb'))
    #open('cat.jpeg', 'wb').write(image)

    return render(request, 'main/rate_choise.html')

def PaymentsPro(request):
    # TODO add builder code
    return render(request, 'main/home.html')

def PaymentsStandart(request):
    # TODO add builder code
    return render(request, 'main/home.html')