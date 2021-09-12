import requests
from bs4 import BeautifulSoup
word = 'acquire'

# url = f"https://www.lexico.com/definition/{word}"
url = f"https://www.lexico.com/"
web = requests.get(url)
soup = BeautifulSoup(web.content, 'html.parser')
# tag=soup.find_all('span','syn') #synonyms
# tag = soup.find_all('li', 'ex')   # More example
# tag=soup.find_all('span','ind')
# tag=soup.find_all('span','pos') #verb
# tag=soup.find_all('div','senseInnerWrapper') #origin
# tag2 = soup.find_all('div', 'ex')
tag2 = soup.find('ol', 'words_section').find_all('li')
# <div class="senseInnerWrapper"


me=[]
for phrase1 in tag2:
    # meaning= meaning + phrase1.text[1:] + '\n'
    # meaning= meaning + phrase1.text
    # meaning = meaning + phrase1.text[1:] + '\n'
    # print(type(phrase1))
    # meaning= phrase1.text + '\n'
 
    me.append(phrase1.text)
print(me)
        
# print(tag)
# print(meaning[4:8])

# <span class="syn">, adult male, gentleman</span>
# <strong class="syn">male</strong>

# <ol class = "words_section" > <li > <a data-behaviour = "ga-event-trending-words" data-value = "word 1"
#  href = "/definition/next_best" > next best < /a > </li > <li > <a data-behaviour = "ga-event-trending-words"
#   data-value = "word 2" href = "/definition/combuster" > combuster < /a > </li > <li > 
#   <a data-behaviour = "ga-event-trending-words" data-value = "word 3" href = "/definition/ashanti" >
#    Ashanti < /a > </li > <li > <a data-behaviour = "ga-event-trending-words" data-value = "word 4" 
#    href = "/definition/white_flight" > white flight < /a > </li > <li > <a data-behaviour = "ga-event-trending-words"
#     data-value = "word 5" href = "/definition/ju-jitsu" > ju-jitsu < /a > </li > </ol >

# mssg = "The National Academies of Sciences, Engineering, and Medicine determined that an adequate dailyfluid\
# intake is: About 15.5 cups(3.7 liters) of fluids for men. About 11.5 cups(2.7 liters) of fluids a day for women."


# def notifyMe():
#     notification.notify(
#         title='Please Drink Water',
#         message=mssg,
#         app_icon='glass.ico',  # Here for ico file accepted
#         timeout=4

#     )


# title='Cases of covid-19'
# message=f"{datalist[1]} \nTotal confirmed cases : {datalist[2]} \nCured/Discharge : {datalist[3]} \nDeath : {datalist[3]}"
# notifyme(title,message)



                    
# # To make notification bar
# def notifyme(title,message):
#     """it gives the notification bar below in taskbar"""
#     notification.notify(
#         title=title,
#         message=message,
#         app_icon=None, # png to ico converter
#         timeout=5  # 3 seconds tk notification rhe gi
#     )