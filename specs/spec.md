# WSRicardo - Professional Site

Documento de planejamento, especificação visual e orientação de manutenção para o site `www.wsricardo.com.br`.

Este arquivo deve servir como fonte de verdade para humanos e agentes de IA, incluindo Codex, Gemini ou outros assistentes. Ao modificar o site, use este documento junto com o estado real dos arquivos `index.html`, `css/style.css` e `js/main.js`.

## Visão Geral

O site WSRicardo é uma landing page pessoal com comportamento de SPA simples, construída para divulgar projetos, estudos, arte, cartuns, canais e links externos de Wandeson Ricardo.

A identidade principal mistura:

- Programação;
- Arte e cartum;
- Matemática e estudos;
- Projetos pessoais e experimentos;
- Divulgação de canais e trabalhos publicados em outras plataformas.

O tom visual deve ser criativo, direto, autoral e acessível. A página precisa parecer feita por alguém que trabalha com código e arte, não por um template genérico.

## Contrato Técnico

- Usar HTML5, CSS3 e JavaScript ES6.
- Usar JavaScript puro, sem frameworks front-end.
- Não adicionar backend.
- Evitar bibliotecas de terceiros, exceto quando houver justificativa forte.
- Manter o site leve, estático, simples de publicar e compatível com GitHub Pages.
- Preservar responsividade como requisito central.
- Manter boas práticas de SEO, acessibilidade e metatags.
- Não quebrar páginas internas que compartilham `css/style.css`, como `projetos.html`, `blog.html`, `galeria.html` e `cartum.html`.
- Antes de alterar design global, conferir se classes antigas ainda usadas nas páginas internas continuam estilizadas.

## Arquitetura Atual

### Arquivos Principais

- `index.html`: home/landing page principal.
- `css/style.css`: sistema visual global do site, incluindo home e páginas internas existentes.
- `js/main.js`: interações leves, como menu mobile e animações de entrada.
- `specs/spec.md`: especificação do produto, design e manutenção.

### Páginas Internas Existentes

- `projetos.html`: listagem de projetos.
- `blog.html` e `blog/`: blog estático/Pelican.
- `galeria.html`: galeria de arte.
- `cartum.html`: cartuns e lightbox.

### Links Externos Relevantes

- `https://www.github.com/wsricardo`
- `https://www.youtube.com/@dimensaoalfa`
- `https://www.youtube.com/@WSRicardoArte`
- `https://www.iscrev.com`
- `https://www.dimensaoalfa.com.br`
- `https://wsricardo.blogspot.com`

## Identidade Visual Base

A identidade visual padrão é híbrida: Comic UI + Neo-brutalismo + programação.

### Conceitos

- Comic UI: inspiração em HQ, cartum e painéis impressos.
- Neo-brutalismo: bordas pretas, sombras sólidas, alto contraste e aparência tátil.
- Programação: uso de fonte monoespaçada em tags, links, marcadores e trechos técnicos.
- Simplicidade: poucos elementos, mas fortes e reconhecíveis.
- Clareza: cada seção deve ter uma função evidente.
- Responsividade: a composição deve continuar legível em mobile.
- Cores acizentadas aspecto outono e sóbrias.

### O Que Manter

- Fundo cinza claro com grid/pontos sutis.
- Superfícies brancas ou quase brancas.
- Bordas pretas de 2px a 3px.
- Sombras sólidas pretas com deslocamento.
- Botões com comportamento físico: hover desloca o elemento e aumenta a sombra.
- Cards com barra superior colorida.
- Tipografia forte nos títulos.
- Fonte monoespaçada para marca, tags, links de cards e pequenos elementos técnicos.
- Uso pontual de cores de acento: amarelo, verde, rosa e azul.

### O Que Evitar

- Visual corporativo genérico.
- Gradientes decorativos sem função.
- Orbs, blobs, bokeh ou fundos excessivamente suaves.
- Cards muito arredondados.
- Paleta monocromática demais.
- Dependência de frameworks ou bibliotecas pesadas.
- Hero puramente textual sem assinatura visual.
- Muitos efeitos animados que prejudiquem leitura ou performance.
- Texto sobre imagem com baixo contraste.

