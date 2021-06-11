from apps import views
from apps.views import home, cartview, addcart
from django.contrib import admin
from django.urls import path, include
# settings config for static
from django.conf import settings
from django.conf.urls.static import static
from auths import urls
import auths

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('cartview', views.cartview, name="cartview"),
    path('addcart', views.addcart, name="addcart"),
    path('accounts/', include("django.contrib.auth.urls")),
    path('register', include("auths.urls")),
    

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
