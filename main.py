class Employer:
    def __init__(self, numpermis, nom, prenom):
        self.numpermis = numpermis
        self.nom = nom
        self.prenom = prenom
        self.voiture = None

    def afficherInformations(self):
        print("----- Employe -----")
        print("Numero de permis :", self.numpermis)
        print("Nom :", self.nom)
        print("Prenom :", self.prenom)

        if self.voiture is None:
            print("Voiture de service : aucune")
        else:
            print("Voiture de service :", self.voiture.matricule)