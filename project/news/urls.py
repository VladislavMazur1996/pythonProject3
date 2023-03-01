from django.urls import path
# Импортируем созданное нами представление
from .views import TitleList, PostDetail, PostCreate, PostUpdate, PostDelete, subscriber

urlpatterns = [
   path('', TitleList.as_view(), name='news'),
   path('<int:pk>', PostDetail.as_view(), name='post_detail'),
   path('create/', PostCreate.as_view(), name='post_create'),
   path('<int:pk>/edit/', PostUpdate.as_view(), name='post_update'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   path('search/', TitleList.as_view(), name='search'),
   path('<int:pk>/subscriber/', subscriber, name='subscriber'),
]
