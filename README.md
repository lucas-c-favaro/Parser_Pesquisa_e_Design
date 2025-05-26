
# Documentação do Analisador de Artigos em PDF

Este projeto em Python tem como objetivo **analisar arquivos PDF de artigos científicos** e encontrar menções a uma palavra-chave específica (como "Ferramenta"). Ele foi criado para ajudar em pesquisas acadêmicas, reduzindo o esforço manual de leitura e triagem de conteúdos.

---

## Como instalar e rodar o Python

### 1. Instalando o Python

Se você nunca usou Python antes, siga os passos abaixo:

#### 💡 Windows / macOS / Linux

1. Acesse o site oficial: [https://www.python.org/downloads](https://www.python.org/downloads)
2. Clique em **Download Python** (ele detecta automaticamente seu sistema).
3. **IMPORTANTE**: Durante a instalação, **marque a opção** `Add Python to PATH`.
4. Finalize a instalação clicando em "Install Now".

### 2. Verificar se o Python foi instalado corretamente

Abra o **Terminal** (macOS/Linux) ou o **Prompt de Comando (cmd)** no Windows e digite:

```bash
python --version
```

Você deverá ver algo como:

```
Python 3.11.5
```

---

### 3. Instalar o pacote necessário

Este projeto usa uma biblioteca chamada `pdfplumber`, que permite ler PDFs:

No terminal, digite:

```bash
pip install pdfplumber
```

---

### 4. Executar o script

Salve o código em um arquivo com nome, por exemplo: `analisador_pdf.py`.

No terminal, vá até a pasta onde está o arquivo e rode o comando:

```bash
python analisador_pdf.py
```

Pronto! O script será executado e os arquivos `.txt` com os resultados serão criados na mesma pasta.

---

## O que este script faz?

1. **Abre automaticamente todos os PDFs de uma pasta (ou um arquivo único).**
2. **Lê o conteúdo da primeira página do artigo.**
3. **Identifica se a página é de fato a primeira página de um artigo científico.**
4. **Procura por uma palavra-chave na introdução do artigo.**
5. **Salva os trechos encontrados em um arquivo de texto com os resultados.**
6. **Gera um relatório com o número total de arquivos e quantos continham a palavra procurada.**

---

## Estrutura dos arquivos

Organize seus arquivos PDF em pastas como no exemplo abaixo:

```
P&D/
├── artigos_2006/
│   └── artigos/
│       ├── artigo1.pdf
│       └── artigo2.pdf
├── artigos_2008/
├── Anais-9-Ped-2010.pdf
└── 2012/
    └── artigo3.pdf
```

---

## Como configurar

No próprio script, existe uma lista chamada `settings` com as configurações que você pode ajustar:

```python
settings = [
    {
        'nome': 'P&D2006',
        'caminho_arquivos': 'caminho/para/os/pdf',
        'tipo': 'pasta',
        'palavra_buscada': 'Ferramenta',
        'dividir_por_palavra_chave': False,
        'dividir_por_resumo': True
    }
]
```

> **Dica**: Use `**/*.pdf` no caminho para procurar PDFs em todas as subpastas.

---

## Como funciona a busca?

- O script verifica se a primeira página contém as palavras **RESUMO** e **ABSTRACT**. Isso indica que é a primeira página de um artigo.
- Depois, ele divide o conteúdo do texto para capturar apenas a **introdução** do artigo.
- Se a **palavra-chave** estiver nessa introdução, ele salva o trecho em um arquivo `.txt`.

---

## Arquivos gerados

Para cada configuração, o script gera:

1. `P&DXXXX_artigos_encontrados.txt`  
   → Contém os trechos de artigos onde a palavra foi encontrada.

2. `P&DXXXX_resultado_busca.txt`  
   → Um resumo com a quantidade total de PDFs e quantos deles contêm a palavra-chave.

---

## Exemplo de resultado

**P&D2006_resultado_busca.txt**

```
Total de PDFs: 20
Artigos contendo "Ferramenta": 7
```

**P&D2006_artigos_encontrados.txt**

```
[...] trecho do artigo [...]
Localização: /Users/voce/arquivo1.pdf - Página 1
```

---

##  Dicas finais

- Se um PDF não abrir corretamente, o script continuará e mostrará uma mensagem de erro, sem travar.
- Para procurar por outra palavra-chave, altere o campo `"palavra_buscada"` na configuração.
- Pode-se adaptar o script para outras seções além de "RESUMO", como "INTRODUÇÃO".

---

## Dúvidas?

Se você tiver dúvidas sobre como usar o script ou instalar algo, procure ajuda com alguém que já tenha familiaridade com Python, ou envie uma dúvida para o responsável pelo projeto.
