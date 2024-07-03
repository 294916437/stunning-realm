from django.urls import path
from . import views
urlpatterns = [
    path('college/', views.getCollegeInfo, name='获取学校信息'),
    path('college/logo/<str:filename>', views.getCollegeLogo, name='获取学校logo'),
    path('college/crawler', views.crawlCollegeData, name='获取学校信息'),
]
