from django.db import models

# ------------------------------------------------------------------
# Modèle de base pour les utilisateurs
# ------------------------------------------------------------------
class Utilisateur(models.Model):
    idutilisateur = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    motdepasse = models.CharField(max_length=255)
    role = models.CharField(max_length=50)
    
    def se_connecter(self):
        # Implémenter la logique de connexion
        pass
    
    def se_deconnecter(self):
        # Implémenter la logique de déconnexion
        pass
    
    def __str__(self):
        return f"{self.prenom} {self.nom}"

# ------------------------------------------------------------------
# Administrateur hérite de Utilisateur
# ------------------------------------------------------------------
class Administrateur(Utilisateur):
    def ajouter_utilisateur(self, utilisateur):
        # Logique pour ajouter un utilisateur
        pass

    def definir_role(self, utilisateur, role):
        # Logique pour définir le rôle d’un utilisateur
        pass

    def superviser_plateforme(self):
        # Logique pour superviser la plateforme
        pass

# ------------------------------------------------------------------
# Comptabilite
# ------------------------------------------------------------------
class Comptabilite(models.Model):
    def suivre_paiements(self):
        pass
    
    def traiter_paie_enseignants(self):
        pass
    
    def generer_rapport_financier(self):
        pass

# ------------------------------------------------------------------
# Enseignant hérite de Utilisateur
# ------------------------------------------------------------------
class Enseignant(Utilisateur):
    # Un enseignant peut enseigner plusieurs matières et inversement
    matieres = models.ManyToManyField('Matiere', related_name='enseignants')
    
    def acceder_matiere(self, matiere):
        pass
    
    def organiser_cours(self):
        pass
    
    def publier_contenu(self):
        pass
    
    def creer_forum(self):
        pass
    
    def ajouter_quiz(self):
        pass

# ------------------------------------------------------------------
# Etudiant hérite de Utilisateur
# ------------------------------------------------------------------
class Etudiant(Utilisateur):
    # Un étudiant suit plusieurs matières
    matieres = models.ManyToManyField('Matiere', related_name='etudiants')
    
    def consulter_cours(self):
        pass
    
    def passer_quiz(self):
        pass
    
    def participer_forum(self):
        pass
    
    def consulter_notes(self):
        pass

# ------------------------------------------------------------------
# Matiere
# ------------------------------------------------------------------
class Matiere(models.Model):
    idmatiere = models.AutoField(primary_key=True)
    nom_matiere = models.CharField(max_length=100)
    
    def get_nom_matiere(self):
        return self.nom_matiere
    
    def __str__(self):
        return self.nom_matiere

# ------------------------------------------------------------------
# Chapitre associé à une Matiere
# ------------------------------------------------------------------
class Chapitre(models.Model):
    idchapitre = models.AutoField(primary_key=True)
    titre = models.CharField(max_length=200)
    # Chaque chapitre appartient à une matière
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE, related_name='chapitres')
    
    def __str__(self):
        return self.titre

# ------------------------------------------------------------------
# Contenu associé à un Chapitre
# ------------------------------------------------------------------
class Contenu(models.Model):
    idcontenu = models.AutoField(primary_key=True)
    type_contenu = models.CharField(max_length=50)
    data = models.TextField()
    # Chaque contenu est lié à un chapitre
    chapitre = models.ForeignKey(Chapitre, on_delete=models.CASCADE, related_name='contenus')
    
    def afficher_contenu(self):
        return self.data
    
    def __str__(self):
        return f"{self.type_contenu}"

# ------------------------------------------------------------------
# Quiz avec une liste de questions
# ------------------------------------------------------------------
class Quiz(models.Model):
    idquiz = models.AutoField(primary_key=True)
    titre = models.CharField(max_length=200)
    nombre_tentatives = models.IntegerField(default=1)
    correction_automatique = models.BooleanField(default=False)
    
    def ajouter_question(self, question):
        # Vous pouvez ajouter la logique pour créer une question associée
        pass
    
    def definir_tentatives(self, tentatives):
        self.nombre_tentatives = tentatives
        self.save()
    
    def activer_correction_auto(self):
        self.correction_automatique = True
        self.save()
    
    def __str__(self):
        return self.titre

# Un modèle complémentaire pour les questions d’un quiz
class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    texte = models.TextField()
    
    def __str__(self):
        return self.texte[:50]

# ------------------------------------------------------------------
# Chat entre utilisateurs
# ------------------------------------------------------------------
class Chat(models.Model):
    idchat = models.AutoField(primary_key=True)
    participants = models.ManyToManyField(Utilisateur, related_name='chats')
    
    def envoyer_message(self, message):
        pass
    
    def consulter_messages(self):
        return self.messages.all()
    
    def __str__(self):
        return f"Chat {self.idchat}"

# Message pour les chats et forums
class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messages')
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    contenu = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.utilisateur} : {self.contenu[:20]}"

# ------------------------------------------------------------------
# Responsable Scolarite hérite de Utilisateur
# ------------------------------------------------------------------
class ResponsableScolarite(Utilisateur):
    def gerer_structure_academique(self):
        pass
    
    def inscrire_utilisateur(self, utilisateur):
        pass
    
    def affecter_matiere(self, utilisateur, matiere):
        pass

# ------------------------------------------------------------------
# Forum
# ------------------------------------------------------------------
class Forum(models.Model):
    idforum = models.AutoField(primary_key=True)
    titre = models.CharField(max_length=200)
    # Vous pouvez lier directement les messages ou créer une relation inverse via Message
    messages = models.ManyToManyField(Message, blank=True, related_name='forums')
    
    def poser_question(self, message):
        pass
    
    def repondre_question(self, message):
        pass
    
    def __str__(self):
        return self.titre
