import altair as alt
import numpy as np
import pandas as pd


def monthly_chart(option):
    outputs = pd.read_csv('data/wsj_names_monthly.csv')
    data = pd.DataFrame({
        'month': outputs['month'].tolist(),
        'male': outputs['male_counter'].tolist(),
        'female': outputs['female_counter'].tolist(),
        'articles': outputs['number_of_articles'].tolist()
    }, columns=['month', 'male', 'female', 'articles'])
    prediction_table =  data.melt('month', var_name='name', value_name='value')
    return prediction_table


def category_chart(option):
    outputs = pd.read_csv('data/wsj_names_category.csv')
    alt.data_transformers.disable_max_rows()
    data = pd.DataFrame({
        'category': outputs['category'].tolist(),
        'male': outputs['male_counter'].tolist(),
        'female': outputs['female_counter'].tolist(),
        'articles': outputs['number_of_articles'].tolist()
    })
    prediction_table = pd.melt(data, id_vars=['category'], value_vars=['male', 'female', 'articles'])
    return prediction_table