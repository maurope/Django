from django.db import models

# Create your models here.
class Car(models.Model):
    title =models.TextField(max_length=250)
    year = models.TextField(max_length=4, null=True)
    color = models.TextField(max_length=20, null=True)

    def __str__(self):
        return f'{self.title} - {self.year} - {self.color}'
    
class Publisher(models.Model):
    name = models.TextField(max_length=200)
    address = models.TextField(max_length=200)

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.TextField(max_length=200)
    birth_date = models.DateField()

    def __str__(self):
        return self.name
    
class Profile(models.Model):
    author = models.OneToOneField(Author, on_delete=models.CASCADE)
    website = models.URLField() # Para que el autor publique su página web
    biography = models.TextField(max_length=500)

class Book(models.Model):
    title = models.TextField(max_length=200)
    publication_date = models.DateField()
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE) #Si alguien intenta borrar el publisher no lo va  poder hacer, porque esta protegido. Si borran el publisher, cascade eliminará todos los libros asociados al publisher.
    authors = models.ManyToManyField(Author, related_name='authors') #Nos permite relacionar varios autores a un mismo libro
    
    def __str__(self):
        return self.title
    

