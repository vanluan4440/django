from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('create',views.create, name='create_class'),
    path('delete/<int:id>',views.delete, name='delete_class'),
    path('edit',views.edit, name='edit_class'),
    path('getAll',views.getAll, name='getAll_class'),
    path('getOnly',views.getOnly, name='getOnly_class'),
    path('getClassByUser',views.getClassByUser, name='getClassByUser'),
   
]

static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)