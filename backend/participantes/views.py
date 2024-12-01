from django.shortcuts import render

# Create your views here.

from participantes.serializers import ParticipantesSerializer
from rest_framework.views import APIView
from participantes.models import Participante
from rest_framework.response import Response

from rest_framework import status

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class RunnersView(APIView):
    @swagger_auto_schema(
            operation_summary='Lista todos os participantes',
            operation_description="Obter informações sobre todos os participantes",
            request_body=None, # opcional
            responses={200: ParticipantesSerializer()}
            )
    def get(self, request):
        '''
Retorna uma lista de participantes. Depende de:
- APIView
- Participante
- ParticipantesSerializer
- Response
:param APIView self: o próprio objeto
:param Request request: um objeto representando o pedido HTTP
:param HTTP: não tem
:return: uma lista de participantes em formato JSON
:rtype: JSON
'''
        queryset = Participante.objects.all().order_by('id')
        # importante informar que o queryset terá mais
        # # de 1 resultado usando many=True
        serializer = ParticipantesSerializer(queryset, many=True)
        return Response(serializer.data)
    

    @swagger_auto_schema(
            operation_description='Remove um participante', request_body=ParticipantesSerializer,
            responses={
                204: ParticipantesSerializer(),
                404: None})
    def delete(self, request):
        id_erro = ""
        erro = False
        for id in request.data:
            participante = Participante.objects.get(id=id)
            if participante:
                participante.delete()
            else:
                id_erro += str(id)
                erro = True
        if erro:
            return Response({'error': f'item [{id_erro}] não encontrado'},
                            status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)


class RunnerView1(APIView):
    @swagger_auto_schema(
        operation_summary='Criar participante',
        operation_description="Criar um novo participante",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'nome': openapi.Schema(default='Michael', description='Nome do participante', type=openapi.TYPE_STRING),
                'sobrenome': openapi.Schema(default='Jackson', description='Sobrenome do participante', type=openapi.TYPE_STRING),
                'distancia': openapi.Schema(default=5, description='Distancia para correr', type=openapi.TYPE_INTEGER),
                'tempo': openapi.Schema(default="20''0'", description='Tempo da corrida do participante', type=openapi.TYPE_STRING),
            },
        ),
        responses={
            201: ParticipantesSerializer(),
            400: 'Dados errados'
        }
    )
    def post(self, request):
        serializer = ParticipantesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # uma boa prática é retornar o próprio objeto a
            return Response(serializer.data,
                            status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,
                            status.HTTP_400_BAD_REQUEST)
        

class RunnerView2(APIView):
    @swagger_auto_schema(
    operation_summary='Dados de um participante',
    operation_description="Obter informações sobre um participante específico",    
    responses={
        200: ParticipantesSerializer(),
        400: 'Mensagem de erro',
        },
        manual_parameters=[
            openapi.Parameter('id_arg', openapi.IN_PATH,
                          default=5,
                          type=openapi.TYPE_INTEGER,
                          required=True,
                          description='id do participante na URL'),
        ],
    )
    def get(self, request, id_arg):
        '''id_arg é o mesmo nome que colocamos em urls.py'''
        queryset = self.singleRunner(id_arg)
        if queryset:
            serializer = ParticipantesSerializer(queryset)
            return Response(serializer.data)
        else:
            # response for IDs that is not an existing runner
            return Response({'msg': f'participante com id #{id_arg} não existe'},
                            status.HTTP_400_BAD_REQUEST)
        
    def singleRunner(self, id_arg):
        try:
            queryset = Participante.objects.get(id=id_arg)
            return queryset
        except Participante.DoesNotExist: # id não existe
            return None
    
    @swagger_auto_schema(
        operation_summary='Atualiza participante', operation_description="Atualizar um participante existente",
        request_body=openapi.Schema(type=openapi.TYPE_OBJECT,
            properties={
                'nome': openapi.Schema(default='Michael', description='Nome do participante', type=openapi.TYPE_STRING),
                'sobrenome': openapi.Schema(default='Jackson', description='Sobrenome do participante', type=openapi.TYPE_STRING),
                'distancia': openapi.Schema(default=5, description='Distancia para correr', type=openapi.TYPE_INTEGER),
                'tempo': openapi.Schema(default="20''0'", description='Tempo da corrida do participante', type=openapi.TYPE_STRING),
            },
            ),
        responses={200: ParticipantesSerializer(),
                   400: ParticipantesSerializer(), },
        manual_parameters=[
            openapi.Parameter('id_arg',openapi.IN_PATH, default=41, type=openapi.TYPE_INTEGER,
                              required=True, description='id do participante na URL')],
                              )
    def put(self, request, id_arg):
        participante = self.singleRunner(id_arg)
        serializer = ParticipantesSerializer(participante,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    

    
    