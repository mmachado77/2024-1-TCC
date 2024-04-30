from django.db import models

class AreaInteresseEnum(models.TextChoices):
    ALGORITMOS_COMBINATORIA_E_OTIMIZACAO = "Algoritmos, Combinatória e Otimização"
    ARQUITETURA_DE_COMPUTADORES_E_PROCESSAMENTO_DE_ALTO_DESEMPENHO = "Arquitetura de Computadores e Processamento de Alto Desempenho"
    BANCO_DE_DADOS = "Banco de Dados"
    BIOLOGIA_COMPUTACIONAL = "Biologia Computacional"
    COMPUTACAO_APLICADA_A_SAUDE = "Computação Aplicada à Saúde"
    COMPUTACAO_GRAFICA_E_PROCESSAMENTO_DE_IMAGENS = "Computação Gráfica e Processamento de Imagens"
    COMPUTACAO_MUSICAL = "Computação Musical"
    COMPUTACAO_UBIQUA_E_PERVASIVA = "Computação Ubíqua e Pervasiva"
    CONCEPCAO_DE_CIRCUITOS_INTEGRADOS = "Concepção de Circuitos Integrados"
    ENGENHARIA_DE_SOFTWARE = "Engenharia de Software"
    GEO_INFORMATICA = "Geo Informática"
    INFORMATICIA_NA_EDUCACAO = "Informática na Educação"
    INTELIGENCIA_ARTIFICIAL = "Inteligência Artificial"
    INTELIGENCIA_COMPUTACIONAL = "Inteligência Computacional"
    INTERACAO_HUMANO_COMPUTADOR = "Interação Humano Computador"
    IAPR = "International Association for Pattern Recognition (IAPR)"
    JOGOS_E_ENTRETENIMENTO = "Jogos e Entretenimento"
    LINGUAGENS_DE_PROGRAMACAO = "Linguagens de Programação"
    METODOS_FORMAIS = "Métodos Formais"
    PROCESSAMENTO_DE_LINGUAGEM_NATURAL = "Processamento de Linguagem Natural"
    REALIDADE_VIRTUAL = "Realidade Virtual"
    REDES_DE_COMPUTADORES_E_SISTEMAS_DISTRIBUIDOS = "Redes de Computadores e Sistemas Distribuídos"
    ROBOTICA = "Robótica"
    SEGURANCA = "Segurança"
    SISTEMAS_COLABORATIVOS = "Sistemas Colaborativos"
    SISTEMAS_DE_INFORMACAO = "Sistemas de Informação"
    SISTEMAS_MULTIMIDIA_E_HIPERMIDIA = "Sistemas Multimídia e Hipermídia"
    SISTEMAS_TOLERANTES_A_FALHAS = "Sistemas Tolerantes a Falhas"

    def __str__(self):
        return self.label