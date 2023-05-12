# streamlit_app.py

import streamlit as st
import snowflake.connector
from snowflake.snowpark.session import Session
import pandas as pd
import numpy as np
import plotly.express as px

# Snowflake connection info is saved in config.py
# from config import snowflake_conn_prop

# Initialize connection.
# Uses st.experimental_singleton to only run once.
# session = Session.builder.configs(snowflake_conn_prop).create()

session = Session.builder.configs(st.secrets["snowflake"]).create()

# Perform query.
# Uses st.experimental_memo to only rerun when the query changes or after 10 min.

st.header('Customer Segmentation example with Snowpark using K-Means. Data is queried live from Snowflake')

st.write('Sample cluster data that shows the recency, frequency and monetary attributes of each customer')

df = session.table("RFM_Clusters")
df_pd = df.to_pandas()
st.dataframe(df_pd)



