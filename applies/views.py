from django.shortcuts import render
from django.views.generic import CreateView
from . import models, forms
from studies import models as studies_model
from notices import models as notices_model

# Create your views here.

class StudyApplyView(CreateView):
    template_name = 'applies/applies_create.html'
    form_class = forms.ApplyModelForm
    queryset = models.Apply.objects.all()

    def form_valid(self, form):
        apply = form.save(commit=False)
        apply.Apply_host = self.request.user
        pk = self.kwargs.get("pk")
        apply.Apply_room = studies_model.Study.objects.get(pk=pk)
        apply.room_Host = studies_model.Study.objects.get(pk=pk)
        form.save()
        notices_model.Notice.objects.create(
            associated_name = "스터디 알람",
            explain = "스터디 지원 신청이 왔어요!",
            send_user = self.request.user,
            receive_user = apply.Apply_room.Room_Host,
        )

        return super().form_valid(form)