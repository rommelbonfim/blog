 from django.db.models.deletion import CASCADE
from django.urls import reverse
from django.db import models
from django.db.models.fields import CharField
from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation



# Create your models here.
class Autores(models.Model):
  nome_autor= models.CharField(null=True,max_length=250)
  cidade_autor = models.CharField(null=True, max_length=250)
  imagem_autor = models.ImageField(null=True, blank= True, upload_to="imagens/" )
class Campos(models.Model):
  titulo = models.CharField(max_length=250)
  subtitulo = models.CharField(max_length=250)
  imagem = models.ImageField(null=True, blank= True, upload_to="imagens/" )
  tipo_noticia = models.CharField(null=True,max_length=250)
  data= models.DateTimeField(null=True,auto_now_add=False)
  legenda_foto = models.CharField(null=True,max_length=250)
  descricao = models.TextField(null=True,max_length=4000)
  autor_materia = models.ForeignKey(Autores,on_delete=CASCADE)
  visualizacoes = models.IntegerField(default=0)
  slug = models.SlugField(null=True)
  hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk',
     related_query_name='hit_count_generic_relation')

  def __str__(self):
        return self.titulo


  def get_absolute_url(self):
        return reverse('materia', kwargs={'slug': self.slug})



  


  