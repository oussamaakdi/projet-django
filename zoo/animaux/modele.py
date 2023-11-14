from .models import animal, equipement

animaux = animal.objects.all()
equipements = equipement.objects.all()
list_equipements = [equipement.name for equipement in equipements]
liste_états = ['affamé', 'fatigué', 'repus', 'endormi']
list_animaux = [animal.name for animal in animaux]


def lit_état(id_animal):
    if id_animal in list_animaux:
        animal_recherche = animal.objects.get(name=id_animal)
        etat_de_animal = animal_recherche.etat
        return etat_de_animal
    else:
        return None


def lit_lieu(id_animal):
    if id_animal in list_animaux:
        animal_recherche = animal.objects.get(name=id_animal)
        lieu_de_animal = animal_recherche.lieu
        return lieu_de_animal
    else:
        return None


def vérifie_disponibilité(id_équipement):
    if id_équipement in list_equipements:
        equipement_recherche = equipement.objects.get(name=id_équipement)
        return equipement_recherche.disponibilite
    else:
        return None


def cherche_occupant(lieu):
    if lieu in list_equipements:
        liste = []
        for id_animal in list_animaux:
            anim = animal.objects.get(name=id_animal)
            if anim.lieu == lieu:
                liste += [id_animal]
        return liste
    else:
        return None



def change_état(id_animal, état):
    if id_animal in list_animaux:
        if état in liste_états:
            animal_recherche = animal.objects.get(name=id_animal)
            animal_recherche.etat = état
            animal_recherche.save()


def change_lieu(id_animal, lieu):
    if id_animal in list_animaux:
        if lieu in list_equipements:
            equipement_lieu = equipement.objects.get(name=lieu)
            animal_ = animal.objects.get(name=id_animal)
            if equipement_lieu.disponibilite != 'occupé':
                lieu_vacant = animal_.lieu
                animal_.lieu = lieu
                if lieu != 'litière':
                    equipement_lieu.disponibilite = 'occupé'
                ancien_equipement_lieu = equipement.objects.get(name=lieu_vacant)
                ancien_equipement_lieu.disponibilite = 'libre'
                animal_.save()
                equipement_lieu.save()
                ancien_equipement_lieu.save()

