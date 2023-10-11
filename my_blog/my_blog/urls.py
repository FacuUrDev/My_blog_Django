from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap


sitemaps = {
    "posts": PostSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),#Se crea una ruta para la lista de post
    path('summernote/', include('django_summernote.urls')),#Se crea una ruta para el detalle del post
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"), #Se crea una ruta para el sitemap
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)