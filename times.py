from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz
from time import strftime
from PIL import Image, ImageTk
import json

root = Tk()
root.title('Météo MAKOULE')
root.geometry('950x550+300+200')
root.configure(bg='#57adff')
root.resizable(False, False)


def getWeather():
    city = textfield.get()
    geolocator = Nominatim(user_agent='geoapiExercise')
    location = geolocator.geocode(city)
    obj = TimezoneFinder()

    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
    timezone.config(text=result)
    long_lat.config(text=f'{round(location.latitude, 4)}°N, {round(location.longitude, 4)}°E')

    home = pytz.timezone(result)
    local_time = datetime.now(home)
    current_time = local_time.strftime('%I:%M %p')
    clock.config(text=current_time)

    ##weather
    api_key = '8f22b840c4bfbd4902cb0e8637241236'
    #api = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"
    #api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&exclude=hourly"
    #api = f"http://api.openweathermap.org/data/2.5/weather?lat={location.latitude}&lon={location.longitude}&units=metric&appid={api_key}"
    api = f'https://api.openweathermap.org/data/2.5/weather?lat=' + str(location.latitude) + '&lon=' + str(location.longitude) + f'&units=metric&exclude=hourly&appid={api_key}'
    #json_data = requests.get(api).json()
        # Effectue une requête GET à l'API OpenWeatherMap
    response = requests.get(api)
    data = response.json()



    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    pressure = data["main"]["pressure"]
    wind = data["wind"]["speed"]
    description = data["weather"][0]["description"]

    t.config(text=(temp, '°C'))
    h.config(text=(humidity, '%'))
    p.config(text=(pressure, 'hPa'))
    w.config(text=(wind, 'm/s'))
    d.config(text=description)


    #######first cell
    firstdayimage = data['weather'][0]['icon']

    photo1 = ImageTk.PhotoImage(file=f'icon/{firstdayimage}@2x.png')
    firstimage.config(image=photo1)
    firstimage.image = photo1

    tempday1 = data['main']['temp']
    day1temp.config(text=f'Day:{tempday1}')



    ######second cell
    secondayimage = data['weather'][0]['icon']

    img = (Image.open(f'icon/{secondayimage}@2x.png'))
    resized_image = img.resize((50, 50))
    photo2 = ImageTk.PhotoImage(resized_image)
    secondimage.config(image=photo2)
    secondimage.image = photo2

    tempday2 = data['main']['temp']
    day2temp.config(text=f'Day:{tempday2}')


    #######third cell
    thridayimage = data['weather'][0]['icon']

    img = (Image.open(f'icon/{thridayimage}@2x.png'))
    resized_image = img.resize((50, 50))
    photo3 = ImageTk.PhotoImage(resized_image)
    trirdimage.config(image=photo3)
    trirdimage.image = photo3

    tempday3 = data['main']['temp']
    day3temp.config(text=f'Day:{tempday3}')



    #######fift cell
    fiftdayimage = data['weather'][0]['icon']

    img = (Image.open(f'icon/{fiftdayimage}@2x.png'))
    resized_image = img.resize((50, 50))
    photo4 = ImageTk.PhotoImage(resized_image)
    fiftimage.config(image=photo4)
    fiftimage.image = photo4

    tempday4 = data['main']['temp']
    day4temp.config(text=f'Day:{tempday4}')


    ########sixth cell
    sixthdayimage = data['weather'][0]['icon']

    img = (Image.open(f'icon/{sixthdayimage}@2x.png'))
    resized_image = img.resize((50, 50))
    photo5 = ImageTk.PhotoImage(resized_image)
    sixthimage.config(image=photo5)
    sixthimage.image = photo5

    tempday5 = data['main']['temp']
    day5temp.config(text=f'Day:{tempday5}')


    #########seventh cell
    seventhdayimage = data['weather'][0]['icon']

    img = (Image.open(f'icon/{seventhdayimage}@2x.png'))
    resized_image = img.resize((50, 50))
    photo6 = ImageTk.PhotoImage(resized_image)
    seventhimage.config(image=photo6)
    seventhimage.image = photo6

    tempday6 = data['main']['temp']
    day6temp.config(text=f'Day:{tempday6}')



    ############seven cell
    sevendayimage = data['weather'][0]['icon']

    img = (Image.open(f'icon/{sevendayimage}@2x.png'))
    resized_image = img.resize((50, 50))
    photo7 = ImageTk.PhotoImage(resized_image)
    sevenimage.config(image=photo7)
    sevenimage.image = photo7

    tempday7 = data['main']['temp']
    day7temp.config(text=f'Day:{tempday7}')




    # days
    first = datetime.now()
    day1.config(text=first.strftime('%A'))

    second = first+timedelta(days=1)
    day2.config(text=second.strftime("%A"))

    trird = first+timedelta(days=2)
    day3.config(text=trird.strftime("%A"))

    fift = first+timedelta(days=3)
    day4.config(text=fift.strftime("%A"))

    sixth = first+timedelta(days=4)
    day5.config(text=sixth.strftime("%A"))

    seventh = first+timedelta(days=5)
    day6.config(text=seventh.strftime("%A"))

    seven = first+timedelta(days=6)
    day7.config(text=seven.strftime("%A"))



