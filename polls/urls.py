from django.urls import path
from .views import YangiKasal, KasallarRoyhati, OzgarganKasallar



urlpatterns=[
    path('YangiKasal/', YangiKasal.as_view()),
    path('KasallarRoyhati/', KasallarRoyhati.as_view()),
    path('OzgarganKasallar/<int:forid>', OzgarganKasallar.as_view()),
]