# Unity replacement password utility.
# Kay Johnston
# Ready?  Aye ready!

import subprocess
from tkinter import *

# Used to avoid spamming cmd windows.
CREATE_NO_WINDOW = 0x08000000

class App():

    def __init__(self,master):

        # Create a frame to hold a status report.
        self.status_frame = Frame(master)
        self.status_frame.pack()

        # Create a status label.
        self.status = StringVar()
        self.status.set('Ready.')
        self.status_label = Label(self.status_frame, textvariable = self.status)
        self.status_label.pack()

        # Create a frame to hold entry boxes for username and password.
        self.entry_frame = Frame(master)
        self.entry_frame.pack()

        # Create entry boxes.
        self.username_box = Entry_Box(self.entry_frame,'Username:','',10,20)
        self.password_box = Entry_Box(self.entry_frame,'Password:','',10,20)

        # Bind entry boxes to procedures.
        self.username_box.entry.bind('<Return>', self.check_username)
        self.password_box.entry.bind('<Return>', self.set_password)

    # Check for the full name associated with a username, if it is a student username.
    def check_username(self,event):
        username = self.username_box.entry.get()
        if username.upper() in known_students:
            command = 'net user ' + username + ' /domain'
            check = subprocess.Popen(command, stdout = subprocess.PIPE, creationflags = CREATE_NO_WINDOW)
            raw_student_data = str(check.communicate())
            lines = raw_student_data.split('\\r\\n')
            # Clunky, but whatever.
            for l in lines:
                if 'Full Name' in l:
                    self.status.set(l[29:])

    # Set the password for a given user, if it is a student username.
    def set_password(self,event):
        username = self.username_box.entry.get()
        password = self.password_box.entry.get()

        if username.upper() in known_students and password != '':
            try:
                command = 'net user ' + username + ' ' + password + ' /domain'
                subprocess.call(command, creationflags = CREATE_NO_WINDOW)
                self.status.set('Password for ' + username + ' set.')
            except:
                self.status.set('Failed to set password for ' + username + '.')
            # The below would perhaps work with a suitably empowered housekeeping username & password.
            # e.g. auto.operator  ^^
            # It doesn't work with a random staff user, sadly. :(
##            try:
##                cr_user = 'BSFADDCC\\STJU01'
##                print(cr_user)
##                cr_pass = 'winnebago'
##                command = 'psexec -u ' + cr_user + ' -p ' + cr_pass + ' net user ' + username + ' ' + password + ' /domain'
##                subprocess.call(command, creationflags = CREATE_NO_WINDOW)
##                self.status.set('Password for ' + username + ' set.')
##            except:
##                self.status.set('Failed horribly.')
                
        else:
            if password == '':
                self.status.set('Choose a password.')
            else:
                self.status.set('Username ' + username + ' not found.')

# Entry boxes with an attached label.  
class Entry_Box():

    def __init__(self,master,nametext,default,w1,w2):
        # Create a frame for this entry box.
        self.frame = Frame(master, padx = 6)
        self.frame.pack(side = TOP)

        # Create a label.
        self.label = Label(self.frame,text = nametext,width = w1)
        self.label.pack(side = LEFT)

        # Create an entry box.
        self.entry = Entry(self.frame, width = w2)
        self.entry.pack(side = LEFT)
        self.entry.insert(0,default)

# Queries AD to get a list of known student users.
# Some junk is stripped out, but there's more at the header could do with trimming.
def get_student_list():
    blanks = ['The command completed successfully.','\',','None']
    found = []
    command = 'net group \"Easington CSC Students SG\" /domain'
    students = subprocess.Popen(command, stdout = subprocess.PIPE, creationflags = CREATE_NO_WINDOW)
    raw_student_list = str(students.communicate())
    for b in blanks:
        raw_student_list = raw_student_list.replace(b,'')
    lines = raw_student_list.split('\\r\\n')
    for line in lines:
        s = line.split(' ')
        for entry in s:
            if len(entry) > 1:
                found.append(entry.upper())
    return found
    
known_students = get_student_list()

# Main loop.
root = Tk()
root.title('Autoset')

mainapp = App(root)

root.mainloop()
