# # making an model og ircts

from tkinter import*
import requests

class Yatra:
    def __init__(self):
        self.root=Tk()

        self.root.title("train route")
        self.root.minsize(400,600)
        self.root.maxsize(400,600)
        self.root.configure(background="#2ecc71")

        label1=Label(self.root,text="Train Route",bg="#2ecc71",fg="#ffffff")
        label1.configure(font=("Constantia",22,"bold"))
        label1.pack(pady=(30,10)) #geometry 

        self.train_no=Entry(self.root)
        self.train_no.pack(ipadx=40,ipady=5)

        click=Button(self.root,text="Fetch",bg="#ffffff",width=28,height=2,command=lambda:self.fetch())
        click.pack(pady=(10,20))

        self.result=Label(self.root,bg="#2ecc71",fg="#ffffff")
        self.result.configure(font=("Constantia",14))
        self.result.pack(pady=(5,10))

        self.root.mainloop()

    def fetch(self):
        train_no=self.train_no.get() #get(): give the entry value
        print(train_no)
        url="https://api.railwayapi.com/v2/route/train/{}/apikey/dykb240vi3/".format(train_no)
        response=requests.get(url)
        data=response.json()
        #print(data)
        station=""
        for i in data["route"]:
            station=station+i['station']['name']+" |"+i['scharr']+"|"+i['schdep']+"|"+str(i['distance'])+"KM"+"\n"
            
        self.result.configure(text=station)
obj=Yatra()
