# Desktop Icon Repair
# v2 using config file
##########

import os
import getpass
import shutil
from tkinter import *

class App():

    def __init__(self,master):

        self.message_frame = Frame(master)
        self.message_frame.pack()

        self.message_text = StringVar()
        self.message_text.set('Icon repair completed.')
        self.message_label = Label(self.message_frame, textvariable = self.message_text)
        self.message_label.pack()

def read_config_file(filename):
    icons_folder = ''
    options = []
    with open(filename, 'r') as opened:
        readtext = opened.read()
        lines = readtext.split('\n')
        for line in lines:
            if '[ICONS_FOLDER]' in line:
                icons_folder = line[14:]

            if '[OPTION]' in line:
                option_text = line[8:]
                split_option_text = option_text.split('%USERNAME%')
                first = split_option_text[0]
                second = split_option_text[1]
                result = first + username + second
                options.append(result)
        
    return icons_folder, options

# Main
##########

# Get the username of the logged-in user.
username = getpass.getuser()

# Read where to copy icons from, and which places to copy to, from the .ini
config_file = 'dir.ini'
icons_folder, options = read_config_file(config_file)
icons = os.listdir(icons_folder)

# Things we won't try to copy as files.
fails = ['$RECYCLE.BIN','Applications by Subject']

for option in options:
    for icon in icons:
        if icon not in fails:
            try:
                shutil.copy(icons_folder + icon,option)
            except:
                print('failed on',icon)

    try:
        shutil.copytree(icons_folder + '/Applications by Subject',option + '/Applications by Subject')
    except:
        print('failed')

# Report.
root = Tk()
root.title('Desktop Icon Repair')
mainapp = App(root)

root.mainloop()
