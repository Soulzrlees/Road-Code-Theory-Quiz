from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import ttk
from tkinter import font
import time
import random
import math
from tkinter import scrolledtext
#For pie graph
from matplotlib import pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#These imports are files for storing each category questions information
from Behaviour import *
from Emergencies import *
from Intersections import *
from Parking import *
from RoadPositions import *
from Sign import *

# This function is to delete all widgets in main interface frame so that the question frame could replace it
def clear_main_interface_frame():
    global main_interface_frame
    main_interface_frame.pack_forget()

#Exit interface once exit icon has clicked (it asks user if there are sure)
def Exit():
    global window, status
    status = messagebox.askyesno(title = "", message = "Are you sure?")
    if status == True:
        window.destroy()
    else:
        pass

#Return function depending on which interface user is on    
def Return(currentinterface):
    global Questionnum, window, numbercorrect, numberincorrect, questions_incorrect, questions_correct, answers_incorrect, answers_correct, toggleOnorOff
    """The return function individually have a number set for example go to line 361, the number
    determines which interface the user is on and when the return function is activated the clearning of the interface
    would be dependant on the number. When the number is 1 it would call the clear quiz interface function, while
    the number 2 would destroy the result interface frame instead"""
    if currentinterface == 1:
        clear_quiz_interface_frame()
    if currentinterface == 2:
        for widget in result_interface_frame.winfo_children():
            widget.destroy()
        result_interface_frame.destroy()
    Questionnum = 1
    numbercorrect = 0
    numberincorrect = 0
    questions_incorrect.clear()
    questions_correct.clear()
    answers_incorrect.clear()
    answers_correct.clear()
    toggleOnorOff = "Off"
    main_interface()

