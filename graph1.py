import streamlit as st
import plotly.express as px
import pandas as pd

#Title of the app
st.title("Flight Data Dashboard")

#Flight data:Passengers
df=pd.read_csv("passengers_yearly.csv")

#Create a bar chart
fig1=px.bar(df, x="Year", y="Domestic", title="Total Passenger Domestic Flights")

fig2=px.bar(df, x="Year", y="International", title="Total Passenger International Flights")

fig3=px.bar(df, x="Year", y="Total", title="Total Passenger Flights")

# Arrange plots: grid layout
col1, col2, col3 =st.columns(3) #Create 3 columns

with col1:
  st.plotly_chart(fig1, use_container_width=True)

with col2:
  st.plotly_chart(fig2, use_container_width=True)

with col3:
  st.plotly_chart(fig3, use_container_width=True)
