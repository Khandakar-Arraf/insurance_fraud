from ..models import Client
from django.shortcuts import render,get_object_or_404
from ..serializers import DataSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
import io



@csrf_exempt
def client_api(request):
    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        if id is not None:
            cli = Client.objects.get(client_id=id)
            serialize = DataSerializer(cli)
            json_data = JSONRenderer().render(serialize.data)
            return HttpResponse(json_data,content_type='application/json')


    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data_format = JSONParser().parse(stream)
        serialize = DataSerializer(data=python_data_format)
        if serialize.is_valid():
            serialize.save()
            res ={'msg':'data created successfully'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')

        return HttpResponse(JSONRenderer().render(serialize.errors),content_type='application/json')




def client_details(request,id):
    
   # client = Client.objects.get(client_id=id)
    try:
        client = get_object_or_404(Client, client_id=id)
        serializer = DataSerializer(client)
        return JsonResponse(serializer.data)
    except not client:
        return HttpResponse("Client does not exist", status=404)


@csrf_exempt
def create_client(request):
    json_data = request.body
    if request.method == 'POST':
        #json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = DataSerializer(data=python_data)

        if serializer.is_valid():
            serializer.save()
            res = {'msg':'data inserted'}
            json_data = JSONRenderer().render(res)


            return HttpResponse(json_data,content_type = 'application/json')
    
    return HttpResponse(JSONRenderer.render(serializer.errors))