# This retry function destroy the result interface frames and calls the selected list from before
def Retry(currentcategory):
    global listvariable, Questionnum, numbercorrect, numberincorrect, toggleOnorOff
    for widget in result_interface_frame.winfo_children():
        widget.destroy() 
        result_interface_frame.destroy()
    numbercorrect = 0
    numberincorrect = 0
    Questionnum = 1
    questions_incorrect.clear()
    questions_correct.clear()
    answers_incorrect.clear()
    question_interface(currentcategory)

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
        global Timelimit_OnorOff, main_interface_frame, randomquestion_spinbox, questionlength, Timelimit_spinbox, toggleOnorOff
        toggleOnorOff = "Off"
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
        global Timelimit_OnorOff, toggleOnorOff
        #Check the current background color of Timelimit_OnorOff
        current_bg = Timelimit_OnorOff.cget("bg")
        # Toggle the background color and change the text
        if current_bg == "green":
            Timelimit_OnorOff.config(bg="red")
            Timelimit_OnorOff.config(text="Timer Off")
            toggleOnorOff = "Off"
        else:
            Timelimit_OnorOff.config(bg="green")
            Timelimit_OnorOff.config(text="Timer On")
            toggleOnorOff = "On"

    #Creating main interface image (that acts as a button) for each different categories
    def main_interface_image():
        global behavior_picture, main_interface_frame, Emergency_picture, Parking_picture, Intersection_picture, Road_Position_picture, Sign_picture, ExitIcon_picture
        behavior_picture = PhotoImage(file="Image_Folder/Main Image/Behaviormainpic.png").subsample(1,1)
        Photo_behavior_picture_label = Button(main_interface_frame, image= behavior_picture, text="Behavior", relief="solid", bd=0, bg = "black", activebackground="white", height = 187, width = 280, command=lambda: activation(QBlist, 10))
        Photo_behavior_picture_label.place(x=60, y=70)

        Emergency_picture = PhotoImage(file="Image_Folder/Main Image/Emergencymainpic.png").subsample(1,1)
        Photo_Emergency_picture_label = Button(main_interface_frame, image= Emergency_picture, text="Emergency", relief="solid", bd=0, bg= "black", activebackground="white", height = 187, width = 280, command=lambda: activation(QElist, 10))
        Photo_Emergency_picture_label.place(x=370, y=70)

        Intersection_picture = PhotoImage(file="Image_Folder/Main Image/Intersectionmainpic.png").subsample(1,1)
        Photo_Intersection_picture_label = Button(main_interface_frame, image= Intersection_picture, text="Intersection", relief="solid", bd=0, bg= "black", activebackground="white", height = 187, width = 280, command=lambda: activation(QIlist, 10))
        Photo_Intersection_picture_label.place(x=680, y=70)

        Parking_picture = PhotoImage(file="Image_Folder/Main Image/Parkingmainpic.png").subsample(1,1)
        Photo_Parking_picture_label = Button(main_interface_frame, image= Parking_picture, text="Parking", relief="solid", bg= "black", bd=0, activebackground="white", height = 187, width = 280, command=lambda: activation(QPlist, 10))
        Photo_Parking_picture_label.place(x=60, y=350)

        Road_Position_picture = PhotoImage(file="Image_Folder/Main Image/Road_Positionmainpic.png").subsample(1,1)
        Photo_Road_Position_picture_label = Button(main_interface_frame, image= Road_Position_picture, text="Road_position", relief="solid", bd=0, bg= "black", activebackground="white", height = 187, width = 280, command=lambda: activation(QRlist, 10))
        Photo_Road_Position_picture_label.place(x=370, y=350)

        Sign_picture = PhotoImage(file="Image_Folder/Main Image/Signmainpic.png").subsample(1,1)
        Photo_Sign_picture_label = Button(main_interface_frame, image= Sign_picture, text="Sign", relief="solid", bd=0, bg= "black", activebackground="white", height = 187, width = 280, command=lambda: activation(QSlist, 10))
        Photo_Sign_picture_label.place(x=680, y=350)

        ExitIcon_picture = PhotoImage(file="Image_Folder/Main Image/ExitIcon.png").subsample(3,3)
        Photo_ExitIcon_picture_label = Button(main_interface_frame, image= ExitIcon_picture, text="Sign", command = Exit, bd=0, bg = "white")
        Photo_ExitIcon_picture_label.place(x=1197, y=500)

    """When button of any category is clicked the frame clear function activates, 
    question interface activates and the listvariable gets replaced"""
    def activation(listvar, Qamount):
        global listvariable, questionlength
        questionlength = Qamount
        clear_main_interface_frame()
        listvariable = listvar
        question_interface(listvariable)
    
    #Activation for the random_question new variable called length to get the number from the randomquestion spinbox
    def Random_Question_activation():
        global listvariable, questionlength, length, randomquestion_spinbox, Total_list, Timelimit_spinbox
        length = int(randomquestion_spinbox.get())
        questionlength = length
        clear_main_interface_frame()
        listvariable = Total_list
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

questions_correct = []
questions_incorrect = []
answers_incorrect = []
answers_correct = []
numbercorrect = 0
numberincorrect = 0

Questionnum = 1

# Destroys the quiz_interface_frame once it is called
def clear_quiz_interface_frame():
    global quiz_interface_frame
    for widget in quiz_interface_frame.winfo_children():
        widget.destroy()
        quiz_interface_frame.destroy()

