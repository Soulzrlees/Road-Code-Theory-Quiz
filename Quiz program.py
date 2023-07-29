from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import ttk
import time
import random

from Behaviour import *
from Emergencies import *
from Intersections import *
from Parking import *
from RoadPositions import *
from Sign import *

# This function is to delete all widgets in main interface frame so that the question frame could replace it
def clear_main_interface_frame():
    global main_interface_frame
    for widget in main_interface_frame.winfo_children():
        widget.destroy() 
        main_interface_frame.destroy()
#_____________________________________________________________Main Interface_________________________________________________________
def main_interface():
    global main_interface_frame,  mainfontstyle, Total_list
    mainfontstyle = ("Helvetica", 10, "bold")
    main_interface_frame = Frame(window)
    main_interface_frame.pack(fill=BOTH, expand=True)
    random.shuffle(Total_list)

    #Background image of main interface
    def background_image():
        global window, bg, main_interface_frame
        bg = PhotoImage(file="Image_Folder/Main Image/mainbackground.png")
        background_image = Label(main_interface_frame, image=bg)
        background_image.place(x=0, y=0, relwidth=1, relheight=1)

    #Creating main interface labels for each different categories
    def main_interface_label():
        global Timelimit_OnorOff, main_interface_frame, randomquestion_spinbox, questionlength
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

        RandomQuestions = Button(main_interface_frame, text="Confirm number of\nRandomized Questions", height= 5, width=20, bg = "black", fg= "white", font = mainfontstyle, command=Random_Question_activation, bd=0)
        RandomQuestions.place(x=1160, y=330)
        #Spinkbox for the user to select number of question from 15 to 30 randomize questions
        randomquestion_spinbox = Spinbox(main_interface_frame, from_=10, to=35, font = mainfontstyle, bd= 10, state='readonly')
        randomquestion_spinbox.place(x=1160, y=300)
        #Spinkbox for timer from 10 min to 60 mins (default 60mins)
        Timelimit_spinbox = Spinbox(main_interface_frame, from_=10, to=60, font = mainfontstyle, bd= 10, state='readonly', increment=2)
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
        global behavior_picture, main_interface_frame, Emergency_picture, Parking_picture, Intersection_picture, Road_Position_picture, Sign_picture, ExitIcon_picture, question_interface, randomquestion_spinbox
        behavior_picture = PhotoImage(file="Image_Folder/Main Image/Behaviormainpic.png").subsample(1,1)
        Photo_behavior_picture_label = Button(main_interface_frame, image= behavior_picture, text="Behavior", relief="solid", bd=0, bg = "black", activebackground="white", height = 187, width = 280, command = Behavior_activation)
        Photo_behavior_picture_label.place(x=60, y=70)

        Emergency_picture = PhotoImage(file="Image_Folder/Main Image/Emergencymainpic.png").subsample(1,1)
        Photo_Emergency_picture_label = Button(main_interface_frame, image= Emergency_picture, text="Emergency", relief="solid", bd=0, bg= "black", activebackground="white", height = 187, width = 280, command = Emergencies_activation)
        Photo_Emergency_picture_label.place(x=370, y=70)

        Intersection_picture = PhotoImage(file="Image_Folder/Main Image/Intersectionmainpic.png").subsample(1,1)
        Photo_Intersection_picture_label = Button(main_interface_frame, image= Intersection_picture, text="Intersection", relief="solid", bd=0, bg= "black", activebackground="white", height = 187, width = 280, command = Intersections_activation)
        Photo_Intersection_picture_label.place(x=680, y=70)

        Parking_picture = PhotoImage(file="Image_Folder/Main Image/Parkingmainpic.png").subsample(1,1)
        Photo_Parking_picture_label = Button(main_interface_frame, image= Parking_picture, text="Parking", relief="solid", bg= "black", bd=0, activebackground="white", height = 187, width = 280, command = Parking_activation)
        Photo_Parking_picture_label.place(x=60, y=350)

        Road_Position_picture = PhotoImage(file="Image_Folder/Main Image/Road_Positionmainpic.png").subsample(1,1)
        Photo_Road_Position_picture_label = Button(main_interface_frame, image= Road_Position_picture, text="Road_position", relief="solid", bd=0, bg= "black", activebackground="white", height = 187, width = 280, command = RoadPositions_activation)
        Photo_Road_Position_picture_label.place(x=370, y=350)

        Sign_picture = PhotoImage(file="Image_Folder/Main Image/Signmainpic.png").subsample(1,1)
        Photo_Sign_picture_label = Button(main_interface_frame, image= Sign_picture, text="Sign", relief="solid", bd=0, bg= "black", activebackground="white", height = 187, width = 280, command = Sign_activation)
        Photo_Sign_picture_label.place(x=680, y=350)

        ExitIcon_picture = PhotoImage(file="Image_Folder/Main Image/ExitIcon.png").subsample(4,4)
        Photo_ExitIcon_picture_label = Button(main_interface_frame, image= ExitIcon_picture, text="Sign", command = main_exit, bd=0)
        Photo_ExitIcon_picture_label.place(x=1197, y=500)

    #When button of any category is clicked the frame clear function activates, question interface activates and the listvariable gets replaced
    def Behavior_activation():
        global listvariable, questionlength
        questionlength = 10
        clear_main_interface_frame()
        listvariable = QBlist
        question_interface(listvariable)

    def Emergencies_activation():
        global listvariable, questionlength
        questionlength = 10
        clear_main_interface_frame()
        listvariable = QElist
        question_interface(listvariable)
    
    def Intersections_activation():
        global listvariable, questionlength
        questionlength = 10
        clear_main_interface_frame()
        listvariable = QIlist
        question_interface(listvariable)

    def Parking_activation():
        global listvariable, questionlength
        questionlength = 10
        clear_main_interface_frame()
        listvariable = QPlist
        question_interface(listvariable)
    
    def RoadPositions_activation():
        global listvariable, questionlength
        questionlength = 10
        clear_main_interface_frame()
        listvariable = QRlist
        question_interface(listvariable)
    
    def Sign_activation():
        global listvariable, questionlength
        questionlength = 10
        clear_main_interface_frame()
        listvariable = QSlist
        question_interface(listvariable)
    
    def Random_Question_activation():
        global listvariable, questionlength, length, randomquestion_spinbox, Total_list
        length = int(randomquestion_spinbox.get())
        questionlength = length
        clear_main_interface_frame()
        listvariable = Total_list
        question_interface(listvariable)

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

