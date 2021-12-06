import streamlit as st
import pandas as pd
import numpy as np
import plotly.figure_factory as ff
import matplotlib.pyplot as plt


@st.cache
def load_data(nrows):
    data = pd.read_csv('sentiment_predictions_NEWSHEADLINES.csv', nrows=nrows)
    return data


data_load_state = st.text('Loading data...')
weekly_data = load_data(250)

st.subheader('News headlines data visualization ')
st.write(weekly_data)

#Bar Chart
st.bar_chart(weekly_data['Positive'])
st.bar_chart(weekly_data['Negative'])
st.bar_chart(weekly_data['Neutral'])

#histogram
df2 = pd.DataFrame(weekly_data[:250], columns = ['Positive', 'Negative', 'Neutral'])
df2.hist()
plt.show()
st.pyplot()

#Line Chart
st.line_chart(weekly_data)

chart_data = pd.DataFrame(weekly_data[:250], columns=['Headline', 'Negative','Positive', 'Neutral'])
st.area_chart(chart_data)

hist_data = [weekly_data['Negative'], weekly_data['Positive']]
group_labels = ['Negative', 'Positive']
fig = ff.create_distplot(hist_data, group_labels, bin_size=[50, 100])
st.plotly_chart(fig, use_container_width=True)