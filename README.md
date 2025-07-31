# 🔍 Site Analyzer & Embedder

Este projeto é um script em Python desenvolvido para analisar sites, clonar seus conteúdos e embutir software em JavaScript diretamente nos arquivos HTML. O objetivo é educativo e autorizado pelo próprio dono do site analisado.

## 📦 Funcionalidades

- Acessa e analisa sites (HTML, CSS e JavaScript).
- Detecta e salva portas abertas.
- Extrai e organiza conteúdos por porta.
- Insere código JS de aviso ("Warn") nos arquivos.
- Salva todos os dados organizados na pasta `sites/`.

## 🚀 Tecnologias Utilizadas

- Python 3 (executado no Pydroid3)
- Requests
- BeautifulSoup
- os, socket, http.client
- Integração com JavaScript via string embutida

## ⚙️ Como Usar

1. Instale o Pydroid3 no Android.
2. Instale as bibliotecas necessárias:

pip install requests beautifulsoup4

3. Execute o script em Python no Pydroid.
4. O conteúdo será salvo na pasta `sites/`.

## 🧠 Objetivo

Este projeto é para fins **educacionais** e demonstrações técnicas. Ele permite:

- Estudo de estrutura de sites
- Análise de backend e frontend
- Integração de scripts externos

## 📂 Estrutura do Projeto

sites/ ├── porta_80/ │   ├── index.html │   ├── style.css │   └── script.js ├── porta_443/ │   └── ...

## ✨ Exemplo de Código Inserido

```js
window.onload = () => {
  alert("Warn: Software ativado.");
};

🧾 Licença

Uso restrito para fins de aprendizado, testes ou com permissão do proprietário do domínio.



