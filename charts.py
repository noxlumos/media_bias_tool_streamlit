import altair as alt
import numpy as np
import pandas as pd

option_monthly = {"Wall Street Journal":"data/wsj_names_monthly.csv",
                  "Washington Post":"data/wp_names_monthly.csv",
                  "New York Times":"data/wp_names_monthly.csv"}

option_category = {"Wall Street Journal":"data/wsj_names_category.csv",
                   "Washington Post":"data/wp_names_category.csv",
                   "New York Times":"data/wp_names_category.csv"}
def monthly_chart(option):
    outputs = pd.read_csv(option_monthly[option])
    data = pd.DataFrame({
        'month': outputs['month'].tolist(),
        'male': outputs['male_counter'].tolist(),
        'female': outputs['female_counter'].tolist(),
        'articles': outputs['number_of_articles'].tolist()
    }, columns=['month', 'male', 'female', 'articles'])
    prediction_table =  data.melt('month', var_name='name', value_name='value')
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