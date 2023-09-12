from django.urls import path
from . import views
from .views import *
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
	
	
    path('events/', EventListAPIView.as_view(), name='event-list'),
    path('gyminfo/', GymInfoListAPIView.as_view(), name='gyminfo-list'),
    path('contactinquiries/', ContactInquiryListAPIView.as_view(), name='contactinquiry-list'),
    path('galleryitems/', GalleryItemListAPIView.as_view(), name='galleryitem-list'),
    path('trainers/', TrainerListAPIView.as_view(), name='trainers'),
    path('createContact/', ContactInquiryListCreateAPIView.as_view(), name='createContact'),
 
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)