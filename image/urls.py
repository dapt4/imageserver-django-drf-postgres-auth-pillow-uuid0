from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('login', views.login),
    path('register', views.register),
    path('image', views.list_images),
    path('image/<int:id>', views.get_image),
    path('image/new', views.new_image),
    path('image/del/<int:id>', views.delete_image),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
