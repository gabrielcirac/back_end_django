from django.urls import path
import poesias.views as views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home_view),
    path('sobre/', views.sobre_view),
    path('blog/', views.blog_view),
    path('user/<str:username>/', views.user_view),

    # Extends
    path('page_extends/', views.page_extends),
    path('principal/', views.principal, name='Principal'),

    path('sobre/', views.sobre, name='Sobre'),


    # Tag if
    path('poema_detail/', views.poema_detail),

    # tag for
    path('poema_list/', views.poema_list, name='poema_list'),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
