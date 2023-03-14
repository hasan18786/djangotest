from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='test'),
    path('add/', views.add, name='add'),
    path('addmember/', views.addmember, name='addmember'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('update/<int:id>', views.update, name='update'),
    path('updatemember/<int:id>', views.updatemember, name='updatemember'),
]
