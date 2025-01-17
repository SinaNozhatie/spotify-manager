from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.core.cache import cache
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from notifications.services import send_notification_email

from .models import Member, SpotifyAccount


class DashboardView(LoginRequiredMixin, ListView):
    model = SpotifyAccount
    template_name = "accounts/dashboard.html"
    context_object_name = "accounts"


class AccountDetailView(LoginRequiredMixin, DetailView):
    model = SpotifyAccount
    template_name = "accounts/account_detail.html"


class MemberCreateView(LoginRequiredMixin, CreateView):
    model = Member
    template_name = "accounts/member_form.html"
    fields = ["name", "email", "spotify_account", "start_date", "end_date"]


class MemberUpdateView(LoginRequiredMixin, UpdateView):
    model = Member
    template_name = "accounts/member_form.html"
    fields = ["name", "email", "start_date", "end_date"]
    success_url = "/"


class MemberDeleteView(LoginRequiredMixin, DeleteView):
    model = Member
    template_name = "accounts/member_confirm_delete.html"
    success_url = "/"


class CustomLoginView(LoginView):
    template_name = "accounts/login.html"
    redirect_authenticated_user = True
    success_url = reverse_lazy("accounts:dashboard")

    def form_valid(self, form):
        messages.success(self.request, "Login successful!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Invalid username or password")
        return super().form_invalid(form)


def rate_limit(request):
    if request.user.is_authenticated:
        key = f"user_{request.user.id}_request_count"
        request_count = cache.get(key, 0)
        if request_count > 100:  # محدودیت 100 درخواست در دقیقه
            raise PermissionDenied
        cache.set(key, request_count + 1, 60)


def send_member_email(request, member_id):
    if request.method == "POST":
        member = get_object_or_404(Member, id=member_id)
        subject = "یادآوری اشتراک Spotify"
        message = f"سلام {member.name}،\n\nاشتراک شما در تاریخ {member.end_date} به پایان می‌رسد."
        send_notification_email(subject, message, member.email)
        messages.success(request, "Email sent successfully")
    else:
        messages.error(request, "Invalid request")

    return redirect("accounts:dashboard")
