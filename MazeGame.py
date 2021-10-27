import turtle


# Maze Game outline Class(spaces and blocks)
class MazeGame(turtle.Turtle) :
    def __init__(self) :
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)


# Final Victory cell
class FinalCell(turtle.Turtle) :
    def __init__(self) :
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("green")
        self.penup()
        self.speed(0)


# User Box in maze
class User(turtle.Turtle) :
    def __init__(self) :
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("red")
        self.penup()
        self.speed(0)

    # On keyboard actions updating px to make the Player movements
    def move_up(self) :
        if (self.xcor(), self.ycor() + 24) not in blocks :
            self.goto(self.xcor(), self.ycor() + 24)
            if (self.xcor(), self.ycor()) == final_cell :
                self.write("Congratulations!! You have cleared the level", font=("Arial", 14, "bold"))

    def move_down(self) :
        if (self.xcor(), self.ycor() - 24) not in blocks :
            self.goto(self.xcor(), self.ycor() - 24)
            if (self.xcor(), self.ycor()) == final_cell :
                self.write("Congratulations!! You have cleared the level", font=("Arial", 14, "bold"))

    def move_left(self) :
        if (self.xcor() - 24, self.ycor()) not in blocks :
            self.goto(self.xcor() - 24, self.ycor())
            if (self.xcor(), self.ycor()) == final_cell :
                self.write("Congratulations!! You have cleared the level", font=("Arial", 14, "bold"))

    def move_right(self) :
        if (self.xcor() + 24, self.ycor()) not in blocks :
            self.goto(self.xcor() + 24, self.ycor())
        if (self.xcor(), self.ycor()) == final_cell :
            self.write("Congratulations!! You have cleared the level", font=("Arial", 14, "bold"))


def difficulty_level(level) :
    pattern = []
    if level == "easy" :
        pattern = [
            "XXXXXXXXXXXXXXXXXXXXXXXX",
            "XU                     X",
            "XXXXXXXXXXXXXXXXXXXXXX X",
            "XXXXXXXXXXXXXXXXXXXXXX X",
            "XXXXXXXXXXXXXXXXXXXXXX X",
            "XXXXXXXXXXXXXXXXXXXXXX X",
            "XXXXXXXXXXXXXXXXXXXXXX X",
            "XXXXXXXXXXXXXXXXXXXXXX X",
            "XXXXXXXXXXXXXXXXXXXXXX X",
            "XXXXXXXXXXXXXXXXXXXXXX X",
            "XXXXXXXXXXXXXXXXXXXXXX X",
            "XXXXXXXXXXXXXXXXXXXXXX X",
            "XXXXXXXXXXXXXXXXXXXXXX X",
            "XXXXXXXXXXXXXXXXXX     X",
            "XXXXXXXXXXXXXXXXXX XXX X",
            "XXXXXXXXXXXXXXXX   XXX X",
            "XXXXX X          XXXXX X",
            "XX    XXXX    XXXXXXXX X",
            "XXX   XXXXX      XXXXX X",
            "XXXXXXXXXX     XXXXXXX X",
            "XXXXF      XX  XXXXXXX X",
            "XXXXXXXXXXXXXXXXXXXXX  X",
            "X                     XX",
            "XXXXXXXXXXXXXXXXXXXXXXXX",
        ]
    elif level == "intermittent" :
        pattern = [
            "XXXXXXXXXXXXXXXXXXXXXXXX",
            "X         XXXXXXXXXXXXXX",
            "X  XXXXX  XXXXXXXXXXXXXX",
            "XU XXXXX  XXXXXXXXXXXXXX",
            "XXXXXXX        XXXXXXXXX",
            "XXXXXX  XXXXX   XXXXXXXX",
            "XXX    XXXXXX   XXXXXXXX",
            "XXXXXXXXXXXXX   XXXXXXXX",
            "XXXXXXXXXXXXXXX    XXXXX",
            "XXXXXXXXXX       XXXXXXX",
            "XXXXXXXXXXXX  XXXXXXXXXX",
            "XXXXXXXXXXX  XXXXXXXXXXX",
            "XXXXXXXXXXXX   XXXXXXXXX",
            "XXX          XXXXXXXXXXX",
            "XXXX     XXXXXXXXXXXXXXX",
            "XXX     XXXXXXXXXXXXXXXX",
            "XXX   X         XXXXXXXX",
            "XX    XXXX    XXXXXXXXXX",
            "XXX   XXXXX      XXXXXXX",
            "XXXXXXXXXXX    XXXXXXXXX",
            "XXXX       XX  XXXXXXXXX",
            "XXXXXXXXXXXXXX XXXXXXXXX",
            "XXXXXXXXXXXXX          X",
            "XXXXXXXXXXXXXXXXXXXXXXFX",
        ]
    elif level == "hard" :
        pattern = [
            "XXXXXXXXXXXXXXXXXXXXXXXX",
            "X                    X X",
            "X  XXXXX  XXXXXXXXXX  UX",
            "X  XXXXX  XXXXXXXXXXXX X",
            "XXXXXXX        XXXXXXX X",
            "XXXXXX  XXXXX   XXXXXX X",
            "XXX    XXXXXX   XXXXXX X",
            "XXXXXXXXXXXXX   XXXXXX X",
            "XXXXXXXXXXXXXXX    XXX X",
            "XXXXXXXXXX       XXXX  X",
            "XXXXXXXXXXXX  XXXXXXX XX",
            "XXXXXXXXXXX  XXXXXXX XXX",
            "XXXXXXXXXXXX   XXXX XXXX",
            "XXX          XXXXX XXXXX",
            "XXXX     XXXXXXXXX XXXXX",
            "XXX     XXXXXXXXXXXXXXXX",
            "XXXXX X         XXXXXXXX",
            "XX    XXXX    XXXXXXXXXX",
            "XXX   XXXXX      XXXXXXX",
            "XXXXXXXXXX     XXXXXXXXX",
            "XXXX       XX  XXXXXXXXX",
            "XXXXXX XX  XXXXXXXXXXXXX",
            "XXXXXX   X             X",
            "XXXXXXXXXXXXXXXXXXXXXXFX",
        ]

    return pattern


