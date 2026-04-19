import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu

# Configurações  iniciais
st.set_page_config(page_title="Dashboard de Vendas", page_icon="☢️", layout="wide")

# Carregar dados
df = pd.read_excel('plotGrafico/Vendas.xlsx')

# FILTROS
# Sidebar
st.sidebar.header("Selecione os Filtros")

# Filtro por loja
lojas = st.sidebar.multiselect(
    "Lojas",
    # Opções do filto
    options=df["ID Loja"].unique(),
    # Opção que vem como por padrão
    default=df["ID Loja"].unique(),
    # Chave única
    key='loja'
)

# Filtro por produto
produtos = st.sidebar.multiselect(
    "Produtos",
    options=df['Produto'].unique(),
    default=df['Produto'].unique(),
    key='produto'
)

# Filtrar o Dataframe com as opções selecionadas
df_selecao = df.query("`ID Loja` in @lojas and Produto in @produtos")

# Graficos e na função da página
def Home():
    st.title('Fatumento das Lojas')

    total_vendas = df_selecao['Quantidade'].sum()
    media = df_selecao['Quantidade'].mean()
    mediana = df_selecao['Quantidade'].median()

    total1, total2, total3 = st.columns(3)
    with total1:
        # Apresentrar indicadores rápidos
        st.metric('Total Vendido', value=int(total_vendas))
    with total2:
        st.metric('Média por pordutro', value=f"{media:.1f}")
    with total3:
        st.metric('Mediana', value=int(mediana))

        st.markdown('- - -')

def Graficos():
    # Criar um grafico de barras
    # Mostrando a quant de produtos por lojas

    fig_barras = px.bar(
        df_selecao,
        x="Produto",
        y="Quantidade",
        color="ID Loja",
        barmode="group",
        title='Quandide de Produtos Vendidos por Loja'
    )
    #Grafico de linha
    # Total de vendas por Loja

    fig_linha = px.line(
        df_selecao.groupby(["ID Loja"]).sum(numeric_only=True).reset_index(),
        x='ID Loja',
        y= 'Quantidade',
        title='Total de Vendas Por loja'

    )

    graf1, graf2 = st.columns(2)
    with graf1:
        st.plotly_chart(fig_barras,  use_container_width=True )
    with graf2:
        st.plotly_chart(fig_linha,  use_container_width=True )

def sideBar():
    with st.sidebar:
        selecionado = option_menu(
            menu_title="Menu",
            options=['Home', 'Gráficos'],
            icons=['house', 'bar-chart'],
            default_index=0
        )

    if selecionado == 'Home':
        Home()
        Graficos()
    elif selecionado == 'Gráficos':
        Graficos()

sideBar()

# python -m streamlit run projeto.py


