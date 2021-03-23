import time, random
import uuid
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(0.2, 1)

    @task
    def read_pessoas(self):
        self.client.get('/pessoa/')

    @task
    def create_pessoa(self):
        json = {
           "nome": str(uuid.uuid4()),
           "data_nascimento": "2000-05-09",
           "genero": random.choice(self.generos),
           "interesse": random.choice(self.interesses)
        }

        self.client.post('/pessoa/', json = json)

    def on_start(self):
        self.generos = ['Hetero', 'Lésbica', 'Gay']
        self.interesses = ['Homens', 'Mulheres']