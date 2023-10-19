from django.db import models

# Create your models here.
# Dans notre heartbeat_app, on va créez un modèle Heartbeat pour stocker les informations du Raspberry Pi :

class Heartbeat(models.Model):
    raspberry_pi_id = models.CharField(max_length=255, unique=True)
    last_heartbeat = models.DateTimeField(auto_now=True)