# main question_interface function contains nessary variables to randomized each list of questions
def question_interface(category_list):
    global quiz_interface_frame, window,  mainfontstyle, question_list, random_question_generator, i, questions_correct, questions_incorrect, numberincorrect, numbercorrect, randomquestion_spinbox, questionlength, Total_list, answers_incorrect, toggleOnorOff
    random_question_generator = []

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
        global quiz_interface_frame, window,  mainfontstyle, question_list, random_question_generator, Questionnum, i, question_list
        global numbercorrect, numberincorrect, questions_incorrect, questions_correct, randomquestion_spinbox, questionlength, randombuttonplacement1, i, question_list
        i += 1
        #Creating the frame for quiz interface
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
        
        """Runtimer function contains detecting if the timer is toggle on or off and gathering the infromation of
        the timelimit spinbox to find the time limit per question"""
        def runTimer():
            global Timelimit_spinbox, questionlength, secondperquestion
            if toggleOnorOff == "On":
                second = int(Timelimit_spinbox.get()) * 60
                secondperquestion = math.trunc(second / questionlength)
                update_timer_label(secondperquestion)
            else:
                pass
        #This function refresh the timer so that the number would be counting down
        def update_timer_label(time_left):
            global secondperquestion, numbercorrect, numberincorrect, Questionnum, questions_incorrect, questions_correct, answers_incorrect, answers_correct, toggleOnorOff
            if time_left >= 0:
                timelabel = Label(quiz_interface_frame, text=(time_left,"s/left"), height=4, width=25, bg="black", fg= "white", font=mainfontstyle)
                timelabel.place(x=70, y=13)
                quiz_interface_frame.after(1000, update_timer_label, time_left - 1)
            #when time reaches 0 a message box would pop up and resets all the variables and calls the main interface.
            else:
                messagebox.showinfo("", "Times Up!")
                numbercorrect = 0
                numberincorrect = 0
                Questionnum = 1
                questions_incorrect.clear()
                questions_correct.clear()
                answers_incorrect.clear()
                answers_correct.clear()
                toggleOnorOff = "Off"
                clear_quiz_interface_frame()
                main_interface()
            
        """Button for the quiz_interface, the button placement randomization is due to the shuffle function of the
        radnombuttonplacement1 variable that contains all the possible positions.
        In (x=randombuttonplacement1[0]['x'], y=randombuttonplacement1[0]['y']) the
        0 represents first variable in the randomized list sof for example if first variable in the shuffle list is position3, then
        the x axis and y axix of potion 3 would be used for the the button."""
        def quiz_interface_button():
            global question_list, randombuttonplacement1
            try:    
                if len(question_list[1]) == 4:
                    choice_button1 = Button(quiz_interface_frame, text=question_list[1][0], height=7, width=40, bg="black", fg="white", font=mainfontstyle, bd=0, command=lambda: Correct_check(0))
                    choice_button1.place(x=randombuttonplacement1[0]['x'], y=randombuttonplacement1[0]['y'])

                    choice_button2 = Button(quiz_interface_frame, text=question_list[1][1], height=7, width=40, bg="black", fg="white", font=mainfontstyle, bd=0, command=lambda: Correct_check(1))
                    choice_button2.place(x=randombuttonplacement1[1]['x'], y=randombuttonplacement1[1]['y'])

                    choice_button3 = Button(quiz_interface_frame, text=question_list[1][2], height=7, width=40, bg="black", fg="white", font=mainfontstyle, bd=0, command=lambda: Correct_check(2))
                    choice_button3.place(x=randombuttonplacement1[2]['x'], y=randombuttonplacement1[2]['y'])

                    choice_button4 = Button(quiz_interface_frame, text=question_list[1][3], height=7, width=40, bg="black", fg="white", font=mainfontstyle, bd=0, command=lambda: Correct_check(3))
                    choice_button4.place(x=randombuttonplacement1[3]['x'], y=randombuttonplacement1[3]['y'])
                """This if statements is for questions that only has 2 choices. In this case there is
                no randomization"""
                if len(question_list[1]) == 2:
                    choice_button1 = Button(quiz_interface_frame, text=question_list[1][0], height=9, width=40, bg="black", fg="white", font=mainfontstyle, bd=0, command=lambda: Correct_check(0))
                    choice_button1.place(x=50, y=400)

                    choice_button2 = Button(quiz_interface_frame, text=question_list[1][1], height=9, width=40, bg="black", fg="white", font=mainfontstyle, bd=0, command=lambda: Correct_check(1))
                    choice_button2.place(x=970, y=400)

            except:
                pass

        """Checks if the selected button is correct, this is done by comparing the second dictionary in the question_list variable
        with the third dictionary in the question_list if both variables are the same than the question text and the correct answer text
        would be appended to a new list. The numbercorrect variable would increase by 1"""
        def Correct_check(index):
            global question_list, numbercorrect, numberincorrect, questions_incorrect, questions_correct, answers_incorrect, answers_correct
            if question_list[1][index] == question_list[2]:
                questions_correct.append(question_list[0])
                answers_correct.append(question_list[2])
                numbercorrect += 1
            """This if statement is if the second dictionary of question_list is not similar to the third dictionary of question_list than
            question text and incorrect answer text would be appended to a new list. The numberincorrect variable would increase by 1 after
            every incorrect choice the user has chosen"""
            if question_list[1][index] != question_list[2]:
                questions_incorrect.append(question_list[0])
                answers_incorrect.append(question_list[2])
                numberincorrect += 1
            
            quiz_interface_next_question()

        """Getting the photo of the questions by choosing the fourth dictionary of the question_list variable since the fourth
        dictionary is for Images"""
        def quiz_interface_image():
            global question_image, question_list
            try:
                question_image = PhotoImage(file = (question_list[3]))
                question_image_label = Label(quiz_interface_frame, image= question_image, relief="solid", bd=0, bg= "black")
                question_image_label.place(x=400, y=100)
            #If there are no pictures in the variable than the function is passed
            except:
                pass

                
        #Labels for the quiz_interface
        def quiz_interface_label():
            global Questionnum, ExitIcon_picture, Return, Photo_ReturnIcon_picture
            numberofquestion = Label(quiz_interface_frame, text= ("Q", Questionnum), height= 4, width=6, bg = "black", fg= "white", font = mainfontstyle)
            numberofquestion.place(x=10, y=13)
            question_label = Label(quiz_interface_frame, text=(question_list[0]), height= 4, width=60, bg = "black", fg= "white", font = mainfontstyle)
            question_label.place(x=430, y=13)
            #Exit Icon for the question interface
            Photo_ReturnIcon_picture = PhotoImage(file="Image_Folder/Main Image/ReturnIcon.png").subsample(3,3)
            Photo_ReturnIcon_picture_label_question = Button(quiz_interface_frame, image= Photo_ReturnIcon_picture, command=lambda: Return(1), bd=0, bg="white")
            Photo_ReturnIcon_picture_label_question.place(x=630, y=500)
        
        #Progress bar on the quiz interface to display visual how many questions are left
        def quiz_interface_progressbar():
            global quiz_interface_frame, Questionnum, questionlength
            progressbar = ttk.Progressbar(quiz_interface_frame, orient=HORIZONTAL, length=400, mode='determinate', maximum=questionlength, value=Questionnum)
            progressbar.place(x=475, y=410)


        #function for switching to the next questions once button a button is clicked on the previous question
        def quiz_interface_next_question():
            global Questionnum, clear_quiz_interface_frame, quiz_interface_frame, question_list, numbercorrect, numberincorrect, questions_incorrect, questions_correct, randomquestion_spinbox, questionlength
            Questionnum = Questionnum + 1
            #Either way when the quiz_interface_next_question is called the quiz_interface_frame would be destroyed
            for widget in quiz_interface_frame.winfo_children():
                widget.destroy()
                quiz_interface_frame.destroy()
            #When current question (i) reaches the maximum question (questionlength) the resul interface would be called
            if i+1 == questionlength:
                result_interface()
            #If not the quiz interface function would continue to run
            else:
                questions()
        
        background_image_question()
        quiz_interface_label()
        quiz_interface_button()
        quiz_interface_image()
        quiz_interface_progressbar()
        runTimer()
    questions()
    
