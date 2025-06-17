import streamlit as st
import plotly.express as px
import pandas as pd

#Title of the app
st.title("Flight Data Dashboard")

#Flight data:Passengers
df=pd.read_csv("passengers.csv")

#Create a bar chart
fig1=px.bar(df, x="Year", y="Domestic", title="Total Passengers Domestic Flights")

fig2=px.bar(df, x="Year", y="Domestic", title="Total Passengers International Flights")

# Arrange plots: grid layout
col1, col2 =st.columns(2) #Create 2 columns

with col1:
  st.plotly_chart(fig1, use_container_width=True)

with col2:
  st.plotly_chart(fig2, use_container_width=True)
