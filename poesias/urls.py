from django.urls import path
import poesias.views as views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'poesias'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('sobre/', views.sobre_view, name='sobre'),
    path('blog/', views.blog_view),
    path('user/<str:username>/', views.user_view, name='user'),

    # Passando parâmtros dinâmicamente
    path('poemas/<int:poema_id>/', views.poema_text, name='poema_text'),

    # Extends
    path('page_extends/', views.page_extends),
    path('principal/', views.principal, name='Principal'),

    path('sobre/', views.sobre, name='Sobre'),


    # Tag if
    path('poema_detail/', views.poema_detail),

    # tag for
    path('poema_list/', views.poema_list, name='poema_list'),


    # TDD
    path('search/', views.search, name='search'),

    # Form
    path('register/', views.register_view, name='register_view'),

    # Login
    path('login/', views.user_login_view, name='login'),
    path('login_form/', views.login_form_view, name='login_form'),

    # Logout
    path('logout/', views.user_logout_view, name='logout'),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
