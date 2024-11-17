from tkinter import *
from tkinter import ttk
import requests


def getData():
    
    try:
        city = city_name.get()
        data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=53253871e463a9dcccda7142ffe6266b").json()

        climate_label1.config(text=": "+data["weather"][0]["main"]) 
        w_label1.config(text=": "+data["weather"][0]["description"])
        temp_label1.config(text=": "+str(int(data["main"]["temp"]-273.15))+"℃")    
        p_label.config(text=": "+str(data["main"]["pressure"])+" hPa")
    
    except Exception as e:
        
        climate_label1.config(text=": Not Found")
        w_label1.config(text=": Not Found")
        temp_label1.config(text=": Not Found")    
        p_label.config(text=": Not Found")
        






myColor = '#7bc7dd'

win = Tk()
win.title("Weather project")
win.config(background=myColor)
win.geometry("500x600")  

name_label = Label(win , text="Weather App",
    font=("Arial", 30, "bold"))

name_label.place(x=25, y=50,height=70 , width=450)


list_name = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]



city_name = StringVar()
com = ttk.Combobox(win , text="Weather App",
    font=("Time New Roman", 15, "bold"),
    values=list_name , textvariable=city_name)

com.place(x=25 , y=150 , height=50 , width=450)



climate_label = Label(win , text="Climate",
    font=("Arial", 10, "bold"))
climate_label.place(x=25 , y=280 , height=40 , width=100)
climate_label1 = Label(win , text="",
    font=("Arial", 10, "bold"))
climate_label1.place(x=100 , y=280 , height=40 , width=100)


w_label = Label(win , text="Description",
    font=("Arial", 10, "bold"))
w_label.place(x=25 , y=340 , height=40 , width=120)
w_label1 = Label(win , text="",
    font=("Arial", 10, "bold"))
w_label1.place(x=120 , y=340 , height=40 , width=130)


temp_label = Label(win , text="Temperature",
    font=("Arial", 10, "bold"))
temp_label.place(x=25 , y=400 , height=40 , width=120)
temp_label1 = Label(win , text="",
    font=("Arial", 10, "bold"))
temp_label1.place(x=130 , y=400 , height=40 , width=90)


p_label = Label(win , text="Pressure",
    font=("Arial", 10, "bold"))
p_label.place(x=25 , y=460 , height=40 , width=100)
p_label = Label(win , text="",
    font=("Arial", 10, "bold"))
p_label.place(x=100 , y=460 , height=40 , width=80)


done_button = Button(win , text="Done",
    font=("Arial", 15, "bold"), command=getData)

done_button.place(x=200 , y=230 , height=30 , width=100)
win.mainloop()