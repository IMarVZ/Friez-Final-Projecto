"""

SDEV 140
Final Project

Friez is a software used for customers to order drinks.
Moreover, Friez only offers cold drinks ranging from a variety of fruit teas, herbal tea, and cifferent types of coffees.
"""

#imports
from tkinter import *
import tkinter as tk #import tkinter
from tkinter import messagebox #import messagebox
from PIL import Image, ImageTk #import image

#Starts window up, Titles the Window, max and min size possible, so user can not resize
window = tk.Tk()
window.geometry("600x650")
window.title("FRIEZ")
window.minsize(600, 650)
window.maxsize(600, 650)


frameOne = tk.LabelFrame(window) #Placeholder for Quit button
frameNew = tk.LabelFrame(window, border= False) #Specifically for images
frameTwo = tk.LabelFrame(window) #Placeholder for Label for asking what drink
frameThree = tk.LabelFrame(window) #Placeholder for asking if they want coffee or Tea
frameFour = tk.LabelFrame(window) #Placeholder for Label for asking what type of drink
frameFive = tk.LabelFrame(window)#Placeholder for Label for displaying drinks 
frameSix = tk.LabelFrame(window) ##Placeholder for Done button and Reset button

#padx or pady adds padding so it does not look clumped
frameOne.pack()
frameNew.pack()
frameTwo.pack(pady=10) 
frameThree.pack(pady=10)
frameFour.pack(pady=10)
frameFive.pack(pady=10)
frameSix.pack(pady=10)

#Logo, and all other images for drinks
image = Image.open("FRIEZ.png")
image = image.resize((200,200))#resizes image
image = ImageTk.PhotoImage(image)

imageLabel = tk.Label(frameNew, image=image)
imageLabel.pack()

#all the other images used for showing what drink user wants
coldBrewImage = Image.open("cold.png")
coldBrewImage = ImageTk.PhotoImage(coldBrewImage)

frappuchinoImage = Image.open("frappuchino.png")
frappuchinoImage = ImageTk.PhotoImage(frappuchinoImage)

icedCoffeeImage = Image.open("iced.png")
icedCoffeeImage = ImageTk.PhotoImage(icedCoffeeImage)

matchaImage = Image.open("matcha.png")
matchaImage = ImageTk.PhotoImage(matchaImage)

raspberryImage = Image.open("raspberry.png")
raspberryImage = ImageTk.PhotoImage(raspberryImage)

peachImage = Image.open("peach.png")
peachImage = ImageTk.PhotoImage(peachImage)

pomeImage = Image.open("pomegranate.png")
pomeImage = ImageTk.PhotoImage(pomeImage)

#Closes program
def quit():
    window.destroy()

#function for when it is called, lays out all the drinks if user wants coffee based drinks
def coffeeOptions():
    c = tk.IntVar()

#disables buttons so user can't press them again, can be reset with reset button
    buttonCoffee.config(state='disabled') 
    buttonTea.config(state='disabled')
#radio buttons for what drink type user wants
    coldBrew = tk.Radiobutton(frameFive, text = "Cold Brew", variable = c, value = 1)
    frap = tk.Radiobutton(frameFive, text = "Frappuchino", variable = c, value = 2)
    icedCoffee = tk.Radiobutton(frameFive, text = "Iced Coffee", variable = c, value = 3)
    coldBrew.pack()
    frap.pack()
    icedCoffee.pack()


#function for when it is called, lays out all the drinks if user wants tea based drinks
def teaOptions():
    t = tk.IntVar()
 
#disables buttons so user can't press them again, can be reset with reset button
    buttonCoffee.config(state='disabled')
    buttonTea.config(state='disabled')

#displays all options for the type of drink they'd like
    matcha = tk.Radiobutton(frameFive, text = "Matcha Tea", variable = t, value = 1)
    raspberry = tk.Radiobutton(frameFive, text = "Raspberry Tea", variable = t, value = 2)
    peach = tk.Radiobutton(frameFive, text = "Peach Tea", variable = t, value = 3)
    pome = tk.Radiobutton(frameFive, text = "Pomegranate Tea", variable = t, value = 4)
    matcha.pack()
    raspberry.pack()
    peach.pack()
    pome.pack()

#Function to reset everything so that user can get different drinks
def reset():

    buttonCoffee.config(state='normal') #resets buttons to normal state so they could be clicked again
    buttonTea.config(state='normal')
    
    for i in frameFive.winfo_children(): #destroys all widgets in frameFive which is for the variety of drinks
        i.destroy()

#Function after creating a selection
def done():
    
    if not frameFive.winfo_children(): #If user has not selected anything this error code should pop up
        messagebox.showinfo("Error", "Please choose a selection before finishing.")
        return
    
#creates a new window to showcase drink     
    popupWindow = tk.Toplevel()
    popupWindow.title("Enjoy!")
    popupWindow.geometry("600x650")
    popupWindow.minsize(600, 650)
    popupWindow.maxsize(600, 650)

#function so user can go back to main window
    def back():
        popupWindow.destroy()
        window.deiconify()

#new frames for new window, corresponds with descriptions with frames in main window
    subFrameOne = tk.LabelFrame(popupWindow)
    subFrameNew = tk.LabelFrame(popupWindow)
    subFrameOne.pack()
    subFrameNew.pack()

#button to close the whole program
    buttonNewQuit = tk.Button(subFrameOne, text = "Quit", command=quit)
    buttonNewQuit.pack()
#button to go back to main window 
    buttonBack = tk.Button(subFrameOne, text = "Back", command =back)
    buttonBack.pack()

#image to show    
    matchaImageLabel = tk.Label(subFrameNew, image=pomeImage)
    matchaImageLabel.pack()
    


#Label to ask user to select drink
select = tk.Label(frameTwo, text = "Please select a drink:")
select.pack()

#Label to ask user to select drink
selectType = tk.Label(frameFour, text = "Please select what kind of drink:")
selectType.pack()

#Buttons for user accessibility
buttonQuit = tk.Button(frameOne, text = "Quit", command=quit) #button to quit, goes to the quit()
buttonReset = tk.Button(frameSix, text = "Reset", command= reset) #button to reset, goes to reset()
buttonDone = tk.Button(frameSix, text = "Done", command= done) #button to showcase drink when finished,goes to done()
buttonTea = tk.Button(frameThree, text = "Tea", padx=19, command = teaOptions )#button to showcase tea drinks
buttonCoffee =tk.Button(frameThree, text = "Coffee", padx=11, command= coffeeOptions )#button to showcase coffee drinks
buttonTea.pack()
buttonCoffee.pack()
buttonQuit.pack()
buttonReset.pack()
buttonDone.pack()

window.mainloop()



