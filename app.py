"""
@Author:    zFei
@Data:      12/1/24
@Project:   streamlit_app
@File:      app.py
"""

import streamlit as st
import pandas as pd
import altair as alt
import numpy as np

st.button('Reload Page')
st.title('st.title')
st.header('st.header')
st.write('st.write')
st.write(1234)

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)

st.write(np.random.randn(200, 3).shape)

st.write('git push')
st.write('lichenglong good')
