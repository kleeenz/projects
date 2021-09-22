from django.db import models


class suggestion_table(models.Model):
    name = models.CharField(max_length=300)
