from django.urls import path, include
from watch_api import views



urlpatterns = [
    path('watch/', views.watch_list, name="watch_list"),
    path('watch/<int:pk>', views.watch_list_by_id, name="watch_list_by_id"),
    path('platform/', views.platform_list, name="platform_list"),
    path('platform/<int:pk>', views.platform_list_by_id, name="platform_list_by_id"),
]