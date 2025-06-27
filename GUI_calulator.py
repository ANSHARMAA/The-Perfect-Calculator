import tkinter as tk

root = tk.Tk()
root.title("Calculator:- ")
root.geometry("340x475")
root.configure(bg="light blue")

def calculate():
    try:
        result = eval(display_board.get())
        display_board.delete(0 , tk.END)
        display_board.insert(0 , str(result))
    except ZeroDivisionError as error:
        print(error)
        display_board.delete(0, tk.END)
        display_board.insert(0, "Error")
    except ValueError as error:
        print(error)
        display_board.delete(0, tk.END)
        display_board.insert(0, "Error")
    except TypeError as error:
        print(error)
        display_board.delete(0, tk.END)
        display_board.insert(0, "Error")
    except SyntaxError:
        display_board.delete(0, tk.END)
        display_board.insert(0, "Syntax Error")
    

def click(value):

    display_board.insert(tk.END , value)

def clear_display():
    display_board.delete(0 , tk.END)

def backspace():
    current = display_board.get()
    display_board.delete(0 , tk.END)
    display_board.insert(0 ,current[:-1])

greet = tk.Label(root , text="Hello User!" , fg="black")
greet.grid(pady=10 , padx=10 )

display_board = tk.Entry(root , font=("Arial" , 20) , justify="right")
display_board.grid(row=2, column=0 , columnspan=4, padx=5 , pady=5)


 
btn = tk.Button(root , text="AC" , width=6, height=3 , fg="gray", command=clear_display)
btn.grid( pady=5 , row=10 , column=0)


btn = tk.Button(root , text="1" , width=6, height=3 , fg="gray" , command=lambda: click("1"))
btn.grid(pady=5 ,row=11 , column=0)

btn = tk.Button(root , text="4" , width=6, height=3 , fg="gray", command=lambda: click("4"))
btn.grid(pady=5 ,row=12, column=0)


btn = tk.Button(root , text="7" , width=6, height=3 , fg="gray", command=lambda: click("7"))
btn.grid(pady=5 ,row=13, column=0)


btn = tk.Button(root , text="00", width=6, height=3 , fg="gray", command=lambda: click("00"))
btn.grid(pady=5 ,row=14, column=0)


btn = tk.Button(root , text="%", width=6, height=3 , fg="gray", command=lambda: click("%"))      # first gap
btn.grid(pady=5 ,row=10, column=1)


btn = tk.Button(root , text="2", width=6, height=3 , fg="gray", command=lambda: click("2"))
btn.grid(pady=5 ,row=11, column=1)


btn = tk.Button(root , text="5" , width=6, height=3 , fg="gray", command=lambda: click("5"))
btn.grid(pady=5 ,row=12, column=1)

btn = tk.Button(root , text="8" , width=6, height=3 , fg="gray", command=lambda: click("8"))
btn.grid(pady=5 ,row=13, column=1)


btn = tk.Button(root , text="0" , width=6, height=3 , fg="gray", command=lambda: click("0"))
btn.grid(pady=5 ,row=14, column=1)


btn = tk.Button(root , text="⇐", width=6, height=3 , fg="gray", command=backspace)      # second gap
btn.grid( padx=15 , pady=5 ,row=10, column=2)

btn = tk.Button(root , text="3" , width=6, height=3 , fg="gray", command=lambda: click("3"))      
btn.grid( padx=15 , pady=5 ,row=11, column=2)


btn = tk.Button(root , text="6" , width=6, height=3 , fg="gray", command=lambda: click("6"))      
btn.grid( padx=15 , pady=5 ,row=12, column=2)


btn = tk.Button(root , text="9" , width=6, height=3 , fg="gray", command=lambda: click("9"))      
btn.grid( padx=15 , pady=5 ,row=13, column=2)


btn = tk.Button(root , text="." , width=6, height=3 , fg="gray", command=lambda: click(".") )      
btn.grid( padx=15 , pady=5 ,row=14, column=2)


btn = tk.Button(root , text="/" , width=6, height=3 , fg="gray", command=lambda: click("/"))      
btn.grid( padx=5 , pady=5 ,row=10, column=3)


btn = tk.Button(root , text="*" , width=6, height=3 , fg="gray", command=lambda: click("*"))      
btn.grid( padx=5 , pady=5 ,row=11, column=3)


btn = tk.Button(root , text="-" , width=6, height=3 , fg="gray" , command=lambda: click("-"))      
btn.grid( padx=10 , pady=5 ,row=12, column=3)


btn = tk.Button(root , text="+", width=6, height=3 , fg="gray", command=lambda: click("+"))      
btn.grid( padx=5 , pady=5 ,row=13, column=3)


btn = tk.Button(root , text="=", width=6, height=3 , fg="gray", command=calculate)      
btn.grid( padx=5 , pady=5 ,row=14, column=3)

exit = tk.Button(root ,text="Exit" , width=4, height=2 , fg="red", command=root.destroy)
exit.grid(padx=5 , pady=5 ,row=16 , column=2 , columnspan=2)

root.mainloop()