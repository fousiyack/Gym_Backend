
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import Event
from .serializers import *
from rest_framework.views import APIView


class GymInfoListAPIView(ListAPIView):
    queryset = GymInfo.objects.all()
    serializer_class = GymInfoSerializer
    
class EventListAPIView(ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer 
    
class ContactInquiryListAPIView(ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactInquirySerializer
    
class GalleryItemListAPIView(ListAPIView):
    queryset = GalleryItem.objects.all()
    serializer_class = GalleryItemSerializer
    
class TrainerListAPIView(ListAPIView):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer
    
class ContactInquiryListCreateAPIView(APIView):    
    def post(self, request):
        serializer = ContactInquirySerializer(data=request.data)
        if serializer.is_valid():
          serializer.save()
          return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
                

# class EventListCreateAPIView(APIView):
#     def get(self, request):
#         events = Event.objects.all()
#         serializer = EventSerializer(events, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = EventSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# class GymInfoListCreateAPIView(APIView):
#     def get(self, request):
#         gym_info = GymInfo.objects.all()
#         serializer = GymInfoSerializer(gym_info, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = GymInfoSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
# class ContactInquiryListCreateAPIView(APIView):
#     def get(self, request):
#         contact_inquiries = ContactInquiry.objects.all()
#         serializer = ContactInquirySerializer(contact_inquiries, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = ContactInquirySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# class GalleryItemListCreateAPIView(APIView):
#     def get(self, request):
#         gallery_items = GalleryItem.objects.all()
#         serializer = GalleryItemSerializer(gallery_items, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = GalleryItemSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
# class EquipmentListCreateAPIView(APIView):
#     def get(self, request):
#         equipment = Equipment.objects.all()
#         serializer = EquipmentSerializer(equipment, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = EquipmentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        