# Serviço de Coleta de Dados do Omini

Este projeto é um serviço em Python que coleta dados do Omini e os salva em um banco de dados PostgreSQL. Ele utiliza o **Alembic** para gerenciamento de migrações de banco de dados.

## Pré-requisitos

- Docker
- Docker Compose

## Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/larissamato/service-report.git
   cd service-report
   ```

2. Copie o arquivo `.env.example` para `.env` na raiz do projeto.

   > **Nota:** Altere os valores conforme necessário para sua configuração local.

3. Execute o comando para iniciar os containers:

   ```bash
   docker-compose up --build
   ```

## Estrutura do Projeto

- **app/**: Contém a aplicação Python.
- **migrations/**: Diretório gerenciado pelo Alembic para migrações do banco de dados.

## Migrações do Banco de Dados

Este projeto usa Alembic para gerenciar as migrações de banco de dados. As migrações serão aplicadas automaticamente quando o serviço for iniciado.

Se você precisar gerar novas migrações manualmente, use os comandos abaixo:

1. Para criar uma nova migração:

   ```bash
   docker-compose exec app alembic revision --autogenerate -m "mensagem da migração"
   ```

2. Para aplicar as migrações:

   ```bash
   docker-compose exec app alembic upgrade head
   ```

## Parar o Serviço

Para parar os containers, execute:

```bash
docker-compose down
```
