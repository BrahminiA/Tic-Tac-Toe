from tkinter import *        
import tkinter.messagebox    
root = Tk() 
root.title("TIC TAC TOE")           
bclick = True                   
def tictac(buttons):                         
    global bclick                              
    if buttons["text"] == " " and bclick==True:         
        buttons["text"] = "X"
        bclick = False
    elif buttons["text"] == " " and bclick == False:
        buttons["text"] = "O"
        bclick = True
    if (button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X'):
        tkinter.messagebox.showinfo("Congratulations", "Winner is Brahmini")
        exit()
        #X=Brahmini
        #O=Lasya
    elif (button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X'):
        tkinter.messagebox.showinfo("Congratulations", "Winner is Brahmini")
    elif (button7['text'] == 'X' and button8['text'] == 'X' and button9['text'] == 'X'):
        tkinter.messagebox.showinfo("Congratulations", "Winner is Brahmini")
    elif (button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X'):
        tkinter.messagebox.showinfo("Congratulations", "Winner is Brahmini")
    elif (button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X'):
        tkinter.messagebox.showinfo("Congratulations", "Winner is Brahmini")

    elif (button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X'):
        tkinter.messagebox.showinfo("Congratulations", "Winner is Brahmini")
    elif (button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X'):
        tkinter.messagebox.showinfo("Congratulations", "Winner is Brahmini")

    elif (button1["text"] == "O" and button2["text"] == "O" and button3["text"] == "O" or
                          button1["text"] == "O" and button5["text"] == "O" and button9["text"] == "O" or
                          button4["text"] == "O" and button5["text"] == "O" and button6["text"] == "O" or
                          button7["text"] == "O" and button8["text"] == "O" and button9["text"] == "O" or
                          button1["text"] == "O" and button4["text"] == "O" and button7["text"] == "O" or
                          button2["text"] == "O" and button5["text"] == "O" and button8["text"] == "O" or
                          button3["text"] == "O" and button6["text"] == "O" and button9["text"] == "O" or
                          button3["text"] == "O" and button5["text"] == "O" and button7["text"] == "O"):
        tkinter.messagebox.showinfo("Congratulations", "Winner is Lasya")
    
        exit()


button1 = Button(root, text=" ", font=('Arial 30 bold'), bg="pink" ,fg="blue" ,height=4, width=8, command=lambda:tictac(button1))
button1.grid(row=0, column=0, sticky=S + N + E+ W)
button2 = Button(root, text=" ", font=('Arial 30 bold'),bg="pink" ,fg="blue" , height=4, width=8, command=lambda: tictac(button2))
button2.grid(row=0, column=1, sticky=S + N + E+ W)
button3 = Button(root, text=" ", font=('Arial 30 bold'),bg="pink" ,fg="blue" , height=4, width=8, command=lambda: tictac(button3))
button3.grid(row=0, column=2, sticky=S + N + E+ W)
button4 = Button(root, text=" ", font=('Arial 30 bold'),bg="pink" ,fg="blue" , height=4, width=8, command=lambda: tictac(button4))
button4.grid(row=1, column=0, sticky=S + N + E+ W)
button5 = Button(root, text=" ", font=('Arial 30 bold'),bg="pink" ,fg="blue" , height=4, width=8, command=lambda: tictac(button5))
button5.grid(row=1, column=1, sticky=S + N + E+ W)
button6 = Button(root, text=" ", font=('Arial 30 bold'),bg="pink" ,fg="blue" , height=4, width=8, command=lambda: tictac(button6))
button6.grid(row=1, column=2, sticky=S + N + E+ W)
button7 = Button(root, text=" ", font=('Arial 30 bold'),bg="pink" ,fg="blue" , height=4, width=8, command=lambda: tictac(button7))
button7.grid(row=2, column=0, sticky=S + N + E+ W)
button8 = Button(root, text=" ", font=('Arial 30 bold'),bg="pink" ,fg="blue" , height=4, width=8, command=lambda: tictac(button8))
button8.grid(row=2, column=1, sticky=S + N + E+ W)
button9 = Button(root, text=" ", font=('Arial 30 bold'),bg="pink" ,fg="blue" , height=4, width=8, command=lambda: tictac(button9))
button9.grid(row=2, column=2, sticky=S + N + E+ W)

root.mainloop()
