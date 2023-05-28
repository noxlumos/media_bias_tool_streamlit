import streamlit as st
import altair as alt
import pandas as pd

import charts
from charts import monthly_chart, category_chart

st.set_page_config(page_title="Coverage Bias")

style = """
    <style>
        .main > div {
            padding-left: 0rem;
            padding-right: 0rem;
        }
    </style>
"""
st.markdown(style, unsafe_allow_html=True)
st.title("Gender Media Bias Tool")
st.subheader('Coverage Bias')
st.sidebar.header('Coverage Bias')

option = st.selectbox(
    'Please Select a Newspaper',
    ('Wall Street Journal', 'Washington Post', 'The Times', 'New York Times'))

if option != 'The Times':
    st.markdown('#')

    chart_monthly = alt.Chart(monthly_chart(option), title='Monthly counts of men and women mentioned') \
        .mark_line() \
        .encode(
        x=alt.X('month:N'),
        y=alt.Y('value:Q'),
        color=alt.Color("name:N"))
    st.altair_chart(chart_monthly, use_container_width=True)

    st.markdown('#')

    chart = alt.Chart(category_chart(option), title='Counts of men and women mentioned through categories').mark_bar(
        opacity=1,
    ).encode(
        column=alt.Column('category', header=alt.Header(labelOrient="bottom"),
                          sort=alt.SortField("articles", order="descending")),
        x=alt.X('variable', axis=None),
        y=alt.Y('value:Q'),
        color=alt.Color('variable')
    ).configure_view(stroke='transparent')
    st.altair_chart(chart)

if option == 'The Times':
    st.markdown('#')

    chart_monthly = alt.Chart(monthly_chart(option), title='Monthly counts of men and women mentioned') \
        .mark_line() \
        .encode(
        x=alt.X('month:N'),
        y=alt.Y('value:Q'),
        color=alt.Color("name:N"))
    st.altair_chart(chart_monthly, use_container_width=True)

    st.markdown('#')

    cols = st.columns([1, 1])

    with cols[0]:
        category = st.selectbox('Please Select a Category', charts.the_times_categories)

    with cols[1]:
        month = st.selectbox('Please Select a Month', charts.months.keys())

    st.markdown('#')

    pie_chart = charts.pie_chart(option=option, month=month, category=category)

