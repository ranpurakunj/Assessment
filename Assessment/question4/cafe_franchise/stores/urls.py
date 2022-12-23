from django.urls import path

from .views import CafeList, OrderDetail

urlpatterns = [
    path("", CafeList.as_view(), name="cafe-list"),
    # path("<int:id>/", OrderList.as_view(), name="order-list"),
    # path("<int:pk>/", OrderDetail.as_view(), name="order-detail"),

]
