from django.urls import path
from .views import roadtrip, stays, roadtrip_detail, roadtrip_delete, roadtrip_update, roadtrip_create, stays
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('roadtrip/', roadtrip.as_view(), name="roadtrip_list"),
    path('roadtrip/<int:id>/', views.roadtrip_detail, name="roadtrip_detail"),
    path('roadtrip/<int:pk>/delete/', roadtrip_delete.as_view(), name="roadtrip_delete"),
    path('roadtrip/<int:pk>/update/', roadtrip_update.as_view(), name="roadtrip_update"),
    path('roadtrip/create', roadtrip_create.as_view(), name='roadtrips_form'),
    path('about/', views.about, name="about"),
    path('stay/', stays.as_view(), name="stay_list"),
    path('stay/<int:id>', views.stay_detail, name="stay_detail"),
    path('stay/<int:pk>/delete/', stays.as_view(), name="stay_delete"),
    path('stay/<int:pk>/update/', stays.as_view(), name="stay_update"),
    path('stay/create', stays.as_view(), name="stays_form")
]