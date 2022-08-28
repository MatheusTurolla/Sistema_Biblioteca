from django.db import models

# Create your models here.
class Editora(models.Model):
    Nome_Editora = models.CharField(max_length = 180)
    Cnpj = models.CharField(max_length = 180)

    def __str__(self):
        return self.task

class Autor(models.Model):
    Nome_Autor = models.CharField(max_length = 180)
    Editora = models.ForeignKey(Editora, on_delete = models.CASCADE, blank = True, null = True)

    def __str__(self):
        return self.task

class Livro(models.Model):
    Titulo = models.CharField(max_length = 180)
    Autor = models.ForeignKey(Autor, on_delete = models.CASCADE, blank = True, null = True)
    Editora = models.ForeignKey(Editora, on_delete = models.CASCADE, blank = True, null = True)
    Gênero = models.CharField(max_length = 180)

    def __str__(self):
        return self.task