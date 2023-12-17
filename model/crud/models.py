from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=50)
    age = models.PositiveIntegerField(default=1, verbose_name='Возраст')
    # gender = models.ForeignKey('Gender',on_delete=models.CASCADE)
    birthDay = models.DateTimeField(verbose_name='Дата рождения', default='2020-03-03')

    def __str__(self):
        return f'{self.name} {self.surname}'

    class Meta:
        verbose_name = 'Человек'
        verbose_name_plural = 'Люди'


class Gender(models.Model):
    sex = models.CharField(max_length=3)

    def __str__(self):
        return f'{self.sex}'


class News(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    is_published = models.BooleanField(default=True)
    category = models.CharField(max_length=20, choices=[(1, 'Cпорт'), (2, 'Красота')])

    def __str__(self):
        return self.title
