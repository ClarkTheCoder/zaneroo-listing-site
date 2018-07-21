"""

// Zaneroo 2018
// Local Listing website similar to used Victoria.
// Design inspiration: Reddit Redesign
// Create by Carson Clark


Contact: Carsonclark2009@gmail.com
Youtube: https://www.youtube.com/user/CarsonsCouchXBL
Twitter: @ClarkTheCoder

"""

from django.conf.urls import url, include
from django.contrib import admin
from home import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^classifieds/', include('classifieds.urls')),
]

if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
