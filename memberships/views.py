from django.shortcuts import render

# Create your views here.
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy


class StaffLoginView(LoginView):
    template_name = "memberships/login.html"

    # def get_success_url(self):
    #     return reverse_lazy("dashboard")

    def form_valid(self, form):
        user = form.get_user()
        if not user.is_staff:
            form.add_error(
                None, "You are not authorized to access this system.")
            return self.form_invalid(form)
        return super().form_valid(form)
