from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random

from Behaviour import *
from Emergencies import *
from Intersections import *
from Parking import *
from RoadPositions import *
from Sign import *


# This function is to delete all widgets in main interface frame so that the question frame could replace it
def clear_frame():
    global main_interface_frame
    for widget in main_interface_frame.winfo_children():
        widget.destroy()
        main_interface_frame.destroy()
#_____________________________________________________________Main Interface_________________________________________________________
def main_interface():
    global main_interface_frame,  mainfontstyle
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
        global behavior_picture, main_interface_frame, Emergency_picture, Parking_picture, Intersection_picture, Road_Position_picture, Sign_picture, ExitIcon_picture, question_interface
        behavior_picture = PhotoImage(file="Image_Folder/Main Image/Behaviormainpic.png").subsample(1,1)
        Photo_behavior_picture_label = Button(main_interface_frame, image= behavior_picture, text="Behavior", relief="solid", bd=0, bg = "black", activebackground="white", height = 187, width = 280, command=button_activation)
        Photo_behavior_picture_label.place(x=60, y=70)

        Emergency_picture = PhotoImage(file="Image_Folder/Main Image/Emergencymainpic.png").subsample(1,1)
        Photo_Emergency_picture_label = Button(main_interface_frame, image= Emergency_picture, text="Emergency", relief="solid", bd=0, bg= "black", activebackground="white", height = 187, width = 280, command=button_activation)
        Photo_Emergency_picture_label.place(x=370, y=70)

        Intersection_picture = PhotoImage(file="Image_Folder/Main Image/Intersectionmainpic.png").subsample(1,1)
        Photo_Intersection_picture_label = Button(main_interface_frame, image= Intersection_picture, text="Intersection", relief="solid", bd=0, bg= "black", activebackground="white", height = 187, width = 280, command=button_activation)
        Photo_Intersection_picture_label.place(x=680, y=70)

        Parking_picture = PhotoImage(file="Image_Folder/Main Image/Parkingmainpic.png").subsample(1,1)
        Photo_Parking_picture_label = Button(main_interface_frame, image= Parking_picture, text="Parking", relief="solid", bg= "black", bd=0, activebackground="white", height = 187, width = 280, command=button_activation)
        Photo_Parking_picture_label.place(x=60, y=350)

        Road_Position_picture = PhotoImage(file="Image_Folder/Main Image/Road_Positionmainpic.png").subsample(1,1)
        Photo_Road_Position_picture_label = Button(main_interface_frame, image= Road_Position_picture, text="Road_position", relief="solid", bd=0, bg= "black", activebackground="white", height = 187, width = 280, command=button_activation)
        Photo_Road_Position_picture_label.place(x=370, y=350)

        Sign_picture = PhotoImage(file="Image_Folder/Main Image/Signmainpic.png").subsample(1,1)
        Photo_Sign_picture_label = Button(main_interface_frame, image= Sign_picture, text="Sign", relief="solid", bd=0, bg= "black", activebackground="white", height = 187, width = 280, command=button_activation)
        Photo_Sign_picture_label.place(x=680, y=350)

        ExitIcon_picture = PhotoImage(file="Image_Folder/Main Image/ExitIcon.png").subsample(4,4)
        Photo_ExitIcon_picture_label = Button(main_interface_frame, image= ExitIcon_picture, text="Sign", command = main_exit, bd=0)
        Photo_ExitIcon_picture_label.place(x=1197, y=500)
    
    #This functions allows to store 2 functions so that when this function is called 2 functions in it will be called
    def button_activation():
        clear_frame()
        question_interface()

    #Exit interface once exit icon has clicked (it asks user if there are sure)
    def main_exit():
        global window, status
        status = messagebox.askyesno(title = "", message = "Are you sure?")
        if status == True:
            window.destroy()
        else:
            pass

    background_image()
    main_interface_image()
    main_interface_label()

#___________________________________________________Question Interface____________________________________________________

