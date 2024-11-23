from django.shortcuts import render

# Create your views here.

from participantes.serializers import ParticipantesSerializer
from rest_framework.views import APIView
from participantes.models import Participante
from rest_framework.response import Response

from rest_framework import status



class RunnersView(APIView):
    def get(self, request):
        queryset = Participante.objects.all().order_by('user_id')
        # importante informar que o queryset terá mais
        # # de 1 resultado usando many=True
        serializer = ParticipantesSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def delete(self, request):
        id_erro = ""
        erro = False
        for id in request.data:
            carro = Participante.objects.get(user_id=id)
            if carro:
                carro.delete()
            else:
                id_erro += str(id)
                erro = True
        if erro:
            return Response({'error': f'item [{id_erro}] não encontrado'},
                            status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)


class RunnerView(APIView):
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
        
    
    def get(self, request, id_arg):
        '''id_arg é o mesmo nome que colocamos em urls.py'''
        queryset = self.singleRunner(id_arg)
        if queryset:
            serializer = ParticipantesSerializer(queryset)
            return Response(serializer.data)
        else:
            # response for IDs that is not an existing runner
            return Response({'msg': f'Carro com id #{id_arg} não existe'},
                            status.HTTP_400_BAD_REQUEST)
        
    def singleRunner(self, id_arg):
        try:
            queryset = Participante.objects.get(user_id=id_arg)
            return queryset
        except Participante.DoesNotExist: # id não existe
            return None
    
    def put(self, request, id_arg):
        carro = self.singleRunner(id_arg)
        serializer = ParticipantesSerializer(carro,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    

    
    