from django.urls import path
from marketplace.views import ClientView, SingleClientView, ProductView, SingleProductView

app_name = "marketplace"

urlpatterns = [
    path('clients/',            ClientView.as_view()),
    path('clients/<int:pk>',    SingleClientView.as_view()),
    path('product/',            ProductView.as_view()),
    path('product/<slug:pk>',   SingleProductView.as_view()),
]
