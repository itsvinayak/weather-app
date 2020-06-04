from tkinter import *
import json
import requests
import os
import threading
HEIGHT=400
WIDTH=800


############################# function #####################################################################

def weather(city):
    key='48a90ac42caa09f90dcaeee4096b9e53'
    #print('Please Wait')
    show['text'] = 'Please wait . . . .'
    try:
        source=requests.get('http://api.openweathermap.org/data/2.5/weather?q=' + city +'&appid='+key)
        data=source.json()
    except:
        show['text'] = "Error ! \nPlease try again"
        return

    a = "name : "+data['name']+'\n'
    b="description : "+data['weather'][0]['description']+'\n'
    c = "coordinate : "+str(data['coord']['lon'])+" , "+str(data['coord']['lat'])+'\n'
    d = "temp : " + str(data['main']['temp'])+'k'+" \npressure : "+str(data['main']['pressure'])+" \nhumidity : "+str(data['main']['humidity'])

    show['text']=a+b+c+d
    return

def start_thread():
    threading.Thread(target=lambda:weather(entry.get())).start()

############################################################################################################

root=Tk()


root.title("weather")
root.configure(background="black")



#################### menu ##################################

m = Menu(root)
menubar = Menu(m, tearoff=0)
menubar.add_command(label="Home",command = '')
menubar.add_command(label="about",command = '')
menubar.add_command(label="exit",command = root.destroy)

root.config(menu=menubar)


#########################################################


################################ window 1 ###################################

canvas = Canvas(root,height=HEIGHT,width=WIDTH).pack()

background_img = PhotoImage(file=os.path.join(os.path.dirname(__file__) ,"pic.png"))
Label(root,image=background_img).place(relx=0,rely=0,relwidth=1,relheight=1)

upper_frame = Frame(root,bg='white')
upper_frame.place(relx=0.5,rely=0.1,relwidth=0.75,relheight=0.1,anchor="n")

entry=Entry(upper_frame,bg="white",bd=0)
entry.place(relx=0,rely=0,relwidth=0.7,relheight=1)
Button(upper_frame,text="search",font=40,bd=0,bg="#f2f2f2",command=start_thread).place(relx=0.7,rely=0,relwidth=0.30,relheight=1)

lower_frame=Frame(root,bg="black",bd=3)
lower_frame.place(relx=0.5,rely=0.3,relwidth=0.75,relheight=0.65,anchor="n")
show=Label(lower_frame,bg="#f2f2f2",font=40,)
show.place(relx=0,rely=0,relwidth=1,relheight=1)

#####################################################################


root.mainloop()
