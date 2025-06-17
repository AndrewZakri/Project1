import streamlit as st
import plotly.express as px
import pandas as pd

#Title of the app
st.title("Flight Data Dashboard")

#Flight data:Passengers
df=pd.read_csv('Passengers.csv')

#Create a bar chart
fig=px.bar(df, x="Year", y="DOMESTIC", title="Total Passengers Domestic Flights")

#Display the Plotly chart in Streamlit
st.plotly_chart(fig)
