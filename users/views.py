from users.forms import CustomUserCreationForm
from django.views.generic.edit import FormView


class RegisterFormView(FormView):
    form_class = CustomUserCreationForm
    success_url = "/main/"
    template_name = "registration/register.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(RegisterFormView, self).form_invalid(form)
