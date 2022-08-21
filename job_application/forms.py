from django.forms import RadioSelect, CheckboxSelectMultiple, FileInput, TextInput, Textarea, EmailInput
from multipage_form.forms import MultipageForm, ChildForm
from .models import JobApplication

from crispy_forms.helper import FormHelper

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

form_control = {'class': 'form-control'}

class JobApplicationForm(MultipageForm):
    model = JobApplication
    starting_form = "Stage1Form"
        
    class Stage1Form(ChildForm):
      display_name = "Informações Pessoais"
      required_fields = "__all__"
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
            ], attrs={'class': 'form-group'}),

          'data_nascimento': DateSelectorWidget(attrs={
            'class': 'form-select',
            }),
          'nome_completo': TextInput(attrs=form_control),
          'email': EmailInput(attrs=form_control),
          'celular': TextInput(attrs=form_control),
        }

    
    class Stage2Form(ChildForm):
      display_name = "Sistemas de Trabalho"
      next_form_class = 'Stage3Form'

      class Meta:
        fields = ['presencial', 'hibrido', 'meio_periodo']
        widgets = { 
          'presencial': RadioSelect(choices=[(True, "Sim"), (False, "Não")]),
          'hibrido': RadioSelect(choices=[(True, "Sim"), (False, "Não")]),
          'meio_periodo': RadioSelect(choices=[(True, "Sim"), (False, "Não")]),
        }

    
    class Stage3Form(ChildForm):
      display_name = "Dispositivos"
      next_form_class = 'Stage4Form'

      class Meta:
        fields = ['possui_pc', 'possui_smartphone']
        widgets = {
          'possui_pc': RadioSelect(choices=[(True, "Sim"), (False, "Não")]),
          'possui_smartphone': RadioSelect(choices=[(True, "Sim"), (False, "Não")]),
        }


    class Stage4Form(ChildForm):
      display_name = "Informações Profissionais"
      next_form_class = 'Stage5Form'

      class Meta:
        fields = ['experiencia_profissional', 'trabalha_atualmente']
        widgets = {
          'experiencia_profissional': RadioSelect(choices=[(True, "Sim"), (False, "Não")]),
          'trabalha_atualmente': RadioSelect(choices=[(True, "Sim"), (False, "Não")]),
        }


    class Stage5Form(ChildForm):
      display_name = "Escolaridade"
      required_fields = ['escola']
      next_form_class = 'Stage6Form'

      class Meta:
        fields = ['ensino_medio_tecnico', 'escola', 'formacao_cursos']
        widgets = {
          'ensino_medio_tecnico': RadioSelect(choices=[(True, "Sim"), (False, "Não")]),
          'escola': TextInput(attrs=form_control),
          'formacao_cursos': Textarea(attrs=form_control),
        }


    class Stage6Form(ChildForm):
      display_name = 'Área Desejada'
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
      display_name = 'Tecnologias Back-end'
      next_form_class = 'Stage7Form'
      required_fields = '__all__'
      
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
      display_name = 'Tecnologias Front-end'
      next_form_class = 'Stage7Form'
      required_fields = '__all__'
      
      class Meta:
        fields = ['frontend']
        widgets = {
          'frontend': CheckboxSelectMultiple(choices=[
            ('javascript', "JavaScript"), 
            ('react', "React"), 
            ('react native', "React Native"), 
            ('typescript', "TypeScript"), 
            ('next.js', "Next.js"), 
            ('vue.js', "Vue.js"), 
            ('flutter', "Flutter"), 
            ('figma', "Figma"), 
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
      display_name = "NOCODE / LOWCODE"
      next_form_class = 'Stage8Form'
      required_fields = '__all__'

      class Meta:
        fields = ['nocode_lowcode_tecnologias']
        widgets = {
          'nocode_lowcode_tecnologias': TextInput(attrs=form_control),
        }
    

    class Stage8Form(ChildForm):
      display_name = "Experiência Profissional"
      next_form_class = 'Stage9Form'
      required_fields = '__all__'

      class Meta:
        fields = ['nivel_profissional', 'tempo_trabalhado']
        widgets = {
          'nivel_profissional': RadioSelect(choices=[
            ('aprendiz', "Aprendiz"), 
            ('júnior', "Júnior"),
            ('pleno', 'Pleno'),
            ('sênior', 'Sênior'),
            ('especialista', 'Especialista'),
            ('gestor', 'Gestor')
            ]),
          'tempo_trabalhado': RadioSelect(choices=[
            ('nenhuma experiência', 'Nenhuma experiência em empresa'),
            ('freelancer', 'Apenas trabalhei como freelancer'),
            ('menos de um ano', 'Menos de um ano'),
            ('até três anos', 'Até três anos'),
            ('até cinco anos', 'Até cinco anos'),
            ('até dez anos', 'Até dez anos'),
            ('até vinte anos', 'Até vinte anos'),
          ])
        }


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
      display_name = 'Inglês'
      next_form_class = 'Stage10Form'

      class Meta:
        fields = ['nivel_ingles']
        widgets = {
          'nivel_ingles': RadioSelect(choices=[
            ('técnico', 'Técnico'),
            ('google translator', 'Google Translator'),
            ('me comunico com dificuldade', 'Consigo me comunicar com certa dificuldade'),
            ('fluente', 'Pronto para viajar para Miami e voltar com um contrato assinado'),
          ])
        }

    
    class Stage10Form(ChildForm):
      display_name = 'Modelo de Contratação'
      required_fields = '__all__'
      
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
      display_name = 'Pessoa Jurídica'
      next_form_class = 'Stage11Form'

      class Meta:
        fields = ['possui_empresa']
        widgets = {
          'possui_empresa': RadioSelect(choices=[(True, "Sim"), (False, "Não")]),
        }

    
    class Stage11Form(ChildForm):
      display_name = 'Dúvidas'
      
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
      display_name = 'Dúvidas'
      next_form_class = 'Stage12Form'
      required_fields = '__all__'
      
      class Meta:
        fields = ['qual_duvida']
        widgets = {
          'qual_duvida': Textarea(attrs=form_control)
        }


    class Stage12Form(ChildForm):
      display_name = 'Sugestões'
      
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
      display_name = 'Sugestões'
      next_form_class = 'Stage13Form'
      required_fields = '__all__'
      
      class Meta:
        fields = ['qual_sugestao']
        widgets = {
          'qual_sugestao': Textarea(attrs=form_control)
        }


    class Stage13Form(ChildForm):
      display_name = 'Indicação'
      
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
      display_name = 'Indicação'
      next_form_class = 'Stage14Form'
      required_fields = '__all__'

      class Meta:
        fields = ['quem_indicou']
        widgets = {
          'quem_indicou': TextInput(attrs=form_control)
        }


    class Stage14Form(ChildForm):
      display_name = 'Pense um pouco!'
      next_form_class = 'Stage15Form'
      required_fields = '__all__'
      
      class Meta:
        fields = ['importancia']
        widgets = {
          'importancia': TextInput(attrs=form_control)
        }


    class Stage15Form(ChildForm):
      display_name = 'Currículo'
      next_form_class = 'LastStageForm'
      required_fields = '__all__'

      class Meta:
        fields = ['curriculo']
        widgets = {
          'curriculo': FileInput(attrs=form_control)
        }


    class LastStageForm(ChildForm):
      required_fields = '__all__'
      template_name = 'form_page_w_summary.html'

      class Meta:
        fields = ['tudo_pronto']