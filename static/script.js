// Função para adicionar item dinamicamente
function adicionarItem() {
    const container = document.getElementById('itens-container');
    const itemDiv = document.createElement('div');
    itemDiv.className = 'item';
    itemDiv.innerHTML = `
        <input type="text" name="itens[]" placeholder="Nome do Item" required>
        <input type="number" name="quantidades[]" placeholder="Quantidade" required>
        <input type="number" step="0.01" name="valores[]" placeholder="Valor Unitário" required>
    `;
    container.appendChild(itemDiv);
}

// Cadastro de cliente
document.getElementById('form-cliente').addEventListener('submit', function(e) {
    e.preventDefault();
    const formData = new FormData(this);
    fetch('/cadastrar_cliente', { method: 'POST', body: formData })
        .then(res => res.json())
        .then(data => document.getElementById('msg-cliente').textContent = data.message + ' ID: ' + data.cliente_id);
});

// Cadastro de pedido
document.getElementById('form-pedido').addEventListener('submit', function(e) {
    e.preventDefault();
    const formData = new FormData(this);
    fetch('/cadastrar_pedido', { method: 'POST', body: formData })
        .then(res => res.json())
        .then(data => document.getElementById('msg-pedido').textContent = data.message + ' ID: ' + data.pedido_id);
});

// Atualizar status
document.getElementById('form-status').addEventListener('submit', function(e) {
    e.preventDefault();
    const formData = new FormData(this);
    fetch('/atualizar_status', { method: 'POST', body: formData })
        .then(res => res.json())
        .then(data => document.getElementById('msg-status').textContent = data.message);
});

// Consultar status
function consultarStatus() {
    const pedidoId = document.getElementById('consulta-pedido-id').value;
    fetch(`/consultar_status/${pedidoId}`)
        .then(res => res.json())
        .then(data => {
            if (data.error) {
                document.getElementById('status-pedido').textContent = data.error;
            } else {
                document.getElementById('status-pedido').textContent = `Status: ${data.status}`;
            }
        });
}

// ... (código existente acima)

// Listar pedidos
function listarPedidos() {
    fetch('/listar_pedidos')
        .then(res => res.json())
        .then(data => {
            const div = document.getElementById('lista-pedidos');
            div.innerHTML = '<h3>Em Andamento</h3>' + data.em_andamento.map(p => `<p>ID: ${p.id}, Status: ${p.status_atual}</p>`).join('') +
                            '<h3>Finalizados</h3>' + data.finalizados.map(p => `<p>ID: ${p.id}, Status: ${p.status_atual}</p>`).join('');
        });
}

// Nova função para listar clientes
function listarClientes() {
    fetch('/listar_clientes')
        .then(res => res.json())
        .then(data => {
            const div = document.getElementById('lista-clientes');
            if (data.clientes.length === 0) {
                div.innerHTML = '<p>Nenhum cliente cadastrado.</p>';
            } else {
                div.innerHTML = '<ul>' + data.clientes.map(c => `<li>ID: ${c.id} - Nome: ${c.nome} - Telefone: ${c.telefone}</li>`).join('') + '</ul>';
            }
        })
        .catch(error => {
            document.getElementById('lista-clientes').innerHTML = '<p>Erro ao carregar clientes.</p>';
        });
}