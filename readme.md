# 🗳️ Sistema de Votação Digital (Projeto Integrador I)

## 📌 Descrição do Projeto

Este projeto tem como objetivo o desenvolvimento de um sistema de votação digital executado via terminal, criado exclusivamente para fins acadêmicos. A proposta busca integrar, na prática, conhecimentos de programação em Python, banco de dados e conceitos básicos de segurança da informação.

O sistema foi pensado para simular um processo eleitoral completo, desde o cadastro de eleitores e candidatos até a realização da votação e a apuração dos resultados. Durante o funcionamento, são aplicadas validações de dados, controle de acesso e mecanismos de proteção de informações sensíveis, garantindo maior organização e confiabilidade.

Além disso, o projeto também trabalha com a ideia de rastreabilidade, registrando eventos importantes do sistema e permitindo auditoria dos dados, o que ajuda a entender melhor como sistemas reais lidam com segurança e integridade das informações.

---

## 👥 Integrantes

* Diego Prandi Silva — RA 25002584
* Felipe Oliveira dos Santos — RA 26008705
* João Victor Grisolia Luis — RA 26005781
* Matheus Ribeiro Sakamae — RA 26008956
* Rafael França Cardoso — RA 26001772

---

## 🛠️ Tecnologias Utilizadas

* Python
* MySQL
* Git

---

## ▶️ Instruções para Execução do Sistema

Para rodar o projeto corretamente, siga os passos abaixo:

1. **Clone o repositório**

   ```bash
   git clone https://github.com/DiegoPrandi/ES-PI1-2026-T1-G09.git
   ```

2. **Acesse a pasta do projeto**

   ```bash
   cd ES-PI1-2026-T1-G09
   ```

3. **Instale as dependências necessárias**
   Certifique-se de ter o Python instalado e execute:

   ```bash
   pip install mysql-connector-python python-dotenv
   ```

4. **Configure o banco de dados**

   * Crie um banco de dados no MySQL
   * Execute os scripts SQL disponíveis no projeto (Docs -> database.sql)
   * Crie um arquivo .env na raíz do projeto e ajuste as configurações de conexão no código (host, usuário, senha e nome do banco)

5. **Execute o sistema**

   ```bash
   python LAD.py
   ```

6. **Utilização**

   * O sistema será executado no terminal
   * Utilize o menu exibido para navegar entre as funcionalidades, como:

     * Cadastro de eleitores
     * Gerenciamento de dados
     * Processo de votação
     * Visualização de resultados e auditoria

---

## ⚠️ Observação

Este sistema foi desenvolvido apenas para fins educacionais e não representa um sistema real de votação. Seu objetivo é auxiliar no aprendizado de conceitos fundamentais de desenvolvimento de software, banco de dados e segurança da informação.

---
