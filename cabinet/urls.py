from django.urls import path
from .views import (get_cabinet, detail_cabinet,
                    create_author, create_image,
                    update_author, delete_author
                    )

urlpatterns = [
    path('', get_cabinet, name='main'),
    path('detail/<int:id>/', detail_cabinet, name='cabinet'),
    path('create/', create_author, name='author_create'),
    path('create/image', create_image, name='image_create'),
    path('update/<int:id>/', update_author, name='author_update'),
    path('delete/<int:id>/', delete_author, name='author_delete'),

    ]