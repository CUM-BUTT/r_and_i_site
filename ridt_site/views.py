from PIL import Image
from PIL.JpegImagePlugin import JpegImageFile
from django.core.files.base import ContentFile
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.

def Home(request):
    return render(request, 'main/home.html')


def GoToBuilder(request, ):
    url = request.POST.get('url', '')
    return render(request, 'main/builder.html', context={'url': url})


def Builder(request, ):
    email = request.POST.get('email', '')

    url = request.POST.get('url', '')
    app_name = request.POST.get('app_name', '')
    app_id = request.POST.get('app_id', '')
    image = request.FILES['image']

    image: Image = Image.open(image)
    image.save(open('cat.jpeg', 'wb'))

    return render(request, 'main/success.html')