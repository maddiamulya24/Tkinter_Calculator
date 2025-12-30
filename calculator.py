import tkinter as tk 
'''Imports the tkinter module tk is an alias for tkinter'''

# Button click handler
def press (v):
    entry.insert(tk.END, v) 
'''Defines a function press that takes a value v as an argument 
and inserts it at the end of the entry widget'''

# clear function 
def clear():
    entry.delete(0, tk.END) 
'''Defines a function clear that deletes all content from the entry widget'''

# calculator function 
def calc():
    try : 
        result = eval(entry.get()) 
        '''entry.get retrieves the expression '''
        
        entry.delete(0, tk.END) 
        '''Clears the entry widget'''
        
        entry.insert(tk.END, result) 
        '''Display the result of expression'''
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error") 
        '''Handles invalid expressions  ex: 5++''' 
        '''Displays "Error" in the entry widget''' 
        
# Create main window
root = tk.Tk()
'''Creates the main application window'''

root.title("Calculator")
'''Sets the title of the window to "Calculator"'''

root.configure(bg="#1e1e1e")
'''Sets the background color of the window'''

root.resizable(False, False)
'''Prevents the window from being resized'''

# Create entry widget for display screen 
entry =tk.Entry(
    root, font=("Times new Roman", 20),
    bg="#2d2d2d",
    fg="white",
    bd=0,
    justify="right"
)
entry.grid(row=0, column=0, columnspan=4, padx=12, pady=12, ipady=10) 
'''Creates an entry widget for displaying input and results
and places it in the grid layout'''

# Button layout
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', 'C', '+',
    '='
]
'''Defines a list of button labels'''
r = 1 
c = 0
for b in buttons:
    cmd = calc if b == '=' else lambda x=b: press(x) 
    tk.Button(
        root, text=b, width=5, height=2,
        bg="#4d4d4d", 
        font=("Calibri", 14),
        bd=0,
        fg= "white",
        command=cmd
    ).grid(row=r, column=c, padx=2, pady=2)
    c += 1
    if c == 4:
        c = 0
        r += 1 
tk.Button( root , text='C', command=clear,font=("Calibri", 14),bg="#ff4d4d", fg="white", 
          bd=0, width=5, height=2
          ).grid(row=r, column=0, padx=2, pady=8)
# Start the main event loop
root.mainloop()