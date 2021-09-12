from tkinter import *
from tkinter import messagebox
import wikipedia
import json
import requests
from bs4 import BeautifulSoup
from win32com.client import Dispatch

class SearchApp:
    def __init__(self, root):
        self.root= root
        self.root.title('Search App | Developed by Abhishek | Alpha')
        # geometry(1350x700+x+y)
        self.root.geometry('1410x700+70+40')
        self.root.config(bg="#262626")


        Label(self.root, text='Search Application', font=('times new roman', 40, 'bold'), bg='white', fg='#262626', bd=5, relief=SUNKEN).place(x=0, y=0, relwidth=1)

        Label(self.root, text='Enter to search', font=('times new roman', 30, 'bold'), bg='#262626', fg='white').place(x=10, y=100)

        self.textVar= StringVar()
        Entry(self.root, font=('times new roman', 22, 'bold'), bg='lightyellow', textvariable=self.textVar).place(x=300, y=110)

        Button(self.root, text='Search', command=self.searcher, font=('times new roman', 22, 'bold'), bg='lightyellow', fg='#262626',cursor='hand2').place(x=630, y=108, height=39, width=135)
        Button(self.root, text='Meaning', command=self.meaning, font=('times new roman', 22, 'bold'), bg='lightyellow', fg='#262626',cursor='hand2').place(x=789, y=108, height=39, width=135)
        Button(self.root, text='Clear', command=self.clear, font=('times new roman', 22, 'bold'), bg='lightyellow', fg='#262626',cursor='hand2').place(x=950, y=108, height=39, width=135)
        Button(self.root, text='Enable', command=self.enable, font=('times new roman', 22, 'bold'), bg='lightyellow', fg='#262626',cursor='hand2').place(x=1110, y=108, height=39, width=135)
        Button(self.root, text='Disable', command=self.disable, font=('times new roman', 22, 'bold'), bg='lightyellow', fg='#262626',cursor='hand2').place(x=1263, y=108, height=39, width=135)

        self.labelMode= Label(self.root, text='MODE :',  font=('times new roman', 15, 'bold'), bg='#262626', fg='yellow')
        self.labelMode.place(x=20, y=270)

        frame1= Frame(self.root, bd=2, relief=RIDGE)
        frame1.place(x=10, y=189, width=1390, height=499)
       

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
    

    def meaning(self):
        if self.textVar.get() == "":
            messagebox.showerror('Error', 'Search Area should not be empty !')
        else:
            word= self.textVar.get()

            url=f"https://www.lexico.com/definition/{word}"
            web= requests.get(url)

            soup=BeautifulSoup(web.content,'html.parser')

            tag=soup.find_all('span','ind')
            tag2=soup.find_all('div','ex')
           

            self.meaning=""
            example=""
           
            for phrase1 in tag:
                self.meaning= self.meaning + phrase1.text + '\n'

            for phrase2 in tag2:
                example= example + phrase2.text + "\n"
            
            # displaying data on the white space
            string= f"\t\t\t\t\t\t\tWord : {word}\n\nMeaning :\n\n {self.meaning}\n\t\t\t\t\t\t****************************\n Some Examlpes Related To {word} :\n\n {example} "
            self.text_area.insert('1.0', string)
                
    def speak(self):
        speak = Dispatch("SAPI.Spvoice")
        string= self.fetchData
        if string != " ":
            speak.speak(string) 
       
            
            

# Creating object
root= Tk()
obj= SearchApp(root)
root.mainloop()