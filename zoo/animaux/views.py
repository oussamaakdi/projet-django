from django.core.checks import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import animal, equipement
from .controleur import nourrir, divertir, coucher, réveiller


def index(request):
    return render(request, 'animaux/index.html')


def decouvrir_animaux(request):
    animaux = animal.objects.all()
    return render(request, 'animaux/decouvrir_animaux.html', {'animaux': animaux})


def animalerie(request):
    animaux = animal.objects.all()
    equipements = equipement.objects.all()
    list_equipements = [equipement.name for equipement in equipements]
    list_animaux = [animal.name for animal in animaux]
    animal_in_nid = animal.objects.filter(lieu="nid")
    nid_url = [animal.image_url for animal in animal_in_nid]

    animal_in_roue = animal.objects.filter(lieu="roue")
    roue_url = [animal.image_url for animal in animal_in_roue]

    animal_in_mangeoire = animal.objects.filter(lieu="mangeoire")
    mangeoire_url = [animal.image_url for animal in animal_in_mangeoire]

    animal_in_litière = animal.objects.filter(lieu="litière")
    litière_urls = [animal.image_url for animal in animal_in_litière]




    return render(request, 'animaux/animalerie.html', {'animaux': animaux, 'equipements': equipements,'list_animaux':list_animaux,'list_equipements':list_equipements ,'nid_url':nid_url,'litière_urls':litière_urls,  'roue_url':roue_url,'mangeoire_url':mangeoire_url})





def action(request):
    if request.method == 'POST':
        id_animal = request.POST.get('id_animal')
        action = request.POST.get('action')

        if action == "nourrir":
            msag = nourrir(id_animal)
            request.session['msag'] = msag
            return redirect('animalerie')
        elif action == "divertir":
            msag = divertir(id_animal)
            request.session['msag'] = msag
            return redirect('animalerie')
        elif action == "coucher":
            msag = coucher(id_animal)
            request.session['msag'] = msag
            return redirect('animalerie')
        else:
            msag = réveiller(id_animal)
            request.session['msag'] = msag
            return redirect('animalerie')
