from django.urls import path

from Podio.api.views import PodioView, AllPodiosView, DocumentoNiños

urlpatterns = [
    path('podios', AllPodiosView.as_view()),
    path('podios/<int:id>/edit', PodioView.as_view()),
    path('docum_niños', DocumentoNiños.as_view()),
]