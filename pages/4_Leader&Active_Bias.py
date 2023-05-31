import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Leader&Active Bias")

st.title("Gender Media Bias Tool")
st.subheader('Leader/Active Bias')
st.sidebar.header("Leader/Active Bias")
st.info('Hypothesis: Across topics men will be more often portrayed as active, dominant, leaders, perpetrators, while women are more often portrayed as passive, submissive, followers, victims.')

st.markdown("In this study, a word embedding model trained using the powerful [**FastText**](https://radimrehurek.com/gensim/models/fasttext.html) algorithm. The model was trained on a corpus of **45,372 articles** meticulously sourced from **The Washington Post** during the year 2022. "
            "Word embeddings capture semantic relationships between words by representing them as dense vectors in a high-dimensional space. By leveraging this model, we aimed to explore whether certain biases exist in how men and women are portrayed in the media.")
st.markdown("The study employed the [**Word Embedding Association Test (WEAT)**](https://wefe.readthedocs.io/en/latest/_modules/wefe/metrics/WEAT.html), a statistical technique used to measure the association between sets of target words and attribute words. The target words in this case were related to gender, with categories such as \"Male\" and \"Female.\" The attribute words represented specific characteristics, such as being active, dominant, leaders, or perpetrators for men, and passive, submissive, followers, or victims for women.")
leader = ['leader', 'active', 'dominant', 'confident', 'strong', 'assertive', 'ambitious', 'successful', 'inspiring', 'influential', 'visionary']
follower = ['follower', 'passive', 'submissive', 'meek', 'dependent', 'obedient', 'quiet', 'shy', 'gentle', 'nurturing', 'emotional']
victimhood = ['vulnerable', 'sensitive', 'emotional', 'caring', 'empathetic', 'compassionate', 'sympathetic', 'nurturing', 'supportive', 'maternal']
perpetrator = ['aggressive', 'violent', 'controlling', 'dominating', 'threatening', 'intimidating', 'dangerous', 'harmful', 'abusive', 'manipulative']

male_names = "he, man, male, boy, gentleman, father, husband, brother, son, grandfather, uncle"
female_names = "she, woman, female, girl, lady, mother, wife, sister, daughter, grandmother, aunt"
leader_words = ', '.join(leader)
follower_words = ', '.join(follower)
perpetrator_words = ', '.join(perpetrator)
victim_words = ', '.join(victimhood)

# Create a list of tuples for the word and category pairs
word_stimuli = [
    ('Male', male_names),
    ('Female', female_names),
    ('Leader', leader_words),
    ('Follower', follower_words),
    ('Perpetrator', perpetrator_words),
    ('Victim', victim_words),
]

# Create a DataFrame from the list of tuples
df = pd.DataFrame(word_stimuli, columns=['Category', 'Word Stimuli'])

df.style.set_properties(**{'background-color': 'black',
                           'color': 'green'})

# CSS to inject contained in a string
hide_table_row_index = """
            <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
            </style>
            """

st.markdown("The following Word Stimulis are used.")

# Inject CSS with Markdown
st.markdown(hide_table_row_index, unsafe_allow_html=True)

# Display a static table
st.write(df.to_html(index_names=False, justify="left"), unsafe_allow_html=True)
st.markdown('')

st.markdown("These word stimuli are used to evaluate the associations between gender-related terms and leadership-related terms, as well as terms associated with perpetration and victimhood. The WEAT score, ranging from -2 to 2, measures the strength and direction of association between these word sets. A score close to -2 or 2 indicates a strong association, while a score close to 0 suggests no or weak association.")
st.markdown("The WEAT score is calculated by comparing the similarities between the target set of words and an attribute set of words. The test measures the differences in similarities between the two sets of words and assesses the statistical significance of the association.")
st.markdown("Additionally, the effect size is another important metric in WEAT. It measures the magnitude of the association between the word sets, indicating the practical significance of the results. The effect size ranges from 0 to 1, where 0 represents no effect or negligible association, and 1 represents a strong effect or significant association.")
st.markdown("A larger effect size indicates a more substantial difference between the two word sets, suggesting a stronger association or bias. It helps to determine the practical importance of the findings beyond statistical significance.")
st.markdown("In this study, two distinct analyses were carried out using the WEAT. The first analysis Male and female names were considered as the target words, while the attribute words were \"leader\" and \"follower\". This analysis aimed to uncover any connections or biases between gendered names and the qualities of leadership or followership.")
st.markdown("The second analysis retained the same target words (male and female names) but shifted the attribute words to \"perpetrator\" and \"victim\". By examining the association between gendered names and the attributes of being a perpetrator or a victim, this analysis sought to shed light on potential associations or biases associated with gender and these specific roles.")
st.markdown("The following results are obtained.")

df2 = pd.DataFrame([[0.195, 0.498, 0.183, 0.608]], index=['The Washington Post'])
df2.columns = pd.MultiIndex.from_product([['Male names and Female names wrt Leader and Follower', 'Male names and Female names wrt Perpetrator and Victim'],['WEAT Score', 'Effect Size']])
df2.index.name = 'Newspaper'
df2.reset_index(inplace=True)

st.write(df2.to_html(index_names=True), unsafe_allow_html=True)
st.markdown('')
st.markdown("The results of the analysis show that in the context of \"Male names and Female names wrt Leader and Follower,\" there is a moderate association between gendered names and the attributes of being a leader or a follower. The WEAT score of 0.195 indicates a positive association, suggesting that male names are slightly more associated with leader-related attributes, while female names are slightly more associated with follower-related attributes. The effect size of 0.498 indicates a moderate practical significance, indicating that there is a notable difference between the word sets.")
st.markdown("In the case of \"Male names and Female names wrt perpetrator and Victim,\" the results indicate a similar pattern. The WEAT score of 0.183 suggests a positive association, indicating that male names are somewhat more associated with the attributes of being a perpetrator, while female names are somewhat more associated with the attributes of being a victim. The effect size of 0.608 indicates a moderate practical significance, highlighting the meaningful distinction between the word sets.")