from django.urls import path

from Podio.api.views import PodioView, AllPodiosView

urlpatterns = [
    path('podios', AllPodiosView.as_view(http_method_names=['get'])),
    path('podios/<int:id>', PodioView.as_view(http_method_names=['get'])),
    path('podios/<int:id>/edit', PodioView.as_view(http_method_names=['put'])),
]