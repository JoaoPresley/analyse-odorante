import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

class Analise:
    def __init__(self, caminho_medidas=r"data/origem.csv"):
        try:
            self.df_medidas = pd.read_csv(
                caminho_medidas,
                encoding="latin1",
                sep=";",
                usecols=["ID Objeto", "Data Registro", "Cód Parâmetro", "Valor Medido"]
            )
        except FileNotFoundError:
            print(f"Erro ao abrir o arquivo {caminho_medidas}")
            self.df_medidas = None
        except Exception as e:
            print(f"Erro desconhecido: {e}")
            self.df_medidas = None

    def transform_data(self):
        if self.df_medidas is None:
            print("Erro: Nenhum dado carregado para transformar.")
            return

        # Ordena a tabela para agrupar os ID Objeto e ficar as ultimas leituras registradas no final
        self.df_medidas.sort_values(by=["ID Objeto", "Data Registro"], inplace=True)

        # Pega apenas os índices dos últimos valores correspondentes
        linhas_TBM_ultimas_medidas = np.array(self.df_medidas[self.df_medidas["Cód Parâmetro"] == "C_TBM"]["ID Objeto"].drop_duplicates(keep="last").index)
        linhas_THT_ultimas_medidas = np.array(self.df_medidas[self.df_medidas["Cód Parâmetro"] == "C_THT"]["ID Objeto"].drop_duplicates(keep="last").index)

        # Junta os índices obtidos e ordena-os
        filtro = np.concatenate([linhas_TBM_ultimas_medidas, linhas_THT_ultimas_medidas], axis=0)
        filtro.sort()

        # Aplica a filtragem no DataFrame original
        self.df_medidas = self.df_medidas.loc[filtro]

    def outputload(self, pasta_destino="data"):
        if self.df_medidas is None:
            print("Erro: Não há dados tratados para exportar.")
            return

        # Garante que a pasta destino existe
        os.makedirs(pasta_destino, exist_ok=True)

        # --- 1. EXPORTAÇÃO DO EXCEL ---
        caminho_excel = os.path.join(pasta_destino, "dados_tratados.xlsx")
        # index=False evita salvar uma coluna extra com os números das linhas antigas
        self.df_medidas.to_excel(caminho_excel, index=False)
        print(f"Tabela salva com sucesso em: {caminho_excel}")

        # --- 2. GERAÇÃO E SALVAMENTO DO GRÁFICO ---
        # Recria a lógica do agrupamento e ordenação para o gráfico
        odorante = self.df_medidas.groupby("ID Objeto")["Valor Medido"].sum()
        eixo_x = odorante.index
        eixo_y = odorante.values

        fig, ax = plt.subplots(figsize=(15, 6), facecolor='white')
        ax.set_facecolor('white')

        # Linhas tracejadas horizontais personalizadas para cada ponto
        ax.hlines(y=eixo_y, xmin=0, xmax=eixo_x, colors='gray', linestyles=':', linewidth=2, alpha=0.5, zorder=1)

        # Gráfico de linha principal
        ax.plot(eixo_x, eixo_y, marker='o', color='blue', label='Valor Medido', zorder=2)

        # Títulos e Labels customizados
        ax.set_ylabel("Quantidade de Odorante (mg/m³)", fontsize=12, color='black', fontweight='bold')
        ax.set_xlabel("ID Objeto", fontsize=12, color='black', fontweight='bold')
        ax.set_title("Análise de Odorante por Objeto", fontsize=14, color='black', fontweight='bold')

        # Customização das marcações no eixo Y (Somas + Limites)
        valores_eixo_y = np.unique(np.append(eixo_y, [5, 20]))
        valores_eixo_y.sort()
        ax.set_yticks(valores_eixo_y)

        ax.tick_params(axis='x', colors='black', labelsize=10)
        ax.tick_params(axis='y', colors='black', labelsize=9)
        plt.xticks(rotation=45)

        # Linhas de contorno pretas
        for spine in ax.spines.values():
            spine.set_color('black')
            spine.set_linewidth(1.2)

        # Linhas críticas e textos centralizados
        ax.axhline(y=5, color='darkred', linestyle='--', linewidth=1.5, zorder=3)
        ax.axhline(y=20, color='darkred', linestyle='--', linewidth=1.5, zorder=3)

        ax.text(x=0.5, y=20.3, s="MÁXIMO", color='darkred', fontsize=10,
                fontweight='bold', ha='center', va='bottom', transform=ax.get_yaxis_transform(), zorder=4)

        ax.text(x=0.5, y=4.7, s="MÍNIMO", color='darkred', fontsize=10,
                fontweight='bold', ha='center', va='top', transform=ax.get_yaxis_transform(), zorder=4)

        ax.legend(loc='upper right', facecolor='white', edgecolor='black', labelcolor='black')

        # Margem suave nas bordas laterais para os textos não flutuarem
        ax.margins(x=0.01)
        plt.tight_layout()

        # Salvando o gráfico como imagem PNG
        caminho_grafico = os.path.join(pasta_destino, "grafico_odorante.png")
        # bbox_inches='tight' calcula as dimensões dinamicamente para os labels do eixo X não serem cortados
        plt.savefig(caminho_grafico, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor(), edgecolor='none')
        print(f"Gráfico salvo com sucesso em: {caminho_grafico}")

        # Fecha a janela do gráfico após gerar os arquivos para liberar espaço na memória RAM
        plt.close(fig)
