# Wizard Recruitment
Um multipage-form utilizando Django como a principal ferramenta de desenvolvimento


## Requisitos
Python 3 (ou superior)


## Instalação
Clone o repositório em um diretório de sua preferência.

Dentro do diretório e após instalado o python, execute os seguintes comandos no terminal:
    
    pip install virtualenv

    virtualenv venv

- Para ativar o ambiente virtual(virtualenv), execute o seguinte comando:
    
        venv\Scripts\activate.bat
    
- Com o ambiente virtual ativado, rode os comandos:
    
        pip install -r requirements.txt
        
        python manage.py migrate
        
        python manage.py runserver
    
O servidor deve estar ativo em [http://127.0.0.1:8000/](http://127.0.0.1:8000/) agora.


### Créditos
[ImaginaryLandscape/django-multipage-form](https://github.com/ImaginaryLandscape/django-multipage-form)
