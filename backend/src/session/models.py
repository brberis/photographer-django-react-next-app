from django.db import models
from events.models import Event
from products.models import Item
from contacts.models import Person
from billing.models import Orders

STATUS = (
    ('Active', 'Active'),
    ('Suspended', 'Suspended'),
    ('Finished', 'Finished'),
    ('Cancelled', 'Cancelled')
)

class Catering(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(default='', blank=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS, default='Active', max_length=50)
    number_of_guests = models.IntegerField(default=10, null=False)
    products = models.ManyToManyField(Item)
    team = models.ManyToManyField(Person)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        return self.title 