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
st.info("Hypothesis: Men are more often represented in new articles than women such as that news outlets mention men far more often than they do women, at a ratio of about 3:1.")

st.markdown("In order to test the hypothesis that men are more frequently represented in news articles compared to women, with a ratio of approximately 3:1, we implemented a methodology based on counting the mentions of men and women in each article."
            " To obtain data for analysis, we scraped articles from prominent news outlets such as **The Wall Street Journal**, **The Washington Post**, **The Times**, and **The New York Times**, specifically focusing on articles published during **the year 2022**.")
st.markdown("To begin, we tokenized the articles, which involved splitting the text into individual words or tokens. With the tokenization process complete, we proceeded to label each token using the appropriate entity recognition technique. Specifically, we identified tokens that represented people or persons in the text. This allowed us to isolate the mentions of individuals within the articles.")
st.markdown("To determine the gender of each mentioned person, we utilized the [gender_guesser](https://pypi.org/project/gender-guesser/) library. By passing the identified person's name to this library, it made an educated guess regarding the individual's gender based on the name itself. It's important to note that this method employs probabilistic inference and may not always accurately predict gender, particularly for names that are gender-neutral or derived from different cultural origins.")

st.markdown('#')

option = st.selectbox(
    'Please Select a Newspaper',
    ('The Wall Street Journal', 'The Washington Post', 'The Times', 'New York Times'))

st.markdown('#')

chart_monthly = alt.Chart(monthly_chart(option), title=f'Monthly counts of men and women mentioned in {option}') \
    .mark_line() \
    .encode(
        x=alt.X('month:N', sort=None),
        y=alt.Y('value:Q', title='counts'),
        color=alt.Color("name:N")
    )
st.altair_chart(chart_monthly, use_container_width=True)

st.markdown('#')

chart = alt.Chart(category_chart(option), title=f'Counts of men and women mentioned across categories in {option}').mark_bar(
    opacity=1,
).encode(
    column=alt.Column('category', header=alt.Header(labelOrient="bottom"),
                      sort=alt.SortField("number_of_articles", order="descending")),
    x=alt.X('variable', axis=None),
    y=alt.Y('value:Q', title='counts'),
    color=alt.Color('variable', legend=alt.Legend(
        orient='none',
        legendX=130, legendY=-20,
        direction='horizontal',
        title=None))
).configure_view(stroke='transparent')
st.altair_chart(chart)

st.markdown('#')

cols = st.columns([1, 1])

with cols[0]:
    category = st.selectbox('Please Select a Category', charts.pie_chart_category[option])

with cols[1]:
    month = st.selectbox('Please Select a Month', charts.months.keys())

st.markdown('#')

pie_chart = charts.pie_chart(option=option, month=month, category=category)
