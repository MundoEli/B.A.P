from django.db import models


class Task(models.Model):
    title = models.CharField('Naming', max_length=50)
    description = models.TextField('Description')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Pokemon'
        verbose_name_plural = 'Types'
