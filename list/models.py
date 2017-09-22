from django.db import models


class List(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return "{}".format(self.title)


class Item(models.Model):
    parent = models.ForeignKey(List)
    content = models.CharField(max_length=255)

    def __str__(self):
        return "{} - {}".format(self.parent, self.content)
