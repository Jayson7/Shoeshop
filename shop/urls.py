from apps import views
from apps.views import *
from django.contrib import admin
from django.urls import path, include

# settings config for static
from django.conf import settings
from django.conf.urls.static import static
from auths import urls
import auths

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("register", include("auths.urls")),
    path("", Homepage.as_view(), name="home"),
    path("product/<slug:slug>/", ProductView.as_view(), name="productview"),
    path("add-to-cart-<int:pro_id>/", AddToCartView.as_view(), name="addtocart"),
    path("my-cart/", MyCartView.as_view(), name="mycart"),
    path("manage-cart/<int:cp_id>/", ManageCartView.as_view(), name="managecart"),
    path("empty-cart/", EmptyCartView.as_view(), name="emptycart"),
    path("checkout/", CheckoutView.as_view(), name="checkout"),
    path("register/", CustomerRegistrationView.as_view(), name="customerregistration"),
    path("logout/", CustomerLogoutView.as_view(), name="customerlogout"),
    path("login/", CustomerLoginView.as_view(), name="customerlogin"),
    path("profile/", CustomerProfileView.as_view(), name="customerprofile"),
    path(
        "profile/order-<int:pk>/",
        CustomerOrderDetailView.as_view(),
        name="customerorderdetail",
    ),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
