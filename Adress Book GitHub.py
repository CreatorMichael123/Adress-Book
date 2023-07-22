import tkinter as tkinter

window = tk.Tk()
window.title("Address Entry Form")

window.columnconfigure(0, weight=1, minsize=75)
window.columnconfigure(1, weight=5, minsize=500)
for i in range(7):
    window.rowconfigure(i, weight=1, minsize=20)

label_fn = tk.Label(window, text='First Name:')
label_fn.grid(row=0, column=0)
entry_fn = tk.Entry(window)
entry_fn.grid(row=0, column=1, sticky='enws')

label_ln = tk.Label(window, text='Last Name:')
label_ln.grid(row=1, column=0)
entry_ln = tk.Entry(window)
entry_ln.grid(row=1, column=1, sticky='enws')

label_a = tk.Label(window, text='Adress:')
label_a.grid(row=2, column=0)
entry_a = tk.Entry(window)
entry_a.grid(row=2, column=1, sticky='enws')

label_city = tk.Label(window, text='City:')
label_city.grid(row=3, column=0)
entry_city = tk.Entry(window)
entry_city.grid(row=3, column=1, sticky='enws')

label_state = tk.Label(window, text='State:')
label_state.grid(row=4, column=0)
entry_state = tk.Entry(window)
entry_state.grid(row=4, column=1, sticky='enws')

label_zip = tk.Label(window, text='Zip Code:')
label_zip.grid(row=5, column=0)
entry_zip = tk.Entry(window)
entry_zip.grid(row=5, column=1, sticky='enws')

def handler_clear():
    