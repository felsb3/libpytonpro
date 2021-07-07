import pytest

from libpythonpro.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'destinatario',
    ['foo@bar.com.br', 'renzo@python.pro.br']
)
def test_remetente(destinatario):
    enviador = Enviador()
    resultato = enviador.enviar(
        destinatario,
        'luvciano@python.pro.br',
        'Cursos Python Pro',
        'Primeira turma Guido Von Rossum aberta.'
    )
    assert destinatario in resultato


@pytest.mark.parametrize(
    'remetente',
    ['', 'renzo']
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'luvciano@python.pro.br',
            'Cursos Python Pro',
            'Primeira turma Guido Von Rossum aberta.'
        )
