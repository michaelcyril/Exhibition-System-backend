from .models import Block, Ticket, Exhibition
from rest_framework import serializers


class BlockPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Block
        fields = ['user', 'exhibition', 'phone', 'description', 'latitude', 'longitude']


class BlockGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Block
        fields = ['id', 'user', 'exhibition', 'phone', 'description', 'latitude', 'longitude', 'created_at']
        depth = 2


class TicketPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['user', 'created_at']


class TicketGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['id', 'user', 'created_at', 'is_active']
        depth = 2


class ExhibitionPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exhibition
        fields = ['name', 'description']


class ExhibitionGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['id', 'name', 'description']
        depth = 2

