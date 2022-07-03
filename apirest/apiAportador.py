from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from rest_framework import status
import json
from core.models import RegistroForm

@api_view(['GET', 'POST'])
def RegistroForm(request):
    if request.method == 'GET':
        response_json = []
        RegistroForm = RegistroForm.objects.all()       
        for RegistroForm in RegistroForm:
            js = {
                'rutAportador': int(RegistroForm.run),
                'nombreAportador' : RegistroForm.nombres,
                'apellidoAportador' : RegistroForm.apellido_paterno,
                'usuarioAportador' : RegistroForm.usuarioAportador,
                'correoAportador' : RegistroForm.correoAportador,
                'passAportador' : RegistroForm.passAportador                
            }
            response_json.append(js)
        status_code = status.HTTP_200_OK
        print('response_json', response_json)
        return HttpResponse(json.dumps(response_json, ensure_ascii=False), content_type="application/json", status=status_code)       