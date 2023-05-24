import streamlit as st
import altair as alt
import pandas as pd

from charts import monthly_chart, category_chart

st.set_page_config(page_title="Coverage Bias")

st.title("Gender Media Bias Tool")
st.subheader('Coverage Bias')
st.sidebar.header('Coverage Bias')

option = st.selectbox(
    'Please Select a Newspaper',
    ('Washington Post', 'Wall Street Journal', 'The Times', 'New York Times'))

if option != 'The Times':
    chart_monthly = alt.Chart(monthly_chart(option), title='Montly counts of man and women mentioned')\
        .mark_line()\
        .encode(
            x=alt.X('month:N'),
            y=alt.Y('value:Q'),
            color=alt.Color("name:N"))
    st.altair_chart(chart_monthly, use_container_width=True)

    chart = alt.Chart(category_chart(option), title='Counts of man and women mentioned through categories').mark_bar(
        opacity=1,
    ).encode(
        column=alt.Column('category', header=alt.Header(labelOrient="bottom"), sort=alt.SortField("articles", order="descending")),
        x=alt.X('variable', axis=None),
        y=alt.Y('value:Q'),
        color=alt.Color('variable')
    ).configure_view(stroke='transparent')
    st.altair_chart(chart)

#if option == 'The Times':
## TO DO AYSENUR





