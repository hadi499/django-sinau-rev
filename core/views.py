from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib import messages



class CustomLoginView(LoginView):
    template_name = 'users/login.html'

    def form_invalid(self, form):
        messages.error(self.request, "Invalid username or password.")
        return super().form_invalid(form)

@login_required
def home(request):
  return render(request, 'home.html')


@login_required
def scores(request):
  return render(request, 'scores.html')


@login_required
def all_scores(request):  
  return render(request, 'all_scores.html')