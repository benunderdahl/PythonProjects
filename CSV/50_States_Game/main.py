import turtle as t
import pandas as pd

data = pd.read_csv("50_states.csv")
state_list = data["state"].to_list()
guessed_states = []

screen  = t.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
t.shape(image)
screen.setup(width=800, height=600)

while len(guessed_states) < 50:
    answer = screen.textinput(f"{len(guessed_states)} / 50", "Type a state name: ").title()

    if answer == "Exit":
        missing_states = []
        for state in state_list:
            if state not in guessed_states:
                missing_states.append(state)
        df = pd.DataFrame(missing_states)
        df.to_csv("states_to_learn.csv")
        break

    if answer in state_list:
        guessed_states.append(answer)
        state_data = data[data.state == answer]
        t.hideturtle()
        t.penup()
        t.goto(int(state_data.x.item()), int(state_data.y.item()))
        t.write(answer)

