import streamlit as st
import composing
import query_functions
st.title("Welcome to What's App Chat Analyzer")

st.image('logo2.png')

st.sidebar.markdown("## Instructions to generate the text file:")
st.sidebar.write( ":green[1. Open your what's app application on your phone.]")
st.sidebar.write(":green[2. Go to your desired chats]")
st.sidebar.write(":green[3. Tap on the three dots on right top corner.]")
st.sidebar.write(":green[4. In the dropdown menu tap on 'more' option.]")
st.sidebar.write(":green[5. Click on export chat and click on without media.]")
st.sidebar.write(":green[6. Drop the generated text file in this app using browse option below.]")
uploaded_file = st.sidebar.file_uploader("Choose the what's app chat file:",type= 'txt')
if uploaded_file is not None: 
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode("utf-8")

    df = composing.composer(data)
    #Creating a Dropdown of User names:
    names = sorted(df['user_names'].unique())
    names.insert(0,'All Members')
    
    
    user_selected=st.sidebar.selectbox('Select Group Members:',names)
    st.sidebar.write('You Selected:', user_selected)
        
    no_mes,words,media,link,count  = query_functions.fetch_data(user_selected, df)
    st.header(f'Stats of : :blue[{user_selected}]')
    st.text(" ")
    st.text(" ")
    col1,col2,col3 = st.columns(3)
    
    with col1:
        st.markdown("### Total Messages :")
        st.subheader(f':red[{no_mes}]')
    with col2:
        st.subheader("Total   words:")
        st.subheader(f':red[{words}]')
    with col3:
        st.subheader("Media   shared:")
        st.subheader(f':red[{media}]')
        
    col4,col5,col6 = st.columns(3)
    with col4:
        st.subheader("Total   links:")
        st.subheader(f':red[{link}]')
    with col5:
        st.subheader("Total   emoji:")
        st.subheader(f':red[{count}]')
    
    st.text(" ")
    st.text(" ")
    st.text(" ")
    if user_selected == 'All Members':
        plot1,plot2,num_users = query_functions.active_users(df)
        if num_users< 10:
            st.header('Most Active Users')
        else:
            st.header('Top 10 most active users')
        col1,col2 = st.columns([2,1])
        with col1:      
            st.pyplot(plot1)
        with col2:
            try:
                st.dataframe(plot2)
            except:
                st.pyplot(plot2)
    st.text(" ")
    st.text(" ")
    st.text(" ")
    
    
    ## Time analysis:
    ## Monthly
    st.header('Time Analysis')
    st.subheader('Monthly')
    year = df.year.unique().astype(str).tolist()
    year.insert(0,'All Time')
    year = st.selectbox('Select year:',year)
    st.write('You selected', year)
    
    
    fig,most_active_month,least_active_month = query_functions.monthly(user_selected, df, year)
    col1,col2 = st.columns(2)
    with col1:
        st.subheader(f'Monthly activity of: :blue[{user_selected}]')
    with col2:
        st.subheader(f'Year: {year}')
        
    try:
        st.pyplot(fig)
    except:
        try:
            st.table(fig)
        except:
            st.write(fig)
    col1,col2 = st.columns(2)
    with col1:
        st.subheader('Most talkitive month:')
        st.subheader(f'{most_active_month[0]} with {most_active_month[1]} messages')
    with col2:
        st.subheader('Least talkitive month:')
        st.subheader(f'{least_active_month[0]} with {least_active_month[1]} messages')
        
    st.text(" ")
    st.text(" ")
    st.text(" ")
    
    ## Weekly
    st.subheader('Weekly')
    col1,col2 = st.columns(2)
    with col1:
        year = df.year.unique().astype(str).tolist()
        year.insert(0,'All Time')
        year = st.selectbox('Select Year:',year)     
        st.write('You selected', year)
        if year == 'All Time':
            month = df.month.unique().astype(str).tolist()
        else:
             month = df[df['year'] == int(year)]['month'].unique().astype(str).tolist()      
        month.insert(0,'All months')
    
    with col2:     
        month = st.selectbox('Select month:',month)     
        st.write('You selected', month)
          
    fig,most_active_week,least_active_week = query_functions.weekly(user_selected, df, year,month)
    col1,col2 = st.columns(2)
    with col1:
        st.subheader(f'Weekly activity of: :blue[{user_selected}]')
    with col2:
        st.subheader(f'Year: {year}, Month: {month}')     
    try:
        st.pyplot(fig)
    except:
        try:
            st.table(fig)
        except:
            st.write(fig)
            
    col1,col2 = st.columns(2)
    with col1:
        st.subheader('Most talkitive week:')
        st.subheader(f'{most_active_week[0]} with {most_active_week[1]} messages')
    with col2:
        st.subheader('Least talkitive week:')
        st.subheader(f'{least_active_week[0]} with {least_active_week[1]} messages')

    st.text(" ")
    st.text(" ")
    st.text(" ")
    ## Most Busy Days
    st.subheader('Most Busy Days')
    col1,col2 = st.columns(2)
    with col1:
        year = df.year.unique().astype(str).tolist()
        year.insert(0,'All Time')
        year = st.selectbox('Choose Year:',year)     
        st.write('You selected', year)
        if year == 'All Time':
            month = df.month.unique().astype(str).tolist()
        else:
             month = df[df['year'] == int(year)]['month'].unique().astype(str).tolist()      
        month.insert(0,'All months')
    
    with col2:     
        month = st.selectbox('Choose month:',month)     
        st.write('You selected', month)
          
    fig = query_functions.Busy_Days(user_selected, df, year,month)
    col1,col2 = st.columns(2)
    with col1:
        st.subheader(f'Busy Days of: :blue[{user_selected}]')
    with col2:
        st.subheader(f'Year: {year}, Month: {month}')     
    try:
        st.pyplot(fig)
    except:
        try:
            st.table(fig)
        except:
            st.write(fig)
    st.text(" ")
    st.text(" ")
    st.text(" ")
    

#Hourly Act
    st.header('Day-Hour Map')
    st.markdown("**Instructions to interpret:**")
    st.markdown("This is a day-Hour heatmap.The vertical axis shows the days of week and horizontal axis shows hours in a day.The more red color a block is more messages has been sent during that day in that hour. And more blue block implies the less talk has been done during that day in that hour")
    fig  = query_functions.hourly_act(user_selected, df)
    st.pyplot(fig)
   
     
    # Word Counts:
    st.text(" ")
    st.text(" ")
    st.text(" ")
    
    word_count = query_functions.most_common_words(user_selected,df)
    st.header(f'Most_Common_Words :blue[{user_selected}]')
    st.pyplot(word_count)
    
    

    
    
    # Word Cloud:
    st.text(" ")
    st.text(" ")
    st.text(" ")
    word_cloud = query_functions.wordcloud(user_selected, df)
    st.header(f'Word Cloud :blue[{user_selected}]')
    st.pyplot(word_cloud)
   
    
    # Emoji Counts:
    st.text(" ")
    st.text(" ")
    st.text(" ")
    emoji_df = query_functions.emoji_analysis(user_selected, df)
    st.header(f'Top 10 emoji used by :blue[{user_selected}]')
    st.dataframe(emoji_df)