##icon
image_icon = PhotoImage(file='Images/logo.png')
root.iconphoto(False, image_icon)

Round_box = PhotoImage(file='Images/Rounded Rectangle 1.png')
Label(root, image=Round_box, bg='#57adff').place(x=30, y=110)

# label
label1 = Label(root, text='Température', font=('Times New Roman', 12), fg='white', bg='#203243')
label1.place(x=50, y=120)

label2 = Label(root, text='Humidité', font=('Times New Roman', 12), fg='white', bg='#203243')
label2.place(x=50, y=140)

label3 = Label(root, text='Préssion', font=('Times New Roman', 12), fg='white', bg='#203243')
label3.place(x=50, y=160)

label4 = Label(root, text='Vitesse du Vent', font=('Times New Roman', 12), fg='white', bg='#203243')
label4.place(x=50, y=180)

label5 = Label(root, text='Description', font=('Times New Roman', 12), fg='white', bg='#203243')
label5.place(x=50, y=200)

# search box
search_image = PhotoImage(file='Images/Rounded Rectangle 3.png')
myimage = Label(image=search_image, bg='#57adff')
myimage.place(x=275, y=120)

weat_image = PhotoImage(file='Images/Layer 7.png')
weatherimage = Label(root, image=weat_image, bg='#203243')
weatherimage.place(x=290, y=127)

textfield = tk.Entry(root, justify='center', width=15, font=('poppins', 25, 'bold'), bg='#203243', border=0, fg='white')
textfield.place(x=370, y=130)
textfield.focus()

search_icon = PhotoImage(file='Images/Layer 6.png')
myimage_icon = Button(image=search_icon, borderwidth=0, cursor='hand2', bg='#203243', command=getWeather)
myimage_icon.place(x=645, y=125)

######Bottom box
frame = Frame(root, width=1000, height=180, bg='#203243')
frame.pack(side=BOTTOM)

###bottom boxes
firstbox = PhotoImage(file='Images/Rounded Rectangle 2.png')
secondbox = PhotoImage(file='Images/Rounded Rectangle 2 copy.png')

Label(frame, image=firstbox, bg='#203243').place(x=40, y=20)
Label(frame, image=secondbox, bg='#203243').place(x=310, y=30)
Label(frame, image=secondbox, bg='#203243').place(x=410, y=30)
Label(frame, image=secondbox, bg='#203243').place(x=510, y=30)
Label(frame, image=secondbox, bg='#203243').place(x=610, y=30)
Label(frame, image=secondbox, bg='#203243').place(x=710, y=30)
Label(frame, image=secondbox, bg='#203243').place(x=810, y=30)

###clock (here we will place time)
clock = Label(root, font=('Times New Roman', 30, 'bold'), fg='white', bg='#57adff')
clock.place(x=30, y=20)

##############################################

