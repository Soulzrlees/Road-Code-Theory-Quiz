from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import ttk
from tkinter import font
import time
import random
from matplotlib import pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from Behaviour import *
from Emergencies import *
from Intersections import *
from Parking import *
from RoadPositions import *
from Sign import *
current_list = 0
# This function is to delete all widgets in main interface frame so that the question frame could replace it
def clear_main_interface_frame():
    global main_interface_frame
    for widget in main_interface_frame.winfo_children():
        widget.destroy() 
        main_interface_frame.destroy()

#Exit interface once exit icon has clicked (it asks user if there are sure)
def Exit():
    global window, status
    status = messagebox.askyesno(title = "", message = "Are you sure?")
    if status == True:
        window.destroy()
    else:
        pass

#Return to main interface once return icon is clicked
def Return():
    global Questionnum, window
    for widget in quiz_interface_frame.winfo_children():
        widget.destroy()
    quiz_interface_frame.destroy()
    Questionnum = 1
    main_interface()
    

def Return2():
    global Questionnum, window
    for widget in result_interface_frame.winfo_children():
        widget.destroy()
    result_interface_frame.destroy()
    Questionnum = 1
    main_interface()

# This retry function destroy the result interface frames and calls the selected list from before
def Retry():
    global current_list, listvariable, Questionnum, numbercorrect, numberincorrect
    for widget in result_interface_frame.winfo_children():
        widget.destroy() 
        result_interface_frame.destroy()
    numbercorrect = 0
    numberincorrect = 0
    Questionnum = 1
    if current_list == 1:
        question_interface(QBlist)
    if current_list == 2:
        question_interface(QElist)
    if current_list == 3:
        question_interface(QIlist)
    if current_list == 4:
        question_interface(QPlist)
    if current_list == 5:
        question_interface(QRlist)
    if current_list == 6:
        question_interface(QSlist)
    if current_list == 7:
        question_interface(Total_list)

