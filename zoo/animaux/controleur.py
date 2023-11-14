from .modele import lit_état, lit_lieu,change_état,change_lieu,cherche_occupant,vérifie_disponibilité

def nourrir(id_animal):
    if lit_état(id_animal) is not None:
        if lit_état(id_animal) != 'affamé':
            f = 'Désolé,' + id_animal + " n'a pas faim..."
            return f
        elif vérifie_disponibilité('mangeoire') != 'libre':
            occupant = cherche_occupant('mangeoire')
            f = 'Désolé, la mangeoire est occupée par ' + occupant[0]
            return f
        else:
            change_état(id_animal, 'repus')
            change_lieu(id_animal, 'mangeoire')
    else:
        f = "Désolé," + id_animal + " n'est pas un animal connu"
        return f


def divertir(id_animal):
    if lit_état(id_animal) is not None:
        if lit_état(id_animal) != 'repus':
            f = 'Désolé,' + id_animal + " n'est pas en état de faire du sport."
            return f
        elif vérifie_disponibilité('roue') != 'libre':
            occupant = cherche_occupant('roue')
            f = 'Désolé, la roue est occupée par ' + occupant[0]
            return f
        else:
            change_état(id_animal, 'fatigué')
            change_lieu(id_animal, 'roue')
    else:
        f = "Désolé," + id_animal + " n'est pas un animal connu"
        return f


def coucher(id_animal):
    if lit_état(id_animal) is not None:
        if lit_état(id_animal) != 'fatigué':
            f = 'Désolé,' + id_animal + " n'est pas fatigué."
            return f
        elif vérifie_disponibilité('nid') != 'libre':
            occupant = cherche_occupant('nid')
            f = 'Désolé, le nid est occupé par ' + occupant[0]
            return f
        else:
            change_état(id_animal, 'endormi')
            change_lieu(id_animal, 'nid')
    else:
        f = "Désolé," + id_animal + " n'est pas un animal connu"
        return f


def réveiller(id_animal):
    if lit_état(id_animal) is not None:
        if lit_état(id_animal) != 'endormi':
            f = 'Désolé,' + id_animal + " ne dort pas."
            return f
        else:
            change_état(id_animal, 'affamé')
            change_lieu(id_animal, 'litière')
    else:
        f = "Désolé," + id_animal + " n'est pas un animal connu"
        return f
