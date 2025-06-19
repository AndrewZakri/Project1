import streamlit as st
import plotly.express as px
import pandas as pd

# Title of the app
st.title("U.S. Flight Data 10-2022 thru 03-2025")

# Flight data:Passengers
df=pd.read_csv("passengers_yearly.csv")
df2=pd.read_csv("operating revenue_yearly.csv")

# Create a bar chart
fig1=px.bar(df, x="Year", y="Domestic", title="Passengers: Domestic Flights")

fig2=px.bar(df, x="Year", y="International", title="Passengers: International Flights")

fig3=px.bar(df, x="Year", y="Total", title="Total Passengers: All Flights")

fig4=px.bar(df2, x="Year", y="DOMESTIC", title="Domestic Operating Revenue")

fig5=px.bar(df2, x="Year", y="INTERNATIONAL", title="International Operating Revenue")

fig6=px.bar(df2, x="Year", y="TOTAL", title="Total Operating Revenue")

# Arrange plots: grid layout
col1, col2 =st.columns(2) #Create 2 columns

with col1:
  st.plotly_chart(fig1, use_container_width=True)

with col2:
  st.plotly_chart(fig2, use_container_width=True)

# Third plot is full-width
st.plotly_chart(fig3, use_container_width=True)

with col1:
  st.plotly_chart(fig4, use_container_width=True)

with col2:
  st.plotly_chart(fig5, use_container_width=True)

st.plotly_chart(fig6, use_container_width=True)

