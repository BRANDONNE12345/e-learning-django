from django.contrib import admin
from .models import (
    Utilisateur, Administrateur, Comptabilite, Enseignant, Etudiant,
    Matiere, Chapitre, Contenu, Quiz, Question, Chat, Message,
    ResponsableScolarite, Forum
)

admin.site.register(Utilisateur)
admin.site.register(Administrateur)
admin.site.register(Comptabilite)
admin.site.register(Enseignant)
admin.site.register(Etudiant)
admin.site.register(Matiere)
admin.site.register(Chapitre)
admin.site.register(Contenu)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Chat)
admin.site.register(Message)
admin.site.register(ResponsableScolarite)
admin.site.register(Forum)