## Tokens Visuais Atuais

Use os valores abaixo como base no CSS:

```css
:root {
    --bg-color: #eceee7;
    --paper-color: #ffffff;
    --paper-soft: #f8f7f1;
    --paper-warm: #fffdf7;
    --ink-color: #11100e;
    --text-color: #27231f;
    --text-light: #635f57;
    --border-dark: #000000;
    --accent-yellow: #e9bf4b;
    --accent-green: #6aa47d;
    --accent-pink: #c85f73;
    --accent-blue: #547fa6;
    --accent-rust: #c8773a;
    --accent-ink: #28251f;
    --footer-bg: #000000;
    --shadow-hard: 8px 8px 0 var(--border-dark);
    --shadow-soft: 5px 5px 0 var(--border-dark);
    --font-sans: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
    --font-mono: "Courier New", Courier, monospace;
    --max-width: 1160px;
    --radius: 8px;
}
```

### Uso de Cores

- `#eceee7`: fundo principal cinza claro, com textura de grid.
- `#ffffff`: superfícies principais.
- `#f8f7f1` e `#fffdf7`: superfícies secundárias com leve tom quente.
- `#11100e` e `#000000`: texto principal, bordas e sombras.
- `#635f57`: texto secundário.
- `#e9bf4b`: destaque principal, marca, estados ativos e seções de apoio.
- `#6aa47d`: destaque dev/código em tom verde mais sóbrio.
- `#c85f73`: destaque criativo/artístico em tom rosa queimado.
- `#547fa6`: destaque de apoio em azul acinzentado.
- `#c8773a`: destaque de ação/hover em tom ferrugem.
- `#28251f`: fundo escuro alternativo para footer e áreas densas.

Não transformar a paleta em um tema apenas amarelo ou apenas cinza. Os acentos devem ser distribuídos com moderação.

## Estrutura da Home

A home deve funcionar como uma landing page com navegação por âncoras.

### Header

Conteúdo:

- Marca `WSRicardo` à esquerda.
- Logo textual ou marca `WS`.
- Navegação à direita no desktop.
- Botão de menu no mobile.

Links recomendados:

- Apresentação: `#apresentacao`
- Projetos: `#projetos`
- Artes: `#artes`
- Sobre: `#sobre-mim`
- Canais: `#canais-youtube`
- Contato: `#contatos`

Regras:

- Header deve ser sticky.
- Fundo branco translúcido é permitido se mantiver contraste.
- Usar borda inferior preta e sombra sólida.
- Mobile deve usar `button.nav-toggle` com `aria-expanded`.

### Apresentação / Hero

Objetivo:

Dar impacto imediato e comunicar a identidade "código + arte + ideias".

Conteúdo atual recomendado:

- H1: `WSRicardo: código, arte e ideias em movimento`
- Subtítulo: `Desenvolvimento web, cartum, matemática e experimentação visual.`
- Texto curto explicando o espaço digital.
- CTAs: `Ver projetos` e `Entrar em contato`.
- Destaques: `Vanilla JS`, `Cartum`, `Matemática`.

Elementos visuais:

- Caixa branca grande com borda preta e sombra forte.
- Painel de código estilizado como janela/editor.
- Nota/cartão tipo sticker ou balão gráfico.
- Acentos coloridos, sem exagero.

### Projetos

Objetivo:

Mostrar trabalhos e estudos principais, com links diretos.

Cards recomendados:

- Site Portfólio SPA;
- Gerador de Site Estático;
- Exercícios de Cálculo;
- News Crawler;
- PYIMM;
- Estudos de Geometria Diferencial.

Regras:

- Usar grid responsivo.
- Cada card deve ter título, descrição curta e link.
- Links externos devem usar `target="_blank"` e `rel="noopener noreferrer"`.
- Evitar `href="#"` em conteúdo final.

### Artes e Galeria

Objetivo:

