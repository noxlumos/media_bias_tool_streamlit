import altair as alt
import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st
from collections import OrderedDict

option_monthly = {"The Wall Street Journal": "data/wsj_names_monthly.csv",
                  "The Washington Post": "data/wp_names_monthly.csv",
                  "New York Times": "data/ny_times_names_monthly.csv",
                  "The Times": "data/times_names_monthly.csv",
                  "The Times Quotation Speakers": "data/times_quotation_speakers_monthly.csv"}

option_category = {"The Wall Street Journal": "data/wsj_names_category.csv",
                   "The Washington Post": "data/wp_names_category.csv",
                   "New York Times": "data/wp_names_category.csv",
                   "The Times": "data/times_names_category.csv",
                   "The Times Quotation Speakers": "data/times_quotation_speakers_category.csv"}

months = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 'July': 7, 'August': 8,
          'September': 9, 'October': 10,
          'November': 11, 'December': 12}

axis_labels = ['Jan, 2022', 'Feb, 2022', 'Mar, 2022', 'Apr, 2022', 'May, 2022', 'Jun, 2022', 'Jul, 2022',
               'Aug, 2022', 'Sep, 2022', 'Oct, 2022', 'Nov, 2022', 'Dec, 2022']

axis_labels_nyt = ['Jun, 2021', 'Jul, 2021', 'Aug, 2021', 'Sep, 2021', 'Oct, 2021', 'Nov, 2021', 'Dec, 2021',
                   'Jan, 2022', 'Feb, 2022', 'Mar, 2022', 'Apr, 2022', 'May, 2022']

the_times_categories = ['UK Politics', 'Global Politics', 'Brexit',
                        'Economy', 'Markets', 'Property', 'Personal Finance', 'Banking',
                        'Health', 'Science', 'Technology', 'Transport', 'Law',
                        'Cricket', 'Tennis', 'Rugby Union', 'Formula One', 'Golf', 'Horse Racing and Tips', 'Boxing',
                        'Winter Olympics 2022',
                        'Television', 'Film', 'Music', 'Radio & Podcasts', 'Books', 'Theatre', 'Art Reviews',
                        'Beauty', 'Food & Drink', 'Fitness & Wellbeing', 'Home Interiors', 'Gardening', 'Driving']

the_washington_post_categories = ['Opinions', 'Local', 'Sports', 'Politics', 'World', 'Lifestyle',
                                  'Entertainment', 'National', 'Business', 'Technology',
                                  'National-security', 'Health', 'Travel', 'Transportation',
                                  'Realestate', 'Elections', 'Education', 'Climate-environment', 'Public-relations',
                                  'Photography', 'News', 'Us-policy']

the_wall_street_journal_categories = ['business', 'opinion', 'world', 'markets', 'us',
                                      'books & arts', 'life & work', 'politics', 'news',
                                      'economy', 'tech', 'sports', 'style', 'real estate']

pie_chart_category = {"The Wall Street Journal": the_wall_street_journal_categories,
                      "The Washington Post": the_washington_post_categories,
                      "New York Times": the_washington_post_categories,
                      "The Times": the_times_categories}


def monthly_chart(option):
    outputs = pd.read_csv(option_monthly[option])

    if option == 'New York Times':
        data = pd.DataFrame({
            'month': axis_labels_nyt,
            'male': outputs['male_counter'].tolist(),
            'female': outputs['female_counter'].tolist(),
        }, columns=['month', 'male', 'female'])

    else:
        data = pd.DataFrame({
            'month': axis_labels,
            'male': outputs['male_counter'].tolist(),
            'female': outputs['female_counter'].tolist(),
            'number_of_articles': outputs['number_of_articles'].tolist()
        }, columns=['month', 'male', 'female', 'number_of_articles'])

    prediction_table = data.melt(id_vars=['month'], var_name='name', value_name='value',
                                 ignore_index=False)
    return prediction_table


def category_chart(option):
    outputs = pd.read_csv(option_category[option])
    alt.data_transformers.disable_max_rows()
    data = pd.DataFrame({
        'category': outputs['category'].tolist(),
        'male': outputs['male_counter'].tolist(),
        'female': outputs['female_counter'].tolist(),
        'number_of_articles': outputs['number_of_articles'].tolist()
    })
    prediction_table = pd.melt(data, id_vars=['category'], value_vars=['male', 'female', 'number_of_articles'])
    return prediction_table


columns = {"The Wall Street Journal": ['male_counter', 'female_counter', 'number_of_articles'],
           "The Washington Post": ['male_counter', 'female_counter', 'number_of_articles'],
           "New York Times": ['male_counter', 'female_counter', 'number_of_articles'],
           "The Times": ['male', 'female', 'article_count'],
           "The Times Quotation Speakers": ['male', 'female', 'article_count']}


def pie_chart(option, month, category):
    outputs = None

    if option == 'The Times':
        outputs = pd.read_csv('data/the_times/N_' + category + '.csv')

    elif option == 'The Times Quotation Speakers':
        outputs = pd.read_csv('data/the_times/QS_' + category + '.csv')

    elif option == 'The Washington Post':
        outputs = pd.read_csv('data/the_washington_post/' + category + '.csv')

    elif option == 'The Wall Street Journal':
        outputs = pd.read_csv('data/the_wall_street_journal/' + category + '.csv')

    elif option == 'New York Times':
        outputs = pd.read_csv('data/the_washington_post/' + category + '.csv')

    df = pd.DataFrame(outputs)

    male_count = df.get(columns.get(option)[0])[months.get(month) - 1]
    female_count = df.get(columns.get(option)[1])[months.get(month) - 1]
    article_count = df.get(columns.get(option)[2])[months.get(month) - 1]

    male_female = {'name_count': [male_count, female_count]}

    fig = px.pie(male_female, values='name_count', names=['Male', 'Female'],
                 title=f'{option}:  Male-Female ratio in the \'{category}\' category in {month} 2022', height=300,
                 width=200, color='name_count', color_discrete_sequence=px.colors.qualitative.G10)
    fig.update_layout(margin=dict(l=20, r=20, t=30, b=0), )
    st.plotly_chart(fig, use_container_width=True)

    cols = st.columns([1, 1])
    with cols[1]:
        st.text(f'Article count: {article_count}')
