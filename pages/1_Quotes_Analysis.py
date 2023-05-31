import streamlit as st
import altair as alt
import charts
from charts import monthly_chart, category_chart

st.set_page_config(page_title="Quotes Analysis")

st.title("Gender Media Bias Tool")
st.subheader('Quotes Analysis')
st.sidebar.header("Quotes Analysis")

# TODO write explanation
st.markdown(
    "In this study, the gender-bias among the people who are **quoted** in the articles of 'The Times' newspaper was analyzed. "
    "30209 articles from 34 categories belonging to 2022 were used in this analysis. ")
st.markdown("The top 3 categories that men are most quoted as percentage are: 'Formula One', 'Golf', 'Cricket'")
st.markdown("The top 3 categories that women are most quoted as percentage are: 'Home Interiors', 'Beauty', 'Radio & Podcasts'")

# TODO find 5 male-female dominant categories

st.markdown('#')

chart_monthly = alt.Chart(monthly_chart('The Times Quotation Speakers'), title='Monthly counts of men and women quoted') \
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

pie_chart = charts.pie_chart(option='The Times Quotation Speakers', month=month, category=category)

st.markdown('#')
st.markdown('#')

chart = alt.Chart(category_chart('The Times Quotation Speakers'),
                  title='Counts of men and women quoted through categories').mark_bar(
    opacity=1,
).encode(
    column=alt.Column('category', header=alt.Header(labelOrient="bottom"),
                      sort=alt.SortField("number_of_articles", order="descending")),
    x=alt.X('variable', axis=None),
    y=alt.Y('value:Q'),
    color=alt.Color('variable')
).configure_view(stroke='transparent')
st.altair_chart(chart)

