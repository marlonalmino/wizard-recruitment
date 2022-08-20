from django.db import models
from multipage_form.models import MultipageModel

from django.utils import timezone

class JobApplication(MultipageModel):
  criacao = models.DateTimeField(default=timezone.now)
  
  # stage test

  # stage 1 fields
  nome_completo = models.CharField('Nome Completo', max_length=100, blank=True)
  data_nascimento = models.DateField('Data de Nascimento', null=True)
  email = models.EmailField('E-mail', max_length=100, blank=True)
  celular = models.CharField('Celular', max_length=15, blank=True)
  cidade = models.CharField('Cidade', max_length=50, blank=True)

  # stage 2 fields
  presencial = models.BooleanField('Trabalhar Presencialmente', default=False)
  hibrido = models.BooleanField('Trabalhar Modelo Híbrido', default=False)
  meio_periodo = models.BooleanField('Trabalhar Meio Período', default=False)
  
  # stage 3 fields
  possui_pc = models.BooleanField('Possui Computador?', default=False)
  possui_smartphone = models.BooleanField('Possui Smartphone?', default=False)
  
  # stage 4 fields
  experiencia_profissional = models.BooleanField('Experiencia Profissional?', default=False)
  trabalha_atualmente = models.BooleanField('Trabalha Atualmente?', default=False)
  partnership = models.BooleanField('Partnership?', default=False)
 
  # stage 5 fields
  ensino_medio_tecnico = models.BooleanField('Ensino Medio Técnico?', default=False)
  escola = models.CharField('Escola', max_length=100, blank=True) # Escola em que estudou/estuda
  formacao_cursos = models.TextField('Formação e Cursos', blank=True)
  
  # stage 6 fields
  produtos_e_tecnologias = models.CharField('Produtos e Tecnologias', max_length=30, blank=True)
  # stage 6b fields
  backend = models.CharField('Backend', max_length=30, blank=True)
  frontend = models.CharField('Frontend', max_length=30, blank=True)



  # stage 7 fields
  wordpress = models.BooleanField('WordPress', default=False)
  elementor = models.BooleanField('Elementor', default=False)
  nocode_lowcode = models.BooleanField('Nocode / Low Code', default=False)
  # stage 6b fields
  nocode_lowcode_tecnologias = models.CharField('Tecnologias Nocode / Low Code', max_length=100, blank=True)
  
  # stage 7 fields
  nivel_profissional = models.CharField('Nível Profissional', max_length=30, blank=True)
  tempo_trabalhado = models.CharField('Tempo Trabalhado', max_length=100, blank=True)

  # stage 8 fields
  exame = models.BooleanField('Exame?', default=False) # Aceita fazer exame?
  ingles = models.BooleanField('Ingles?', default=False) # Possui conhecimento em Inglês?
  # stage 8b fields
  nivel_ingles = models.CharField('Nível de Inglês', max_length=30, blank=True)

  # stage 9 fields
  modelo_contratacao = models.CharField('Modelo de Contratação', max_length=30, blank=True)
  # stage 9b fields
  possui_empresa = models.BooleanField('Você possui empresa aberta?', default=False)

  # stage 10 fields
  duvida = models.BooleanField('Dúvida?', default=False)
  # stage 10b fields
  qual_duvida = models.TextField('Qual a dúvida?', blank=True)

  # stage 11 fields
  sugestao = models.BooleanField('Sugestão?', default=False)
  # stage 11b fields
  qual_sugestao = models.TextField('Qual a sugestão?', blank=True)

  # stage 12 fields
  indicacao = models.BooleanField('Indicacao?', default=False)
  # stage 12b fields
  quem_indicou = models.CharField('Quem indicou?', max_length=100, blank=True)

  # stage 13 fields
  importancia = models.CharField('Qual a coisa mais importante da sua vida?', max_length=100, blank=True)
  
  # last stage
  tudo_pronto = models.BooleanField('Tudo pronto?', default=False)
