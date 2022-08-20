from dataclasses import field, fields
from django.core.exceptions import ValidationError
from django.forms import RadioSelect, CheckboxSelectMultiple, FileInput
from multipage_form.forms import MultipageForm, ChildForm
from .models import JobApplication

from datetime import date
from django import forms

# Class to get the date
class DateSelectorWidget(forms.MultiWidget):
    def __init__(self, attrs=None):
        days = [(day, day) for day in range(1, 32)]
        months = [(month, month) for month in range(1, 13)]
        years = [(year, year) for year in reversed(range(1950, 2023))]
        widgets = [
            forms.Select(attrs=attrs, choices=days),
            forms.Select(attrs=attrs, choices=months),
            forms.Select(attrs=attrs, choices=years),
        ]
        super().__init__(widgets, attrs)

    def decompress(self, value):
        if isinstance(value, date):
            return [value.day, value.month, value.year]
        elif isinstance(value, str):
            year, month, day = value.split('-')
            return [day, month, year]
        return [None, None, None]

    def value_from_datadict(self, data, files, name):
        day, month, year = super().value_from_datadict(data, files, name)
        # DateField expects a single string that it can parse into a date.
        return f'{day}/{month}/{year}'


class JobApplicationForm(MultipageForm):
    model = JobApplication
    starting_form = "Stage1Form"
        
    class Stage1Form(ChildForm):
      display_name = "Informações Pessoais"
      #required_fields = "__all__"
      next_form_class = 'Stage2Form'

      class Meta:
        fields = ['nome_completo', 'data_nascimento', 'email', 'celular', 'cidade']
        widgets = {
          'cidade': RadioSelect(choices=[
            ('Juazeiro do Norte', 'Juazeiro do Norte'), 
            ('Crato', 'Crato'), 
            ('Barbalha', 'Barbalha'),
            ('Miami', 'Miami'),
            ('São Paulo', 'São Paulo'),
            ]),
          'data_nascimento': DateSelectorWidget()
        }

    
    class Stage2Form(ChildForm):
      display_name = "Informações Adicionais"
      # required_fields = "__all__"
      next_form_class = 'Stage3Form'

      class Meta:
        fields = ['presencial', 'hibrido', 'meio_periodo']
        widgets = { 
          'presencial': RadioSelect(choices=[(True, "Sim"), (False, "Não")]),
          'hibrido': RadioSelect(choices=[(True, "Sim"), (False, "Não")]),
          'meio_periodo': RadioSelect(choices=[(True, "Sim"), (False, "Não")]),
        }

    
    class Stage3Form(ChildForm):
      display_name = "Suporte a Home Office"
      next_form_class = 'Stage4Form'

      class Meta:
        fields = ['possui_pc', 'possui_smartphone']
        widgets = {
          'possui_pc': RadioSelect(choices=[(True, "Sim"), (False, "Não")]),
          'possui_smartphone': RadioSelect(choices=[(True, "Sim"), (False, "Não")]),
        }


    class Stage4Form(ChildForm):
      display_name = "Trabalho"
      next_form_class = 'Stage5Form'

      class Meta:
        fields = ['experiencia_profissional', 'trabalha_atualmente']
        widgets = {
          'experiencia_profissional': RadioSelect(choices=[(True, "Sim"), (False, "Não")]),
          'trabalha_atualmente': RadioSelect(choices=[(True, "Sim"), (False, "Não")]),
        }


    class Stage5Form(ChildForm):
      display_name = "Escolaridade"
      next_form_class = 'Stage6Form'

      class Meta:
        fields = ['ensino_medio_tecnico', 'escola', 'formacao_cursos']
        widgets = {
          'ensino_medio_tecnico': RadioSelect(choices=[(True, "Sim"), (False, "Não")]),
        }


    class Stage6Form(ChildForm):
      display_name = 'Stage6'
      required_fields = '__all__'

      class Meta:
        fields = ['produtos_e_tecnologias']
        widgets = {
          'produtos_e_tecnologias': RadioSelect(choices=[
            ('backend', "Back-end"), 
            ('frontend', "Front-end"),
            ]),
        }

      def get_next_form_class(self):
        if (self.instance.produtos_e_tecnologias.upper() == 'BACKEND'):
          return 'Stage6bForm'
        if (self.instance.produtos_e_tecnologias.upper() == 'FRONTEND'):
          return 'Stage6cForm'


    class Stage6bForm(ChildForm):
      display_name = 'Stage 6b'
      next_form_class = 'Stage7Form'
      
      class Meta:
        fields = ['backend']
        widgets = {
          'backend': CheckboxSelectMultiple(choices=[
            ('php', "PHP"), 
            ('python', "Python"),
            ('django', 'Django'),
            ('node', 'Node.js'),
            ('java', 'Java'),
            ('go', 'GO'),
            ('c#', 'C#'),
            ('sql', 'SQL'),
            ]),
        }


    class Stage6cForm(ChildForm):
      display_name = 'Stage 6c'
      next_form_class = 'Stage7Form'
      
      class Meta:
        fields = ['frontend']
        widgets = {
          'frontend': RadioSelect(choices=[
            ('test', "test"), 
            ('test', "test"), 
            ('test', "test"), 
            ('test', "test"), 
            ('test', "test"), 
            ('test', "test"), 
            ('test', "test"), 
            ('test', "test"), 
            ]),
        }


    class Stage7Form(ChildForm):
      display_name = "Tecnologias Adicionais"
    
      class Meta:
        fields = ['wordpress', 'elementor', 'nocode_lowcode']
        widgets = {
          'wordpress': RadioSelect(choices=[(True, "Sim"), (False, "Não")]),
          'elementor': RadioSelect(choices=[(True, "Sim"), (False, "Não")]),
          'nocode_lowcode': RadioSelect(choices=[(True, "Sim"), (False, "Não")]),
        }

      def get_next_form_class(self):
        if self.instance.nocode_lowcode:
          return 'Stage7bForm'
        return 'Stage8Form'
    

    class Stage7bForm(ChildForm):
      display_name = "Tecnologias Adicionais"
      next_form_class = 'Stage8Form'

      class Meta:
        fields = ['nocode_lowcode_tecnologias']
    

    class Stage8Form(ChildForm):
      display_name = "Job"
      next_form_class = 'Stage9Form'

      class Meta:
        fields = ['nivel_profissional', 'tempo_trabalhado']


    class Stage9Form(ChildForm):
      display_name = 'Mais informações'

      class Meta:
        fields = ['exame', 'ingles']
        widgets = {
          'exame': RadioSelect(choices=[(True, "Sim"), (False, "Não")]),
          'ingles': RadioSelect(choices=[(True, "Sim"), (False, "Não")]),
        }

      def get_next_form_class(self):
        if self.instance.ingles:
          return 'Stage9bForm'
        return 'Stage10Form'


    class Stage9bForm(ChildForm):
      display_name = 'Mais informações'
      next_form_class = 'Stage10Form'

      class Meta:
        fields = ['nivel_ingles']

    
    class Stage10Form(ChildForm):
      display_name = 'Stage 10'
      #next_form_class = 'Stage10Form'
      

      class Meta:
        fields = ['modelo_contratacao']
        widgets = {
          'modelo_contratacao': RadioSelect(choices=[
            ('clt', 'CLT'), 
            ('pj', 'PJ'), 
            ('estágio', 'Contrato Estágio'), 
            ('aprendiz', 'Contrato Aprendiz')
            ])
        }
        
      def get_next_form_class(self):
        # print(self.instance.modelo_contratacao)
        if (self.instance.modelo_contratacao.upper() == 'PJ'):
          return 'Stage10bForm'
        return 'Stage11Form'

    
    class Stage10bForm(ChildForm):
      display_name = 'Stage10bForm'
      next_form_class = 'Stage11Form'

      class Meta:
        fields = ['possui_empresa']
        widgets = {
          'possui_empresa': RadioSelect(choices=[(True, "Sim"), (False, "Não")]),
        }

    
    class Stage11Form(ChildForm):
      display_name = 'Stage 11'
      
      class Meta:
        fields = ['duvida']
        widgets = {
          'duvida': RadioSelect(choices=[(True, "Sim"), (False, "Não")]),
        }

      def get_next_form_class(self):
        if self.instance.duvida:
          return 'Stage11bForm'
        return 'Stage12Form'

    
    class Stage11bForm(ChildForm):
      display_name = 'Stage 11b'
      next_form_class = 'Stage12Form'
      
      class Meta:
        fields = ['qual_duvida']


    class Stage12Form(ChildForm):
      display_name = 'Stage 12'
      
      class Meta:
        fields = ['sugestao']
        widgets = {
          'sugestao': RadioSelect(choices=[(True, "Sim"), (False, "Não")]),
        }

      def get_next_form_class(self):
        if self.instance.sugestao:
          return 'Stage12bForm'
        return 'Stage13Form'

    
    class Stage12bForm(ChildForm):
      display_name = 'Stage 12b'
      next_form_class = 'Stage13Form'
      
      class Meta:
        fields = ['qual_sugestao']


    class Stage13Form(ChildForm):
      display_name = 'Stage 13'
      
      class Meta:
        fields = ['indicacao']
        widgets = {
          'indicacao': RadioSelect(choices=[(True, "Sim"), (False, "Não")]),
        }

      def get_next_form_class(self):
        if self.instance.indicacao:
          return 'Stage13bForm'
        return 'Stage14Form'


    class Stage13bForm(ChildForm):
      display_name = 'Stage 13b'
      next_form_class = 'Stage14Form'

      class Meta:
        fields = ['quem_indicou']


    class Stage14Form(ChildForm):
      display_name = 'Stage 14'
      next_form_class = 'Stage15Form'
      
      class Meta:
        fields = ['importancia']


    class Stage15Form(ChildForm):
      display_name = 'Stage 15'
      next_form_class = 'LastStageForm'

      class Meta:
        fields = ['curriculo']
        widgets = {
          'curriculo': FileInput()
        }


    class LastStageForm(ChildForm):
      required_fields = '__all__'
      template_name = 'form_page_w_summary.html'

      class Meta:
        fields = ['tudo_pronto']