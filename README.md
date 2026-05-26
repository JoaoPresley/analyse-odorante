# Análise de Odorante - MSGÁS 🛢️📊

Este projeto automatiza a leitura, tratamento e visualização de dados de odorantes (TBM e THT) a partir de registros de medição. O script identifica as últimas leituras válidas por objeto, consolida os valores, exporta os dados tratados para uma planilha Excel e gera um gráfico estatístico com os limites operacionais.

---

## 📁 Estrutura do Projeto

```text
analyse-odorante/
├── .venv/                  # Ambiente virtual do Python (gerado automaticamente)
├── data/                   # Pasta de dados (Inputs e Outputs)
│   ├── origem.csv          # Arquivo bruto com as medições (Base de dados)
│   ├── dados_tratados.xlsx # Relatório gerado pelo script (Output)
│   └── grafico_odorante.png# Gráfico gerado pelo script (Output)
├── analise.py              # Classe interna com a lógica de tratamento e plotagem
├── main.py                 # Script principal que executa o fluxo
├── requirements.txt        # Dependências do projeto
└── executar_projeto.bat    # Automatizador para usuários no Windows

```

---

## 🛠️ Pré-requisitos

Antes de começar, você precisa ter instalado na sua máquina:

* **Python 3.8 ou superior** (Certifique-se de marcar a opção *"Add Python to PATH"* durante a instalação).

---

## 🚀 Como Usar (O Jeito Mais Fácil)

Se você está no Windows, não é necessário abrir o terminal ou o PyCharm para rodar o projeto.

1. Certifique-se de que o seu arquivo de dados bruto está na pasta `data/` com o nome **`origem.csv`**.
2. Dê **dois cliques** no arquivo **`executar_projeto.bat`**.

**O que o instalador automatizado vai fazer?**

* Criará o ambiente virtual (`.venv`) caso ele não exista.
* Instalará todas as bibliotecas necessárias de forma silenciosa.
* Executará a análise dos dados.
* Manterá a tela aberta para você conferir o resultado.

---

## 💻 Execução Manual (Terminal)

Caso prefira rodar os comandos manualmente no terminal, siga os passos abaixo:

1. **Crie e ative o ambiente virtual:**
```bash
python -m venv .venv
# No Windows (Prompt de Comando):
call .venv\Scripts\activate

```


2. **Instale as dependências:**
```bash
pip install -r requirements.txt -q

```


3. **Rode o script principal:**
```bash
python main.py

```



---

## 📈 Entendendo as Saídas (Outputs)

Após a execução, o script gerará dois arquivos cruciais na pasta `data/`:

* **`dados_tratados.xlsx`**: Uma planilha Excel contendo apenas as últimas medições válidas de `C_TBM` e `C_THT` de cada objeto, ordenadas cronologicamente.
* **`grafico_odorante.png`**: Um gráfico de alta resolução configurado com:
* Soma das concentrações por ID de Objeto.
* Linhas horizontais tracejadas representando os limites críticos de operação: **Mínimo (5 mg/m³)** e **Máximo (20 mg/m³)**.
* Linhas verticais pontilhadas discretas ligando cada ponto ao eixo Y para facilitar a leitura dos índices exatos.
* Fundo branco de alto contraste e labels escuros para relatórios formais.



---

## 🔧 Tecnologias Utilizadas

* **Python**: Linguagem base do projeto.
* **Pandas**: Manipulação e tratamento da base de dados.
* **NumPy**: Filtros de alta performance e indexação vetorial.
* **Matplotlib**: Engenharia de visualização de dados e gráficos.
* **OpenPyXL**: Engine de conversão e exportação para o formato Excel.
