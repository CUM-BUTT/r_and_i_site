from urllib import request

from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from requests import Response
from rest_framework.views import APIView
from django.shortcuts import render
#from builder.builder import Builder
# Create your views here.

from rest_framework.permissions import AllowAny

"""class Builder(APIView):
    permission_classes = (AllowAny,)
    def post(self, request, format=None):
        return(Response("hi"))
"""

class BuilderView(TemplateView):
    template_name = 'main/builder.html'
    http_method_names = ['get', 'post']

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        image = request.FILES['image']
        data = dict(request.POST)

        data = {key: val[0] for key, val in data.items()}
        data["randi_url"] = request.build_absolute_uri('/')

        print(data)
        #Builder(data, image).Build()

        return render(request, 'main/success.html',)