Apresentar a dimensão artística do site.

Conteúdos:

- Cartuns Diários;
- Pinturas e desenhos;
- Programação Criativa.

Links recomendados:

- `cartum.html`
- `galeria.html`
- `projetos.html` para estudos/experimentos criativos, enquanto não houver página dedicada.

### Sobre Mim

Objetivo:

Explicar a ligação entre lógica, criatividade, agricultura, estudo e produção autoral.

Conteúdo deve ser humano, direto e sem parecer currículo corporativo. Pode mencionar:

- HTML, CSS e JavaScript;
- design responsivo;
- cartum e desenho;
- matemática e educação;
- análise de dados e estudos.

### Canais no YouTube

Objetivo:

Divulgar canais e conteúdos em vídeo.

Canais atuais:

- Dimensão Alfa;
- WSRicardo Arte.

### Contatos

Objetivo:

Dar caminhos claros para conversa, redes e colaboração.

Links recomendados:

- GitHub;
- LinkedIn;
- Instagram;
- E-mail.

## Componentes

### Cards

Classe base:

- `.card`

Variações:

- `.accent-yellow`
- `.accent-green`
- `.accent-pink`
- `.accent-blue`

Regras:

- Borda preta de 3px.
- Sombra sólida.
- Barra superior colorida via `::before`.
- Hover com deslocamento e sombra mais longa.
- Evitar nested cards.

### Botões

Classes:

- `.btn`
- `.btn-primary`
- `.btn-secondary`

Regras:

- Tamanho mínimo confortável para toque.
- Borda preta de 3px.
- Sombra sólida.
- Texto forte.
- Hover deve parecer movimento físico.

### Headings de Seção

Usar:

- `.section-heading`
- `.section-number`
- `h2`
- `.section-desc`

Regras:

- Número em bloco colorido monoespaçado.
- Título grande e direto.
- Descrição curta e específica.

### Footer

Regras:

- Fundo preto.
- Texto branco ou cinza claro.
- Altura média.
- Manter `Copyright WSRicardo`.
- Pode conter frase curta, mas sem poluir.

## Responsividade

Breakpoints atuais:

- Até `980px`: hero passa para uma coluna.
- Até `820px`: navegação vira menu mobile.
- Até `560px`: títulos e painéis reduzem escala.
- Até `430px`: ajustes extras de respiro, tipografia e largura para aparelhos estreitos.

Regras:

- Nunca permitir overflow horizontal.
- Usar `width: calc(100% - 28px)` em containers mobile.
- Botões devem ficar em coluna em telas estreitas.
- Cards devem virar uma coluna quando necessário.
- Texto longo deve quebrar dentro do container.
- O conteúdo principal não pode depender de animação para ficar visível.

## JavaScript

Uso atual:

- Adicionar classe `has-js` ao documento.
- Ativar `.fade-in.visible` com IntersectionObserver.
- Controlar menu mobile com `nav-open` e `aria-expanded`.
- Fechar menu mobile ao clicar em um link.

Regras:

- JavaScript deve ser progressivo.
- Se JS falhar, o conteúdo precisa continuar visível.
- Não adicionar scripts externos sem justificativa.
- Evitar logs de debug em produção.

## SEO e Metatags

Toda página HTML pública deve ter metadados próprios. Não copiar sem critério a descrição da home para todas as páginas.

### Metatags Obrigatórias

Exemplo base para a home:

```html
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="description" content="Portfólio de WSRicardo com projetos de desenvolvimento, arte, matemática, cartuns e experimentos criativos.">
<meta name="robots" content="index, follow">
<meta name="author" content="Wandeson Ricardo">
<meta name="keywords" content="WSRicardo, Wandeson Ricardo, portfolio, programação, arte, cartum, matemática">
<meta name="language" content="pt-BR">
<title>WSRicardo | Código, arte e ideias</title>
```

### Open Graph

Usar em páginas principais:

