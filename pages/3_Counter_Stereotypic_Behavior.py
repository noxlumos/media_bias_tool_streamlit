import streamlit as st
import altair as alt
import pandas as pd

outputs = pd.read_csv('data/sentiment_analysis_wsj.csv')

def sentiment_analysis(section):

    print(outputs)
    alt.data_transformers.disable_max_rows()
    data = pd.DataFrame({
        'gender': ['male', 'female'],
        'negative': [outputs['m_n_p'][section]+outputs['m_v_n_p'][section], outputs['f_n_p'][section]+outputs['f_v_n_p'][section]],
        'positive': [outputs['m_p_p'][section]+outputs['m_v_p_p'][section], outputs['f_p_p'][section]+outputs['f_v_p_p'][section]],
        'neutral': [outputs['m_n'][section], outputs['f_n'][section]],
    })
    prediction_table = pd.melt(data, id_vars=['gender'], value_vars=['negative', 'positive', 'neutral'])
    return prediction_table


st.set_page_config(page_title="Counter Stereotypic Behavior")

st.title("Gender Media Bias Tool")
st.subheader('Backlash for Counter Stereotypic Behavior')
st.sidebar.header("Counter Stereotypic Behavior")
st.info('Hypothesis: Men and women who break gender stereotypes by showing counter-stereotypic behavior or taking counter-stereotypic roles such as female politicians are portrayed in a more negative tone than men and women who do not break gender stereotypes.')

st.markdown('The hypothesis posited that men and women who break gender stereotypes by exhibiting counter-stereotypic behavior or assuming unconventional roles, such as female politicians, would be portrayed in a more negative tone compared to those who conform to traditional gender stereotypes. To test this hypothesis, we employed a two-step approach utilizing **sentiment analysis**.'
            'Sentiment analysis, also known as opinion mining, '
            'is a Natural Language Processing technique that aims to extract subjective information from text and categorize it as **positive**, **negative**, or **neutral**.')

st.markdown('Firstly, we focused specifically on the politics category. We identified sentences that mentioned the names of politicians and subjected those sentences to [VADER sentiment analysis](https://www.nltk.org/api/nltk.sentiment.vader.html#nltk.sentiment.vader.SentimentIntensityAnalyzer). By doing so, we assessed the sentiment expressed towards each politician. We recorded the number of times female and male politicians were mentioned and categorized the sentiments associated with their mentions as positive, negative, or neutral. This allowed us to calculate the percentage of female and male politicians mentioned in each sentiment category.')
st.markdown('Secondly, we broadened our analysis to encompass all categories, not limited to politics alone. We identified sentences that mentioned women or men and subjected those sentences to sentiment analysis using the same module. This enabled us to gauge the sentiments expressed towards women and men in general. Similar to the politics category, we collected the sentiments associated with these mentions and calculated the percentages of positive, negative, and neutral sentiments for both women and men.')
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
    st.markdown("Number of articles analyzed: **1485**")

with col2:
    st.markdown("**Sentiment Analysis: Portrayal of Men and Women Across All Categories**")
    chart = alt.Chart(sentiment_analysis(14)).mark_bar(opacity=1).encode(
        column=alt.Column('gender', header=alt.Header(title=' ', labelOrient="bottom")),
        x=alt.X('variable', axis=None),
        y=alt.Y('value:Q', title='percentage'),
        color=alt.Color('variable')
    ).configure_view(stroke='transparent')
    st.altair_chart(chart)
    st.markdown("Number of articles analyzed: **31956**")

st.markdown('Surprisingly, the results revealed a contrasting pattern. Specifically, the sentiment analysis on female and male politicians mentioned in politics indicated that male politicians were mentioned in a more negative way compared to their female counterparts. This finding contradicts the hypothesis, suggesting that female politicians may not face the anticipated negative portrayal when breaking gender stereotypes.')
st.markdown('In contrast, when sentiment analysis was performed on all men and women mentioned across all categories, it was observed that both genders were mentioned in a negative less frequently. This implies that the negative portrayal of men and women, in general, was less prevalent compared to the specific context of politics.')
st.markdown('These divergent results suggest that while male politicians may face negativity in their portrayal within the politics category, the overall sentiment toward men and women across all categories tends to be less negative. These findings challenge the initial hypothesis and indicate a need for further investigation into the factors influencing the portrayal of gender stereotypes in different contexts and categories.')

st.markdown('Furthermore, to provide a comprehensive analysis, individual sentiment analysis results for each category were examined. This allowed for a closer examination of how men and women were portrayed within specific domains. The following graphs displaying the sentiment analysis results for each individual category can be observed.')

col1, col2 = st.columns(2)


categories = ['markets', 'real estate', 'news','economy','opinion','style','business','sports','life & work','politics','us','tech','world','books & arts']
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
    str = f"Number of articles analyzed: **{outputs['number_of_articles'][categories.index(option)]}**"
    st.markdown(str, unsafe_allow_html=True)

st.markdown("Women were mentioned in a more negative manner within the 'World' category, while men received a higher proportion of negative mentions within the 'US' category."
            "Both men and women were mentioned most positively in the 'Magazine' category, suggesting a relatively favorable portrayal of both genders in this context.")

st.markdown("**P.S.** All the data analyzed in this study was obtained exclusively from articles published by The Wall Street Journal during the year 2022. ")