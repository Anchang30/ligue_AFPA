from django.db import models

# Create your models here.
class Joueur(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=50)
    prenoms = models.CharField(max_length=80)
    photo = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nom
    
class Club(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=60) 
    logo = models.CharField(max_length=255)
    nom_ligue = models.CharField(max_length=50)
    ville = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nom
    
class Rencontre(models.Model):
    id = models.AutoField(primary_key=True)
    date_match = models.DateField()
    num_journee = models.IntegerField(default=0)
    equipe_dom = models.CharField(max_length=60)
    equipe_vis = models.CharField(max_length=60)
    buts_dom = models.IntegerField(default=0)
    buts_vis = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.equipe_dom} face à {self.equipe_vis}"
    
class Ligue(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=50)
    pays = models.CharField(max_length=50)
    logo = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nom