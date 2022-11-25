from django.urls import path

from jorgeav527.cvmaker.views import (
    english_pdf_view,
    spanish_pdf_view,
    portuguese_pdf_view,
)

app_name = "cvmaker"
urlpatterns = [
    path("english/", view=english_pdf_view, name="english"),
    path("spanish/", view=spanish_pdf_view, name="spanish"),
    path("portuguese/", view=portuguese_pdf_view, name="portuguese"),
]
