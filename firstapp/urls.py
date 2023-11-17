from django.urls import path
from firstapp.views import index,PostCreate,detail
from django.conf.urls.static import static
app_name="firstapp"
urlspatterns=[
    path('',index,name='index'),
    path('create/',PostCreate.as_view(),name='create'),
    path('detail/<int:pk>/',detail,name='detail'),
]