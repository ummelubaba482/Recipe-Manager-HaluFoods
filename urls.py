# from django.contrib import admin
# from django.urls import path, include
# from recipes import views as recipe_views
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', recipe_views.home, name='home'),  # Home page
#     path('', include('recipes.urls')),
#     path('accounts/', include('django.contrib.auth.urls')),
# ]



from django.contrib import admin
from django.urls import path, include
from recipes import views as recipe_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', recipe_views.home, name='home'),
    path('', include('recipes.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)