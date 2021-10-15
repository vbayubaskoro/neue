from django.db import models
import string
import random




# Create your models here.
class Playlist(models.Model):
    id = models.CharField(max_length =10, default = "", unique = True, primary_key=True)
    name = models.CharField(max_length =50, default = "", unique = True)
    number_of_tracks = models.CharField(max_length =10, default = "", unique = True)
    user_id = models.CharField(max_length =10, default = "", unique = True)
    saved = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add=True)

class User(models.Model):
    id = models.CharField(max_length =10, default = "", unique = True,primary_key=True)
    name = models.CharField(max_length =50, default = "", unique = True)
    created_at = models.DateTimeField(auto_now_add=True)



class Track(models.Model):
    id = models.CharField(max_length =10, default = "", unique = True,primary_key=True)
    name = models.CharField(max_length =50, default = "", unique = True)
    artist_id = models.CharField(max_length =10, default = "", unique = False)
    album_id = models.CharField(max_length =10, default = "", unique = False) 
    release_date = models.DateTimeField(auto_now_add=True) 
    genre_id = models.IntegerField(max_length =10, default = "", unique = False)


class Artist(models.Model):
    id = models.CharField(max_length =10, default = "", unique = True,primary_key=True)
    name = models.CharField(max_length =50, default = "", unique = True)
    


class Album(models.Model):
    id = models.CharField(max_length =10, default = "", unique = True,primary_key=True)
    name = models.CharField(max_length =50, default = "", unique = True)




