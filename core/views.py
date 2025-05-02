from django.shortcuts import render,redirect
import logging
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views.generic import View

from .forms import (
    AddBookForm,
    AddMemberForm,
    LendBookForm,
    LendMemberBookForm,
    PaymentForm,
    UpdateBorrowedBookForm,
    UpdateMemberForm,
)
from .models import Book, BorrowedBook, Member, Transaction
# Create your views here.

@method_decorator(login_required, name="dispatch")
class HomeView(View):
    """
    Home view for the library management system. Displays the Dashboard.
    get(): Returns the home page with the following context:
        - total_members: Total number of members in the library.
        - total_books: Total number of books in the library.
        - total_borrowed_books: Total number of books currently borrowed.
        - total_overdue_books: Total number of books that are overdue.
        - recently_added_books: The 4 most recently added books.
        - total_amount: Total amount of money collected from payments.
        - overdue_amount: Total amount of money that overdue books have accrued.
    """

    def get(self, request, *args, **kwargs):
        members = Member.objects.all()
        books = Book.objects.all()
        borrowed_books = BorrowedBook.objects.filter(returned=False)
        overdue_books = BorrowedBook.objects.filter(return_date__lt=timezone.now().date(), returned=False)

        total_members = members.count()
        total_books = books.count()
        total_borrowed_books = borrowed_books.count()
        total_overdue_books = overdue_books.count()

        recently_added_books = books.order_by("-created_at")[:4]

        total_amount = sum([payment.amount for payment in Transaction.objects.all()])
        overdue_amount = sum([book.fine for book in overdue_books])

        context = {
            "total_members": total_members,
            "total_books": total_books,
            "total_borrowed_books": total_borrowed_books,
            "total_overdue_books": total_overdue_books,
            "recently_added_books": recently_added_books,
            "total_amount": total_amount,
            "overdue_amount": overdue_amount,
        }

        return render(request, "index.html", context)


