# py manage.py shell
# >>> exec(open('script_inicial.py').read())

from django.contrib.auth.models import User
from app.models import TccStatus, Tcc, Semestre, Configuracoes, ProfessorInterno, Estudante, StatusCadastro, Coordenador, ProfessorExterno
from datetime import datetime
from oauth2_provider.models import Application
from meutcc.settings import SOCIAL_AUTH_GOOGLE_REDIRECT_URI, SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET, SOCIAL_AUTH_GOOGLE_OAUTH2_KEY

# Criando usuário admin
superuser = User.objects.create_superuser("admin", "admin@admin.com", "123")

# Cria Status André
status = StatusCadastro.objects.create(
    aprovacao = True
)
status2 = StatusCadastro.objects.create(
    aprovacao = False
)
status3 = StatusCadastro.objects.create(
    aprovacao = False
)

status4 = StatusCadastro.objects.create(
    aprovacao = True
)
status5 = StatusCadastro.objects.create(
    aprovacao = False
)

# Cria um professor interno
andreUser = User.objects.create_user("andre@restinga.ifrs.edu.br", "andre@restinga.ifrs.edu.br", "151515")
andre = ProfessorInterno.objects.create(nome="André Schneider", 
                         cpf="12345678911", 
                         email="andre@restinga.ifrs.edu.br",
                         area = "Informática",
                         grau_academico = "Mestre",
                         titulos="Rei do VPL, Inimigo do Python",
                         matricula="1994000401",
                         status = status,
                         user = andreUser
                        )

ProfInterUser = User.objects.create_user("cleitin@restinga.ifrs.edu.br", "cleitin@restinga.ifrs.edu.br", "05156413231")
cleitin = ProfessorInterno.objects.create(nome="Cleitin", 
                         cpf="05156413231", 
                         email="cleitin@restinga.ifrs.edu.br",
                         area = "Informática",
                         grau_academico = "Mestre",
                         titulos="Rei do VPL, Inimigo do Python",
                         matricula="1994000402",
                         status = status4,
                         user = ProfInterUser
                        )

ProfInter2User = User.objects.create_user("interno@restinga.ifrs.edu.br", "interno@restinga.ifrs.edu.br", "05156413232")
adastolfo = ProfessorInterno.objects.create(nome="Adastolfo", 
                         cpf="05156413232", 
                         email="interno@restinga.ifrs.edu.br",
                         area = "Informática",
                         grau_academico = "Challenger",
                         titulos="Pai do inter",
                         matricula="1994000402",
                         status = status5,
                         user = ProfInter2User
                        )

# Adiciona professor como atual coordenador
configMaster = Configuracoes.objects.create(
        dataAberturaPrazoPropostas=datetime.today(),
        dataFechamentoPrazoPropostas=datetime.today(),
        coordenadorAtual=andre)

# Cria usuario estudante
estudanteUser = User.objects.create_user("estudante@gmail.com", "estudante@gmail.com", "12345678912")
estudante = Estudante.objects.create(nome="Estudante", 
                      cpf="12345678912", 
                      email="estudante@gmail.com",
                      user=estudanteUser)

coordenadorUser = User.objects.create_user("coordenador@gmail.com", "coordenador@gmail.com", "151515")
coordenador = Coordenador.objects.create(nome="Coordenador", cpf="151515", email="coordenador@gmail.com", user = coordenadorUser)

ProfExternoUser = User.objects.create_user("externo@gmail.com", "externo@gmail.com", "98765432153")
ProfExterno = ProfessorExterno.objects.create(
                        nome="ProfExterno",
                        cpf="98765432153", 
                        email="externo@gmail.com",
                        area = "Informática",
                        grau_academico = "Doutorado",
                        titulos="Gremista",
                        status = status3,
                        user = ProfExternoUser
                        )

ProfExterno2User = User.objects.create_user("externo2@gmail.com", "externo2@gmail.com", "98765432154")
ProfExterno = ProfessorExterno.objects.create(
                        nome="ProfExterno2",
                        cpf="98765432154", 
                        email="externo2@gmail.com",
                        area = "Informática",
                        grau_academico = "Mestre",
                        titulos="2 Copa do Brasil",
                        status = status2,
                        user = ProfExterno2User
                        )

semestre = Semestre.objects.create(
        periodo='2024/1',
        dataAberturaSemestre=datetime.today(),
        dataFechamentoSemestre=datetime.today(),
        configuracoes=configMaster,
        coordenador=andre
    )


tcc = Tcc.objects.create(
        autor= estudante,
        orientador= cleitin,
        semestre= semestre,
        tema='Desenvolvimento de um Sistema de Gerenciamento de Tarefas',
        resumo='Este trabalho apresenta o desenvolvimento de um sistema web para gerenciamento de tarefas, utilizando Django como framework.'
    )

tcc_status = TccStatus.objects.create(
                        status= "PROPOSTA_ANALISE_PROFESSOR",
                        dataStatus= datetime.today(),
                        tcc= tcc                                

)

Application.objects.create(
    client_id=SOCIAL_AUTH_GOOGLE_OAUTH2_KEY,
    client_secret=SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET,
    redirect_uris=SOCIAL_AUTH_GOOGLE_REDIRECT_URI,
    client_type="confidential",
    authorization_grant_type="authorization-code",
    name="Google",
    user=superuser,
)

print("Usuários criados com sucesso!")