# Based on level stamps Maze,User and Final Cell
def design_maze(pattern) :
    if pattern == "easy" :
        pattern = difficulty_level("easy")
    elif pattern == "intermittent" :
        pattern = difficulty_level("intermittent")
    else :
        pattern = difficulty_level("hard")
    for y_value in range(len(pattern)) :
        for x_value in range(len(pattern[y_value])) :
            pattern_value = pattern[y_value][x_value]
            x_axis = -288 + (x_value * 24)
            y_axis = 288 - (y_value * 24)
            if pattern_value == "X" :
                maze.goto(x_axis, y_axis)
                maze.stamp()
                blocks.append((x_axis, y_axis))
            elif pattern_value == "U" :
                user.goto(x_axis, y_axis)
            elif pattern_value == "F" :
                final.goto(x_axis, y_axis)


# Supporting Functions
def getVictoryCell(pattern) :
    ret_cordinates = ()
    if pattern == "easy" :
        pattern = difficulty_level("easy")
    elif pattern == "intermittent" :
        pattern = difficulty_level("intermittent")
    else :
        pattern = difficulty_level("hard")
    for y_value in range(len(pattern)) :
        for x_value in range(len(pattern[y_value])) :
            pattern_value = pattern[y_value][x_value]
            x_axis = -288 + (x_value * 24)
            y_axis = 288 - (y_value * 24)
            if pattern_value == "F" :
                ret_cordinates = (x_axis, y_axis)
                break
    return ret_cordinates


def game_settings(level) :
    design_maze(level)
    screen = turtle.Screen()
    screen.title("Maze (Difficulty :" + level + ")")
    screen.bgcolor("black")
    screen.screensize()
    screen.setup(width=1.0, height=1.0)

    screen.onkey(user.move_up, "w")
    screen.onkey(user.move_down, "s")
    screen.onkey(user.move_left, "a")
    screen.onkey(user.move_right, "d")
    screen.listen()
    screen.mainloop()


# User Input
is_ExceptionThrown = False
try :
    user_input = int(input("""Select the Difficulty Level
                            : Enter 1 for easy
                            : Enter 2 for intermittent
                            : Enter 3+ for Hard
                        Reach Green Box to Win!
                        Note: "A" --> Left Movement
                              "W" --> Up Movement
                              "S" --> Down Movement
                              "D" --> Right Movement
                             """))
except ValueError  :
    print("Game Loading Failed as you have not provided the Input in number")
    is_ExceptionThrown = True

if not is_ExceptionThrown :
    if user_input == 1 :
        level = "easy"
    elif user_input == 2 :
        level = "intermittent"
    else :
        level = "hard"

    final_cell = getVictoryCell(level)
    blocks = []
    maze = MazeGame()
    user = User()
    final = FinalCell()
    game_settings(level)
