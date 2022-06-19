import imp
from pydoc import describe
from django.db import models
from django.core.validators import MinLengthValidator


class Contact(models.Model):
    address = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.address

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Person(models.Model):
    genders = (
        ('M','Male'),
        ('F','Female')
    )
    duty_types = (
        ('1','Crew'),
        ('2','Cast'),
        ('3','Director'),
        ('4','Writer'),
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.CharField(max_length=3000)
    last_name = models.CharField(max_length=100)
    image_name = models.CharField(max_length=50)
    date= models.DateField()
    gender = models.CharField(max_length=1,choices=genders)
    duty_type = models.CharField(max_length=1,choices=duty_types)
    contact = models.OneToOneField(Contact,on_delete=models.CASCADE,null=True,blank=True)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    full_name.fget.short_description = "name surname"

    class Meta:
        verbose_name = "Person"
        verbose_name_plural = "Persons"

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.duty_types[int(self.duty_type)-1][1]})"


class Movie(models.Model):
    title = models.CharField("Title",max_length=100)
    describe = models.TextField("Describe",validators=[MinLengthValidator(20)])
    image_name = models.CharField(max_length=50)
    image_cover = models.CharField(max_length=50)
    date= models.DateField()
    slug = models.SlugField(unique=True, db_index=True)
    budget = models.DecimalField(max_digits=19,decimal_places=2)
    language = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)
    is_home = models.BooleanField(default=False)
    people = models.ManyToManyField(Person)
    genres = models.ManyToManyField(Genre)

    class Meta:
        verbose_name = "Film"
        verbose_name_plural = "Films"
    
    def __str__(self):
        return self.title

class Video(models.Model):
    title = models.CharField(max_length=200)
    url =  models.CharField(max_length=200)
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)

    def __str__(self):
        return self.title