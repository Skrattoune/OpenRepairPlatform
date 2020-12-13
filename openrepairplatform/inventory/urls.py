from django.urls import path
from django.conf.urls import url
from . import views

app_name = "inventory"
urlpatterns = [
    path(
        "device_autocomplete/",
        views.DeviceAutocomplete.as_view(),
        name="device_autocomplete",
    ),
    path(
        "brand_autocomplete/",
        views.BrandAutocomplete.as_view(create_field='name'),
        name="brand_autocomplete",
    ),
    path(
        "action_autocomplete/",
        views.ActionAutocomplete.as_view(create_field='name'),
        name="action_autocomplete",
    ),
    path(
        "observation_autocomplete/",
        views.ObservationAutocomplete.as_view(create_field='name'),
        name="observation_autocomplete",
    ),
    path(
        "status_autocomplete/",
        views.StatusAutocomplete.as_view(create_field='name'),
        name="status_autocomplete",
    ),
    path(
        "reasoning_autocomplete/",
        views.ReasoningAutocomplete.as_view(create_field='name'),
        name="reasoning_autocomplete",
    ),
    path(
        "category_autocomplete/",
        views.CategoryAutocomplete.as_view(),
        name="category_autocomplete",
    ),
    path(
        "device/<int:pk>/<slug>/",
        views.DeviceDetailView.as_view(),
        name="device_view"
    ),
    path(
        "",
        views.StockListView.as_view(),
        name="stock_list"
    ),
    path(
        "stuff/<int:stuff_pk>/",
        views.StuffDetailView.as_view(),
        name="stuff_view"
    ),
    path(
        "user_stuff_list/<int:user_pk>/",
        views.StuffUserListView,
        name="user_stuff_list"
    ),
    path(
        "create_stuff/<int:user_pk>/",
        views.StuffUserFormView.as_view(),
        name="create_user_stuff"
    ),
    path(
        "create_stuff/<str:orga_slug>/",
        views.StuffOrganizationFormView.as_view(),
        name="create_organization_stuff"
    ),
    path(
        "update_stuff/<int:pk>/",
        views.StuffUpdateView.as_view(),
        name="update_stuff"
    ),
    path(
        "update_owner_stuff/<int:pk>/",
        views.StuffUpdateOwnerView.as_view(),
        name="update_owner_stuff"
    ),
    path(
        "update_visibility_stuff/<int:pk>/",
        views.StuffEditVisibilityStuffView.as_view(),
        name="update_visibility_stuff"
    ),
    path(
        "update_place_stuff/<int:pk>/",
        views.StuffUpdatePlaceView.as_view(),
        name="update_place_stuff"
    ),
    path(
        "update_state_stuff/<int:pk>/",
        views.StuffUpdateStateView.as_view(),
        name="update_state_stuff"
    ),
    path(
        "create_folder/<int:pk>/",
        views.FolderCreateView.as_view(),
        name="create_folder"
    ),
    path(
        "create_intervention/<int:pk>/",
        views.InterventionCreateView.as_view(),
        name="create_intervention"
    ),
    path(
        "update_intervention/<int:pk>/",
        views.InterventionUpdateView.as_view(),
        name="update_intervention"
    ),
]
