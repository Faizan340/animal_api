from django.db import models

class AnimalModel(models.Model):
    Type = (
        ('1', 'Herbivore'),
        ('2', 'Carnivore'),
        ('3', 'Omnivore')
    )
    name = models.CharField(max_length = 100)
    sound = models.CharField(max_length = 100, null = True, blank = True)
    type = models.CharField(max_length = 1, choices = Type, null = True, blank = True)
    species = models.CharField(max_length = 100, null = True, blank = True)
    habitat = models.CharField(max_length = 100, null = True, blank = True)

    # Function to return name on table
    def __str__(self):
        return self.name
