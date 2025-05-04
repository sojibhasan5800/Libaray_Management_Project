from django.urls import path,include
from .views import( HomeView,AddMemberView,UpdateMemberDetailsView,DeleteMemberView,
                   MembersListView,AddBookView,UpdateBookDetailsView,DeleteBookView,
                   BooksListView,LendBookView,LendMemberBookView,LentBooksListView,
                   UpdateBorrowedBookView,DeleteBorrowedBookView,ReturnBookView,
                   ReturnBookFineView,ListPaymentsView,DeletePaymentView,OverdueBooksView)
                

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("add-member/", AddMemberView.as_view(), name="add-member"),
    path("update-member/<str:pk>/", UpdateMemberDetailsView.as_view(), name="update-member"),
    path("delete-member/<str:pk>/", DeleteMemberView.as_view(), name="delete-member"),
    path("members-list/", MembersListView.as_view(), name="members"),
    path("add-book/", AddBookView.as_view(), name="add-book"),
    path("update-bookr/<str:pk>/", UpdateBookDetailsView.as_view(), name="update-book"),
    path("delete-book/<str:pk>/", DeleteBookView.as_view(), name="delete-book"),
    path("books-list/", BooksListView.as_view(), name="books"),
    path("lend-book/", LendBookView.as_view(), name="lend-book"),
    path("lend-book/<str:pk>/", LendMemberBookView.as_view(), name="lend-member-book"),
    path("lent-books/", LentBooksListView.as_view(), name="lent-books"),
    path("edit-borrowed-book/<str:pk>/", UpdateBorrowedBookView.as_view(), name="edit-borrowed-book"),
    path("delete-borrowed-book/<str:pk>/", DeleteBorrowedBookView.as_view(), name="delete-borrowed-book"),
    path("return-book/<str:pk>/", ReturnBookView.as_view(), name="return-book"),
    path("return-book-fine/<str:pk>/", ReturnBookFineView.as_view(), name="return-book-fine"),
    path("payments/", ListPaymentsView.as_view(), name="payments"),
    path("delete-payment/<str:pk>/", DeletePaymentView.as_view(), name="delete-payment"),
    path("overdue-books/", OverdueBooksView.as_view(), name="overdue-books"),



]
