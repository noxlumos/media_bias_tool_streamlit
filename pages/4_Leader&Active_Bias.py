import streamlit as st
import pandas as pd

st.set_page_config(page_title="Leader&Active Bias")

st.title("Gender Media Bias Tool")
st.subheader('Leader/Active Bias')
st.sidebar.header("Leader/Active Bias")
st.markdown("In this study, a FastText word embedding model trained on corpus of 45372 articles obtained from the Washington Post during 2022 was used to investigate potential biases in word associations. Word embeddings capture semantic relationships between words by representing them as dense vectors in a high-dimensional space. By leveraging this model, researchers aimed to explore whether certain biases exist in how men and women are portrayed in the media.")
st.markdown("The study employed the Word Embedding Association Test (WEAT), a statistical technique used to measure the association between sets of target words and attribute words. The target words in this case were related to gender, with categories such as \"Male\" and \"Female.\" The attribute words represented specific characteristics, such as being active, dominant, leaders, or perpetrators for men, and passive, submissive, followers, or victims for women.")
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
st.table(df)

st.markdown("By applying the WEAT analysis to the word embedding model, we aimed to quantitatively assess any potential bias in how men and women are depicted in the Washington Post articles.")

st.markdown("The WEAT score is a quantitative measure that assesses the strength and direction of the association between word categories in the Word Embedding Association Test (WEAT). It can range from -2 to 2. A WEAT score of 0 indicates no association or bias between the target and attribute word categories. Values closer to -2 or 2 suggest a stronger association, with negative values indicating an association biased towards the attribute words and positive values indicating an association biased towards the target words.")

st.markdown("The following results are obtained.")

st.slider('Male names and Female names wrt Leader and Follower', min_value=-2.0, max_value=2.0, value=0.19, step=1.0, disabled=True)

st.slider('Male names and Female names wrt Perpetrator and Victim', min_value=-2.0, max_value=2.0, value=0.18, step=1.0, disabled=True)

st.markdown("The WEAT score of 0.19 and 0.18 indicates that the association is stronger than what would be expected by chance alone. "
            "This suggests that there is a meaningful difference in the way that men and women are portrayed in the text, "
            "with men more often associated as leaders, perpetrators  and women more often associated as followers, victims.")