#List of All variabels of dictionary of each category
QBlist = [Q1B, Q2B, Q3B, Q4B, Q5B, Q6B, Q7B, Q8B, Q9B, Q10B]
QIlist = [Q1I, Q2I, Q3I, Q4I, Q5I, Q6I, Q7I, Q8I, Q9I, Q10I]
QElist = [Q1E, Q2E, Q3E, Q4E, Q5E, Q6E, Q7E, Q8E, Q9E, Q10E]
QPlist = [Q1P, Q2P, Q3P, Q4P, Q5P, Q6P, Q7P, Q8P, Q9P, Q10P]
QRlist = [Q1R, Q2R, Q3R, Q4R, Q5R, Q6R, Q7R, Q8R, Q9R, Q10R]
QSlist = [Q1S, Q2S, Q3S, Q4S, Q5S, Q6S, Q7S, Q8S, Q9S, Q10S]

Total_list = [Q1B, Q2B, Q3B, Q4B, Q5B, Q6B, Q7B, Q8B, Q9B, Q10B,
            Q1I, Q2I, Q3I, Q4I, Q5I, Q6I, Q7I, Q8I, Q9I, Q10I,
            Q1E, Q2E, Q3E, Q4E, Q5E, Q6E, Q7E, Q8E, Q9E, Q10E,
            Q1P, Q2P, Q3P, Q4P, Q5P, Q6P, Q7P, Q8P, Q9P, Q10P,
            Q1R, Q2R, Q3R, Q4R, Q5R, Q6R, Q7R, Q8R, Q9R, Q10R,
            Q1S, Q2S, Q3S, Q4S, Q5S, Q6S, Q7S, Q8S, Q9S, Q10S]

def question_interface():
    global TotalbehaviourQ, question_interface, window,  mainfontstyle, question_list, random_question_generator, random_question_generated
    quiz_interface_frame = Frame(window)
    quiz_interface_frame.pack(fill=BOTH, expand=True)
    random_question_generator = random.randint(0, 9)
    random_question_generated = [random_question_generator]
    print(random_question_generated)
    question_list = list(QBlist[random_question_generator].values())

    
    # Button for the quiz_interface
    def quiz_interface_button():
        global question_list
        try:    
            choice_button1 = Button(quiz_interface_frame, text=(question_list[1][0]), height= 7, width=40, bg = "black", fg= "white", font = mainfontstyle, bd=0)
            choice_button1.place(x=50, y=400)

            choice_button2 = Button(quiz_interface_frame, text=(question_list[1][1]), height= 7, width=40, bg = "black", fg= "white", font = mainfontstyle, bd=0)
            choice_button2.place(x=970, y=400)

            choice_button3 = Button(quiz_interface_frame, text=(question_list[1][2]), height= 7, width=40, bg = "black", fg= "white", font = mainfontstyle, bd=0)
            choice_button3.place(x=50, y=540)

            choice_button4 = Button(quiz_interface_frame, text=(question_list[1][3]), height= 7, width=40, bg = "black", fg= "white", font = mainfontstyle, bd=0)
            choice_button4.place(x=970, y=540)
        except:
            choice_button1 = Button(quiz_interface_frame, text=(question_list[1][0]), height= 11, width=40, bg = "black", fg= "white", font = mainfontstyle, bd=0)
            choice_button1.place(x=50, y=400)

            choice_button2 = Button(quiz_interface_frame, text=(question_list[1][1]), height= 11, width=40, bg = "black", fg= "white", font = mainfontstyle, bd=0)
            choice_button2.place(x=970, y=400)

    
    #Image of questions for the
    def quiz_interface_image():
        global question_image, question_list
        try:
            question_image = PhotoImage(file = (question_list[3]))
            question_image_label = Label(quiz_interface_frame, image= question_image, relief="solid", bd=0, bg= "black")
            question_image_label.place(x=400, y=100)
        #If there are no pictures in the variable than the function is passed
        except:
            pass

            
    # Labels for the quiz_interface
    def quiz_interface_label():
        numberofquestion = Label(quiz_interface_frame, text= "Q", height= 3, width=6, bg = "black", fg= "white", font = mainfontstyle)
        numberofquestion.place(x=10, y=10)
        question_label = Label(quiz_interface_frame, text=(question_list[0]), height= 4, width=60, bg = "black", fg= "white", font = mainfontstyle)
        question_label.place(x=430, y=20)

    quiz_interface_label()
    quiz_interface_button()
    quiz_interface_image()

#Main function to create a window
def Main():
    global window, main_interface_frame, quiz_interface_frame, question_interface, question_image
    window = Tk()
    window.title("Road Code Quiz")
    window.geometry("1350x679")
    main_interface()
    window.mainloop()

Main()
