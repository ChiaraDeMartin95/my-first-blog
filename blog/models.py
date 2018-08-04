from django.db import models
from django.utils import timezone

#from, import servono per importare pezzi di un altro file in questo stesso file
class Post(models.Model):
    # Con Class creiamo il nostro oggetto, che si chiama Post (p maiuscola).
    # Il pezzo in parentesi indica che si tratta di un modello Django, che dovrà essere salvato nel suo database
    author = models.ForeignKey('auth.User')  #link ad un altro modello
    title = models.CharField(max_length=200) #definisco testo con numero limitato di caratteri
    text = models.TextField()                #definisco testo con numero illimitato di caratteri
    created_date = models.DateTimeField(
        default=timezone.now
    )
    published_date = models.DateTimeField(
        blank=True,
        null=True
    )

    def publish(self):   #def indica che si tratta di una funzione/metodo e publish è il nome del metodo
        self.published_date = timezone.now()
        self.save()

    def __str__(self):   #questo metodo mi ritorna il titolo del post
        return self.title