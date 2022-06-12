# ===========================================================================
#                            Conway's Game of Life
# ===========================================================================

import click
import time
from game import Grid


@click.command()
@click.option("--width", default=100, help="Width of the draw grid.")
@click.option("--height", default=30, help=" Height of draw grid.")
def main(width, height):
    game = Grid(width, height)
    print(width, height)
    # click.echo(click.style("Hello World!", fg="green"))

    while True:
        time.sleep(1)
        game.update()


if __name__ == "__main__":
    main()
