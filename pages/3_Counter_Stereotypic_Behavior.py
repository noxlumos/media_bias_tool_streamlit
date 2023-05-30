import streamlit as st
import altair as alt
from charts import sentiment_analysis
st.set_page_config(page_title="Counter Stereotypic Behavior")

st.title("Gender Media Bias Tool")
st.subheader('Backlash for Counter Stereotypic Behavior')
st.sidebar.header("Counter Stereotypic Behavior")
st.info('Hypothesis: Men and women who break gender stereotypes by showing counter-stereotypic behavior or taking counter-stereotypic roles such as female politicians are portrayed in a more negative tone than men and women who do not break gender stereotypes.')

st.markdown('The hypothesis posited that men and women who break gender stereotypes by exhibiting counter-stereotypic behavior or assuming unconventional roles, such as female politicians, would be portrayed in a more negative tone compared to those who conform to traditional gender stereotypes. To test this hypothesis, **sentiment analysis** was conducted separately on female and male politicians mentioned within the politics category, as well as on all men and women mentioned across all categories.'
            'Sentiment analysis, also known as opinion mining, '
            'is a Natural Language Processing technique that aims to extract subjective information from text and categorize it as **positive**, **negative**, or **neutral**.')

col1, col2 = st.columns(2)
with col1:
    st.markdown("**Sentiment Analysis: Portrayal of Male and Female Politicians in Politics Category**")
    chart = alt.Chart(sentiment_analysis(10)).mark_bar(opacity=1).encode(
            column=alt.Column('gender', header=alt.Header(title=' ', labelOrient="bottom")),
            x=alt.X('variable', axis=None),
            y=alt.Y('value:Q', title='percentage'),
            color=alt.Color('variable')
        ).configure_view(stroke='transparent')
    st.altair_chart(chart)

with col2:
    st.markdown("**Sentiment Analysis: Portrayal of Men and Women across all categories**")
    chart = alt.Chart(sentiment_analysis(15)).mark_bar(opacity=1).encode(
        column=alt.Column('gender', header=alt.Header(title=' ', labelOrient="bottom")),
        x=alt.X('variable', axis=None),
        y=alt.Y('value:Q', title='percentage'),
        color=alt.Color('variable')
    ).configure_view(stroke='transparent')

    st.altair_chart(chart)

st.markdown('Surprisingly, the results revealed a contrasting pattern. Specifically, the sentiment analysis on female and male politicians mentioned in politics indicated that male politicians were mentioned in a more negative way compared to their female counterparts. This finding contradicts the hypothesis, suggesting that female politicians may not face the anticipated negative portrayal when breaking gender stereotypes.')
st.markdown('In contrast, when sentiment analysis was performed on all men and women mentioned across all categories, it was observed that both genders were mentioned in a negative less frequently. This implies that the negative portrayal of men and women, in general, was less prevalent compared to the specific context of politics.')
st.markdown('These divergent results suggest that while male politicians may face negativity in their portrayal within the politics category, the overall sentiment toward men and women across all categories tends to be less negative. These findings challenge the initial hypothesis and indicate a need for further investigation into the factors influencing the portrayal of gender stereotypes in different contexts and categories.')

st.markdown('Furthermore, to provide a comprehensive analysis, individual sentiment analysis results for each category were examined. This allowed for a closer examination of how men and women were portrayed within specific domains. The following graphs displaying the sentiment analysis results for each individual category can be observed.')

col1, col2 = st.columns(2)


categories = ['markets', 'real estate', 'magazine','news','economy','opinion','style','business','sports','life & work','politics','us','tech','world','books & arts']
with col1:
    option = st.selectbox(
        'Please Select a Category',
       categories)

with col2:
    html_str = f"**Sentiment Analysis: Portrayal of Men and Women in {option} category**"
    st.markdown(html_str, unsafe_allow_html=True)
    chart = alt.Chart(sentiment_analysis(categories.index(option))).mark_bar(opacity=1).encode(
        column=alt.Column('gender', header=alt.Header(title=' ', labelOrient="bottom")),
        x=alt.X('variable', axis=None),
        y=alt.Y('value:Q', title='percentage'),
        color=alt.Color('variable')
    ).configure_view(stroke='transparent')

    st.altair_chart(chart)

st.markdown("Women were mentioned in a more negative manner within the 'World' category, while men received a higher proportion of negative mentions within the 'US' category."
            "Both men and women were mentioned most positively in the 'Magazine' category, suggesting a relatively favorable portrayal of both genders in this context.")

st.markdown("**P.S.** All the data analyzed in this study was obtained exclusively from articles published by The Wall Street Journal during the year 2022. ")