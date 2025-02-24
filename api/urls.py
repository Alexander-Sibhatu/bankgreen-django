from django.urls import path

from brand.views import get_bank_commentary

from . import views


app_name = "rest_api"
urlpatterns = [
    path("", views.BrandSuggestionAPIView.as_view()),
    path("bank-contacts/", views.ContactView.as_view(), name="contacts"),
    path("bank/", views.BrandsView.as_view(), name="bank"),
<<<<<<< HEAD
<<<<<<< HEAD
    path("banks/<int:bank_id>/", get_bank_commentary, name="get_bank_commentary"),
=======
=======
>>>>>>> origin/main
    path(
        "bank/<int:brand_id>/feature_override/",
        views.BrandFeatureOverride.as_view(),
        name="brand_feature_override",
    ),
<<<<<<< HEAD
>>>>>>> 7b4cd04da2fb31b47755f9090beecb8cc0df7d78
=======
>>>>>>> origin/main
]
