from django.contrib import admin
from django.urls import path, include

#UNTUK MENAMPILKAN GAMBAR YANG SUDAH DI UPLOAD PADA FOLDER MEDIA
from django.conf import settings
from django.conf.urls.static import static


from webku.views import home, about

urlpatterns = [
    path("admin/", admin.site.urls),
    
    path('', home, name="home"),
    
    path('dashboard', include("berita.urls")),
]

#UNTUK MENAMPILKAN GAMBAR YANG SUDAH DI UPLOAD PADA FOLDER MEDIA
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  