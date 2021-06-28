importar  codecs
importar  os
import  sys

de  distutils . util  import  convert_path
from  fnmatch  import  fnmatchcase
em  setuptools  , configuração de importação  , find_packages


def  read ( fname ):
    retornar  codecs . open ( os . path . join ( os . path . dirname ( __file__ ), fname )). ler ()


# Fornecido como um atributo, para que você possa anexá-los
# de replicá-los:
standard_exclude  = [ "* .py" , "* .pyc" , "* $ py.class" , "* ~" , ". *" , "* .bak" ]
standard_exclude_directories  = [
    ". *" , "CVS" , "_darcs" , "./build" , "./dist" , "EGG-INFO" , "* .egg-info"
]


# (c) 2005 Ian Bicking e colaboradores; escrito para Paste (http://pythonpaste.org)
# Licenciado pela licença MIT: http://www.opensource.org/licenses/mit-license.php
# Nota: você pode querer copiar isso para o seu arquivo setup.py literalmente, como
# você não pode importar isso de outro pacote, quando você não sabe se
# esse pacote ainda está instalado.
def  find_package_data (
        onde = "." ,
        pacote = "" ,
        exclude = standard_exclude ,
        exclude_directories = standard_exclude_directories ,
        only_in_packages = True ,
        show_ignored = False ):
    "" "
    Retorne um dicionário adequado para uso em `` package_data``
    em um arquivo distutils `` setup.py``.
    O dicionário se parece com:
        {"pacote": [arquivos]}
    Onde `` files`` é uma lista de todos os arquivos nesse pacote que
    não corresponde a nada em `` excluir``.
    Se `` only_in_packages`` for verdadeiro, então os diretórios de nível superior que
    não são pacotes não serão incluídos (mas diretórios sob pacotes
    vontade).
    Os diretórios que correspondem a qualquer padrão em `` exclude_directories`` irão
    ser ignorado; por diretórios padrão com `` .``, `` CVS``,
    e `` _darcs`` será ignorado.
    Se `` show_ignored`` for verdadeiro, então todos os arquivos que não são
    incluídos nos dados do pacote são mostrados em stderr (para depuração
    finalidades).
    Os padrões de nota usam curingas ou podem ser caminhos exatos (incluindo
    levando ``. / ``), e todas as pesquisas não diferenciam maiúsculas de minúsculas.
    "" "
    out  = {}
    stack  = [( convert_path ( onde ), "" , pacote , only_in_packages )]
    enquanto  pilha :
        onde , prefixo , pacote , only_in_packages  =  stack . pop ( 0 )
        para  nome  em  os . listdir ( onde ):
            fn  =  os . caminho . junte-se ( onde , nome )
            se  os . caminho . isdir ( fn ):
                bad_name  =  False
                para o  padrão  em  exclude_directories :
                    if ( fnmatchcase ( nome , padrão )
                            ou  fn . inferior () ==  padrão . inferior ()):
                        bad_name  =  True
                        se  show_ignored :
                            print ( "Diretório% s ignorado pelo padrão% s"  %
                                  ( fn , padrão ), arquivo = sys . stderr )
                        pausa
                if  bad_name :
                    Prosseguir
                if ( os . path . isfile ( os . path . join ( fn , "__init__.py" ))
                        e  não  prefixo ):
                    se  não  for pacote :
                        novo_pacote  =  nome
                    mais :
                        novo_pacote  =  pacote  +  "."  +  nome
                    empilhar . append (( fn , "" , new_package , False ))
                mais :
                    empilhar . anexar (( fn , prefixo  +  nome  +  "/" , pacote , apenas_em_pacotes ))
             pacote  elif ou  não  only_in_packages :
                # é um arquivo
                bad_name  =  False
                para  padrão  em  excluir :
                    if ( fnmatchcase ( nome , padrão )
                            ou  fn . inferior () ==  padrão . inferior ()):
                        bad_name  =  True
                        se  show_ignored :
                            print ( "Arquivo% s ignorado pelo padrão% s"  %
                                  ( fn , padrão ), arquivo = sys . stderr )
                        pausa
                if  bad_name :
                    Prosseguir
                para fora . setdefault ( pacote , []). anexar ( prefixo  +  nome )
    voltar  para fora


PACKAGE  =  "libpythonpro"
NOME  =  PACKAGE
DESCRIPTION  =  "Módulo para exemplificar construção de projetos Python no curso PyTools"
AUTOR  =  "Renzo Nuccitelli"
AUTHOR_EMAIL  =  "renzo@python.pro.br"
URL  =  "https://github.com/pythonprobr/libpythonpro"
VERSÃO  =  __importar__ ( PACOTE ). __versão__

configuração (
    nome = NOME ,
    versão = VERSÃO ,
    descrição = DESCRIÇÃO ,
    long_description = read ( 'README.md' ),
    long_description_content_type = 'text / markdown' ,
    autor = AUTOR ,
    author_email = AUTHOR_EMAIL ,
    licença = "GNU AFFERO GENERAL PUBLIC LICENSE" ,
    url = URL ,
    pacotes = find_packages ( exclude = [ "testes. *" , "testes" ]),
    package_data = find_package_data ( PACKAGE , only_in_packages = False ),
    classificadores = [
        "Status de Desenvolvimento :: 2 - Pré-Alfa" ,
        "Ambiente :: Console" ,
        "Público-alvo :: Desenvolvedores" ,
        "Licença :: OSI Aprovado :: GNU Affero General Public License v3 ou posterior (AGPLv3 +)" ,
        "Sistema operacional :: Independente do SO" ,
        "Linguagem de programação :: Python" ,
        "Linguagem de programação :: Python :: 3.6" ,
        "Framework :: Pytest" ,
    ],
    install_requires = [
        'solicitações de'
    ],
    zip_safe = False ,
)