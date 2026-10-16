from django.db import models

class modalidade(models.Model):
    nome = models.CharField(max_length=150, unique=True)
    tipo = models.BooleanField(choices=[(True, 'Coletivo'), (False, 'Individual')], default=True)
    max_jogadores = models.PositiveIntegerField()
    atletas = models.ManyToManyField('atleta', blank=True, related_name='modalidades_associadas')

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']
        verbose_name = 'Modalidade'
        verbose_name_plural = 'Modalidades'

class equipe(models.Model):
    nome = models.CharField(max_length=150, unique=True)
    curso = models.CharField(max_length=150)
    cor = models.CharField(max_length=7, default='#000000') 
    criada_em = models.DateTimeField(auto_now_add=True)
    atletas = models.ManyToManyField('atleta', blank=True, related_name='equipes_associadas')
    tecnico = models.ForeignKey('tecnico', on_delete=models.CASCADE, related_name='equipes_associadas')
    class Meta:
        ordering = ['nome']
        verbose_name = 'Equipe'
        verbose_name_plural = 'Equipes'

    def __str__(self):
        return self.nome

class tecnico(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField(max_length=150, unique=True)  
    telefone = models.CharField(max_length=150)
    tecnico_equipe = models.ForeignKey(equipe, on_delete=models.CASCADE, related_name='tecnico_associado', null=True, blank=True)
   
    class Meta:
        verbose_name = 'Técnico'
        verbose_name_plural = 'Técnicos'

    def __str__(self):
        return self.nome

class atleta(models.Model):
    nome = models.CharField(max_length=150)
    matricula = models.CharField(max_length=150, unique=True)
    data_nascimento = models.DateField()
    equipe = models.ForeignKey(equipe, on_delete=models.PROTECT, related_name='atletas_membros')
    modalidade = models.ManyToManyField(modalidade, blank=True, related_name='atletas_associados')
    class Meta:
        ordering = ['nome']
        verbose_name = 'Atleta'
        verbose_name_plural = 'Atletas'

    def __str__(self):
        return self.nome



