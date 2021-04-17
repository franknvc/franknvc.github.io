import turtle
import sys

window = turtle.Screen()
window.bgcolor("black")
window.title("A BFS Maze Solver")
window.setup(1300, 700)


class Block(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)

    def draw_block(self, x, y):
        self.goto(x, y)
        self.stamp()


block = Block()

maze = [
    "+++++++++++++++++++++++++++++++++++++++++++++++++++",
    "+               +                                 +",
    "+  ++++++++++  +++++++++++++  +++++++  ++++++++++++",
    "+s          +                 +               ++  +",
    "+  +++++++  +++++++++++++  +++++++++++++++++++++  +",
    "+  +     +  +           +  +                 +++  +",
    "+  +  +  +  +  +  ++++  +  +  +++++++++++++  +++  +",
    "+  +  +  +  +  +  +        +  +  +        +       +",
    "+  +  ++++  +  ++++++++++  +  +  ++++  +  +  ++   +",
    "+  +     +  +          +   +           +  +  ++  ++",
    "+  ++++  +  +++++++ ++++++++  +++++++++++++  ++  ++",
    "+     +  +     +              +              ++   +",
    "++++  +  ++++++++++ +++++++++++  ++++++++++  +++  +",
    "+  +  +                    +     +     +  +  +++  +",
    "+  +  ++++  +++++++++++++  +  ++++  +  +  +  ++   +",
    "+  +  +     +     +     +  +  +     +     +  ++  ++",
    "+  +  +  +++++++  ++++  +  +  +  ++++++++++  ++  ++",
    "+                       +  +  +              ++  ++",
    "+ ++++++             +  +  +  +  +++        +++  ++",
    "+ ++++++ ++++++ +++++++++    ++ ++   ++++++++++  ++",
    "+ +    +    +++ +     +++++++++ ++  +++++++    + ++",
    "+ ++++ ++++ +++ + +++ +++    ++    ++    ++ ++ + ++",
    "+ ++++    +     + +++ +++ ++ ++++++++ ++ ++ ++   ++",
    "+      ++ +++++++e+++     ++          ++    +++++++",
    "+++++++++++++++++++++++++++++++++++++++++++++++++++",
]

grid = [[]]
visited = []
queue = []
solution = {}
start_x, start_y = 0, 0
end_x, end_y = 0, 0


def draw_maze():
    global start_x, start_y, end_x, end_y

    for row in range(len(maze)):
        for column in range(len(maze[row])):
            character = maze[row][column]
            cor_x = -588 + (column * 24)
            cor_y = 288 - (row * 24)

            if character == "+":
                block.color("white")
                block.draw_block(cor_x, cor_y)

            if character == "s":
                block.color("red")
                block.draw_block(cor_x, cor_y)
                start_x, start_y = column, row

            if character == "e":
                block.color("purple")
                block.draw_block(cor_x, cor_y)
                end_x, end_y = column, row

            grid[row].append((cor_x, cor_y))
        grid.append([])


def search_maze():
    visited.append((start_y, start_x))
    queue.append((start_y, start_x))

    while queue:
        s = queue.pop(0)

        neighbours = [(s[0] - 1, s[1]),
                      (s[0], s[1] + 1),
                      (s[0] + 1, s[1]),
                      (s[0], s[1] - 1)]

        for neighbour in neighbours:
            if neighbour not in visited:
                if maze[neighbour[0]][neighbour[1]] == " ":
                    queue.append((neighbour[0], neighbour[1]))
                    visited.append((neighbour[0], neighbour[1]))
                    block.color("green")
                    block.draw_block(grid[neighbour[0]][neighbour[1]][0],
                                     grid[neighbour[0]][neighbour[1]][1])
                    solution[neighbour] = s
                if maze[neighbour[0]][neighbour[1]] == "e":
                    block.color("yellow")
                    block.draw_block(grid[neighbour[0]][neighbour[1]][0],
                                     grid[neighbour[0]][neighbour[1]][1])
                    solution[neighbour] = s
                    break


def back_tracking():
    row, column = end_y, end_x
    block.color("yellow")

    while (row, column) != (start_y, start_x):
        cor_x = -588 + (column * 24)
        cor_y = 288 - (row * 24)

        block.draw_block(cor_x, cor_y)
        row, column = solution[row, column]


def end():
    window.exitonclick()
    sys.exit()


draw_maze()
search_maze()
back_tracking()
end()
