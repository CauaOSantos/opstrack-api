
def test_raiz_informa_servico_online(client):
    # Arrange: o client vem da fixture (tests/conftest.py)
    # Act
    resposta = client.get('/')

    # Assert
    assert resposta.status_code == 200
    esperado = {
        'servico': 'OpsTrack API',
        'status': 'online'
    }
    assert resposta.get_json() == esperado


def test_status_retorna_ok(client):
    resposta = client.get('/status')

    assert resposta.status_code == 200
    assert resposta.get_json()['status'] == 'ok'


def test_tickets_retorna_lista_com_id_e_titulo(client):
    resposta = client.get('/tickets')

    assert resposta.status_code == 200
    tickets = resposta.get_json()['tickets']

    assert len(tickets) >= 1
    assert 'id' in tickets[0]
    assert 'titulo' in tickets[0]


def test_usuarios_retorna_dois_usuarios(client):
    # Act
    resposta = client.get('/usuarios')

    # Assert
    assert resposta.status_code == 200
    assert len(resposta.get_json()['usuarios']) == 2


def test_rota_inexistente_retorna_404(client):
    # Act
    resposta = client.get('/nao-existe')

    # Assert
    assert resposta.status_code == 404


def test_versao_retorna_versao_atual(client):
    resposta = client.get('/versao')

    assert resposta.status_code == 200
    assert resposta.get_json()['versao'] == '1.0.0'
