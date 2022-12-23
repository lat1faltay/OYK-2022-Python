from xml.dom.expatbuilder import Namespaces
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from config.views import home #, ad_soyad_yaz, isim_yaz,python
from django.urls import include, path 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('kullanici/', include('django.contrib.auth.urls')),
    path('wallet/', include('wallet.urls', namespace='wallet')),
    path('__debug__/', include('debug_toolbar.urls')),

    path('', home, name='home'),
    # path('python/', python),
    # path('<isim>/', isim_yaz), 
    # path('<ad>/<soyad>/', ad_soyad_yaz),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)


