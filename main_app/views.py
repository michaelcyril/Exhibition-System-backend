from django.shortcuts import render
from .serializer import *
from .models import *
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.decorators import api_view, permission_classes


# Create your views here.

class BlockView(APIView):
    permission_classes = (AllowAny,)

    @staticmethod
    def post(request, *args, **kwargs):
        data = request.data
        serialized = BlockPostSerializer(data=data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.validated_data)
        return Response(serialized.errors)

    @staticmethod
    def get(request, *args, **kwargs):
        queryset = Block.objects.all()
        exhibition = request.GET.get('exhibition_id')
        serialized = BlockPostSerializer(instance=queryset.filter(exhibition=exhibition), many=True)

        return Response(serialized.data)


class ExhibitionView(APIView):
    permission_classes = (AllowAny,)

    @staticmethod
    def get(request, *args, **kwargs):
        queryset = Exhibition.objects.all()
        serialized = ExhibitionGetSerializer(queryset, many=True)
        return Response(serialized.data)


class TicketView(APIView):
    permission_classes = (AllowAny, )

    @staticmethod
    def post(request, *args, **kwargs):
        serialized_list = []
        for data in request.data:
            serialized = TicketPostSerializer(data=data)
            if serialized.is_valid():
                serialized_list.append(serialized)
            else:
                return Response(serialized.errors)

        for data2 in serialized_list:
            data2.save()
        return Response({'message': 'saved'})

    @staticmethod
    def get(request, *args, **kwargs):
        queryset = Ticket.objects.all()
        is_active = request.GET.get('active')  # yes or no
        # user = request.GET.get('user_id')
        user = "1"
        if is_active == "yes":
            serialized = TicketGetSerializer(instance=queryset.filter(is_active=True, user=int(user)))
            return Response(serialized.data)
        serialized = TicketGetSerializer(instance=queryset.filter(is_active=False, user=int(user)))
        return Response(serialized.data)


@api_view(["GET"])
@permission_classes([AllowAny])
def ticketStatusChanger(request):
    ticket_id = request.GET.get('ticket_id')
    ticket = Ticket.objects.get(id=ticket_id)
    ticket.is_active = False
    ticket.save()
    return Response({'save': 'Successful save!'})

