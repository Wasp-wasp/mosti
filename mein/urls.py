"""
URL configuration for mein project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from mein import views
from django.conf.urls.static import static
from django.conf import settings

from mein import views as user_views

urlpatterns = [
                  path('', views.index, name='index'),
                  path('admin/', admin.site.urls),
                  path('login/', views.login_user, name='login'),
                  path('about/', views.about, name='about'),
                  path('test/', views.test, name='test'),
                  path('proects/', views.proects, name='proects'),
                  path('km/', views.km, name='km'),
                  path('kozm/', views.kozm, name='kozm'),
                  path('buy/<int:id_object>/', views.buy, name='buy'),
                  path('pdf', views.getpdf, name='pdf'),
                  path('shedule', views.shedule, name='shedule'),
                  path('send_mail/', views.send_email, name="send_mail"),
                    path('logout/', views.logout_user, name='logout'),

    # path('auth/', include('authentification.urls')),
                  #
                  # path('<pk>/pdf', views.users_render_pdf_view, name='user_pdf_view'),
              ]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
