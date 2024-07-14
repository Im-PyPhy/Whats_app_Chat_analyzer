import emoji

import pandas as pd

import re

import matplotlib.pyplot as plt

import seaborn as sns

from wordcloud import WordCloud,STOPWORDS

from collections import Counter

from urlextract import URLExtract
import streamlit as st



def fetch_data(user_selected,df):
<<<<<<< HEAD
    if user_selected != 'All Members':
=======

    if user_selected != 'All':

>>>>>>> 0654f89660535ff5362dbb4d943baab5d26dbbe7
        df = df[df['user_names'] == user_selected]

    

    

    num_messages = df.shape[0]

    # no of words:

    words2 = []

    series1 = df['messages'].str.replace('?',' ').str.replace('.',' ').str.replace(',',' ').str.replace('-',' ')

    series1 = series1[series1 != ' <Media omitted>']

    series1  = series1.apply( lambda x: emoji.replace_emoji(x,' '))

    for i in series1:

        box = i.split()

        words2.extend(box)

    # no of media Shared

    media=[]

    for i in df['messages']:

        media.extend(re.findall('<[\sa-zA-Z]+>',i))   

    # no of links shared

    extractor = URLExtract()

    links =[]

    for mes in df['messages']:

        links.extend(extractor.find_urls(mes))

    links = len(links)

    #No of emoji sent:

    count = 0

    for i in df['messages']:

        count = count+emoji.emoji_count(i)

    return num_messages, len(words2), len(media),links,count
<<<<<<< HEAD
@st.cache_data
=======

    

>>>>>>> 0654f89660535ff5362dbb4d943baab5d26dbbe7
def active_users(df):

    series2 =df['user_names'].value_counts().head(10)

    series3 =round(df['user_names'].value_counts(normalize = True).head(10)*100,2)

    plt.style.use('fivethirtyeight')

    fig,ax1 = plt.subplots()

    #fig1,ax2 = plt.subplots()

    sns.barplot(x=series2.index,y=series2.values,ax= ax1)

    for i in ax1.containers:

        ax1.bar_label(i,)

    plt.xticks(rotation='vertical')

    plt.ylabel('No of messages')

    if df['user_names'].nunique()>6:

        fig2=pd.DataFrame(data=series3).reset_index().rename(columns={'index':'User_names','user_names':'No_of_messages(%)'})

    else:

        fig2,ax2 = plt.subplots(figsize=(10,10))

        plt.pie(series2.values,labels=series2.index,autopct='%1.1f%%',rotatelabels=True)     

    return fig,fig2, df['user_names'].nunique()





## Creating WordCloud    

def wordcloud(user_selected,df):
<<<<<<< HEAD
    if user_selected != 'All Members':
=======

    if user_selected != 'All':

>>>>>>> 0654f89660535ff5362dbb4d943baab5d26dbbe7
        df = df[df['user_names'] == user_selected]

    wc = WordCloud(width=500,height=500,stopwords=STOPWORDS,min_word_length=3,background_color='white',min_font_size=10)

    cloud = wc.generate(df['messages'].str.cat(sep=''))

    fig,ax = plt.subplots()

    ax.axes.xaxis.set_ticklabels([]) ## removes the axes scale values

    ax.axes.yaxis.set_ticklabels([])

    ax.grid(False)

    ax.axis('off')

    ax.imshow(cloud)

    return fig

## Most commonly used words



def most_common_words(user_selected,df):

    
<<<<<<< HEAD
    if user_selected != 'All Members':
=======

    if user_selected != 'All':

>>>>>>> 0654f89660535ff5362dbb4d943baab5d26dbbe7
        df = df[df['user_names'] == user_selected]

    stops = open('stop_hinglish',mode='r')

    stop_words = stops.read()

    stop_words = stop_words+'h'

    words4 = []

    series1 = df['messages'].str.replace('?',' ').str.replace('.',' ').str.replace(',',' ').str.replace('-',' ')

    series1 = series1[series1 != ' <Media omitted>']

    series1 = series1[series1 != ' This message was deleted']

    series1  = series1.apply( lambda x: emoji.replace_emoji(x,' '))

    for i in series1.str.lower():

        for word in i.split():

            if word not in stop_words and len(word) >2:  

                words4.append(word)

    series1 = pd.DataFrame(Counter(words4).most_common(20)).rename(columns={0:'Words',1:'Frequency'})

    plt.style.use('fivethirtyeight')

    fig,ax1 = plt.subplots(figsize=(8,8))

    sns.barplot(y=series1['Words'],x=series1['Frequency'])

    for i in ax1.containers:

        ax1.bar_label(i,)

    return fig



## Emoji Count



def emoji_analysis(user_selected,df):
<<<<<<< HEAD
    if user_selected != 'All Members':
=======

    if user_selected != 'All':

>>>>>>> 0654f89660535ff5362dbb4d943baab5d26dbbe7
        df = df[df['user_names'] == user_selected]

    

    emojis = []

    for mes in df['messages']:

        emojis.extend([ x['emoji'] for x in emoji.emoji_list(mes)])

    emoti =pd.DataFrame(Counter(emojis).most_common(10)).rename(columns={0:'Emoji',1:'Count'})   

    return emoti



