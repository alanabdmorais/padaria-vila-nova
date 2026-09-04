# Padaria Vila Nova

Mini site estilo "link bio" (parecido com Linktree) para a Padaria Vila Nova.
Gerado com [Hugo](https://gohugo.io/) e pensado para ser editado direto pelo
[Pouta](https://pouta.dev/) (CMS git-based) e publicado no Cloudflare Pages.

## Estrutura do projeto

```
padaria-vila-nova/
├── config.toml            # configuração do site Hugo
├── pouta.config.json      # define o que é editável no Pouta
├── content/
│   ├── _index.md          # perfil: nome, bio, foto, redes sociais
│   └── links/              # cada arquivo é um link/card exibido no site
│       ├── cardapio.md
│       ├── encomendas.md
│       └── localizacao.md
├── layouts/
│   └── index.html          # template da página principal
├── static/
│   ├── css/style.css       # visual (tons de marrom/bege, cards, hover)
│   └── img/perfil.svg      # foto de perfil placeholder
└── archetypes/links.md     # modelo usado ao criar um novo link
```

## Editando o conteúdo

- **Perfil** (`content/_index.md`): `title` (nome do negócio), `bio`
  (descrição curta), `foto_perfil` (caminho da imagem) e `redes_sociais`
  (lista com `nome`, `url` e `icone`, usando classes do
  [Font Awesome](https://fontawesome.com/search?ic=free), ex:
  `fa-brands fa-instagram`).
- **Links** (`content/links/*.md`): cada arquivo vira um card na página, com
  `title`, `link_url`, `icone` (opcional) e `peso` (ordem de exibição, menor
  aparece primeiro). O campo se chama `link_url` (e não `url`) porque `url`
  é uma palavra reservada do Hugo para sobrescrever o link da própria
  página.

## Rodando localmente

Requer o [Hugo](https://gohugo.io/installation/) instalado.

```bash
hugo server -D
```

Abra `http://localhost:1313`.

## Deploy no Cloudflare Pages

1. Suba este repositório no GitHub (já feito, se você está lendo isso por
   aqui).
2. No painel do Cloudflare Pages, crie um projeto conectado a este
   repositório.
3. Configurações de build:
   - **Framework preset:** Hugo
   - **Build command:** `hugo`
   - **Build output directory:** `public`
   - (opcional) variável de ambiente `HUGO_VERSION` com a versão do Hugo que
     você usa localmente.
4. Publique. A cada novo commit na branch principal, o Cloudflare Pages
   gera um novo deploy automaticamente.

## Editando com o Pouta

1. Acesse [app.poutacms.fi](https://app.poutacms.fi/) e entre com sua conta
   do GitHub.
2. Autorize o acesso a este repositório (o Pouta pede permissão só na pasta
   de conteúdo).
3. O Pouta lê o `pouta.config.json` na raiz do repositório e monta a
   interface de edição automaticamente (perfil + lista de links).
4. Cada alteração salva no Pouta vira um commit direto neste repositório,
   o que dispara um novo deploy no Cloudflare Pages.

> **Nota:** o `pouta.config.json` deste projeto foi montado com base na
> documentação pública do Pouta (tipos de conteúdo, caminhos de escrita e
> campos customizados). Se a interface do Pouta pedir ajustes ao conectar o
> repositório pela primeira vez, adapte os nomes dos campos conforme a tela
> mostrar — a estrutura de `content/` já está pronta para funcionar com
> qualquer CMS git-based baseado em Markdown.

## Personalizando

- Cores: `static/css/style.css` (`--primary` e `--secondary`) e
  `config.toml` (`params.primaryColor` / `params.secondaryColor`).
- Foto de perfil: troque `foto_perfil` em `content/_index.md` (pelo Pouta ou
  direto no arquivo) por uma imagem enviada em `static/img/`.
