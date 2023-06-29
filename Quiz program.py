from tkinter import *
from tkinter import ttk
from tkinter import messagebox

mainfontstyle = ("Helvetica", 10, "bold")
#Background image of main interface
def background_image():
    global window, bg
    bg = PhotoImage(file="Image_Folder/Main Image/mainbackground.png")
    background_image = Label(window, image=bg)
    background_image.place(x=0, y=0, relwidth=1, relheight=1)


#Creating main interface labels for each different categories
def main_interface_label():
    global window, bg
    Behavior_Label = Label(window, text="Behavior", height= 2, width=18, bg = "black", fg= "white", 
    font = mainfontstyle).place(x=60, y=225)
    Emergencies_Label = Label(window, text=" Emergencies", height= 2, width=20, bg = "black", fg= "white", 
    font = mainfontstyle).place(x=370, y=225)
    Intersection_Label = Label(window, text="Intersection", height= 2, width=20, bg = "black", fg= "white", 
    font = mainfontstyle).place(x=680, y=225)
    Parking_Label = Label(window, text="Parking", height= 2, width=20, bg = "black", fg= "white", 
    font = mainfontstyle).place(x=60, y=507)
    Road_Positions_Label = Label(window, text="Road Positions", height= 2, width=20, bg = "black", fg= "white", 
    font = mainfontstyle).place(x=370, y=507)
    Sign_label = Label(window, text="Sign", height= 2, width=20, bg = "black", fg= "white", 
    font = mainfontstyle).place(x=680, y=507)
    Timelimit_label = Button(window, text="Time limit on / off", height= 5, width=20, bg = "black", fg= "white", 
    font = mainfontstyle).place(x=1150, y=100)
    RandomQuestion_label = Button(window, text="Random 10 Questions", height= 5, width=20, bg = "black", fg= "white", 
    font = mainfontstyle).place(x=1150, y=200)

#Creating main interface image (that acts as a button) for each different categories
def main_interface_image():
    global behavior_picture, window, Emergency_picture, Parking_picture, Intersection_picture, Road_Position_picture, Sign_picture, ExitIcon_picture
    behavior_picture = PhotoImage(file="Image_Folder/Main Image/Behaviormainpic.png").subsample(1,1)
    Photo_behavior_picture_label =Button(window, image= behavior_picture, text="Behavior", relief="solid", bg= "black", activebackground="#f6f3a2", height = 187, width = 280)
    Photo_behavior_picture_label.place(x=60, y=70)
    Emergency_picture = PhotoImage(file="Image_Folder/Main Image/Emergencymainpic.png").subsample(1,1)
    Photo_Emergency_picture_label = Button(window, image= Emergency_picture, text="Emergency", relief="solid", bg= "black", activebackground="#f6f3a2", height = 187, width = 280)
    Photo_Emergency_picture_label.place(x=370, y=70)
    Intersection_picture = PhotoImage(file="Image_Folder/Main Image/Intersectionmainpic.png").subsample(1,1)
    Photo_Intersection_picture_label = Button(window, image= Intersection_picture, text="Intersection", relief="solid", bg= "black", activebackground="#f6f3a2", height = 187, width = 280)
    Photo_Intersection_picture_label.place(x=680, y=70)
    Parking_picture = PhotoImage(file="Image_Folder/Main Image/Parkingmainpic.png").subsample(1,1)
    Photo_Parking_picture_label = Button(window, image= Parking_picture, text="Parking", relief="solid", bg= "black", activebackground="#f6f3a2", height = 187, width = 280)
    Photo_Parking_picture_label.place(x=60, y=350)
    Road_Position_picture = PhotoImage(file="Image_Folder/Main Image/Road_Positionmainpic.png").subsample(1,1)
    Photo_Road_Position_picture_label = Button(window, image= Road_Position_picture, text="Road_position", relief="solid", bg= "black", activebackground="#f6f3a2", height = 187, width = 280)
    Photo_Road_Position_picture_label.place(x=370, y=350)
    Sign_picture = PhotoImage(file="Image_Folder/Main Image/Signmainpic.png").subsample(1,1)
    Photo_Sign_picture_label = Button(window, image= Sign_picture, text="Sign", relief="solid", bg= "black", activebackground="#f6f3a2", height = 187, width = 280)
    Photo_Sign_picture_label.place(x=680, y=350)
    ExitIcon_picture = PhotoImage(file="Image_Folder/Main Image/ExitIcon.png").subsample(4,4)
    Photo_ExitIcon_picture_label = Button(window, image= ExitIcon_picture, text="Sign", command = Exit)
    Photo_ExitIcon_picture_label.place(x=1197, y=500)

#Exit interface once exit icon has clicked (it asks user if there are sure)
def Exit():
    global window, status
    status = messagebox.askyesno(title = "", message = "You sure?")
    if status == True:
        window.destroy()
    else:
        pass

# Main function to create a window
def Main():
    global window
    window = Tk()
    window.geometry("1350x679")
    background_image()
    main_interface_image()
    main_interface_label()
    window.mainloop()
    
Main()
