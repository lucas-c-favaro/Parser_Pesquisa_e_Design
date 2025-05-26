from glob import glob
import pdfplumber
import re


def is_paper_first_page(text: str) -> bool:
    """Verifica se a página contém as seções RESUMO e ABSTRACT."""
    upper_text = text.upper()
    return 'RESUMO' in upper_text and 'ABSTRACT' in upper_text


def extract_intro(text: str, split_by_keyword: bool, split_by_resumo: bool) -> str:
    """Extrai a introdução com base na palavra-chave ou na seção RESUMO."""
    try:
        if split_by_keyword:
            intro = re.split(r'PALAVRA[\w\s\S]{1,2}CHAVE', text.upper())
        elif split_by_resumo:
            intro = re.split(r'RESUMO\n', text.upper())
        else:
            intro = [text]

        if len(intro) == 1:
            # Fallback para as primeiras linhas
            lines = text.split('\n')[:5]
            intro = ['\n'.join(lines)]

        return intro[0]
    except Exception as e:
        print(f"Erro ao extrair introdução: {e}")
        return ""


def process_pdf_file(article_path: str, item: dict, result_ferramenta: list, log_file: str):
    """Processa um único arquivo PDF."""
    try:
        with pdfplumber.open(article_path) as pdf:
            pages = pdf.pages if item['tipo'] == 'arquivo' else [pdf.pages[0]]

            for page in pages:
                text = page.dedupe_chars().extract_text() or ""
                if item['tipo'] == 'arquivo' and not is_paper_first_page(text):
                    continue

                intro = extract_intro(text, item['dividir_por_palavra_chave'], item['dividir_por_resumo'])
                if item['palavra_buscada'].upper() in intro.upper():
                    result_ferramenta.append(page)
                    with open(log_file, 'a') as f:
                        f.write(f"{intro}\nLocalização: {article_path} - {page}\n\n")
    except Exception as e:
        print(f"[ERRO] Falha ao processar: {article_path}")
        print(f"Motivo: {e}")


def process_config(item: dict):
    """Processa uma configuração específica."""
    print(f"\n🔍 Processando: {item['nome']}")
    result_ferramenta = []

    output_log = f"{item['nome']}_artigos_encontrados.txt"
    output_summary = f"{item['nome']}_resultado_busca.txt"

    # Limpa arquivo de saída anterior
    open(output_log, 'w').close()

    pdf_files = glob(item['caminho_arquivos'], recursive=True)

    for pdf_path in pdf_files:
        process_pdf_file(pdf_path, item, result_ferramenta, output_log)

    # Salva o resumo dos resultados
    with open(output_summary, 'w') as summary_file:
        summary_file.write(f"Total de PDFs: {len(pdf_files)}\n")
        summary_file.write(f'Artigos contendo "{item["palavra_buscada"]}": {len(result_ferramenta)}\n')

    print(f"✅ {item['nome']} finalizado — {len(result_ferramenta)} artigos encontrados de {len(pdf_files)} arquivos.")


def main(settings: list):
    """Executa o processamento para todas as configurações."""
    for item in settings:
        process_config(item)


# Lista de configurações
settings = [
    {
        'nome': 'P&D2006',
        'caminho_arquivos': r'/Users/lucascostafavaro/Documents/P&D/artigos_2006/artigos/**/*.pdf',
        'tipo': 'pasta',
        'palavra_buscada': 'Ferramenta',
        'dividir_por_palavra_chave': False,
        'dividir_por_resumo': True
    },
    {
        'nome': 'P&D2008',
        'caminho_arquivos': r'/Users/lucascostafavaro/Documents/P&D/artigos_2008/**/*.pdf',
        'tipo': 'pasta',
        'palavra_buscada': 'Ferramenta',
        'dividir_por_palavra_chave': False,
        'dividir_por_resumo': True
    },
    {
        'nome': 'P&D2010',
        'caminho_arquivos': r'/Users/lucascostafavaro/Documents/P&D/Anais-9-Ped-2010.pdf',
        'tipo': 'arquivo',
        'palavra_buscada': 'Ferramenta',
        'dividir_por_palavra_chave': False,
        'dividir_por_resumo': True
    },
    {
        'nome': 'P&D2012',
        'caminho_arquivos': r'/Users/lucascostafavaro/Documents/P&D/2012/**/*.pdf',
        'tipo': 'pasta',
        'palavra_buscada': 'Ferramenta',
        'dividir_por_palavra_chave': False,
        'dividir_por_resumo': True
    }
]

if __name__ == "__main__":
    main(settings)
