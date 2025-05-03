from django.shortcuts import render,redirect
import logging
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views.generic import View

logger = logging.getLogger(__name__)
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
    

@method_decorator(login_required, name="dispatch")
class AddMemberView(View):
    """
    Add Member view for the library management system.
    get(): Returns the add member page with the AddMemberForm.
    post(): Validates the form and saves the new member to the database.
    """

    def get(self, request, *args, **kwargs):
        form = AddMemberForm()
        return render(request, "members/add-member.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = AddMemberForm(request.POST)

        if form.is_valid():
            form.save()
            logger.info("New member added successfully.")
            return redirect("members")

        logger.error(f"Error occurred while adding member: {form.errors}")

        return render(request, "members/add-member.html", {"form": form})
    


@method_decorator(login_required, name="dispatch")
class MembersListView(View):
    """
    Members List view for the library management system.
    get(): Returns the list of members in the library.
    post(): Returns the list of members in the library based on the search query.
    """

    def get(self, request, *args, **kwargs):
        members = Member.objects.all()
        return render(request, "members/list-members.html", {"members": members})

    def post(self, request, *args, **kwargs):
        query = request.POST.get("query")
        members = Member.objects.filter(name__icontains=query)
        return render(request, "members/list-members.html", {"members": members})


@method_decorator(login_required, name="dispatch")
class UpdateMemberDetailsView(View):
    """
    Update Member details view for the library management system.
    get(): Returns the update member page with the UpdateMemberForm.
    post(): Validates the form and updates the member details in the database.
    """

    def get(self, request, *args, **kwargs):
        member = Member.objects.get(pk=kwargs["pk"])
        form = UpdateMemberForm(instance=member)
        return render(request, "members/update-member.html", {"form": form, "member": member})

    def post(self, request, *args, **kwargs):
        member = Member.objects.get(pk=kwargs["pk"])
        form = UpdateMemberForm(request.POST, instance=member)

        if form.is_valid():
            form.save()
            logger.info("Member details updated successfully.")
            return redirect("members")

        logger.error(f"Error occurred while updating member: {form.errors}")

        return render(request, "members/update-member.html", {"form": form, "member": member})


@method_decorator(login_required, name="dispatch")
class DeleteMemberView(View):
    """
    Delete Member view for the library management system.
    get(): Deletes the member from the database.
    """

    def get(self, request, *args, **kwargs):
        member = Member.objects.get(pk=kwargs["pk"])
        member.delete()
        logger.info("Member deleted successfully.")
        return redirect("members")




