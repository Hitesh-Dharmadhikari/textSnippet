from django.shortcuts import redirect
from django.shortcuts import render
from django import forms
from .models import AddToDatabase


def Home(request):
    form = form = TakeInput()
    if request.method == 'POST':
        form = TakeInput(request.POST)
        if form.is_valid():
            form_instance = form.save(commit=False)
            form_instance.save()
            return redirect("form_detail", random_url=form_instance.random_url)
    return render(request, 'index.html', {'form':form})


def form_detail(request, random_url):
    template = "form_detail.html"
    context = {}
    form_detail = get_object_or_404(AddToDatabase, random_url=random_url)
    context["form_detail"] = form_detail
    return render(request, template, context)

class TakeInput(forms.ModelForm):

    class Meta:
      model = AddToDatabase
      fields = ["user_input"]