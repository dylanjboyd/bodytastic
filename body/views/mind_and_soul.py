from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView

from body.models import EmotionReport
from body.forms import EmotionReportForm


class UserOnlyMixin:
    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


class EmotionReportListView(UserOnlyMixin, ListView):
    model = EmotionReport


class EmotionReportDetailView(UserOnlyMixin, DetailView):
    model = EmotionReport


class EmotionReportCreateView(CreateView):
    model = EmotionReport
    form_class = EmotionReportForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["disabled_dates"] = EmotionReport.objects.filter(
            user=self.request.user
        ).values_list("when", flat=True)
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
