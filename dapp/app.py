import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

years = list(range(1980, 2014))

@st.cache
def load_dataset():
    df = pd.read_excel("dapp/Canada.xlsx", sheet_name= 1 ,skiprows=20, skipfooter = 2)
    df.drop(['AREA', 'REG', 'DEV', 'Type', 'Coverage'], axis=1 , inplace= True)
    df.rename(columns={'OdName':'Country','AreaName':'Continent', 'RegName': 'Region', 'DevName':'Status'}, inplace=True)
    df.set_index('Country', inplace=True)
    df['Total'] = df[years].sum(axis=1)
    return df

with st.spinner('Loading data...'):
    df = load_dataset()
    st.balloons()

countries = df.index.tolist()

sel_country = st.selectbox('Select a country', countries)
st.info(f'You selected {sel_country}')

total_imigrants = df.loc[sel_country, 'Total' ]
avg_immigrants =  df.loc[sel_country, years].mean()

st.subheader("Key Performance Indicators")
c1,c2,c3 = st.columns(3)
c1.metric("Total Immigrants", f'{total_imigrants} people', '👨‍👩‍👧‍👦')
c2.metric('Avg. Immigrants/yr', f'{round(avg_immigrants)} people', '👨‍👩‍👧‍👦/year')
c3.metric("Total years", f'{len(years)} years', '📆')

country_df = df.loc[sel_country, years]
fig = px.bar(y=country_df, x=country_df.index, title=f'{sel_country} Immigrants to Canada')
fig2 = px.scatter(y=country_df, x=country_df.index,title=f'{sel_country} stats' )
c1,c2 = st.columns(2)
c1.plotly_chart(fig, use_container_width=True)
c2.plotly_chart(fig2, use_container_width=True)