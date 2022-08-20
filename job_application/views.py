from django.urls import reverse_lazy
from django.views.generic import TemplateView
from multipage_form.views import MultipageFormView
from .forms import JobApplicationForm


class JobApplicationView(MultipageFormView):
    template_name = 'form_page.html'
    form_class = JobApplicationForm
    success_url = reverse_lazy("job_application:thank_you")

class JobApplicationThankYouView(TemplateView):
    template_name = 'thank_you.html'