"""courier URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static

from delivery import views
# for api_views
import delivery.api_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.first_page, name='first_page'),
    path('home/', views.home, name='home'),
    path('confirm/', views.confirm, name='confirm'),
    path('delivery_request/', views.delivery_request, name='delivery_request'),
    path('send_driver/', views.send_driver, name='send_driver'),
    path('signup/', views.signup, name='signup'),
    path('admin_account/', views.admin_account, name='admin_account'),
    path('personal_account/', views.personal_account, name='personal_account'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('send_driver/',views.send_driver,name='send_driver'),

    # api_views path
    path('api/drivers/',delivery.api_views.DriverList.as_view()),
    path('api/drivers/new',delivery.api_views.DriverCreate.as_view()),
    path('api/drivers/<int:id>/destroy',delivery.api_views.DriverDestroy.as_view()),
    path('api/drivers/<int:id>',delivery.api_views.DriverRetrieveUpdateDestroy.as_view()),
]

# if settings.DEBUG: 
#         urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns +=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
