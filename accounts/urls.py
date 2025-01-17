from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from . import views

app_name = "accounts"

urlpatterns = [
    path("", views.DashboardView.as_view(), name="dashboard"),
    path(
        "accounts/login/",
        LoginView.as_view(template_name="accounts/login.html"),
        name="login",
    ),
    path("logout/", LogoutView.as_view(next_page="accounts:login"), name="logout"),
    path("member/add/", views.MemberCreateView.as_view(), name="member_add"),
    path("account/<int:pk>/", views.AccountDetailView.as_view(), name="account_detail"),
    path("member/<int:pk>/edit/", views.MemberUpdateView.as_view(), name="member_edit"),
    path(
        "member/<int:pk>/delete/",
        views.MemberDeleteView.as_view(),
        name="member_delete",
    ),
    path("send-email/<int:member_id>/", views.send_member_email, name="send_email"),
]
