from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    def save_model(self, request, obj, form, change):
        if not change:
            obj.autor = request.user
        obj.save()


# tutorial/models.py https://django-tables2.readthedocs.io/en/latest/pages/tutorial.html
class Person(models.Model):
    name = models.CharField(max_length=100, verbose_name="full name")

class Pizza(models.Model):
    LARGE = 'L'
    MEDIUM = 'M'
    SMALL = 'S'
    ROZMIARY = (
        (LARGE, 'duża'),
        (MEDIUM, 'średnia'),
        (SMALL, 'mała'),
    )
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    nazwa = models.CharField(verbose_name='Pizza', max_length=30)
    opis = models.TextField(blank=True, help_text='Opis Pizzy')
    rozmiar = models.CharField(max_length=1, choices=ROZMIARY, default=MEDIUM)
    cena = models.DecimalField(max_digits=5, decimal_places=2)
    data = models.DateField('dodano', auto_now_add=True)
    class Meta:
        verbose_name_plural = 'pizzunie'
    def __str__(self):
        return self.nazwa + '  ' + str(self.cena)

class Skladnik(models.Model):
    pizza = models.ForeignKey(Pizza,
                              on_delete=models.CASCADE,
                              related_name='skladniki')
    nazwa = models.CharField(verbose_name="składnik", max_length=30)
    jarski = models.BooleanField(
        default=False,
        verbose_name="jarski ?",
        help_text="Zaznacz, jeżeli składnik jest odpowiedni dla wegetarian.")
    class Meta:
        verbose_name_plural = 'Składniki'
    def __str__(self):
        return self.nazwa

class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)




