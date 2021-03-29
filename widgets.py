import generator as gen
import tkinter as tk


window = tk.Tk()
window.title("Content Generator")
window.geometry("600x800")
window.configure(bg="gray90")

# create 8x3 grid system for widgets
for i in range(8):  # number of rows
    if i == 0:
        window.rowconfigure(i, weight=1, minsize=5)
    elif i != 7:
        window.rowconfigure(i, weight=1, minsize=5)
    else:
        window.rowconfigure(i, weight=20, minsize=100)
    for j in range(3):  # number of columns
        if j != 1:
            window.columnconfigure(j, weight=1, minsize=10)
        else:
            window.columnconfigure(j, weight=5, minsize=100)
        frame = tk.Frame(master=window)
        frame.grid(row=i, column=j)

# program title
lbl_title = tk.Label(text="Content Generator")
lbl_title.config(font=("Helvetica", 24), bg="gray90")
lbl_title.grid(row=0, column=1, sticky="s")

# primary keyword label, entry field
lbl_primary = tk.Label(text="Primary keyword")
lbl_primary.config(font=("Helvetica", 12), bg="gray90")
lbl_primary.grid(row=1, column=1, sticky="s")
ent_primary = tk.Entry(bg="white", width=25)
ent_primary.config(font=("Helvetica", 12), justify=tk.CENTER,
                   highlightthickness=0)
ent_primary.grid(row=2, column=1, sticky="n")

# secondary keyword label, entry field
lbl_secondary = tk.Label(text="Secondary keyword")
lbl_secondary.config(font=("Helvetica", 12), bg="gray90")
lbl_secondary.grid(row=3, column=1, sticky="s")
ent_secondary = tk.Entry(bg="white", width=25)
ent_secondary.config(font=("Helvetica", 12), justify=tk.CENTER,
                     highlightthickness=0)
ent_secondary.grid(row=4, column=1, sticky="n")

# generate button
btn_generate = tk.Button(
    window,
    text="Generate",
    width=10,
    height=2,
    bg="gray50",
    fg="black",
    highlightthickness=0,
    font=("Helvetica", 14)
)
btn_generate.grid(row=5, column=1)

# output checkbox for creating output.csv file
checked = tk.IntVar()
chk_output = tk.Checkbutton(
    window,
    text="Create output.csv",
    variable=checked,
    bg="gray90",
    font=("Helvetica", 12)
)
chk_output.grid(row=6, column=1)

# text box used to display generated content
txt_content = tk.Text(height=30)
txt_content.config(font=("Helvetica", 12), highlightthickness=0,
                   wrap=tk.WORD)
txt_content.grid(row=7, column=1, sticky="n")


def feedback(event):
    """Provides visual feedback after clicking generate button.

    Args:
        event (obj): Tkinter event object.
    """
    # animates generate button
    btn_generate.config(width=8, fg="red")
    btn_generate.after(100, lambda: btn_generate.config(width=10,
                                                        fg="black"))

    # clears out text box in GUI if not empty, then displays generating msg
    text_length = txt_content.get("1.0", tk.END)
    if len(text_length) != 0:
        txt_content.delete("1.0", tk.END)
    txt_content.insert(tk.END, "Generating...")

    # retrieve primary and secondary keywords from fields in GUI
    primary = ent_primary.get().lower()
    secondary = ent_secondary.get().lower()

    fields = [primary, secondary, txt_content]
    options = [checked.get()]
    btn_generate.after(200, lambda: gen.generate_GUI(event, fields, options))


# binds event handler to generate button
btn_generate.bind("<ButtonRelease-1>", feedback)
