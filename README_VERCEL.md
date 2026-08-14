# Deploy no Vercel

## Estrutura

- `api/index.py` — entrada da aplicação Flask no Vercel.
- `app.py` — aplicação Flask.
- `templates/` — frontend.
- `static/` — CSS.
- `requirements.txt` — dependência Python.
- `vercel.json` — encaminha as rotas para a função Flask.

## Pelo GitHub + Vercel

1. Crie um repositório no GitHub.
2. Envie todos estes arquivos para o repositório.
3. Entre no Vercel.
4. Escolha **Add New Project**.
5. Importe o repositório.
6. Não coloque `python app.py` como Build Command.
7. Faça o Deploy.

A Vercel detecta a função Python em `api/index.py`.

## Pela Vercel CLI

Instale Node.js e depois:

```bash
npm install -g vercel
vercel login
vercel
```

Para produção:

```bash
vercel --prod
```

Depois a Vercel fornecerá uma URL `*.vercel.app`.

## Teste

Abra a URL principal:

```text
https://SEU-PROJETO.vercel.app/
```

A API também pode ser testada em:

```text
https://SEU-PROJETO.vercel.app/api/stats
```

## Atenção

Este é um projeto demonstrativo de análise estatística. Ele não deve ser apresentado como um sistema capaz de prever ou garantir o próximo resultado de um jogo de azar.

A versão atual guarda os resultados em memória. Para produção, use um banco de dados externo em vez de depender do armazenamento local da função.
