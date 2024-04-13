from django.shortcuts import render
from resApp.models import Evenement
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from datetime import datetime


@login_required
def index(request):
    evenements = Evenement.objects.filter(author=request.user.id)
    context = { "evenements": evenements }
    return render(request, "index.html", context)

# formulaire pour créer un événement
# views.py
from django.shortcuts import render, redirect
from .forms import EvenementForm

def create_evenement(request):
    if request.method == 'POST':
        form = EvenementForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            start_date = form.cleaned_data['start_date']
            start_time = form.cleaned_data['start_time']
            end_date = form.cleaned_data['end_date']
            end_time = form.cleaned_data['end_time']
            
            # Combiner la date et l'heure de début et de fin
            start = datetime.combine(start_date, start_time)
            end = datetime.combine(end_date, end_time)
            
            # Créer un nouvel événement avec les données récupérées
            nouvel_evenement = Evenement.objects.create(
                name=name,
                start=start,
                end=end,
                author=request.user
            )
            return redirect('index')  # Redirigez vers une vue de confirmation
    else:
        form = EvenementForm()
    return render(request, 'create_evenement.html', {'form': form})

# formulaire pour modifier un événement
def update_evenement(request,evenement_id):
    evenement = Evenement.objects.get(id=evenement_id)
    if request.method == 'POST':
        form = EvenementForm(request.POST, instance=evenement)
        if form.is_valid():
            name = form.cleaned_data['name']
            start_date = form.cleaned_data['start_date']
            start_time = form.cleaned_data['start_time']
            end_date = form.cleaned_data['end_date']
            end_time = form.cleaned_data['end_time']
            
            # Combiner la date et l'heure de début et de fin
            start = datetime.combine(start_date, start_time)
            end = datetime.combine(end_date, end_time)
            
            # Mettre à jour l'événement avec les données récupérées
            evenement.name = name
            evenement.start = start
            evenement.end = end
            evenement.save()
            return redirect('index')  # Redirigez vers une vue de confirmation
    else:
        form = EvenementForm(instance=evenement)
    return render(request, 'update_evenement.html', {'form': form})




@login_required
def lister_evenements(request):
    evenements = Evenement.objects.filter(author=request.user)
    return render(request, 'evenements.html', {'evenements': evenements})


@login_required
def evenements(request):
    evenements = Evenement.objects.filter(author=request.user)
    out = []

    for evenement in evenements:
        start_formatted = evenement.start.strftime("%Y-%m-%dT%H:%M:%S") if evenement.start else None
        end_formatted = evenement.end.strftime("%Y-%m-%dT%H:%M:%S") if evenement.end else None
        out.append({
            "title": evenement.name,
            "id": evenement.id,
            "start": start_formatted,
            "end": end_formatted,
        })
    return JsonResponse(out, safe=False)



def add_evenement(request):
    title = request.GET.get("title")
    start = request.GET.get("start")
    end = request.GET.get("end")
    evenement = Evenement(name=title, start=start, end=end)
    evenement.save()
    data = {}

    return JsonResponse(data)


def edit_evenement(request):
    id = request.GET.get("id")
    title = request.GET.get("title")
    start = request.GET.get("start")
    end = request.GET.get("end")
    evenement = Evenement.objects.get(id=id)
    evenement.name = title
    evenement.start = start
    evenement.end = end
    evenement.save()
    data = {}

    return JsonResponse(data)


def delete_evenement(request):
    id = request.GET.get("id")
    evenement = Evenement.objects.get(id=id)
    evenement.delete()
    data = {}

    return JsonResponse(data)