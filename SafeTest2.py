# Import the required module for text
# to speech conversion
from tkinter import *
import tkinter.ttk as ttk
from gtts import gTTS
from deep_translator import GoogleTranslator
import playsound

ttk.output = ""


def lang_options():
    global output
    option = option_variable.get()
    if option == "English":
        # translator
        ttk.output = GoogleTranslator(source='auto', target="en").translate(entry.get("1.0", "end-1c"))
    elif option == "French":
        # translator
        ttk.output = GoogleTranslator(source='auto', target="fr").translate(entry.get("1.0", "end-1c"))
    elif option == "Spanish":
        # translator
        ttk.output = GoogleTranslator(source='auto', target="es").translate(entry.get("1.0", "end-1c"))
    elif option == "Mandarin":
        # translator
        ttk.output = GoogleTranslator(source='auto', target="zh-CN").translate(entry.get("1.0", "end-1c"))


def speak():
    lang_options()

    result.config(text=ttk.output)

    # Passing the text and language to the engine,
    # here we have marked slow=False. Which tells
    # the module that the converted audio should
    myobj = gTTS(text=ttk.output, slow=False)

    # Saving the converted audio in a mp3 file named
    # welcome
    myobj.save("speech.mp3")

    # Playing the converted file
    playsound.playsound('speech.mp3', True)


root = Tk()

root.geometry("700x500")
root.title("Translate")
root.resizable(False, False)

# Dark/Light mode toggle
is_on = True

def switch():
    global is_on

    # Determine is on or off
    if is_on:
        onButton.config(image=off)
        is_on = False
        root.tk.call("set_theme", "light")
    else:
        onButton.config(image=on)
        is_on = True
        root.tk.call("set_theme", "dark")


# Define Our Images
on = PhotoImage(file="dark.png")

off = PhotoImage(file="light.png")

onButton = Button(root, image=on, bd=0, cursor="hand2", command=switch)
onButton.place(x=630, y=25)
#

root.tk.call("source", "azure.tcl")
root.tk.call("set_theme", "dark")


labelTittle = ttk.Label(root, text="Translator", font=('Helvetica', 32, 'underline'))
labelTittle.place(x=250, y=25)

# prompt = Label(text="Enter Your Birthday:")

# copy/paste https://stackoverflow.com/questions/36990396/automatically-copy-tkinter-text-widget-content-to-clipboard
# stuff like googletrans and messagebox could be useful https://codingshiksha.com/python/python-tkinter-gui-script-to-make-language-translate-app-using-google-translate-api-full-project-for-beginners/
# Flag stuff in options https://morioh.com/p/f900651c5e48


entryValue = StringVar()
option_variable = StringVar()
option_variable.set("English")

# entry = ttk.Entry(root, textvariable=entryValue, width=20)
# entry.place(x=50, y=100)
entry = Text(root, width=30, height=10, borderwidth=5, relief=RIDGE)
entry.place(x=10, y=100)


options = ttk.OptionMenu(root, option_variable, "English", "French", "Spanish", "Mandarin")
options.place(x=550, y=105)

submit = ttk.Button(text="Speak", command=speak).place(x=325, y=450)
# , font=20, bg="#492C1D", fg="white",
# result = Label(text="", fg="white")
# result.place(x=50, y=250)
result = Label(root, width=30, height=10, borderwidth=5, relief=RIDGE)
result.place(x=260, y=100)


root.mainloop()