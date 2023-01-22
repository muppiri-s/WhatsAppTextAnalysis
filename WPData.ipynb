WHATSAPP TEXT ANALYTICS CODE:


#Packages
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import emoji
import re
import datetime
import calendar
from wordcloud import WordCloud, STOPWORDS

#Conversion of notepad to csv ~ chat log to pandas dataframe
#Conversion of notepad to csv ~ chat log to pandas dataframe
def parse_file(text_file):
    
    # some regex to account for messages taking up multiple lines
    pat = re.compile(r'^(\d\d\/\d\d\/\d\d\d\d.*?)(?=^^\d\d\/\d\d\/\d\d\d\d|\Z)', re.S | re.M)
    with open(text_file, encoding="utf8") as f:
        data = [m.group(1).strip().replace('\n', ' ') for m in pat.finditer(f.read())]

    sender = []; message = []; date = []; time = [];
    for row in data:

        # date is before the coma
        date.append(row.split(' , ')[0])
        
        #time is between comma and dash
        try:
            t = re.search('m , (.*?) -',row).group(0)
            time.append(t)
        except:
            time.append('')

        # sender is between am/pm, dash and colon
        try:
            s = re.search('m - (.*?):', row).group(1)
            sender.append(s)
        except:
            sender.append('')

        # message content is after the first colon
        try:
            message.append(row.split(': ', 1)[1])
        except:
            message.append('')

    df = pd.DataFrame(zip(date,time, sender, message), columns=['date','time','sender', 'message'])
    #df['timestamp'] = pd.to_datetime(df.timestamp, format='%d/%m/%Y, %I:%M %p')

    # remove events not associated with a sender
    df = df[df.sender != ''].reset_index(drop=True)
    return df

df = parse_file('D:/WhatsApp Text Analytics/individual/Akhi.txt')

#Post conversion to csv
chat = pd.read_csv(r"D:/WhatsApp Text Analytics/individual/chat_with_akhi.csv")
chat.head()chat.head()

#deleting the unwanted rows and columns
del chat['Unnamed: 0']

#visualizing the data
chat.describe()

#check the data
chat.head()

#Who sent max messages and visualize
chat_msg = chat['sender'].value_counts()
chat_msg
chat_msg.plot.bar()

#Images shared between each of them
chat_media = chat[chat['message'] == '<Media omitted>']
media = chat_media['sender'].value_counts()
media

#When did the people mostly texted out with each other
time = chat['time'].apply(lambda x : x.split(':')[0])
busy_hours = time.value_counts()
busy_hours.sort_index(inplace=True)
plt.axes([1,1,1,0.98])
plt.grid(True)
busy_hours.plot.bar()
plt.xlabel('Hour')
plt.ylabel('No. of Messages')
plt.xticks(rotation=0)
plt.show()
%matplotlib inline

#deleted messages
sahithi_deleted = chat['message'].value_counts()['You deleted this message']
#Akhi_deleted = chat['message'].value_counts()['This message was deleted']
print('Sahithi deleted '+ str(sahithi_deleted) + ' messages')
#print('Akhi deleted '+ str(akhi_deleted) +' messages')

#count emojis 
def extract_emoji(columnname):
    emoji_list = []
    for word in chat:
        if any(ch in emoji.UNICODE_EMOJI for ch in word):
                emoji_list.append(word)
        
    return emoji_list

#Get the day from the respective dates 
date = pd.DataFrame({'inputDates':list(pd.date_range('12/06/2017','08/06/2020',freq='D').to_series())})
date['inputDates'] = pd.to_datetime(date['inputDates']) 
chat['day'] = date['inputDates'].dt.dayofweek 
chat['day'] = date['inputDates'].dt.day_name()
chat.head()

#Shift the last column to 3rd row
chat = chat[['date','time','day','sender','message']] #Simple method
chat.head()
#Max messages were sent on which day
max_msgDays = chat['day'].value_counts()
#print("Max messages were sent on which day",max_msgDays.plot.pie())
max_msgDays.plot.bar()

#heatmap
Index = chat['day']
Cols = chat['sender']
df = pd(abs(np.random.randn(5,4)), index=Index, columns=Cols)

plt.pcolor(df)
plt.show()

#word cloud - frequently used words
text= ''.join(chat.message.astype(str)).lower()

stopwords = set(STOPWORDS)
stopwords.update(["inka","hehe","le","aha","chepu","akhi"])
# Generate a word cloud image
wordcloud = WordCloud(stopwords=stopwords, background_color="black").generate(text)
# Display the generated image:
# the matplotlib way:

plt.figure( figsize=(10,5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
