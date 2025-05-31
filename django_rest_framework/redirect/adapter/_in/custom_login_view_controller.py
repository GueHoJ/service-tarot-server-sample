from django.contrib.auth import login
from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import FormView


class CustomLoginView(FormView):
    template_name = 'registration/login.html'
    form_class = AuthenticationForm

    def form_valid(self, form):
        login(self.request, form.get_user())
        return redirect('/swagger/')  # Redirect to Swagger page after successful login

    def form_invalid(self, form):
        # If the form is invalid, render the login page with errors
        return self.render_to_response(self.get_context_data(form=form))