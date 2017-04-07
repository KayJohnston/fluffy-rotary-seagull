# Random name chooser.

from tkinter import *
import random

class Student_List():

    def __init__(self,name,pupils):
        self.name = name
        self.pupils = pupils
        random.shuffle(self.pupils)

class App():

    def __init__(self,master):

        # Create a frame for showing classes to choose from.
        self.show_classes_frame = Frame(master)
        self.show_classes_frame.pack()

        # Default to the first class in the list.  Set initial position and maximum length accordingly.
        self.chosen = StringVar()
        self.chosen.set(choices[0].name)
        self.working = choices[0]
        self.position = 0
        self.max_position = len(self.working.pupils)

        self.choose_class_box = OptionMenu(self.show_classes_frame, self.chosen, *choices_n, command = self.choice_made)
        self.choose_class_box.pack()

        # Create a frame for control buttons.
        self.control_frame = Frame(master)
        self.control_frame.pack()

        self.go_button = Button(self.control_frame, text = 'PICK', command = self.start)
        self.go_button.pack()

        master.bind("<Key>", self.keypress)

        # Create a frame for displaying the result.
        self.result_frame = Frame(master)
        self.result_frame.pack()

        self.result_text = StringVar()
        self.result_text.set('')

        self.result_label = Label(self.result_frame, textvariable = self.result_text, width = 22)
        self.result_label.config(font=("Arial Bold", 70))
        self.result_label.pack()

    def start(self):
        self.result_text.set(self.working.pupils[self.position])
        self.position += 1
        if self.position == self.max_position:
            self.position = 0
            random.shuffle(self.working.pupils)

    def keypress(self,thing):
        self.result_text.set(self.working.pupils[self.position])
        self.position += 1
        if self.position == self.max_position:
            self.position = 0
            random.shuffle(self.working.pupils)

    def choice_made(self,choice):
        for s in choices:
            if s.name == choice:
                random.shuffle(s.pupils)
                self.working = s
                self.position = 0
                self.max_position = len(self.working.pupils)
                self.result_text.set('')

# Setup
choices = []

# Extremely kludgy bit that reads from a SIMS outputted report saved as .csv
filename = 'GHE classes.csv'
with open(filename, 'r') as opened:
    readtext = str(opened.read())

lines = readtext.split('\n')

reading = False

for line in lines:
    if 'Class List Report' in line:

        if reading == True:
            N = Student_List(name,pupils)
            choices.append(N)
            pupils = []
        else:
            reading = True
            pupils = []
        
        partial = line[20:]
        a = partial.split(' ')
        name = a[0]

    elif ',Male' in line or ',Female' in line:
        alice = 'do nowt'
        s = line.split('\"')
        r = s[1].split(', ')
        f = r[1] + ' ' + r[0]
        pupils.append(f)
        

# Workaround to display the right names in the option box.
choices_n = []
for s in choices:
    choices_n.append(s.name)

# Main loop.
root = Tk()
root.title('Random Names')

mainapp = App(root)

root.mainloop()
