from tkinter import *
from tkinter import messagebox
import wikipedia
import json
import requests
from bs4 import BeautifulSoup
from win32com.client import Dispatch
import time
from plyer import notification

# Created by Abhishek singh
class SearchApp:
    def __init__(self, root):
        self.root= root
        self.root.title('Search App | Developed by Abhishek | Alpha')
        # geometry(1350x700+x+y)
        self.root.geometry('1410x780+70+10')
        # self.root.geometry('1410x700+70+40')
        self.root.config(bg="#262626")
        self.trendingWords()
       

        Label(self.root, text='Search Application', font=('times new roman', 40, 'bold'), bg='white', fg='#262626', bd=5, relief=SUNKEN).place(x=0, y=0, relwidth=1)

        # Label(self.root, text='Enter to search', font=('times new roman', 30, 'bold'), bg='#262626', fg='white').place(x=10, y=90)
        Label(self.root, text='Enter to search', font=('times new roman', 30, 'bold'), bg='#262626', fg='white').place(x=420, y=90)

        self.textVar= StringVar()
        Entry(self.root, font=('times new roman', 22, 'bold'), bg='lightyellow', textvariable=self.textVar).place(x=720, y=100)
        
        frame_for_button= Frame(self.root, bd=2, relief=RIDGE)
        frame_for_button.place(x=60, y=155, width=1290, height=72)
        # frame_for_button.place(x=10, y=155, width=1390, height=72)

        Button(frame_for_button, text='Search', command=self.searcher, font=('times new roman', 22, 'bold'), bg='#ff5722', fg='lightyellow', activebackground='#ff5722', activeforeground='blue', cursor='hand2').place(x=35, y=15, height=42, width=138)
        Button(frame_for_button, text='Meaning', command=self.meaning, font=('times new roman', 22, 'bold'), bg='#95e342', fg='lightyellow',activebackground='#95e342', activeforeground='red', cursor='hand2').place(x=215, y=15, height=42, width=138)
        Button(frame_for_button, text='Clear', command=self.clear, font=('times new roman', 22, 'bold'), bg='#e3a542', fg='lightyellow',activebackground='#e3a542', activeforeground='red', cursor='hand2').place(x=395, y=15, height=42, width=138)
        Button(frame_for_button, text='Enable', command=self.enable, font=('times new roman', 22, 'bold'), bg='#e3a542', fg='lightyellow', activebackground='#e3a542', activeforeground='red', cursor='hand2').place(x=570, y=15, height=42, width=138)
        Button(frame_for_button, text='Disable', command=self.disable, font=('times new roman', 22, 'bold'), bg='#43d1c5', fg='lightyellow',activebackground='#43d1c5', activeforeground='red', cursor='hand2').place(x=755, y=15, height=42, width=138)
        Button(frame_for_button, text='Synonyms', command=self.synonyms, font=('times new roman', 22, 'bold'), bg='#48e04a', fg='lightyellow',activebackground='#48e04a', activeforeground='red', cursor='hand2').place(x=935, y=15, height=42, width=138)
        Button(frame_for_button, text='Trending', command=self.Trending, font=('times new roman', 22, 'bold'), bg='lightpink', fg='lightyellow',activebackground='lightpink', activeforeground='red', cursor='hand2').place(x=1115, y=15, height=42, width=138)

        self.labelMode= Label(self.root, text='MODE :',  font=('times new roman', 15, 'bold'), bg='#262626', fg='yellow')
        self.labelMode.place(x=20, y=230)
        # self.labelMode.place(x=20, y=270)

        frame1= Frame(self.root, bd=2, relief=RIDGE)
        # frame1.place(x=10, y=189, width=1390, height=499)
        frame1.place(x=10, y=270, width=1390, height=499)

        scrolly= Scrollbar(frame1, orient=VERTICAL)
        scrolly.pack(side=RIGHT, fill='y')

        self.text_area= Text(frame1, font=('times new roman', 15), yscrollcommand=scrolly)
        self.text_area.pack(fill=BOTH, expand=1)
        scrolly.config(command=self.text_area.yview)

    # Making Some Function
    def enable(self):
        self.text_area.config(state=NORMAL)
        self.labelMode.config(text='MODE : ENABLED')

    def disable(self):
        self.text_area.config(state=DISABLED)
        self.labelMode.config(text='MODE : DISABLED')
    
    def searcher(self):
        if self.textVar.get() == "":
            messagebox.showerror('Error', 'Search Area should not be empty !')
        else:
            self.fetchData= wikipedia.summary(self.textVar.get())
            self.text_area.insert('1.0', self.fetchData)

    def clear(self):
        self.textVar.set("")
        self.text_area.delete('1.0', END)
        self.labelMode.config(text="")

    def get_data_from_url(self, word):
            url=f"https://www.lexico.com/definition/{word}"
            web= requests.get(url)

            soup=BeautifulSoup(web.content,'html.parser')
            return soup
    

    def meaning(self):
        if self.textVar.get() == "":
            messagebox.showerror('Error', 'Search Area should not be empty !')
        else:
            word= self.textVar.get()
            soup=self.get_data_from_url(word)

            tag=soup.find_all('span','ind')
            tag2=soup.find_all('div','ex')
            tag3=soup.find_all('span','pos') #verb

            self.meaning=""
            example=""
            verb=""
           
            for phrase1 in tag:
                self.meaning= self.meaning + phrase1.text + '\n'

            for phrase2 in tag2:
                example= example + phrase2.text + "\n"

            for phrase3 in tag3:
                verb= verb + phrase3.text + "\n"
            
            # displaying data on the white space
            string= f"\n\t\t\t\t\t\t\tWord : {word}\n\nMeaning :\n\n {self.meaning}\n\t\t\t\t\t\t****************************\n Some Examlpes Related To {word} :\n\n {example}"
            self.text_area.insert('1.0', string)


    def synonyms(self):
        if self.textVar.get() == "":
            messagebox.showerror('Error', 'Search Area should not be empty !')
        else:
            word= self.textVar.get()
            soup=self.get_data_from_url(word)
            tag=soup.find_all('span','syn') #synonyms
            synonyms=''
            for phrase1 in tag:
                synonyms= synonyms + phrase1.text[1:] + '\n'

            string= f"\n\t\t\t\t\t\t\tSynonyms ({word}) : \n\n{synonyms}"
            self.text_area.insert('1.0', string)

    # To make notification bar
    def notifyme(self, title, message):
        """it gives the notification bar below in taskbar"""
        notification.notify(
            title=title,
            message=message,
            app_icon=None, # png to ico converter
            timeout=22  # 3 seconds tk notification rhe gi
        )

    def trendingWords(self):
        url = f"https://www.lexico.com/"
        web = requests.get(url)
        soup = BeautifulSoup(web.content, 'html.parser')
        tag2 = soup.find('ol', 'words_section').find_all('li')
        Trending_words=[]
        for phrase10 in tag2:
            # print(phrase1.text)
            # print(Trending_words)
            Trending_words.append(phrase10.text)
        title= f'Trending words'
        # mssg= f"{Trending_words[0]}\n{Trending_words[1]}\n{Trending_words[2]}\n{Trending_words[3]}\n{Trending_words[4]}"
        self.mssg= f"{Trending_words[0]}\n{Trending_words[1]}\n{Trending_words[2]}\n{Trending_words[3]}\n{Trending_words[4]}"
        self.notifyme(title, self.mssg)

    def Trending(self):
        self.text_area.insert('1.0', f'\n\nTrending Words : \n\n{self.mssg}')       

    # def speak(self):
    #     speak = Dispatch("SAPI.Spvoice")
    #     string= self.fetchData
    #     if string != " ":
    #         speak.speak(string) 
       
            
# Creating object
root= Tk()
obj= SearchApp(root)
root.mainloop()