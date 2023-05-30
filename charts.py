import altair as alt
import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

option_monthly = {"Wall Street Journal": "data/wsj_names_monthly.csv",
                  "Washington Post": "data/wp_names_monthly.csv",
                  "New York Times": "data/wp_names_monthly.csv",
                  "The Times": "data/times_names_monthly.csv",
                  "The Times Quotation Speakers": "data/times_quotation_speakers_monthly.csv"}

option_category = {"Wall Street Journal": "data/wsj_names_category.csv",
                   "Washington Post": "data/wp_names_category.csv",
                   "New York Times": "data/wp_names_category.csv"}

months = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 'July': 7, 'August': 8,
          'September': 9, 'October': 10,
          'November': 11, 'December': 12}

the_times_categories = ['UK Politics', 'Global Politics', 'Brexit',
                        'Economy', 'Markets', 'Property', 'Personal Finance', 'Banking',
                        'Health', 'Science', 'Technology', 'Transport', 'Law',
                        'Cricket', 'Tennis', 'Rugby Union', 'Formula One', 'Golf', 'Horse Racing and Tips', 'Boxing',
                        'Winter Olympics 2022',
                        'Television', 'Film', 'Music', 'Radio & Podcasts', 'Books', 'Theatre', 'Art Reviews',
                        'Beauty', 'Food & Drink', 'Fitness & Wellbeing', 'Home Interiors', 'Gardening', 'Driving']


def monthly_chart(option):
    outputs = pd.read_csv(option_monthly[option])
    data = pd.DataFrame({
        'month': outputs['month'].tolist(),
        'male': outputs['male_counter'].tolist(),
        'female': outputs['female_counter'].tolist(),
        'articles': outputs['number_of_articles'].tolist()
    }, columns=['month', 'male', 'female', 'articles'])
    prediction_table = data.melt('month', var_name='name', value_name='value')
    return prediction_table


def category_chart(option):
    outputs = pd.read_csv(option_category[option])
    alt.data_transformers.disable_max_rows()
    data = pd.DataFrame({
        'category': outputs['category'].tolist(),
        'male': outputs['male_counter'].tolist(),
        'female': outputs['female_counter'].tolist(),
        'articles': outputs['number_of_articles'].tolist()
    })
    prediction_table = pd.melt(data, id_vars=['category'], value_vars=['male', 'female', 'articles'])
    return prediction_table


def pie_chart(option, month, category):
    outputs = None

    if option == 'The Times':
        outputs = pd.read_csv('data/the_times/N_' + category + '.csv')

    elif option == 'The Times Quotation Speakers':
        outputs = pd.read_csv('data/the_times/QS_' + category + '.csv')

    df = pd.DataFrame(outputs)

    male_count = df.get('male')[months.get(month) - 1]
    female_count = df.get('female')[months.get(month) - 1]
    article_count = df.get('article_count')[months.get(month) - 1]

    male_female = {'name_count': [male_count, female_count]}

    fig = px.pie(male_female, values='name_count', names=['Male', 'Female'],
                 title=f'Male-Female ratio in the \'{category}\' category in {month} 2022', height=300,
                 width=200, color='name_count', color_discrete_sequence=px.colors.qualitative.G10)
    fig.update_layout(margin=dict(l=20, r=20, t=30, b=0), )
    st.plotly_chart(fig, use_container_width=True)

    cols = st.columns([1, 1])
    with cols[1]:
        st.text(f'Article count: {article_count}')

