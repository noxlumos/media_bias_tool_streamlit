import streamlit as st
import altair as alt
import charts
from charts import monthly_chart, category_chart

st.set_page_config(page_title="gendered division of duties and representation in media")

st.title("Gender Media Bias Tool")
st.subheader('Gendered Division of Duties & Representation In Media')
st.sidebar.header("Gender Representation In Media")

st.info(
    "Hypothesis: Topics such as lifestyle, arts and entertainment, and healthcare tend to be prominent in articles "
    "that quote more women than men. Topics such as sports, politics, and business are characteristic of articles "
    "that quote more men than women.")

st.markdown(
    "In this study, the gender-bias among the people who are **quoted** in the articles of **The Times** newspaper "
    "was analyzed. "
    "30209 articles from 34 categories belonging to 2022 were used in this analysis. ")

st.markdown(
    "To begin with, the sentences that include direct quotations are extracted from the article texts and tokenized, "
    "which involved splitting the sentences into individual words or tokens. With the tokenization process complete, "
    "the tokens are labeled using the appropriate entity recognition technique. Specifically, the tokens representing "
    "quotation speakers in the sentences are identified.")

st.markdown(
    "The genders of the quotation speakers found as personal pronouns could be directly labeled as 'male' or 'female'.")

st.markdown(
    "On the other hand, to determine the gender of the quotation speakers found as names, the [gender_guesser]("
    "https://pypi.org/project/gender-guesser/) library was used. By passing the identified quotation speaker's name "
    "to this library, it made an educated guess regarding the individual's gender based on the name itself. It's "
    "important to note that this method employs probabilistic inference and may not always accurately predict gender, "
    "particularly for names that are gender-neutral or derived from different cultural origins.")

st.markdown(
    "According to the analysis results, the categories that most quoted men or women as percentages were found. The "
    "top 3 categories that men are most quoted as percentage are: 'Formula One', 'Golf', 'Cricket'. The top 3 "
    "categories that women are most quoted as percentage are: 'Home Interiors', 'Beauty', 'Radio & Podcasts'. These "
    "findings confirm the hypothesis.")

st.markdown('#')

chart_monthly = alt.Chart(monthly_chart('The Times Quotation Speakers'), title='Monthly counts of men and women quoted') \
    .mark_line() \
    .encode(
    x=alt.X('month:N', sort=None),
    y=alt.Y('value:Q'),
    color=alt.Color("name:N"))
st.altair_chart(chart_monthly, use_container_width=True)

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

st.markdown('#')

cols = st.columns([1, 1])

with cols[0]:
    category = st.selectbox('Please Select a Category', charts.the_times_categories)

with cols[1]:
    month = st.selectbox('Please Select a Month', charts.months.keys())

st.markdown('#')

pie_chart = charts.pie_chart(option='The Times Quotation Speakers', month=month, category=category)

st.markdown('#')
