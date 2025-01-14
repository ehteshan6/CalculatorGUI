import tkinter as tk
def button_click(number):
    current=display.get()
    display.delete(0,tk.END)
    display.insert(0, current+str(number))

def clear_display():
    display.delete(0,tk.END)

def calculate():
    try:
        result=eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, str(result))
        
    except Exception:
        display.delete(0,tk.END)
        display.insert(0, "Error")




root=tk.Tk()
root.title("Calculator")


display = tk.Entry(root,width=40, font=('Arial',18),borderwidth=5,relief='ridge')
display.grid(row=0, column=0, columnspan=4, padx=10,pady=10)

buttons = [('7',1,0),('8',1,1),('9',1,2),('/',1,3),('4',2,0),('5',2,1),('6',2,2),('*',2,3),('1',3,0),('2',3,1),('3',3,2),('-',3,3),('c',4,0),('0',4,1),('=',4,2),('+',4,3)]
for (text, row, col) in buttons:
    if text == "=":
        btn=tk.Button(root, text=text, width=5, height=2, command=calculate)
    elif text == 'c':
        btn=tk.Button(root, text=text, width=5, height=2, command=clear_display)
    else:
        btn=tk.Button(root, text=text, width=5, height=2, command=lambda t=text: button_click(t))
    btn.grid(row=row, column=col, padx=5, pady=5)

root.mainloop()