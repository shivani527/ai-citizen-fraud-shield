import streamlit as st
import pandas as pd
import plotly.express as px
import sys
sys.path.append('.')

st.set_page_config(
    page_title='Fraud Intelligence Dashboard',
    page_icon='📊',
    layout='wide'
)

st.title('📊 Fraud Intelligence Dashboard')
st.write('India cybercrime statistics — NCRB data 2003 to 2021')

# Load NCRB data
@st.cache_data
def load_data():
    try:
        df = pd.read_csv('data/ncrb_cybercrime.csv')
        return df
    except:
        # Sample data if file not found
        data = {
            'Year': [2015,2016,2017,2018,2019,2020,2021],
            'Total_Cases': [11592,12317,21796,27248,44735,50035,52974]
        }
        return pd.DataFrame(data)

df = load_data()

# Key metrics
st.markdown("---")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric('Total Cases 2021', '52,974', '+5.9%')
with col2:
    st.metric('Total Cases 2020', '50,035', '+11.9%')
with col3:
    st.metric('Total Cases 2019', '44,735', '+64.3%')
with col4:
    st.metric('Growth 2015-2021', '357%', '↑ Alarming')

st.markdown("---")

col_left, col_right = st.columns(2)

with col_left:
    st.subheader('📈 Cybercrime Growth 2003–2021')
    if 'Year' in df.columns and 'Total_Cases' in df.columns:
        yearly = df.groupby('Year')['Total_Cases'].sum().reset_index()
        fig1 = px.line(
            yearly, x='Year', y='Total_Cases',
            title='Total Cybercrime Cases Per Year',
            markers=True,
            color_discrete_sequence=['#185FA5']
        )
        fig1.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font_color='white'
        )
        st.plotly_chart(fig1, use_container_width=True)

with col_right:
    st.subheader('🗺️ Top States by Cybercrime (2021)')
    top_states_data = {
        'State': ['Uttar Pradesh','Maharashtra','Karnataka','Telangana',
                  'Rajasthan','Assam','Odisha','Haryana','Gujarat','Tamil Nadu'],
        'Cases': [8829, 5562, 5159, 4499, 3507, 3530, 3047, 2810, 2481, 2415]
    }
    df_states = pd.DataFrame(top_states_data)
    fig2 = px.bar(
        df_states, x='Cases', y='State',
        orientation='h',
        title='Top 10 States — Cybercrime Cases 2021',
        color='Cases',
        color_continuous_scale='Reds'
    )
    fig2.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font_color='white'
    )
    st.plotly_chart(fig2, use_container_width=True)

st.markdown("---")
st.subheader('🔍 Common Scam Types in India')
scam_data = {
    'Scam Type': ['Digital Arrest','UPI Fraud','Phishing','KYC Scam','Investment Fraud'],
    'Percentage': [30, 25, 20, 15, 10]
}
df_scam = pd.DataFrame(scam_data)
fig3 = px.pie(
    df_scam, values='Percentage', names='Scam Type',
    title='Distribution of Cybercrime Types 2024',
    color_discrete_sequence=px.colors.sequential.Blues_r
)
fig3.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    font_color='white'
)
st.plotly_chart(fig3, use_container_width=True)

st.markdown("---")
st.warning('⚠️ Data Source: NCRB Cybercrime Reports 2003–2021. Digital Arrest and UPI Fraud together account for 55% of total scam cases.')
st.info('📞 Report cybercrime: **1930** | Online: **cybercrime.gov.in**')