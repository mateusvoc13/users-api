from django.urls import path
from marketplace.views import ClientView, SingleClientView, ProductView, SingleProductView
from django.contrib.auth.decorators import login_required

app_name = "marketplace"

urlpatterns = [
    path('clients/',         ClientView.as_view()),
    path('clients/<int:pk>', login_required(SingleClientView.as_view())),
    path('product/',         login_required(ProductView.as_view())),
    path('product/<int:pk>', login_required(SingleProductView.as_view())),
]
