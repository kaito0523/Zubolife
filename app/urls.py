from django.urls import path
from . import views

app_name = "app"

urlpatterns = [
    path('', views.cooklist, name="cooklist"),
    path('<int:id>', views.detail, name="detail"),
    path('follow/<int:id>/', views.followPlace, name='follow'),  
    path('favorite/', views.favorite, name="favorite"),
    path('newrecipe', views.newrecipe, name="newrecipe"),
    path('memo', views.memo, name="memo"),
    path('memo/<int:id>', views.memo_detail, name="memo_detail"),
    path('newmemo', views.newmemo, name="newmemo"),
    path('newmemo2', views.newmemo2, name="newmemo2"),
]