#_____________________________________________________________Main Interface_________________________________________________________
def main_interface():
    global main_interface_frame,  mainfontstyle, Total_list
    mainfontstyle = ("Verdana", 10)
    main_interface_frame = Frame(window)
    main_interface_frame.pack(fill=BOTH, expand=True)
    random.shuffle(Total_list)

    #Background image of main interface
    def background_image_main():
        global window, bgm, main_interface_frame
        bgm = PhotoImage(file="Image_Folder/Main Image/mainbackground.png")
        background_image_main = Label(main_interface_frame, image=bgm)
        background_image_main.place(x=0, y=0, relwidth=1, relheight=1)

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

        Timelimit_OnorOff = Button(main_interface_frame, text="Time limit\n In minutes\n On / Off", height=5, width=23, bg="red", fg="white", font=mainfontstyle, bd=0, command=Timelimit_activation)
        Timelimit_OnorOff.place(x=1160, y=120)

        RandomQuestions = Button(main_interface_frame, text="Confirm number of\nRandomized Questions", height= 5, width=23, bg = "black", fg= "white", font = mainfontstyle, command=Random_Question_activation, bd=0)
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

        ExitIcon_picture = PhotoImage(file="Image_Folder/Main Image/ExitIcon.png").subsample(3,3)
        Photo_ExitIcon_picture_label = Button(main_interface_frame, image= ExitIcon_picture, text="Sign", command = Exit, bd=0, bg = "white")
        Photo_ExitIcon_picture_label.place(x=1197, y=500)

    #When button of any category is clicked the frame clear function activates, question interface activates and the listvariable gets replaced
    def Behavior_activation():
        global listvariable, questionlength, current_list
        questionlength = 10
        clear_main_interface_frame()
        listvariable = QBlist
        current_list = 1
        question_interface(listvariable)

    def Emergencies_activation():
        global listvariable, questionlength, current_list
        questionlength = 10
        clear_main_interface_frame()
        listvariable = QElist
        current_list = 2
        question_interface(listvariable)
    
    def Intersections_activation():
        global listvariable, questionlength, current_list
        questionlength = 10
        clear_main_interface_frame()
        listvariable = QIlist
        current_list = 3
        question_interface(listvariable)

    def Parking_activation():
        global listvariable, questionlength, current_list
        questionlength = 10
        clear_main_interface_frame()
        listvariable = QPlist
        current_list = 4
        question_interface(listvariable)
    
    def RoadPositions_activation():
        global listvariable, questionlength, current_list
        questionlength = 10
        clear_main_interface_frame()
        listvariable = QRlist
        current_list = 5
        question_interface(listvariable)
    
    def Sign_activation():
        global listvariable, questionlength, current_list
        questionlength = 10
        clear_main_interface_frame()
        listvariable = QSlist
        current_list = 6
        question_interface(listvariable)
    
    def Random_Question_activation():
        global listvariable, questionlength, length, randomquestion_spinbox, Total_list, current_list
        length = int(randomquestion_spinbox.get())
        questionlength = length
        clear_main_interface_frame()
        listvariable = Total_list
        current_list = 7
        question_interface(listvariable)

    background_image_main()
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
        main_interface()

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

    i=-1
    #Background of the quiz interface frame
    def background_image_question():
        global window, bgq, quiz_interface_frame
        bgq = PhotoImage(file="Image_Folder/Main Image/questionbackground.png")
        background_image_question = Label(quiz_interface_frame, image=bgq)
        background_image_question.place(x=0, y=0, relwidth=1, relheight=1)

    #This functions contains the nessary componets the quiz interface such as button, image, label, progress bar, checking input
    def questions():
        global TotalbehaviourQ, quiz_interface_frame, window,  mainfontstyle, question_list, random_question_generator, random_question_generated, Questionnum, i, question_list, numbercorrect, numberincorrect, questions_incorrect, questions_correct, randomquestion_spinbox, questionlength, randombuttonplacement1
        global i, question_list
        i += 1

        quiz_interface_frame = Frame(window)
        quiz_interface_frame.pack(fill=BOTH, expand=True)

        question_list = list(category_list[random_question_generator[i]].values())
        #Randomizing position of choice buttons
        position1 = {'x': 50, 'y': 400}
        position2 = {'x': 970, 'y': 400}
        position3 = {'x': 50, 'y': 540}
        position4 = {'x': 970, 'y': 540}
        randombuttonplacement1 = [position1, position2, position3, position4]
        random.shuffle(randombuttonplacement1)

        #Button for the quiz_interface
        def quiz_interface_button():
            global question_list, randombuttonplacement1
            try:    
                if len(question_list[1]) == 4:
                    choice_button1 = Button(quiz_interface_frame, text=question_list[1][0], height=7, width=40, bg="black", fg="white", font=mainfontstyle, bd=0, command=Correct_check_B1)
                    choice_button1.place(x=randombuttonplacement1[0]['x'], y=randombuttonplacement1[0]['y'])

                    choice_button2 = Button(quiz_interface_frame, text=question_list[1][1], height=7, width=40, bg="black", fg="white", font=mainfontstyle, bd=0, command=Correct_check_B2)
                    choice_button2.place(x=randombuttonplacement1[1]['x'], y=randombuttonplacement1[1]['y'])

                    choice_button3 = Button(quiz_interface_frame, text=question_list[1][2], height=7, width=40, bg="black", fg="white", font=mainfontstyle, bd=0, command=Correct_check_B3)
                    choice_button3.place(x=randombuttonplacement1[2]['x'], y=randombuttonplacement1[2]['y'])

                    choice_button4 = Button(quiz_interface_frame, text=question_list[1][3], height=7, width=40, bg="black", fg="white", font=mainfontstyle, bd=0, command=Correct_check_B4)
                    choice_button4.place(x=randombuttonplacement1[3]['x'], y=randombuttonplacement1[3]['y'])

                if len(question_list[1]) == 2:
                    choice_button1 = Button(quiz_interface_frame, text=question_list[1][0], height=9, width=40, bg="black", fg="white", font=mainfontstyle, bd=0, command=Correct_check_B1)
                    choice_button1.place(x=50, y=400)

                    choice_button2 = Button(quiz_interface_frame, text=question_list[1][1], height=9, width=40, bg="black", fg="white", font=mainfontstyle, bd=0, command=Correct_check_B2)
                    choice_button2.place(x=970, y=400)

            except:
                pass

        
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
            global Questionnum, ExitIcon_picture, Return, Photo_ReturnIcon_picture
            numberofquestion = Label(quiz_interface_frame, text= ("Q", Questionnum), height= 4, width=6, bg = "black", fg= "white", font = mainfontstyle)
            numberofquestion.place(x=10, y=13)
            question_label = Label(quiz_interface_frame, text=(question_list[0]), height= 4, width=60, bg = "black", fg= "white", font = mainfontstyle)
            question_label.place(x=430, y=13)
            #Exit Icon for the question interface
            Photo_ReturnIcon_picture = PhotoImage(file="Image_Folder/Main Image/ReturnIcon.png").subsample(3,3)
            Photo_ReturnIcon_picture_label_question = Button(quiz_interface_frame, image= Photo_ReturnIcon_picture, command = Return, bd=0, bg="white")
            Photo_ReturnIcon_picture_label_question.place(x=630, y=500)
        
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
                questions_correct.clear()                                        
                questions_incorrect.clear()
                result_interface()
            else: 
                questions()
        background_image_question()
        quiz_interface_label()
        quiz_interface_button()
        quiz_interface_image()
        quiz_interface_progressbar()
    questions()
    
