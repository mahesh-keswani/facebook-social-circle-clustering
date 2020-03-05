from django.db import models

class Edge(models.Model):

    from_edge = models.IntegerField()
    to_edge = models.IntegerField()
    cluster = models.IntegerField(default=0)
    