import uuid
from django.db import models
from multipage_form.models import MultipageModel

from django.utils import timezone


def get_file_path(_instance, filename):
  ext = filename.split('.')[-1]
  filename = f'{uuid.uuid4()}.{ext}'
  return filename


class JobApplication(MultipageModel):
  criacao = models.DateTimeField(default=timezone.now)

  # stage 1 fields
  nome_completo = models.CharField('Nome Completo', max_length=100, blank=True)
  data_nascimento = models.DateField('Data de Nascimento', null=True)
  email = models.EmailField('E-mail', max_length=100, blank=True)
  celular = models.CharField('Celular', max_length=15, blank=True)
  cidade = models.CharField('Cidade', max_length=50, blank=True)

  # stage 2 fields
  presencial = models.BooleanField('Você aceita trabalhar presencialmente em nosso escritório?', default=False)
  hibrido = models.BooleanField('Você aceita trabalhar no modelo híbrido (home office / escritório)?', default=False)
  meio_periodo = models.BooleanField('Você aceita trabalhar meio período?', default=False)
  
  # stage 3 fields
  possui_pc = models.BooleanField('Você possui Computador?', default=False)
  possui_smartphone = models.BooleanField('Você possui Smartphone?', default=False)
  
  # stage 4 fields
  experiencia_profissional = models.BooleanField('Você possui experiência profissional?', default=False)
  trabalha_atualmente = models.BooleanField('Você trabalha atualmente?', default=False)
 
  # stage 5 fields
  ensino_medio_tecnico = models.BooleanField('Você já concluiu o ensino médio técnico?', default=False)
  escola = models.CharField('Escola em que estuda/estudou', max_length=100, blank=True)
  formacao_cursos = models.TextField('Você possui alguma outra formação ou cursos?', blank=True)
  
  # stage 6 fields
  produtos_e_tecnologias = models.CharField('Área de Desenvolvimento', max_length=30, blank=True)
  # stage 6b fields
  backend = models.CharField('Backend', max_length=100, blank=True)
  frontend = models.CharField('Frontend', max_length=100, blank=True)

  # stage 7 fields
  wordpress = models.BooleanField('Você conhece WordPress?', default=False)
  elementor = models.BooleanField('Você conhece Elementor?', default=False)
  nocode_lowcode = models.BooleanField('Você conhece NOCODE / LOWCODE?', default=False)
  # stage 7b fields
  nocode_lowcode_tecnologias = models.CharField('Quais tecnologias você conhece?', max_length=100, blank=True)
  
  # stage 8 fields
  nivel_profissional = models.CharField('Qual nível profissional você se considera?', max_length=30, blank=True)
  tempo_trabalhado = models.CharField('Quanto tempo trabalhou em uma empresa?', max_length=100, blank=True)

  # stage 9 fields
  exame = models.BooleanField('Você aceita realizar um teste?', default=False) # Aceita fazer exame?
  ingles = models.BooleanField('Possui conhecimento de inglês?', default=False) # Possui conhecimento em Inglês?
  # stage 9b fields
  nivel_ingles = models.CharField('Nível de Inglês', max_length=30, blank=True)

  # stage 10 fields
  modelo_contratacao = models.CharField('Qual modelo de contratação você prefere ser contratado?', max_length=30, blank=True)
  # stage 10b fields
  possui_empresa = models.BooleanField('Você possui empresa aberta?', default=False)

  # stage 11 fields
  duvida = models.BooleanField('Você tem alguma dúvida?', default=False)
  # stage 11b fields
  qual_duvida = models.TextField('Qual é a sua dúvida?', blank=True)

  # stage 12 fields
  sugestao = models.BooleanField('Você tem alguma sugestão?', default=False)
  # stage 12b fields
  qual_sugestao = models.TextField('Qual é a sua sugestão?', blank=True)

  # stage 13 fields
  indicacao = models.BooleanField('Você foi indicado por alguém?', default=False)
  # stage 13b fields
  quem_indicou = models.CharField('Quem te indicou?', max_length=100, blank=True)

  # stage 14 fields
  importancia = models.CharField('Qual é a coisa MAIS IMPORTANTE da sua vida?', max_length=100, blank=True)

  # stage 15 fields
  curriculo = models.FileField('Anexe seu currículo aqui', upload_to=get_file_path, blank=True)
  
  # last stage
  tudo_pronto = models.BooleanField('Tudo pronto?', default=False)
