from django.db import models

class Tipo_residencia(models.Model):
    name = models.CharField(max_length = 20)
    color = models.CharField(max_length = 10)

    def __unicode__(self):
        return self.color

class Residencia(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    title = models.CharField(max_length = 100)
    address = models.CharField(max_length = 50)
    phone1 = models.CharField(max_length = 15)
    phone2 = models.CharField(max_length = 15)
    email = models.EmailField()
    description = models.CharField(max_length = 300)
    date = models.DateField()
    tipo_residencia = models.ForeignKey(Tipo_residencia)

    def __unicode__(self):
        return self.title

class Imagenes(models.Model):
    url = models.URLField()
    residencia = models.ForeignKey(Residencia)

    def __unicode__(self):
        return self.url

class Institucion(models.Model):
    name = models.CharField(max_length = 100)
    short_name = models.CharField(max_length = 10)

    def __unicode__(self):
        return self.name

class Sede(models.Model):
    name = models.CharField(max_length = 20)
    latitude = models.FloatField()
    longitude = models.FloatField()
    institucion = models.ForeignKey(Institucion)

    def __unicode__(self):
        return self.name