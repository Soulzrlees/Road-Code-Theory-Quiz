from tkinter import *
from tkinter import ttk

#Background image of main interface
def background_image():
    global root, bg
    bg = PhotoImage(file="Image_Folder/Main Image/mainbackground.png")
    background_image = Label(root, image=bg)
    background_image.place(x=0, y=0, relwidth=1, relheight=1)

#Creating main interface labels for each different categories
def main_interface_label():
    global root, bg
    Behavior_Label = Label(root, text="Behavior", height= 2, width=18).place(x=100, y=220)
    Emergencies_Label = Label(root, text=" Emergencies", height= 2, width=20).place(x=400, y=220)
    Intersection_Label = Label(root, text="Intersection", height= 2, width=20).place(x=700, y=220)
    Parking_Label = Label(root, text="Parking", height= 2, width=20).place(x=100, y=500)
    Road_Positions_Label = Label(root, text="Road Positions", height= 2, width=20).place(x=400, y=500)
    Sign_label = Label(root, text="Sign", height= 2, width=20).place(x=700, y=500)
    Timelimit_label = Button(root, text="Time limit on / off", height= 2, width=20).place(x=1150, y=250)
    RandomQuestion_label = Button(root, text="Random 10 Questions", height= 2, width=20).place(x=1150, y=400)

#Creating main interface image (that acts as a button) for each different categories
def main_interface_image():
    global behavior_picture, root, Emergency_picture, Parking_picture, Intersection_picture, Road_Position_picture, Sign_picture
    behavior_picture = PhotoImage(file="Image_Folder/Main Image/Behaviormainpic.png").subsample(1,1)
    Photo_behavior_picture_label =Button(root, image= behavior_picture, text="Behavior")
    Photo_behavior_picture_label.place(x=99, y=70)
    Emergency_picture = PhotoImage(file="Image_Folder/Main Image/Emergencymainpic.png").subsample(1,1)
    Photo_Emergency_picture_label = Button(root, image= Emergency_picture, text="Emergency")
    Photo_Emergency_picture_label.place(x=400, y=70)
    Intersection_picture = PhotoImage(file="Image_Folder/Main Image/Intersectionmainpic.png").subsample(1,1)
    Photo_Intersection_picture_label = Button(root, image= Intersection_picture, text="Intersection")
    Photo_Intersection_picture_label.place(x=700, y=70)
    Parking_picture = PhotoImage(file="Image_Folder/Main Image/Parkingmainpic.png").subsample(1,1)
    Photo_Parking_picture_label = Button(root, image= Parking_picture, text="Parking")
    Photo_Parking_picture_label.place(x=99, y=350)
    Road_Position_picture = PhotoImage(file="Image_Folder/Main Image/Road_Positionmainpic.png").subsample(1,1)
    Photo_Road_Position_picture_label = Button(root, image= Road_Position_picture, text="Road_position")
    Photo_Road_Position_picture_label.place(x=400, y=350)
    Sign_picture = PhotoImage(file="Image_Folder/Main Image/Signmainpic.png").subsample(1,1)
    Photo_Sign_picture_label = Button(root, image= Sign_picture, text="Sign")
    Photo_Sign_picture_label.place(x=700, y=350)
    
    
# Main function to create a window
def Main():
    global root
    root = Tk()
    root.geometry("1350x679")
    background_image()
    main_interface_image()
    main_interface_label()
    root.mainloop()
    
Main()
