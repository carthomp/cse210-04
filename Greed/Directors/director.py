import random
from Greed.Common.point import Point
from Greed.Common.color import Color
from Greed.Actors.actor import Actor
from Greed.Actors.rock import Rock
from Greed.Actors.gem import Gem


class Director():
    """
    Responsibility: Start the game and direct its flow
    Specifics -
        Start the game
        Manage the input phase of the game (take keypress from user)
        Manage the update phase of the game (update positions, collisions, points, etc)
        Manage the output phase of the game (show updated positions in preparation for next move)
    """

    def __init__(self, keyboard_service, video_service, rows, cols, cell_size, font_size):
        """Constructs a new Director using the specified keyboard and video services.

        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        self._rows = rows
        self._cols = cols
        self._cell_size = cell_size
        self._font_size = font_size
        self._score = 0

    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()

    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the robot.

        Args:
            cast (Cast): The cast of actors.
        """
        robot = cast.get_first_actor("robots")
        velocity = self._keyboard_service.get_direction()
        robot.set_velocity(velocity)

    def _do_updates(self, cast):
        """Updates the robot's position and resolves any collisions with artifacts.

        Args:
            cast (Cast): The cast of actors.
        """
        banner = cast.get_first_actor("banners")
        robot = cast.get_first_actor("robots")
        gems = cast.get_actors("gems")
        rocks = cast.get_actors("rocks")

        new_rocks = random.randint(-10, 2)
        new_gems = random.randint(-10, 2)
        if new_rocks < 0:
            new_rocks = 0
        if new_gems < 0:
            new_gems = 0
        for i in range(new_rocks):
            rock = self._make_new_rock()
            cast.add_actor("rocks", rock)
        for i in range(new_gems):
            gem = self._make_new_gem()
            cast.add_actor("gems", gem)

        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        robot.move_next(max_x, max_y)

        for gem in gems:
            gem.move_next(max_x, max_y)
            if robot.get_position().equals(gem.get_position()):
                score = gem.add_score(self._score)
                self._score = score
                cast.remove_actor("gems", gem)
            position = gem.get_position()
            if position.get_y() >= max_y:
                cast.remove_actor("gems", gem)

        for rock in rocks:
            rock.move_next(max_x, max_y)
            if robot.get_position().equals(rock.get_position()):
                score = rock.add_score(self._score)
                self._score = score
                cast.remove_actor("rocks", rock)
            position = rock.get_position()
            if position.get_y() >= max_y:
                cast.remove_actor("rocks", rock)

        banner.set_text(f"Score: {self._score}")

    def _do_outputs(self, cast):
        """Draws the actors on the screen.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()

    def _make_new_rock(self):
        x = random.randint(1, self._cols - 1)
        y = 0
        position = Point(x, y)
        position = position.scale(self._cell_size)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)

        velocity = Point(0, self._cell_size)

        rock = Rock()
        rock.set_text("o")
        rock.set_font_size(self._font_size)
        rock.set_color(color)
        rock.set_position(position)
        rock.set_velocity(velocity)
        return rock

    def _make_new_gem(self):
        x = random.randint(1, self._cols - 1)
        y = 0
        position = Point(x, y)
        position = position.scale(self._cell_size)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)

        velocity = Point(0, self._cell_size)

        gem = Gem()
        gem.set_text("*")
        gem.set_font_size(self._font_size)
        gem.set_color(color)
        gem.set_position(position)
        gem.set_velocity(velocity)
        return gem
