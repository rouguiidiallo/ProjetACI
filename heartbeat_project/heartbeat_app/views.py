from django.shortcuts import render

# Create your views here.
# views.py: Créez une vue pour gérer les Heartbeat packets et le transfert de données audio à Kafka :
from django.http import HttpResponse
from .models import Heartbeat
from django.utils import timezone
from kafka import KafkaProducer

def receive_heartbeat(request, raspberry_pi_id):
    try:
        heartbeat = Heartbeat.objects.get(raspberry_pi_id=raspberry_pi_id)
        heartbeat.last_heartbeat = timezone.now()
        heartbeat.save()
    except Heartbeat.DoesNotExist:
        Heartbeat.objects.create(raspberry_pi_id=raspberry_pi_id)

    return HttpResponse("Heartbeat received")

# transfer audio data to Kafka
def transfer_audio(request, raspberry_pi_id):
    producer = KafkaProducer(bootstrap_servers='your_kafka_broker')
    audio_data = request.body  # Assuming audio data is sent in the request body
    producer.send('audio_topic', value=audio_data)
    
    return HttpResponse("Audio data transferred to Kafka")
