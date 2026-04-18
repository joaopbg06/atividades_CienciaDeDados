import streamlit as st
import pandas as pd
import plotly_express as px
from streamlit_option_menu import option_menu
from query import conexao


# Primeira Consulta e Atualização

query = 'SELECT * FROM tb_carro'
df = conexao(query)

if st.button('Atualizar Dados') :
    df = conexao(query)

# --------------------------------
# Filtro lateral

st.sidebar.title('Barra lateral de Filtro')

# marca
marca = st.sidebar.multiselect(
    'Marca',
    options=df['marca'].unique(),
    default=df['marca'].unique()
)

# modelo
modelo = st.sidebar.multiselect(
    'Modelo',
    options=df['modelo'].unique(),
    default=df['modelo'].unique()
)

# ano
ano = st.sidebar.slider(
    'Ano',
    min_value=int(df['ano'].min()),
    max_value=int(df['ano'].max()),
    value=(int(df['ano'].min()), int(df['ano'].max()))
)

# valor
valor = st.sidebar.slider(
    'Valor',
    min_value=float(df['valor'].min()),
    max_value=float(df['valor'].max()),
    value=(float(df['valor'].min()), float(df['valor'].max()))
)

# cor
cor = st.sidebar.multiselect(
    'Cor',
    options=df['cor'].unique(),
    default=df['cor'].unique()
)

# número de vendas
numero_vendas = st.sidebar.slider(
    'Número de vendas',
    min_value=int(df['numero_vendas'].min()),
    max_value=int(df['numero_vendas'].max()),
    value=(int(df['numero_vendas'].min()), int(df['numero_vendas'].max()))
)


# Aplicação do filtros

df_selecionado = df[
    (df['marca'].isin(marca)) &
    (df['modelo'].isin(modelo)) &
    (df['ano'] >= ano[0]) &
    (df['ano'] <= ano[1]) &
    (df['valor'] >= valor[0]) &
    (df['valor'] <= valor[1]) &
    (df['cor'].isin(cor)) &
    (df['numero_vendas'] >= numero_vendas[0]) &
    (df['numero_vendas'] <= numero_vendas[1]) 
]

# ----------------------------
# Dashboard

def paginaInicial():
    with st.expander("Tabelas de carros"):
        exibicao = st.multiselect(
            "Filtro",
            df_selecionado.columns,
            default=[],
            key="filtro_exibicao"
        )

        if exibicao:
            st.write(df_selecionado[exibicao])
    
    if not df_selecionado.empty:
        total_vendas = df_selecionado['numero_vendas'].sum()
        media_valor = df_selecionado['valor'].mean()
        media_vendas = df_selecionado['numero_vendas'].mean()
    
        card1, card2, card3 = st.columns(3, gap="large")

        with card1:
            st.info('Total de vendas', icon='📍')
            st.metric("Total", value=f'{total_vendas:,.0f}')

        with card2:
            st.info('Média do valores', icon='📍')
            st.metric("Média", value=f'{media_valor:,.0f}')

        with card3:
            st.info('Média de vendas', icon='📍')
            st.metric("Média", value=f'{media_vendas:,.0f}')
    else:
        st.warning('Nenhum dado disponível com o filtro atual')
    
    st.markdown("""-----""")

# ------------------------
# Graficos

def graficos(df_selecionado):
    if df_selecionado.empty:
        st.warning('Nenhum dado disponível com o filtro atual')
        return
    
    graf1, graf2 = st.tabs([
        'Grafico de barras',
        'Grafico de linhas'
    ])

    with graf1:
        st.write('Grafico de barras')
        valor = df_selecionado.groupby('marca').count()[['valor']].sort_values(by="valor", ascending=False)

        fig1 = px.bar(
            valor,
            x=valor.index,
            y='valor',
            orientation='h',
            title='Valores dos carros',
            color_discrete_sequence=['#8DAA11']
        )

        st.plotly_chart(fig1, use_container_width=True)

    with graf2:
        st.write('Grafico de linhas')
        valor_linhas = df_selecionado.groupby('modelo').count()[['valor']]

        fig2 = px.line(
            valor_linhas,
            x=valor_linhas.index,
            y='valor',
            title='valor por modelo',
            color_discrete_sequence=['#EC2A56']
        )

        st.plotly_chart(fig2, use_container_width=True)

paginaInicial()

graficos(df_selecionado)