```html
<meta property="og:title" content="WSRicardo | Código, arte e ideias">
<meta property="og:description" content="Um espaço pessoal para projetos, estudos e experimentos entre programação, arte e matemática.">
<meta property="og:image" content="imgs/wan-vectorArt1-thumbnail.jpg">
<meta property="og:url" content="https://www.wsricardo.com.br/">
<meta property="og:type" content="website">
<meta property="og:site_name" content="WSRicardo">
<meta property="og:locale" content="pt_BR">
```

### Recomendados

Adicionar quando fizer manutenção de SEO:

```html
<link rel="canonical" href="https://www.wsricardo.com.br/">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="WSRicardo | Código, arte e ideias">
<meta name="twitter:description" content="Portfólio de WSRicardo com projetos de desenvolvimento, arte, matemática, cartuns e experimentos criativos.">
<meta name="twitter:image" content="https://www.wsricardo.com.br/imgs/wan-vectorArt1-thumbnail.jpg">
```

### Links de Infraestrutura

Manter:

```html
<link rel="stylesheet" href="css/style.css">
<link rel="shortcut icon" href="imgs/wsricardo-thumbnail.ico" type="image/x-icon">
<link rel="alternate" href="blog/feeds/all.atom.xml" type="application/atom+xml" title="Atom">
```

### Regras de SEO

- Apenas um `h1` por página.
- O `title` deve ser único por página.
- `description` deve ter cerca de 120 a 160 caracteres quando possível.
- Imagens precisam de `alt` útil quando forem informativas.
- Imagens decorativas podem usar `aria-hidden="true"` no container ou `alt=""`.
- Links externos devem ser explícitos e seguros.
- Evitar títulos genéricos como `Portfolio` sem marca.
- Usar `pt-BR` como idioma principal.
- Manter URLs canônicas absolutas para páginas públicas.

## Acessibilidade

- Usar HTML semântico: `header`, `nav`, `main`, `section`, `article`, `footer`.
- Menus interativos precisam de `button`, não apenas `div`.
- `nav` deve ter `aria-label` quando útil.
- Botão mobile deve atualizar `aria-expanded`.
- Cores precisam manter contraste alto.
- Estados de hover não podem ser o único indicador de interação.
- Conteúdo textual não deve ficar invisível se JavaScript falhar.
- Respeitar `prefers-reduced-motion`.

## Orientações Para Agentes de IA

Ao trabalhar neste projeto:

1. Leia este arquivo antes de propor mudanças grandes.
2. Leia `index.html`, `css/style.css` e a página específica que será alterada.
3. Preserve a identidade Comic UI / Neo-brutalista.
4. Não substituir por visual corporativo, minimalista frio ou template SaaS.
5. Não adicionar dependências sem necessidade.
6. Não remover metatags úteis.
7. Não criar links `href="#"` em conteúdo final.
8. Não quebrar páginas internas que usam classes antigas como `.site-header`, `.container`, `.project-card`, `.gallery-grid`, `.post-card` e `.site-footer`.
9. Se alterar `css/style.css`, verificar a home e pelo menos uma página interna.
10. Se alterar navegação mobile, testar desktop e mobile.
11. Se adicionar nova página, criar metatags próprias e manter o padrão visual.

### Checklist Antes de Finalizar Alterações

- A página abre sem erro.
- Não há overflow horizontal no mobile.
- Header e menu mobile funcionam.
- CTAs e links levam para destinos reais.
- Metatags essenciais estão presentes.
- `title` e `description` estão coerentes com a página.
- Cards, botões e headings seguem os tokens visuais.
- O site continua legível sem JavaScript.
- `git diff --check` não aponta problemas.

## Próximas Melhorias Sugeridas

- Adicionar `canonical` e Twitter Card em todas as páginas públicas.
- Criar uma página dedicada para programação criativa, se o conteúdo crescer.
- Revisar links temporários ou genéricos em páginas internas antigas.
- Padronizar metatags de `blog.html`, `projetos.html`, `galeria.html` e `cartum.html`.
- Adicionar imagens otimizadas para Open Graph em tamanho adequado.
- Criar um pequeno guia de conteúdo para novos cards de projetos e artes.
