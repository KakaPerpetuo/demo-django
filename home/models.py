from django.db import models


class Mensagem(models.Model):
    titulo = models.CharField(max_length=120)
    conteudo = models.TextField()
    autor = models.CharField(max_length=80, default="Anônimo")   # ← novo campo
    criada_em = models.DateTimeField(auto_now_add=True)
    tag = models.CharField(max_length=80, default="Geral") # ← novo campo

    class Meta:
        ordering = ["-criada_em"]

    def __str__(self):
        return self.titulo
