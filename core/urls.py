from django.urls import path,include
from .views import( HomeView,AddMemberView,UpdateMemberDetailsView,DeleteMemberView,
                   MembersListView)
                

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
     path("add-member/", AddMemberView.as_view(), name="add-member"),
    path("update-member/<str:pk>/", UpdateMemberDetailsView.as_view(), name="update-member"),
    path("delete-member/<str:pk>/", DeleteMemberView.as_view(), name="delete-member"),
    path("members/", MembersListView.as_view(), name="members"),


]
