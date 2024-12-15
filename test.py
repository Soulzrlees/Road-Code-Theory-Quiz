#Main function to create a window
def Main():
    global window, main_interface_frame, quiz_interface_frame, question_interface, question_image, listvariable
    window = Tk()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    width_percentage = 0.9
    height_percentage = 0.7
    window_width = int(screen_width * width_percentage)
    window_height = int(screen_height * height_percentage)

    x_position = (screen_width - window_width) // 2  # Center the window horizontally
    y_position = (screen_height - window_height) // 2  # Center the window vertically

    window.title("Road Code Quiz")
    window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
    window.resizable(False, False)
    main_interface()
    window.mainloop()

Main()  