from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("show/<int:id>", views.show_category, name="show_category"),
    # listing routes
    path("listing", views.listing, name="listing"),
    path("listing/<int:id>", views.list_item, name="single_item"),
]

# router.get("/listing/:id")
