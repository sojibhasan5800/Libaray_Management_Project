from django.urls import path,include
from .views import HomeView,AddMemberView,UpdateMemberDetailsView,DeleteMemberView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
     path("add-member/", AddMemberView.as_view(), name="add-member"),
    path("update-member", UpdateMemberDetailsView.as_view(), name="update-member"),
    path("delete-member", DeleteMemberView.as_view(), name="delete-member"),

]