Questionnum = 1

# Destroys the quiz_interface_frame once it is called
def clear_quiz_interface_frame():
    global quiz_interface_frame
    for widget in quiz_interface_frame.winfo_children():
        widget.destroy()
        quiz_interface_frame.destroy()

# main question_interface function contains nessary variables to randomized each list of questions
def question_interface(category_list):
    global TotalbehaviourQ, quiz_interface_frame, window,  mainfontstyle, question_list, random_question_generator, random_question_generated, i, questions_correct, questions_incorrect, numberincorrect, numbercorrect, randomquestion_spinbox, questionlength, Total_list

    questions_correct = []
    questions_incorrect = []
    random_question_generator = []
    numbercorrect = 0
    numberincorrect = 0


    for i in range (questionlength):
        random_question_generator.append(i)

    random.shuffle(random_question_generator)
    print(random_question_generator)

    i=-1
    def questions():
        global TotalbehaviourQ, quiz_interface_frame, window,  mainfontstyle, question_list, random_question_generator, random_question_generated, Questionnum, i, question_list, numbercorrect, numberincorrect, questions_incorrect, questions_correct, randomquestion_spinbox, questionlength
        global i, question_list
        i += 1

        quiz_interface_frame = Frame(window)
        quiz_interface_frame.pack(fill=BOTH, expand=True)

        question_list = list(category_list[random_question_generator[i]].values())


        # Button for the quiz_interface
        def quiz_interface_button():
            global question_list, randomquestion_spinbox
            try:    
                choice_button1 = Button(quiz_interface_frame, text=(question_list[1][0]), height= 7, width=40, bg = "black", fg= "white", font = mainfontstyle, bd=0, command = Correct_check_B1)
                choice_button1.place(x=50, y=400)

                choice_button2 = Button(quiz_interface_frame, text=(question_list[1][1]), height= 7, width=40, bg = "black", fg= "white", font = mainfontstyle, bd=0, command = Correct_check_B2)
                choice_button2.place(x=970, y=400)

                choice_button3 = Button(quiz_interface_frame, text=(question_list[1][2]), height= 7, width=40, bg = "black", fg= "white", font = mainfontstyle, bd=0, command = Correct_check_B3)
                choice_button3.place(x=50, y=540)

                choice_button4 = Button(quiz_interface_frame, text=(question_list[1][3]), height= 7, width=40, bg = "black", fg= "white", font = mainfontstyle, bd=0, command = Correct_check_B4)
                choice_button4.place(x=970, y=540)
            except:
                choice_button1 = Button(quiz_interface_frame, text=(question_list[1][0]), height= 11, width=40, bg = "black", fg= "white", font = mainfontstyle, bd=0, command = Correct_check_B1)
                choice_button1.place(x=50, y=400)

                choice_button2 = Button(quiz_interface_frame, text=(question_list[1][1]), height= 11, width=40, bg = "black", fg= "white", font = mainfontstyle, bd=0, command = Correct_check_B2)
                choice_button2.place(x=970, y=400)
        
        #Checks if the selected button is correct
        def Correct_check_B1():
            global question_list, numbercorrect, numberincorrect, questions_incorrect, questions_correct
            if (question_list[1][0]) == (question_list[2]):
                questions_correct.append(question_list[0])
                numbercorrect = numbercorrect + 1
    
            if (question_list[1][0]) != (question_list[2]):
                questions_incorrect.append(question_list[0])
                numberincorrect = numberincorrect + 1

            quiz_interface_next_question()

            print("Questions Correct: ", questions_correct)
            print("Questions Incorrect: ", questions_incorrect)
            print("Number of QCorrect: ", numbercorrect)
            print("Number of QIncorrect: ", numberincorrect)
        
        def Correct_check_B2():
            global question_list, numbercorrect, numberincorrect, questions_incorrect, questions_correct
            if (question_list[1][1]) == (question_list[2]):
                questions_correct.append(question_list[0])
                numbercorrect = numbercorrect + 1
    
            if (question_list[1][1]) != (question_list[2]):
                questions_incorrect.append(question_list[0])
                numberincorrect = numberincorrect + 1

            quiz_interface_next_question()

            print("Questions Correct: ", questions_correct)
            print("Questions Incorrect: ", questions_incorrect)
            print("Number of QCorrect: ", numbercorrect)
            print("Number of QIncorrect: ", numberincorrect)

        def Correct_check_B3():
            global question_list, numbercorrect, numberincorrect, questions_incorrect, questions_correct
            if (question_list[1][2]) == (question_list[2]):
                questions_correct.append(question_list[0])
                numbercorrect = numbercorrect + 1
    
            if (question_list[1][2]) != (question_list[2]):
                questions_incorrect.append(question_list[0])
                numberincorrect = numberincorrect + 1
                
            quiz_interface_next_question()

            print("Questions Correct: ", questions_correct)
            print("Questions Incorrect: ", questions_incorrect)
            print("Number of QCorrect: ", numbercorrect)
            print("Number of QIncorrect: ", numberincorrect)

        def Correct_check_B4():
            global question_list, numbercorrect, numberincorrect, questions_incorrect, questions_correct
            if (question_list[1][3]) == (question_list[2]):
                questions_correct.append(question_list[0])
                numbercorrect = numbercorrect + 1
    
            if (question_list[1][3]) != (question_list[2]):
                questions_incorrect.append(question_list[0])
                numberincorrect = numberincorrect + 1
                
            quiz_interface_next_question()

            print("Questions Correct: ", questions_correct)
            print("Questions Incorrect: ", questions_incorrect)
            print("Number of QCorrect: ", numbercorrect)
            print("Number of QIncorrect: ", numberincorrect)

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
            global Questionnum
            numberofquestion = Label(quiz_interface_frame, text= ("Q", Questionnum), height= 3, width=6, bg = "black", fg= "white", font = mainfontstyle)
            numberofquestion.place(x=10, y=10)
            question_label = Label(quiz_interface_frame, text=(question_list[0]), height= 4, width=60, bg = "black", fg= "white", font = mainfontstyle)
            question_label.place(x=430, y=20)
        
        # Progress bar on the quiz interface to display visual how many questions are left
        def quiz_interface_progressbar():
            global quiz_interface_frame, Questionnum, questionlength
            progressbar = ttk.Progressbar(quiz_interface_frame, orient=HORIZONTAL, length=400, mode='determinate', maximum=questionlength, value=Questionnum)
            progressbar.place(x=475, y=410)


        #function for switching to the next questions once button a button is clicked on the previous question
        def quiz_interface_next_question():
            global Questionnum, clear_quiz_interface_frame, quiz_interface_frame, question_listquestion_list, numbercorrect, numberincorrect, questions_incorrect, questions_correct, randomquestion_spinbox, questionlength
            Questionnum = Questionnum + 1

            for widget in quiz_interface_frame.winfo_children():
                widget.destroy()
                quiz_interface_frame.destroy()

            if i+1 == questionlength:
                Questionnum = 1
                questions_correct.clear()                                        
                questions_incorrect.clear()
                main_interface()
            else: 
                questions()

        quiz_interface_label()
        quiz_interface_button()
        quiz_interface_image()
        quiz_interface_progressbar()
    questions()
    


#Main function to create a window
def Main():
    global window, main_interface_frame, quiz_interface_frame, question_interface, question_image, listvariable
    window = Tk()
    window.title("Road Code Quiz")
    window.geometry("1350x679")
    main_interface()
    window.mainloop()

Main()
