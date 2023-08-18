import plotly.express as px
from pathlib import Path
import streamlit as st
import pandas as pd
import os

# Establish a filepath to the oracle_cards.csv file
filepath = os.path.join(Path(__file__).parents[1], 'data/oracle_cards.csv')
df = pd.read_csv(filepath, low_memory=False)

# Take in a user input:
vis_to_use = ['Histogram', 'Bar Chart', 'Scatter Plot', 'Pie Chart', 'Line Chart', 'Area Chart']
type_vis = st.selectbox('Select the type of Visualization you would like to see:', options=vis_to_use)

if type_vis == 'Histogram':
    selected_column = st.selectbox('Select a Column for the Histogram:', options=sorted(list(df.columns)))
    if selected_column:
        st.plotly_chart(px.histogram(df, x=selected_column), use_container_width=True)

elif type_vis == 'Bar Chart':
    x_column = st.selectbox('Select a Column for the X-axis:', options=sorted(list(df.columns)))
    y_column = st.selectbox('Select a Column for the Y-axis:', options=sorted(list(df.columns)))
    if x_column and y_column:
        st.plotly_chart(px.bar(df, x=x_column, y=y_column), use_container_width=True)

elif type_vis == 'Scatter Plot':
    x_column = st.selectbox('Select a Column for the X-axis:', options=sorted(list(df.columns)))
    y_column = st.selectbox('Select a Column for the Y-axis:', options=sorted(list(df.columns)))
    if x_column and y_column:
        st.plotly_chart(px.scatter(df, x=x_column, y=y_column, hover_data=['name']), use_container_width=True)

elif type_vis == 'Pie Chart':
    selected_column = st.selectbox('Select a Column for the Pie Chart:', options=sorted(list(df.columns)))
    if selected_column:
        st.plotly_chart(px.pie(df, names=selected_column), use_container_width=True)

elif type_vis == 'Line Chart':
    x_column = st.selectbox('Select a Column for the X-axis:', options=sorted(list(df.columns)))
    y_column = st.selectbox('Select a Column for the Y-axis:', options=sorted(list(df.columns)))
    if x_column and y_column:
        st.plotly_chart(px.line(df, x=x_column, y=y_column), use_container_width=True)

elif type_vis == 'Area Chart':
    x_column = st.selectbox('Select a Column for the X-axis:', options=sorted(list(df.columns)))
    y_column = st.selectbox('Select a Column for the Y-axis:', options=sorted(list(df.columns)))
    if x_column and y_column:
        st.plotly_chart(px.area(df, x=x_column, y=y_column), use_container_width=True)
