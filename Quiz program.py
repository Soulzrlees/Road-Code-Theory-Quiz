from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# This function is to delete all widgets in main interface frame so that the question frame could replace it
def clear_frame():
    global main_interface_frame
    for widget in main_interface_frame.winfo_children():
        widget.destroy()
#_____________________________________________________________Main Interface_________________________________________________________
def main_interface():
    global main_interface_frame
    mainfontstyle = ("Helvetica", 10, "bold")
    main_interface_frame = Frame(window)
    main_interface_frame.pack(fill=BOTH, expand=True)

    #Background image of main interface
    def background_image():
        global window, bg, main_interface_frame
        bg = PhotoImage(file="Image_Folder/Main Image/mainbackground.png")
        background_image = Label(main_interface_frame, image=bg)
        background_image.place(x=0, y=0, relwidth=1, relheight=1)

    #Creating main interface labels for each different categories
    def main_interface_label():
        global Timelimit_OnorOff, main_interface_frame
        Behavior_Label = Label(main_interface_frame, text="Behavior", height= 2, width=18, bg = "black", fg= "white", font = mainfontstyle)
        Behavior_Label.place(x=60, y=220)

        Emergencies_Label = Label(main_interface_frame, text=" Emergencies", height= 2, width=20, bg = "black", fg= "white", font = mainfontstyle)
        Emergencies_Label.place(x=370, y=220)

        Intersection_Label = Label(main_interface_frame, text="Intersection", height= 2, width=20, bg = "black", fg= "white", font = mainfontstyle)
        Intersection_Label.place(x=680, y=220)

        Parking_Label = Label(main_interface_frame, text="Parking", height= 2, width=20, bg = "black", fg= "white", font = mainfontstyle)
        Parking_Label.place(x=60, y=500)

        Road_Positions_Label = Label(main_interface_frame, text="Road Positions", height= 2, width=20, bg = "black", fg= "white", font = mainfontstyle)
        Road_Positions_Label.place(x=370, y=500)

        Sign_label = Label(main_interface_frame, text="Sign", height= 2, width=20, bg = "black", fg= "white",font = mainfontstyle)
        Sign_label.place(x=680, y=500)

        Timelimit_OnorOff = Button(main_interface_frame, text="Time limit\n In minutes\n On / Off", height=5, width=20, bg="red", fg="white", font=mainfontstyle, bd=0, command=Timelimit_activation)
        Timelimit_OnorOff.place(x=1160, y=120)

        RandomQuestions = Button(main_interface_frame, text="Confirm number of\nRandomized Questions", height= 5, width=20, bg = "black", fg= "white", font = mainfontstyle, command=clear_frame, bd=0)
        RandomQuestions.place(x=1160, y=330)
        #Spinkbox for the user to select number of question from 15 to 30 randomize questions
        randomquestion_spinbox = Spinbox(main_interface_frame, from_=10, to=35, font = mainfontstyle, bd= 10)
        randomquestion_spinbox.place(x=1160, y=300)
        #Spinkbox for timer from 10 min to 60 mins (default 60mins)
        Timelimit_spinbox = Spinbox(main_interface_frame, from_=10, to=60, font = mainfontstyle, bd= 10)
        Timelimit_spinbox.place(x=1160, y=100)

    def Timelimit_activation():
        global Timelimit_OnorOff
        #Check the current background color of Timelimit_OnorOff
        current_bg = Timelimit_OnorOff.cget("bg")
        # Toggle the background color
        if current_bg == "green":
            Timelimit_OnorOff.config(bg="red")
        else:
            Timelimit_OnorOff.config(bg="green")

    #Creating main interface image (that acts as a button) for each different categories
    def main_interface_image():
        global behavior_picture, main_interface_frame, Emergency_picture, Parking_picture, Intersection_picture, Road_Position_picture, Sign_picture, ExitIcon_picture
        behavior_picture = PhotoImage(file="Image_Folder/Main Image/Behaviormainpic.png").subsample(1,1)
        Photo_behavior_picture_label = Button(main_interface_frame, image= behavior_picture, text="Behavior", relief="solid", bd=0, bg = "black", activebackground="white", height = 187, width = 280, command=clear_frame)
        Photo_behavior_picture_label.place(x=60, y=70)

        Emergency_picture = PhotoImage(file="Image_Folder/Main Image/Emergencymainpic.png").subsample(1,1)
        Photo_Emergency_picture_label = Button(main_interface_frame, image= Emergency_picture, text="Emergency", relief="solid", bd=0, bg= "black", activebackground="white", height = 187, width = 280, command=clear_frame)
        Photo_Emergency_picture_label.place(x=370, y=70)

        Intersection_picture = PhotoImage(file="Image_Folder/Main Image/Intersectionmainpic.png").subsample(1,1)
        Photo_Intersection_picture_label = Button(main_interface_frame, image= Intersection_picture, text="Intersection", relief="solid", bd=0, bg= "black", activebackground="white", height = 187, width = 280, command=clear_frame)
        Photo_Intersection_picture_label.place(x=680, y=70)

        Parking_picture = PhotoImage(file="Image_Folder/Main Image/Parkingmainpic.png").subsample(1,1)
        Photo_Parking_picture_label = Button(main_interface_frame, image= Parking_picture, text="Parking", relief="solid", bg= "black", bd=0, activebackground="white", height = 187, width = 280, command=clear_frame)
        Photo_Parking_picture_label.place(x=60, y=350)

        Road_Position_picture = PhotoImage(file="Image_Folder/Main Image/Road_Positionmainpic.png").subsample(1,1)
        Photo_Road_Position_picture_label = Button(main_interface_frame, image= Road_Position_picture, text="Road_position", relief="solid", bd=0, bg= "black", activebackground="white", height = 187, width = 280, command=clear_frame)
        Photo_Road_Position_picture_label.place(x=370, y=350)

        Sign_picture = PhotoImage(file="Image_Folder/Main Image/Signmainpic.png").subsample(1,1)
        Photo_Sign_picture_label = Button(main_interface_frame, image= Sign_picture, text="Sign", relief="solid", bd=0, bg= "black", activebackground="white", height = 187, width = 280, command=clear_frame)
        Photo_Sign_picture_label.place(x=680, y=350)

        ExitIcon_picture = PhotoImage(file="Image_Folder/Main Image/ExitIcon.png").subsample(4,4)
        Photo_ExitIcon_picture_label = Button(main_interface_frame, image= ExitIcon_picture, text="Sign", command = Exit, bd=0)
        Photo_ExitIcon_picture_label.place(x=1197, y=500)

    #Exit interface once exit icon has clicked (it asks user if there are sure)
    def Exit():
        global window, status
        status = messagebox.askyesno(title = "", message = "Are you sure?")
        if status == True:
            window.destroy()
        else:
            pass

    background_image()
    main_interface_image()
    main_interface_label()

#Main function to create a window
def Main():
    global window, main_interface_frame
    window = Tk()
    window.title("Road Code Quiz")
    window.geometry("1350x679")
    main_interface()
    window.mainloop()

Main()
