#import packages
from textblob import TextBlob
from tkinter import *
import tkinter as tk


checker = Tk()
checker.geometry('500x500')
checker.title("Spellar")


def corrector():
    input_word = Entry1.get()
    w = TextBlob(input_word)
    corrected_word = str(w.correct())
    Entry2.delete(0, END)
    Entry2.insert(0, corrected_word)


Label(checker, text="Spelling Corrector", font="Arial 25 bold", fg="lightblue", bg="white").pack()
frame1 = tk.Frame(checker)
frame1.pack(pady=10)
Label(frame1, text="Enter a word:", font="Arial 15").pack(side="left", pady=20)


#create an input field for an input word that is incorrect.
Entry1 = Entry(frame1, width=20)
Entry1.pack(side="left", padx=10)
frame2 = tk.Frame(checker)
frame2.pack(pady=10)


#create a button to correct the word
Button(frame2, text="Correct It", font="Arial 15", command=corrector).pack(pady=10)


#create a label to display the correct text
Label(frame2, text="Correct words:", font="Arial 15").pack(pady=10)
Entry2 = Entry(frame2, width=25)
Entry2.pack(pady=10)


#run the tkinter window
checker.mainloop()
