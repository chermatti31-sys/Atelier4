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

    def affecterVoiture(self, voiture):
        if self.voiture is not None:
            print("Erreur : cet employe possede deja une voiture.")
        elif voiture.chauffeur is not None:
            print("Erreur : cette voiture est deja attribuee.")
        else:
            self.voiture = voiture
            voiture.chauffeur = self
            print("Voiture affectee avec succes.")

    def retirerVoiture(self):
        if self.voiture is None:
            print("Erreur : cet employe n'a pas de voiture.")
        else:
            self.voiture.chauffeur = None
            self.voiture = None
            print("Voiture retiree avec succes.")

class Voiture:
    def __init__(self, matricule, annee, marque, kilometrage):
        self.matricule = matricule
        self.annee = annee
        self.marque = marque
        self.kilometrage = kilometrage
        self.chauffeur = None

    def afficherInformations(self):
        print("----- Voiture -----")
        print("Matricule :", self.matricule)
        print("Annee :", self.annee)
        print("Marque :", self.marque)
        print("Kilometrage :", self.kilometrage)

        if self.chauffeur is None:
            print("Chauffeur : aucun")
        else:
            print("Chauffeur :", self.chauffeur.nom, self.chauffeur.prenom)

e1 = Employee("J131", "Ifticene", "Tommy")
e2 = Employee("J103", "Kiwi", "Anis")
e3 = Employee("J129", "Bana", "Lyes")

v1 = Voiture("A15", 2021, "Toyota", 133500)
v2 = Voiture("A16", 2024, "BMW", 45000)
v3 = Voiture("A31", 2025, "Audi", 25000)