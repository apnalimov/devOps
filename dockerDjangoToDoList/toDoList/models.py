from django.db import models

# Create your models here.
class ToDo(models.Model):
    title = models.CharField('Название', max_length = 100)
    body = models.TextField('Описание задачи', max_length = 100)
    open_date = models.DateTimeField('Задача открыта', blank = True)
    control_date = models.DateTimeField('Контрольный срок', blank = True)
    is_complete = models.BooleanField('Задача выполенена', default= False)

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return self.title
    