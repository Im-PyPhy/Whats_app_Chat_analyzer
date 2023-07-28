import re
import pandas as pd
import numpy as np

def composer(chat_data):   
    ## Extractiong date in a list
    date_pattern = '\d{1,2}.\d{1,2}.\d{2,4},\s\d{1,2}:\d{1,2}\s.m\s' #pattern for 24 hrs setting
    date = re.findall(date_pattern,chat_data)
    date
    if len(date) == 0:
        date_pattern =  '\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{1,2}\s'  #pattern for 24 hrs setting
        date = re.findall(date_pattern,chat_data)
        date 
    # Extracting messages
    chat_messages = re.split(date_pattern+'-\s',chat_data)
    chat_messages = chat_messages[1:]
    chat_messages
    ## Converting to dataFrame

    df = pd.DataFrame({'date': date, 'user_messages': chat_messages})
    df['date'] = pd.to_datetime(df['date'])
    df['date_2'] = df['date'].apply(lambda x: pd.Timestamp(x).strftime('%Y-%m-%d %H:%M:%S'))
    ## Extracting user names and creating a new column with the user name
    user_name = []
    messages = []
    
    for i,message in enumerate(df['user_messages']):
        string = message.split(':')
        if len(string)>1:
            user_name.append(string[0])
            messages.append((' '.join(string[1:]))[:-1])
        else:
            user_name.append('') ## replacing the usernames with  '' for group notification messages:
            messages.append(string[0])
    df['user_names'] = user_name
    df['messages'] = messages
    df.drop('user_messages',axis=1,inplace=True)
    
    ## Removing group notification messages
    ## These are the messages which are basically the group notifications and not actual messages and we will exclude these 
    ## from our dataframe
    
    df.drop(index=np.where(df['user_names'] == '')[0],axis=0,inplace= True)
    df.reset_index(drop=True, inplace= True)
        
    ## Extracting year,month,day,day_name,hour,minute
    df['year'] =df['date'].dt.year
    df['month'] = df['date'].dt.month_name()
    df['month_no'] = df['date'].dt.month
    df['day'] = df['date'].dt.day_name()
    df['hour'] = df['date'].dt.hour
    df['minute'] = df['date'].dt.minute  
    df['week'] = df['date_2'].apply(lambda x: pd.Timestamp(x).week)
    df['week_day_no']=df['date'].dt.weekday
    df['period'] =  df['hour'].apply(lambda x: str(x) + '-'+ str(x+1) if x!=23 else str(x)+ '-'+ str(0) )
 #   emoji_count =[]
 #   for i in df['messages']:
  #      emoji_count.append(emoji.emoji_count(i))
   # emoji_count= pd.Series(emoji_count,name='emoji_count')    
    #df = pd.concat([df,emoji_count],axis=1)
    
    return df
    
