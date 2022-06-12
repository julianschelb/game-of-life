import time
import click


class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = dict()
        self.iter = 0
        self.x = 0
        self.y = 0

    def update(self):
        click.clear()
        click.echo(
            click.style("Conway's Game of Life in Python", fg="green", bold=True)
        )
        click.echo(click.style("Press Ctrl + c to exit", fg="blue", bold=True))
        self.empty_grid()
        self.draw_grid()
        click.echo(click.style(f"Iteration: {self.iter}", fg="green"))

        self.iter = self.iter + 1
        self.x = self.x + 1
        self.y = self.y + 1

    def empty_grid(self):
        self.grid = dict()
        str = ""
        for row in range(0, self.height):
            str = ""
            for i in range(0, self.width):
                if i == self.x and row == self.y:
                    str += "O"
                else:
                    str += "`"
            self.grid[row] = str

    def draw_grid(self):
        for row in self.grid:
            print(self.grid[row])
