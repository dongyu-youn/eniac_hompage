from django.shortcuts import render
from django.views.generic import CreateView
from . import models, forms
from studies import models as studies_models
from users import models as users_models

# Create your views here.

class CreateApplyView(CreateView):
    
    template_name = 'applies/create.html'
    form_class = forms.ApplyModelForm
    queryset = models.Apply.objects.all()

    def form_valid(self, form):
        apply=form.save(commit=False)
        apply.apply_room = studies_models.Study.objects.get(pk=self.kwargs.get("pk"))
        # print(form.apply_room)
        apply.apply_user = self.request.user
        apply.save()

        return super().form_valid(form)

def applieslist(request, pk):
    study = studies_models.Study.objects.get(pk = pk)
    applies = models.Apply.objects.filter(apply_room = study)
    # print(request.POST.get("allow"))
    # print(users_models.User.objects.get(email = request.POST.get("allow")))
    if(request.POST.get('allow')):
        study.Room_Member.add(users_models.User.objects.get(email = request.POST.get("allow")))
        apply = models.Apply.objects.get(apply_user = users_models.User.objects.get(email = request.POST.get("allow")))
        apply.delete()
    applies = models.Apply.objects.filter(apply_room = study)
    return render(request, "applies/list.html",{
        "applies": applies,
        "study": study,
    })