from soccer_data_api import SoccerDataAPI
from tkinter import *
import json

soccer_data = SoccerDataAPI()


premTest = json.dumps(soccer_data.english_premier())
prem = soccer_data.english_premier()

window = Tk()
window.title("Hello, dan")
window.geometry("800x600+10+20")

label = Label(text="[TEAMS] [Points] [Goal Difference] [Top Scorer]")
listBox = Listbox(window, height=100, width=20, bg="grey", activestyle='dotbox', font='Times', fg="black")
goalListBoxTK = Listbox(window, height=100, width=20, bg="grey", activestyle='dotbox', font='Times', fg="black")
pointsBoxTK = Listbox(window, height=100, width=20, bg="grey", activestyle='dotbox', font='Times', fg="black")
topScorerTK = Listbox(window, height=100, width=40, bg="grey", activestyle='dotbox', font='Times', fg="black")
premTeamsList = []
goalListBox = []
pointsBox = []
topScorerBox = []

for team in prem:
    premTeamsList.append(team["team"])
    goalListBox.append(team["goal_diff"])    
    pointsBox.append(team['points'])
    topScorerBox.append(team["top_scorer"])
listBox.insert(END, *premTeamsList)
pointsBoxTK.insert(END, *pointsBox)
goalListBoxTK.insert(END, *goalListBox)
topScorerTK.insert(END, *topScorerBox)
label.pack(side=TOP)
listBox.pack(side=LEFT)
pointsBoxTK.pack(side=LEFT)
goalListBoxTK.pack(side=LEFT)
topScorerTK.pack(side=LEFT)
window.mainloop()
