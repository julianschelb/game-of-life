# ===========================================================================
#                            Conway's Game of Life
# ===========================================================================

import click
import time
from game import Grid


@click.command()
@click.option("--width", default=80, help="Width of grid.")
@click.option("--height", default=25, help="Height of grid.")
@click.option("--fps", default=4, help="Refresh rate of grid")
def main(width, height, fps):

    # Initializing the grid
    game = Grid(width, height)

    # Keep updating the grid
    while True:
        time.sleep(1 / fps)
        game.update()


if __name__ == "__main__":
    main()
