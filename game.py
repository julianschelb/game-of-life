# ===========================================================================
#                            Grid Class
# ===========================================================================


from scipy.ndimage import convolve
import click
import numpy


def is_alive(prev, current):
    """Determines whether a cell is alive or dead."""

    # Any live cell with two or
    # three live neighbours survives.
    if (prev == 1) & (2 <= current <= 3):
        return 1

    # Any dead cell with three live
    # neighbours becomes a live cell.
    elif (prev == 0) & (current == 3):
        return 1

    # All other live cells die in the
    # next generation. Similarly, all
    # other dead cells stay dead.
    else:
        return 0


class Grid:
    """
    Grid of variable height and width.
    Initial grid configuration is random.
    Grid is updated according to the rules
    of Conway's Game of Life.
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.iter = 0
        self.kernel = numpy.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])

        # Initiate grid
        self.grid = numpy.random.rand(self.height, self.width)
        self.grid = numpy.round(self.grid)

    def update(self):
        """Update grid according to the rules
        of Conway's Game of Life."""

        # Update terminal output
        click.clear()
        self.draw_header()
        self.draw_grid()
        self.draw_footer()

        self.iter = self.iter + 1  # Increase Iteration counter
        self.update_grid()  # Update cell status

    def draw_grid(self):
        """Print grid on the terminal."""

        str = ""
        for i in range(0, self.grid.shape[0]):
            str = ""
            for j in range(0, self.grid.shape[1]):
                if self.grid[i, j] == 1:
                    str += click.style("O", fg="red")
                else:
                    str += click.style("`", fg="bright_black")
            print(str)

    def update_grid(self):
        """Print grid on the terminal."""

        grid_sum = convolve(self.grid, self.kernel, mode="constant")

        for i in range(0, grid_sum.shape[0]):
            for j in range(0, grid_sum.shape[1]):
                self.grid[i, j] = is_alive(self.grid[i, j], grid_sum[i, j])

    def draw_header(self):
        """Print header and instructions."""
        click.echo(click.style("Conway's Game of Life", fg="green", bold=True))
        click.echo(click.style("Press Ctrl + c to exit", fg="blue", bold=True))

    def draw_footer(self):
        """Print footer with iteration counter."""
        click.echo(click.style(f"Iteration: {self.iter}", fg="green"))
