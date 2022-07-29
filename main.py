# from ensurepip import version
from tkinter import *
from tkinter import ttk


class SneakersRater():

    def mainWindow():
        # Variables
        global author, version, window, liked, disliked, scoreText
        author = "gqdThinky"
        version = "1.0.0"
        window = Tk()
        liked = 0
        disliked = 0
        #sneakerFrame = Frame(window, bg="#DB9898") # Frame for the images


        # Setting up the main window -------------------------------------------------------------------------------
        window.geometry('1150x900') # The dimensions of the window (WIDTHxHEIGHT)
        window.title(f"Sneaker Rater • Created by : {author} • Version : {version}") # Title of the main windows
        window.iconbitmap(default="assets/icon.ico") # Set the icon of the window
        window.config(bg="#F2B3B3") # Change the background of the window


        # Setting up the labels/texts -------------------------------------------------------------------------------
        # Main Text
        mainText = Label(window, text="Start the game !", font=("Arial Bold", 30), bg="#DB9898", borderwidth=4, relief="groove")
        mainText.place(
            relx = 0.51,
            rely = 0.05,
            anchor = 'center'
        )

        # Score Text
        scoreText = Label(
            window, 
            text=f"Liked = {liked}\nDisliked = {disliked}", 
            fg="black", 
            bg="#DB9898", 
            font=("Arial", 20),
            borderwidth=4,
            relief="groove"
        )
        scoreText.place(
            relx = 0.08,
            rely = 0.05,
            anchor = "center"
        )

        # Setting up the images --------------------------------------------------------------------------------------
        placeholderPath = PhotoImage(file="assets/placeholder.ppm", height=580, width=750)
        placeholder = Label(window, image=placeholderPath)
        placeholder.place(
            relx = 0.499,
            rely = 0.45,
            anchor = 'center'
        )
        
        # Setting up the buttons -------------------------------------------------------------------------------------
        # Like Button
        likeButton = Button(window, text="Like", command=None, height=4, width=48, bg="#DB9898", fg="black")
        likeButton.place(
            relx = 0.32,
            rely = 0.88,
            anchor = 'center'
        )

        # Dislike Button
        dislikeButton = Button(window, text="Dislike", command=None, height=4, width=48, bg="#DB9898", fg="black")
        dislikeButton.place(
            relx = 0.675,
            rely = 0.88,
            anchor = 'center'
        )

        # Help/Rules Button
        def rulesWindow():
            # The window that shows up when the questionmark button is clicked.
            name = "rulesWindow"
            print("New window opened : " + name)       

            rulesWindow = Toplevel(window) # Toplevel object which will be treated as a new window

            rulesWindow.title(f"Sneaker Rater • Created by : {author} • Version : {version}") # Define the title of the window
            rulesWindow.geometry("900x800") # Define the size of the window
            rulesWindow.iconbitmap(default="assets/icon.ico") # Define the icon of the window
            rulesWindow.config(bg="#F2B3B3") # Change the background of the window

            Label(rulesWindow, text ="Rules of Sneaker Rater", bg="#DB9898", font=("Helvetica 30 underline")).pack()
            Label(rulesWindow, text="There is no real goal in this game.\nYou just have to rate the pairs of shoes according to your tastes by selecting either the 'like' button or the 'dislike' button.\nAnd do this until you've seen all the pairs.", bg="#DB9898", font=("Helvetica 13")).place(relx = 0.014,rely=0.1)

        helpButton = Button(window, text="?", command=rulesWindow, height=2, width=4, bg="#DB9898", fg="black", borderwidth=4, relief="groove")
        helpButton.place(
            relx = 0.973,
            rely = 0.035,
            anchor = 'center'
        )

        # Start Button
        startButton = Button(window, text="Start !", command=None, height=2, width=4, bg="#DB9898", fg="black", borderwidth=4, relief="groove")
        startButton.pack()
        
        window.mainloop() # Show the window ---------------------------------------------------------------------------



    if __name__ == "__main__":
        mainWindow()