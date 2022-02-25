"""
Things we need to do in main:
    Import all 8 (or 9) classes
    Set some global variables:
        Frame Rate
        Max width and height of window
        Cell size of an individual cell in the window's grid
        The font size (presumably, this will always be the same as cell size)
        The number of columns
        The number of rows
        The caption (name of the game)
        The starting number of rocks
        The starting number of gems
    Create the banner actor so it can show the score
    Create the robot actor and start it on the bottom middle of the screen
    Create the starting rocks and gems
    Start the game
"""
import random

from Greed.Directors.director import Director

from Greed.Actors.actor import Actor
from Greed.Actors.gem import Gem
from Greed.Actors.rock import Rock
from Greed.Actors.cast import Cast

from Greed.Services.keyboard_service import KeyboardService
from Greed.Services.video_service import VideoService

from Greed.Common.point import Point
from Greed.Common.color import Color


FRAME_RATE = 6
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40
CAPTION = "Greed"
WHITE = Color(255, 255, 255)


def main():

    # create the cast
    cast = Cast()

    # create the banner
    banner = Actor()
    banner.set_text("")
    banner.set_font_size(FONT_SIZE)
    banner.set_color(WHITE)
    banner.set_position(Point(CELL_SIZE, 0))
    cast.add_actor("banners", banner)

    # create the robot
    x = int(MAX_X / 2)
    y = MAX_Y - CELL_SIZE
    position = Point(x, y)

    robot = Actor()
    robot.set_text("#")
    robot.set_font_size(FONT_SIZE)
    robot.set_color(WHITE)
    robot.set_position(position)
    cast.add_actor("robots", robot)

    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service,
                        ROWS, COLS, CELL_SIZE, FONT_SIZE)
    director.start_game(cast)


if __name__ == "__main__":
    main()
