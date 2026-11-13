# BACKLOG — API de tarefas pessoais

## 1. Visão do projeto

Uma API para você registrar e acompanhar suas pendências pessoais. A proposta é permitir criar, consultar e concluir tarefas com poucos comandos, mantendo os dados entre sessões.

## 2. Escopo do MVP

**Entra:**

- Criar uma tarefa com título.
- Listar todas as tarefas, mostrando quais estão concluídas.
- Marcar uma tarefa como concluída.
- Preservar os dados em SQLite, um banco armazenado em arquivo local.

**Base técnica:** Python 3.12, disponível no ambiente; Django 5.2; Django REST Framework; SQLite. Registrar as versões instaladas para reproduzir o ambiente. Compatibilidade conferida na documentação de [Django](https://docs.djangoproject.com/en/5.2/intro/tutorial01/) e [DRF](https://www.django-rest-framework.org/#requirements).

**Contrato mínimo da API:**

| Operação | Requisição | Resultado |
|---|---|---|
| Criar | `POST /tasks/` com `{"title":"Estudar Django"}` | `201`, com `id`, `title` e `completed: false` |
| Listar | `GET /tasks/` | `200`, com uma lista ordenada por ID crescente |
| Concluir | `POST /tasks/{id}/complete/`, sem corpo | `200`, com a tarefa e `completed: true` |

O título deve conter de 1 a 200 caracteres após remover espaços das extremidades. Dados inválidos retornam `400`; concluir um ID inexistente retorna `404`. Repetir a conclusão mantém a tarefa concluída e retorna `200`.

**Não vai entrar:**

- Interface gráfica ou aplicativo.
- Login, usuários ou compartilhamento.
- Edição, exclusão ou reabertura de tarefas.
- Prazos, prioridades, categorias ou notificações.
- Busca, filtros ou paginação.
- Publicação na internet.

## 3. Critério de sucesso

Até o fim das duas semanas, você terá:

- Registrado pelo menos **5 tarefas reais**.
- Concluído pelo menos **3 tarefas**.
- Consultado a lista em **3 dias distintos**.
- Reiniciado o servidor e confirmado que os dados permaneceram.
- Executado os testes automatizados do fluxo principal com resultado satisfatório.

## 4. Backlog de microtarefas

Execute na ordem indicada. Nas funcionalidades, siga **RED → GREEN → REFACTOR**: escreva um teste que falha, implemente o necessário e simplifique preservando os testes.

### Marco 1 — Preparação

- [ ] **Preparar o ambiente e o projeto Django** — T1 · 1h30. Criar ambiente virtual, registrar dependências e configurar um projeto com uma aplicação de tarefas e SQLite. **Pronto quando:** `python manage.py check` executar sem erros e o servidor iniciar em `127.0.0.1`.

### Marco 2 — Fluxo principal

- [ ] **Implementar a criação de tarefas com testes** — T2 · 2h · depende de T1. Criar o modelo, a migração local e o endpoint de criação. **Pronto quando:** um título válido gerar uma tarefa persistida, inicialmente pendente; títulos ausentes, vazios, compostos apenas por espaços ou maiores que 200 caracteres retornarem `400`; os testes passarem.

- [ ] **Implementar a listagem com testes** — T3 · 1h · depende de T2. Retornar os três campos definidos no contrato. **Pronto quando:** uma base vazia retornar `[]` e uma base preenchida mostrar tarefas pendentes e concluídas na ordem combinada; os testes passarem.

- [ ] **Implementar a conclusão com testes** — T4 · 1h30 · depende de T3. Localizar a tarefa e persistir sua conclusão. **Pronto quando:** concluir e consultar novamente mostrar `completed: true`; repetir a operação funcionar; um ID inexistente retornar `404`; os testes passarem.

### Marco 3 — Uso e validação

- [ ] **Documentar como executar e usar a API** — T5 · 30min · depende de T4. Escrever um README curto com preparação do ambiente, migrações locais, inicialização, execução dos testes e exemplos com `curl`. **Pronto quando:** os comandos documentados permitirem reproduzir as três operações.

- [ ] **Validar o MVP na sua rotina** — T6 · 1h de trabalho, distribuída em 3 dias · depende de T5. Usar tarefas reais, registrar datas e contagens e verificar a persistência após reiniciar. **Pronto quando:** todos os critérios de sucesso tiverem evidências anotadas e a suíte de testes passar.

**Estimativa:** 7h30 de trabalho + 2h30 de margem. Na primeira semana, executar T1–T3; na segunda, T4–T6, começando a validação com antecedência para alcançar três dias distintos.

## 5. Riscos e dúvidas em aberto

- **Usabilidade:** usar comandos pode ser trabalhoso no cotidiano; o uso real verificará essa hipótese.
- **Prazo:** dificuldades com Django ou DRF devem consumir a margem antes de motivar novos recursos.
- **Dados:** o arquivo SQLite guarda as tarefas; reiniciar o servidor preserva os registros, apagar o banco não.
- **Limite de uso:** a versão sem autenticação será executada somente no computador local.
- **Dúvidas bloqueantes:** nenhuma. Os limites do MVP foram confirmados na entrevista.

### Depois do MVP

Somente se o uso real justificar: edição/exclusão, uma tela simples, filtros ou prioridades. Acesso pela internet exigirá um planejamento próprio, incluindo autenticação.

## 6. Próximo passo imediato

Executar **T1 — Preparar o ambiente e o projeto Django**.

Ao encerrar o MVP, fazer uma revisão curta: como os dados percorrem a requisição até o banco, qual teste protege cada operação e quais recursos excluídos fizeram falta no uso real.