class Horloge(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Horloge")

        self.label_heure = tk.Label(root, font=('Times New Roman', 30, 'bold'), fg='white', bg='#57adff')
        self.label_heure.pack(anchor='center')

        # Appeler la fonction pour mettre à jour l'heure en temps réel
        self.actualiser_heure()

    def actualiser_heure(self):
        heure_actuelle = strftime('%H:%M:%S %p')  # Format de l'heure
        self.label_heure['text'] = heure_actuelle
        self.after(1000, self.actualiser_heure)  # Actualiser toutes les secondes


################################################


# timezone
timezone = Label(root, font=('Times New Roman', 25), fg='white', bg='#57adff')
timezone.place(x=650, y=20)

long_lat = Label(root, font=('Times New Roman', 15), fg='white', bg='#57adff')
long_lat.place(x=650, y=60)

# thpwd
t = Label(root, font=('Times New Roman', 12), bg='#203243', fg='white')
t.place(x=150, y=120)

h = Label(root, font=('Times New Roman', 12), bg='#203243', fg='white')
h.place(x=150, y=140)

p = Label(root, font=('Times New Roman', 12), bg='#203243', fg='white')
p.place(x=150, y=160)

w = Label(root, font=('Times New Roman', 12), bg='#203243', fg='white')
w.place(x=150, y=180)

d = Label(root, font=('Times New Roman', 12), bg='#203243', fg='white')
d.place(x=150, y=200)




# first cell
firstframe = Frame(root, width=230, height=132, bg='#282829')
firstframe.place(x=45, y=395)

day1 = Label(firstframe, font='arial 15', bg='#282829', fg='#fff')
day1.place(x=108, y=5)

firstimage = Label(firstframe, bg='#282829')
firstimage.place(x=1, y=15)

day1temp = Label(firstframe, bg='#282829', fg='#fff', font='Castellar 15 bold')
day1temp.place(x=100, y=60)


# second cell
secondframe = Frame(root, width=71, height=115, bg='#282829')
secondframe.place(x=315, y=405)

day2 = Label(secondframe, bg='#282829', fg='#fff')
day2.place(x=8, y=3)

secondimage = Label(secondframe, bg='#282829')
secondimage.place(x=7, y=20)

day2temp = Label(secondframe, bg='#282829',fg='#fff')
day2temp.place(x=10, y=70)



# trird cell
trirdframe = Frame(root, width=71, height=115, bg='#282829')
trirdframe.place(x=415, y=405)

day3 = Label(trirdframe, bg='#282829', fg='#fff')
day3.place(x=8, y=3)

trirdimage = Label(trirdframe, bg='#282829')
trirdimage.place(x=7, y=20)

day3temp = Label(trirdframe, bg='#282829',fg='#fff')
day3temp.place(x=10, y=70)



# fift cell
fiftframe = Frame(root, width=71, height=115, bg='#282829')
fiftframe.place(x=515, y=405)

day4 = Label(fiftframe, bg='#282829', fg='#fff')
day4.place(x=8, y=3)

fiftimage = Label(fiftframe, bg='#282829')
fiftimage.place(x=7, y=20)

day4temp = Label(fiftframe, bg='#282829',fg='#fff')
day4temp.place(x=10, y=70)



# sixth cell
sixthframe = Frame(root, width=71, height=115, bg='#282829')
sixthframe.place(x=615, y=405)

day5 = Label(sixthframe, bg='#282829', fg='#fff')
day5.place(x=8, y=3)

sixthimage = Label(sixthframe, bg='#282829')
sixthimage.place(x=7, y=20)

day5temp = Label(sixthframe, bg='#282829',fg='#fff')
day5temp.place(x=10, y=70)



# seventh cell
seventhframe = Frame(root, width=71, height=115, bg='#282829')
seventhframe.place(x=715, y=405)

day6 = Label(seventhframe, bg='#282829', fg='#fff')
day6.place(x=8, y=3)

seventhimage = Label(seventhframe, bg='#282829')
seventhimage.place(x=7, y=20)

day6temp = Label(seventhframe, bg='#282829',fg='#fff')
day6temp.place(x=10, y=70)



# seven cell
sevenframe = Frame(root, width=71, height=115, bg='#282829')
sevenframe.place(x=815, y=405)

day7 = Label(sevenframe, bg='#282829', fg='#fff')
day7.place(x=8, y=3)

sevenimage = Label(sevenframe, bg='#282829')
sevenimage.place(x=7, y=20)

day7temp = Label(sevenframe, bg='#282829',fg='#fff')
day7temp.place(x=10, y=70)





app = Horloge()
root.mainloop()