#__________________________________________________Result_Interface_____________________________________________________________
def result_interface():
    global result_interface_frame, numbercorrect, Questionnum

    result_interface_frame = Frame(window)
    result_interface_frame.pack(fill=BOTH, expand=True)
    # Displaying Labels for the result interface
    def ResultLabel():
        global numbercorrect, Questionnum, result_interface_frame
        result_label = Label(result_interface_frame, text=("Correct", numbercorrect, "/", Questionnum - 1), height=4, width=30, font = ("Verdana", 22), bg = "black", fg = "white")
        result_label.place(x=100, y=500)
    # Buttons for the result interface includes the Icons (Exit, Retry and Return Icons)
    def Result_Buttons():
        global ExitIcon_picture, Photo_ReturnIcon_picture, RetryIcon_picture
        Photo_ExitIcon_picture_label2 = Button(result_interface_frame, image= ExitIcon_picture, command = Exit, bd=0, bg = "white")
        Photo_ExitIcon_picture_label2.place(x=700, y=170)
        Photo_ReturnIcon_picture_label2 = Button(result_interface_frame, image= Photo_ReturnIcon_picture, command = Return2, bd=0, bg="white")
        Photo_ReturnIcon_picture_label2.place(x=700, y=270)
        RetryIcon_picture = PhotoImage(file="Image_Folder/Main Image/RetryIcon.png").subsample(3,3)
        Photo_RetryIcon_picture_label = Button(result_interface_frame, image= RetryIcon_picture, command = Retry, bd=0, bg="white")
        Photo_RetryIcon_picture_label.place(x=700, y=370)
    
    #Piechart for visualy displaying the results
    def Piegraph():
        global numbercorrect, numberincorrect
        data = [numbercorrect, numberincorrect]
        resultdata = ['Correct', 'Incorrect']
        colour = ['tab:green', 'tab:red']
        text_prop = {'color':'white',"fontsize":13, 'fontstyle':'italic', 'fontfamily':'sans-serif'}
        #Adjusting Size of the graph
        fig = plt.figure(figsize=(6, 5), dpi=91, facecolor="black")
        ax = fig.add_subplot(111)
        # Specification of the graph as well as ploting the graph into the result interface frame
        ax.pie(data, labels=resultdata, colors=colour, autopct='%.1f%%', textprops=text_prop, shadow=True, wedgeprops=
       {'edgecolor':'white'}, labeldistance=0.3)
        title = ax.text(0.5, 1, "Result", ha='center', va='center', color='white', transform=ax.transAxes, fontsize = 20)
        canvas = FigureCanvasTkAgg(fig, master=result_interface_frame)
        canvas.draw()
        canvas.get_tk_widget().place(x=100, y=35)
            
    ResultLabel()
    Result_Buttons()
    Piegraph()
    

#Main function to create a window
def Main():
    global window, main_interface_frame, quiz_interface_frame, question_interface, question_image, listvariable
    window = Tk()
    window.title("Road Code Quiz")
    window.geometry("1350x679")
    main_interface()
    window.mainloop()

Main()