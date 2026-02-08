from flask import Flask, render_template, request, jsonify
import threading
import time
import uuid  # Para gerar IDs únicos

app = Flask(__name__)

# Estruturas de dados em memória (simulando banco)
clientes = {}  # {id: {'nome': str, 'telefone': str}}
pedidos = []   # Lista de pedidos: [{'id': str, 'cliente_id': str, 'itens': [{'nome': str, 'quantidade': int, 'valor': float}], 'valor_total': float, 'status_atual': str, 'historico': [{'status': str, 'timestamp': str}], 'tipo_negocio': str}]

# Configuração de status por tipo de negócio (personalizável)
status_por_tipo = {
    'Delivery': ['Pedido Recebido', 'Em Preparo', 'Saiu para Entrega', 'Entregue']
    # Adicione mais tipos aqui, ex.: 'Balconista': ['Recebido', 'Preparando', 'Pronto']
}

# Função para simular tempo de preparo (opcional)
def simular_preparo(pedido_id):
    pedido = next((p for p in pedidos if p['id'] == pedido_id), None)
    if not pedido:
        return
    status_list = status_por_tipo.get(pedido['tipo_negocio'], [])
    for i, status in enumerate(status_list[1:], 1):  # Pula o primeiro status (já definido)
        time.sleep(5)  # Simula 5 segundos por etapa (ajuste conforme necessário)
        atualizar_status(pedido_id, status)

# Função para atualizar status
def atualizar_status(pedido_id, novo_status):
    pedido = next((p for p in pedidos if p['id'] == pedido_id), None)
    if pedido:
        pedido['status_atual'] = novo_status
        pedido['historico'].append({'status': novo_status, 'timestamp': time.strftime('%Y-%m-%d %H:%M:%S')})

@app.route('/', endpoint='index_endpoint')
def index():
    return render_template('index.html')

# Nova rota para a página do cliente
@app.route('/cliente', endpoint='cliente_endpoint')
def pagina_cliente():
    return render_template('cliente.html')

@app.route('/cadastrar_cliente', methods=['POST'], endpoint='cadastrar_cliente_endpoint')
def cadastrar_cliente():
    nome = request.form['nome']
    telefone = request.form['telefone']
    cliente_id = str(uuid.uuid4())  # Gera ID único
    clientes[cliente_id] = {'nome': nome, 'telefone': telefone}
    return jsonify({'message': 'Cliente cadastrado com sucesso!', 'cliente_id': cliente_id})

@app.route('/cadastrar_pedido', methods=['POST'], endpoint='cadastrar_pedido_endpoint')
def cadastrar_pedido():
    cliente_id = request.form['cliente_id']
    itens = request.form.getlist('itens[]')  # Lista de nomes de itens
    quantidades = request.form.getlist('quantidades[]')  # Lista de quantidades
    valores = request.form.getlist('valores[]')  # Lista de valores unitários
    tipo_negocio = request.form['tipo_negocio']
    
    # Calcula valor total e estrutura itens
    itens_pedido = []
    valor_total = 0
    for nome, qtd, val in zip(itens, quantidades, valores):
        qtd = int(qtd)
        val = float(val)
        itens_pedido.append({'nome': nome, 'quantidade': qtd, 'valor': val})
        valor_total += qtd * val
    
    pedido_id = str(uuid.uuid4())
    status_inicial = status_por_tipo.get(tipo_negocio, ['Recebido'])[0]  # Status inicial
    pedido = {
        'id': pedido_id,
        'cliente_id': cliente_id,
        'itens': itens_pedido,
        'valor_total': valor_total,
        'status_atual': status_inicial,
        'historico': [{'status': status_inicial, 'timestamp': time.strftime('%Y-%m-%d %H:%M:%S')}],
        'tipo_negocio': tipo_negocio
    }
    pedidos.append(pedido)
    
    # Inicia simulação de preparo em thread separada (opcional)
    # threading.Thread(target=simular_preparo, args=(pedido_id,)).start()
    
    return jsonify({'message': 'Pedido cadastrado com sucesso!', 'pedido_id': pedido_id})

@app.route('/atualizar_status', methods=['POST'], endpoint='atualizar_status_endpoint')
def atualizar_status_route():
    pedido_id = request.form['pedido_id']
    novo_status = request.form['novo_status']
    atualizar_status(pedido_id, novo_status)
    return jsonify({'message': 'Status atualizado!'})

@app.route('/consultar_status/<pedido_id>', methods=['GET'], endpoint='consultar_status_endpoint')
def consultar_status(pedido_id):
    pedido = next((p for p in pedidos if p['id'] == pedido_id), None)
    if pedido:
        return jsonify({'status': pedido['status_atual'], 'historico': pedido['historico']})
    return jsonify({'error': 'Pedido não encontrado'}), 404

@app.route('/listar_pedidos', methods=['GET'], endpoint='listar_pedidos_endpoint')
def listar_pedidos():
    em_andamento = [p for p in pedidos if p['status_atual'] != 'Entregue']  # Ajuste conforme status final
    finalizados = [p for p in pedidos if p['status_atual'] == 'Entregue']
    return jsonify({'em_andamento': em_andamento, 'finalizados': finalizados})

@app.route('/historico_cliente/<cliente_id>', methods=['GET'], endpoint='historico_cliente_endpoint')
def historico_cliente(cliente_id):
    historico = [p for p in pedidos if p['cliente_id'] == cliente_id and p['status_atual'] == 'Entregue']
    return jsonify({'historico': historico})

# Nova rota para listar todos os clientes
@app.route('/listar_clientes', methods=['GET'], endpoint='listar_clientes_endpoint')
def listar_clientes():
    # Retorna a lista de clientes como JSON: [{'id': str, 'nome': str, 'telefone': str}, ...]
    lista_clientes = [{'id': cid, 'nome': dados['nome'], 'telefone': dados['telefone']} for cid, dados in clientes.items()]
    return jsonify({'clientes': lista_clientes})

if __name__ == '__main__':
    app.run(debug=True)




    