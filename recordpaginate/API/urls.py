from django.urls import path
from .models import cases, labs, quarantine, sqliteseq, summery, vaccine
from .views import casesList, labList, quarantineList, sqliteseqList, vaccineList, summeryList

urlpatterns = [
    path('cases/', casesList.as_view(), name='cases'),
    path('labs/', labList.as_view(), name='labs'),
    path('quarantine/', quarantineList.as_view(), name='quarantine'),
    path('sqliteseq/', sqliteseqList.as_view(), name='sqliteseq'),
    path('summery/', summeryList.as_view(), name='summery'),
    path('vaccine/', vaccineList.as_view(), name='vaccine'),
]