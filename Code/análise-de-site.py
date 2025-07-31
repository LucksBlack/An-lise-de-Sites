import os
import requests
from bs4 import BeautifulSoup
import socket
from urllib.parse import urlparse

# ========== CONFIGURAÇÕES ==========
URL = "https://blocogiratorio.netlify.app"  # Coloque seu site aqui
SOFTWARE_JS = """
<script>
window.onload = () => {
  alert("Warn: Software ativado.");
};
</script>
"""
PASTA_SITES = "sites"
PORTAS_COMUNS = [80, 443, 8080]

# ========== FUNÇÃO PARA SALVAR ARQUIVOS ==========
def salvar_arquivo(path, conteudo):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(conteudo)

# ========== FUNÇÃO PARA CLONAR CONTEÚDO DO SITE ==========
def clonar_site(url, porta_nome="padrao"):
    print(f"[+] Acessando: {url}")
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")

        # Insere o JS de software no HTML
        html_modificado = response.text.replace("</body>", f"{SOFTWARE_JS}</body>")

        # Define a pasta
        pasta = os.path.join(PASTA_SITES, porta_nome)
        salvar_arquivo(os.path.join(pasta, "index.html"), html_modificado)

        # CSS externo
        for link in soup.find_all("link", {"rel": "stylesheet"}):
            href = link.get("href")
            if href and href.startswith("http"):
                try:
                    css = requests.get(href).text
                    salvar_arquivo(os.path.join(pasta, "style.css"), css)
                except:
                    continue

        # JS externo
        for script in soup.find_all("script", src=True):
            src = script.get("src")
            if src and src.startswith("http"):
                try:
                    js = requests.get(src).text
                    salvar_arquivo(os.path.join(pasta, "script.js"), js)
                except:
                    continue

        print(f"[✔] Site salvo com sucesso em '{pasta}'")
    except Exception as e:
        print(f"[!] Erro ao acessar {url}: {e}")

# ========== FUNÇÃO PARA DETECTAR PORTAS ABERTAS ==========
def detectar_portas(hostname):
    ip = socket.gethostbyname(hostname)
    print(f"[+] Escaneando IP: {ip}")
    portas_abertas = []
    for porta in PORTAS_COMUNS:
        try:
            s = socket.socket()
            s.settimeout(1)
            s.connect((ip, porta))
            portas_abertas.append(porta)
            s.close()
        except:
            continue
    return portas_abertas

# ========== EXECUÇÃO PRINCIPAL ==========
if __name__ == "__main__":
    print("=== ANALISADOR DE SITE + EMBEDDER ===")

    parsed_url = urlparse(URL)
    hostname = parsed_url.hostname
    if not hostname:
        print("[!] URL inválida.")
        exit()

    portas = detectar_portas(hostname)
    print(f"[+] Portas abertas detectadas: {portas if portas else 'Nenhuma detectada'}")

    if portas:
        for porta in portas:
            protocolo = "https" if porta == 443 else "http"
            nova_url = f"{protocolo}://{hostname}:{porta}"
            clonar_site(nova_url, f"porta_{porta}")
    else:
        clonar_site(URL, "sem_porta")

    print("\n[✓] Finalizado. Veja a pasta 'sites/'")