## Time Analysis:

    # Monthly

def monthly(user_selected,df,year):
<<<<<<< HEAD
    if user_selected != 'All Members':
        df = df[df['user_names'] == user_selected]
    if year !='All Time':
=======

    if user_selected != 'All':

        df = df[df['user_names'] == user_selected]

    if year !='All':

>>>>>>> 0654f89660535ff5362dbb4d943baab5d26dbbe7
        df = df[df['year'].astype(str)== year]

    monthly =pd.DataFrame(df.groupby(by = ['year','month_no','month'])['messages'].agg( ['count'])).reset_index()

    monthly['Time'] = monthly['year'].astype(str) + '-' + monthly['month']

    most_active_month = monthly.sort_values(by=['count']).tail(1)[['Time','count']].values[0].tolist()

    least_active_month = monthly.sort_values(by=['count']).head(1)[['Time','count']].values[0].tolist()

    if monthly.shape[0] >1:

        plt.style.use('fivethirtyeight')

        fig,ax = plt.subplots(figsize=(10,6))

        #plt.plot('Time', 'count', data = monthly,color = 'magenta')

        sns.lineplot(x='Time', y='count', data = monthly,color = 'magenta',ax=ax)

        plt.xticks(rotation='vertical')

        plt.ylabel('No of Messages')

        return  fig,most_active_month,least_active_month

    

    elif monthly.shape[0]==1:

        return monthly,most_active_month,least_active_month

    elif monthly.shape[0] == 0:

        return 'No Activity',most_active_month,least_active_month

    

    

      # weekly  
<<<<<<< HEAD
def weekly(user_selected,df,year,month='All months'):
    if user_selected != 'All Members':
        df = df[df['user_names'] == user_selected]
    if year !='All Time':
        df = df[df['year'].astype(str)== year]
    if month !='All months':
=======

def weekly(user_selected,df,year,month='All'):

    if user_selected != 'All':

        df = df[df['user_names'] == user_selected]

    if year !='All':

        df = df[df['year'].astype(str)== year]

    if month !='All':

>>>>>>> 0654f89660535ff5362dbb4d943baab5d26dbbe7
        df = df[df['month'].astype(str)== month]

    weekly = df.groupby(by = ['year','week'])['messages'].agg(['count']).reset_index()

    weekly['Date'] = weekly['year'].astype(str) + '- week'+ weekly['week'].astype(str)

    most_active_week= weekly.sort_values(by=['count']).tail(1)[['Date','count']].values[0].tolist()

    least_active_week = weekly.sort_values(by=['count']).head(1)[['Date','count']].values[0].tolist()

    if weekly.shape[0] >1:

        plt.style.use('seaborn')

        fig,ax = plt.subplots(figsize=(10,8))

        sns.lineplot(x='Date',y= 'count', data = weekly,color = 'magenta',ax=ax)

        plt.xticks(rotation='vertical')

        plt.ylabel('No of Messages')

        return  fig,most_active_week,least_active_week

    elif weekly.shape[0]==1:

        return weekly,most_active_week,least_active_week

    elif weekly.shape[0] == 0:

        return 'No Activity',most_active_week,least_active_week

    

    

   # Busy Days  

## Most busy days:

def Busy_Days(user_selected,df,year,month):
<<<<<<< HEAD
    if user_selected != 'All Members':
        df = df[df['user_names'] == user_selected]
    if year !='All Time':
        df = df[df['year'].astype(str)== year]
    if month !='All months':
=======

    if user_selected != 'All':

        df = df[df['user_names'] == user_selected]

    if year !='All':

        df = df[df['year'].astype(str)== year]

    if month !='All':

>>>>>>> 0654f89660535ff5362dbb4d943baab5d26dbbe7
        df = df[df['month'].astype(str)== month]

    Days= df.groupby(by = ['week_day_no','day'])['messages'].agg(['count']).reset_index()

    if Days.shape[0] >1:

        plt.style.use('seaborn')

        fig,ax = plt.subplots(figsize=(10,8))

        sns.barplot(x='day', y='count', data = Days,ax=ax)

        plt.xticks(rotation='vertical')

        plt.ylabel('No of Messages')

        for i in ax.containers:

            ax.bar_label(i)

        return  fig 

    elif Days.shape[0]==1:

        return Days

    elif Days.shape[0] == 0:

        return 'No Activity'

    

## Hourly Activity

def hourly_act(user_selected,df):
<<<<<<< HEAD
    if user_selected != 'All Members':
=======

    if user_selected != 'All':

>>>>>>> 0654f89660535ff5362dbb4d943baab5d26dbbe7
        df = df[df['user_names'] == user_selected]   

    plt.style.use('seaborn')

    fig,ax = plt.subplots(figsize=(14,6))

    sns.heatmap(df.pivot_table(values='messages',index='day',columns='period',aggfunc='count').fillna(0).astype('int32'),cmap='coolwarm')

    plt.xticks(rotation='vertical');

    return fig