#__________________________________________________Result_Interface_____________________________________________________________
def result_interface():
    global result_interface_frame, numbercorrect, Questionnum

    result_interface_frame = Frame(window)
    result_interface_frame.pack(fill=BOTH, expand=True)

    #Background for  result interface
    def background_image_result():
        global window, bgr, result_interface_frame
        bgr = PhotoImage(file="Image_Folder/Main Image/resultbackground.png")
        background_image_result = Label(result_interface_frame, image=bgr)
        background_image_result.place(x=0, y=0, relwidth=1, relheight=1)

    # Displaying Labels for the result interface
    def ResultLabel():
        global numbercorrect, Questionnum, result_interface_frame
        result_label = Label(result_interface_frame, text=("Correct", numbercorrect, "/", Questionnum - 1), height=4, width=30, font = ("Verdana", 22), bg = "black", fg = "white")
        result_label.place(x=50, y=500)
        Questions_Incorrect_label = Label(result_interface_frame, text="Questions Incorrect", height=2, width=33, font = ("Verdana", 15, "bold"), bg = "black", fg = "white")
        Questions_Incorrect_label.place(x=840, y=35)
        Questions_Correct_label = Label(result_interface_frame, text="Questions Correct", height=2, width=33, font = ("Verdana", 15, "bold"), bg = "black", fg = "white")
        Questions_Correct_label.place(x=840, y=355)

    # Buttons for the result interface includes the Icons (Exit, Retry and Return Icons)
    def Result_Buttons():
        global ExitIcon_picture, Photo_ReturnIcon_picture, RetryIcon_picture, listvariable
        Photo_ExitIcon_picture_label2 = Button(result_interface_frame, image= ExitIcon_picture, command = Exit, bd=0, bg = "white")
        Photo_ExitIcon_picture_label2.place(x=675, y=180)
        Photo_ReturnIcon_picture_label2 = Button(result_interface_frame, image= Photo_ReturnIcon_picture, command=lambda: Return(2), bd=0, bg="white")
        Photo_ReturnIcon_picture_label2.place(x=675, y=280)
        RetryIcon_picture = PhotoImage(file="Image_Folder/Main Image/RetryIcon.png").subsample(3,3)
        Photo_RetryIcon_picture_label = Button(result_interface_frame, image= RetryIcon_picture, command=lambda: Retry(listvariable), bd=0, bg="white")
        Photo_RetryIcon_picture_label.place(x=675, y=380)
    
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
        ax.pie(data, colors=colour, autopct='%.1f%%', textprops=text_prop, shadow=True, wedgeprops=
       {'edgecolor':'white'}, labeldistance=0.6)
        title = ax.text(0.5, 1, "Result", ha='center', va='center', color='white', transform=ax.transAxes, fontsize = 25)
        canvas = FigureCanvasTkAgg(fig, master=result_interface_frame)
        canvas.draw()
        canvas.get_tk_widget().place(x=50, y=35)
    
    #This function displays all incorrect questions with the answers in one text and the other textbox for questions that the user got correct with the answers
    def text():
        global answers_incorrect, questions_correct, questions_incorrect, answers_correct

        #Ensure both lists have at least one element
        if questions_incorrect and answers_incorrect:
            inccombined_text = ""
            """For every text in question_correct and answers_correct variable the each items would
            be combine for example the first text of the list of question_correct and answers_correct
            would be combined by the zip function. The enumrate function adds a number to the side of the 
            each combined_text(question_correct and answers_correct). So each time a question and answer is combined
            a number would be attached to it and increased by 1. 
             """
            for idx, (question, answer) in enumerate(zip(questions_incorrect, answers_incorrect), start=1):
                inccombined_text += f"{idx}. {question}: \n{answer}\n\n"
            #Displaying the text
            display_question_incorrect = scrolledtext.ScrolledText(result_interface_frame, wrap=WORD, width=45, height=13, font=("Verdana", 11))
            display_question_incorrect.insert(END, inccombined_text)    
            display_question_incorrect.config(state=DISABLED)
            display_question_incorrect.place(x=840, y=90)
        #Same thing but instead the variables are swap with question_correct and answer_correct variable
        if questions_correct and answers_correct:
            corcombined_text = ""

            for idx, (question, answer) in enumerate(zip(questions_correct, answers_correct), start=1):
                corcombined_text += f"{idx}. {question}: \n{answer}\n\n"

            display_question_incorrect = scrolledtext.ScrolledText(result_interface_frame, wrap=WORD, width=45, height=13, font=("Verdana", 11))
            display_question_incorrect.insert(END, corcombined_text)
            display_question_incorrect.config(state=DISABLED)
            display_question_incorrect.place(x=840, y=410)
    
    background_image_result()
    ResultLabel()
    Result_Buttons()
    text()
    Piegraph()
    

#Main function to create a window
def Main():
    global window, main_interface_frame, quiz_interface_frame, question_interface, question_image, listvariable
    window = Tk()
    window.title("Road Code Quiz")
    window.geometry("1350x679")
    window.resizable(False, False)
    main_interface()
    window.mainloop()

Main()