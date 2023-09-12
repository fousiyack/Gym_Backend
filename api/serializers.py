from rest_framework import serializers
from .models import *




class GymInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = GymInfo
        fields = '__all__'
        
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'        
        
class ContactInquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
        
class GalleryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryItem
        fields = '__all__'                

class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = '__all__'