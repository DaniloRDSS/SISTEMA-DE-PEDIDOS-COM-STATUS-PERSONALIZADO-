# Sistema de Pedidos com Status Personalizado
License: MIT

Sistema web simples e funcional para o gerenciamento de pedidos em empresas de delivery, lanchonetes e negócios similares, com acompanhamento em tempo real e status personalizáveis. Desenvolvido em Python (Flask) no back-end e HTML, CSS e JavaScript no front-end, é ideal para protótipos e pode ser facilmente escalado para uso em produção. O sistema permite o cadastro de clientes e pedidos, atualização automática ou manual de status, consulta em tempo real e organização dos pedidos por situação.

## Funcionalidades
Cadastro de clientes e pedidos com itens, quantidades e valores.
Atualização automática (simulada) ou manual de status.
Status personalizáveis por tipo de negócio (ex.: Delivery).
Consulta em tempo real do status e histórico do pedido via ID.
Listagem de pedidos em andamento e finalizados.
Histórico de pedidos por cliente.
Interface responsiva com tema de delivery (cores vibrantes, ícones e barra de progresso).

## Tecnologias Utilizadas
### Back-end
Python 3.x
Flask (APIs RESTful)
uuid (geração de IDs únicos)
threading e time (simulação de progresso dos pedidos)
### Front-end
HTML5
CSS3
JavaScript (AJAX com Fetch API)
### Outros
Estruturas de dados em memória (facilmente migráveis para SQLite ou PostgreSQL).

## Pré-requisitos
Python 3.8 ou superior
Pip (gerenciador de pacotes do Python)
Navegador web moderno (Chrome, Firefox, Edge, etc.)

## Instalação e Execução
- Clone o repositório:
<img width="500" height="300" alt="Codigo Clone" src="https://github.com/user-attachments/assets/4ea92f58-3a2c-4e16-9104-808ddda76daa" />

- Instale as dependências:

<img width="500" height="300" alt="Dependencias" src="https://github.com/user-attachments/assets/bc7134b5-3cfb-4ed6-8d39-3fd0926eba15" />

- Estrutura de Arquivos: Certifique-se de que o projeto esteja organizado da seguinte forma:

<img width="500" height="300" alt="estrutura" src="https://github.com/user-attachments/assets/3e5633f0-3a25-40c2-96f4-ab2cd40d423a" />


- Execute o servidor:

<img width="500" height="300" alt="Codigo servidor " src="https://github.com/user-attachments/assets/5dfd258b-53ab-44b3-97af-ca7fc67f320f" />

O servidor será iniciado em: 👉 http://127.0.0.1:5000/

## Uso do Sistema
- Página Principal (/)
Cadastro de clientes e pedidos
Atualização manual de status
Listagem de pedidos e clientes

- Página do Cliente (/cliente)
Consulta do status do pedido via ID
Visualização da barra de progresso
Histórico completo do pedido

## Fluxo de Funcionamento (Exemplo)
Cadastre um cliente (nome e telefone).
Cadastre um pedido vinculado ao cliente.
O pedido inicia com o status "Pedido Recebido".
O status avança automaticamente a cada 5 segundos (simulação).
O cliente acompanha o pedido informando o ID.
O atendente pode alterar o status manualmente, se necessário.

## Estrutura do Projeto
app.py: Contém as rotas Flask, regras de negócio, simulação de status e gerenciamento dos dados.
templates/index.html: Interface principal do atendente.
templates/cliente.html: Página dedicada ao cliente para consulta do pedido.
static/styles.css: Estilos visuais, layout responsivo e tema de delivery.
static/script.js: Scripts JavaScript responsáveis pelas interações dinâmicas e requisições AJAX.

## Escalabilidade e Expansões Futuras
Há possibilidades futuras de:

Integração com leitores de código de barras (ex.: pyzbar).
Aplicativo mobile para entregadores (Flutter ou React Native).
Integração com GPS e notificações.
Migração para banco de dados persistente.
Autenticação de usuários (Flask-Login).
Uso de HTTPS e deploy em ambiente de produção.

## Contribuição
Faça um fork do projeto.
Crie uma branch: git checkout -b feature/nova-funcionalidade
Faça o commit: git commit -m "Adiciona nova funcionalidade"
Envie o push e abra um Pull Request.
## Licença
Este projeto está licenciado sob a Licença MIT. Consulte o arquivo LICENSE para mais informações.

