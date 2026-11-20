
# Monitoramento Automático de Sites e Servidores

## 1. Descrição do projeto

Sistema desenvolvido em Python para monitorar automaticamente
a disponibilidade de sites e servidores por meio de requisições HTTP.

O programa identifica falhas, envia alertas para um canal do Discord,
detecta a recuperação dos serviços e registra as verificações
em um arquivo JSON.

Projeto desenvolvido para a disciplina de Automação e
Programabilidade em Redes.

## 2. Problema e objetivo

A indisponibilidade de sites e servidores pode passar despercebida
quando não existe um processo de monitoramento contínuo.

O objetivo deste projeto é automatizar essa verificação,
reduzindo a necessidade de consultas manuais e permitindo
uma resposta mais rápida a falhas.

## 3. Funcionalidades

- Monitoramento de múltiplos sites por HTTP/HTTPS.
- Identificação de códigos de resposta HTTP.
- Medição do tempo de resposta em milissegundos.
- Detecção de serviços online e offline.
- Envio de alertas automáticos ao Discord.
- Notificação quando um serviço volta a funcionar.
- Prevenção de alertas repetidos enquanto a falha persiste.
- Agendamento automático de verificações.
- Armazenamento do histórico em JSON.
- Tratamento de erros de conexão e timeout.
- Configuração de credenciais por variáveis de ambiente.

## 4. Tecnologias utilizadas

- Python
- Requests
- Schedule
- Python-dotenv
- Discord Webhooks
- HTTP/HTTPS
- JSON


## 5. Arquitetura

Fluxo de funcionamento:

```text
Agendador (Schedule)
        |
        v
Programa principal (main.py)
        |
        v
Monitor HTTP (monitor.py)
        |
        v
Sites e servidores
        |
        v
Resultado da verificação
        |
        +----> Histórico JSON
        |
        +----> Detecção de mudança de estado
                    |
                    v
              Discord Webhook
```


O sistema utiliza requisições HTTP para consultar os sites
e uma integração HTTP POST para enviar notificações ao Discord.


## 6. Estrutura do projeto

O projeto está organizado da seguinte forma:

```text
monitoramento-redes/
│
├── main.py
├── monitor.py
├── discord_alert.py
├── config.py
├── historico.py
├── teste_recuperacao.py
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
│
└── data/
    └── historico.json (gerado localmente)
```

### Descrição dos arquivos

- **main.py:** controla a execução e o agendamento do monitoramento.
- **monitor.py:** realiza as requisições HTTP e verifica a disponibilidade dos sites.
- **discord_alert.py:** envia alertas de falha e recuperação ao Discord.
- **config.py:** carrega e valida as configurações do sistema.
- **historico.py:** registra os resultados das verificações em JSON.
- **teste_recuperacao.py:** simula uma queda e recuperação para testar as notificações.
- **requirements.txt:** lista as dependências do projeto.
- **.env.example:** apresenta as variáveis de ambiente necessárias.
- **.gitignore:** impede o versionamento de arquivos privados e temporários.
- **README.md:** contém a documentação do projeto.
- **data/historico.json:** armazena localmente o histórico das verificações.


## 7. Instalação e configuração

### Requisitos

- Python 3.10 ou superior
- Conexão com a internet
- Webhook de um canal do Discord

### Instalação

Clone o repositório:

```bash
git clone https://github.com/AnthonyTLOU7/monitoramento-redes.git
cd monitoramento-redes
```

Crie o ambiente virtual:

```bash
python -m venv .venv
```

Ative o ambiente virtual no Windows:

```powershell
.\.venv\Scripts\Activate.ps1
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Crie um arquivo `.env` com base no `.env.example`:

```dotenv
DISCORD_WEBHOOK_URL=COLE_SEU_WEBHOOK_AQUI
CHECK_INTERVAL=60
```

Execute o programa:

```bash
python main.py
```

Para interromper, pressione Ctrl+C.

## 8. Funcionamento dos alertas

O programa verifica o estado dos sites periodicamente.

- Se um site estiver offline na primeira verificação,
  um alerta será enviado.
- Se um site passar de online para offline,
  um novo alerta será enviado.
- Enquanto continuar offline, o alerta não será repetido.
- Quando voltar a ficar online, será enviada uma
  notificação de recuperação.

Os estados anteriores são mantidos em memória durante a execução.

## 9. Histórico em JSON

Cada verificação gera um registro com:

- URL monitorada.
- Data e hora.
- Código HTTP.
- Tempo de resposta.
- Estado online ou offline.
- Descrição do erro, quando houver.

O histórico é armazenado localmente em `data/historico.json`.

## 10. Testes realizados

- Monitoramento de sites com HTTP 200.
- Identificação de resposta HTTP 503.
- Envio de alertas reais ao Discord.
- Prevenção de alertas duplicados.
- Teste simulado de queda e recuperação,
  com envio real das notificações ao Discord.
- Registro automático das verificações em JSON.

## 11. Segurança

A URL do webhook é armazenada no arquivo `.env`.

O arquivo `.gitignore` impede o envio do `.env`,
do ambiente virtual e do histórico local ao GitHub.

O arquivo `.env.example` documenta as variáveis necessárias,
sem divulgar credenciais reais.

## 12. Limitações e melhorias futuras

- Criar uma interface web para acompanhar os servidores.
- Permitir configurar os sites por arquivo externo.
- Implementar relatórios e gráficos.
- Armazenar o histórico em banco de dados.
- Adicionar notificações por e-mail.
- Permitir configurar limites de tempo de resposta.
- Melhorar o desempenho para monitorar muitos servidores.

## 13. Demonstração

A demonstração apresenta:

1. Inicialização do monitoramento.
2. Verificação dos sites configurados.
3. Identificação de falha HTTP 503.
4. Recebimento de alerta no Discord.
5. Registro das verificações em JSON.
6. Teste simulado de queda e recuperação.
