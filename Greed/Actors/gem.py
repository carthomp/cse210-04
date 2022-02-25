from greed.Actors.actor import Actor
from greed.Common.point import Point
class Gem(Actor):
    """
    Responsibility: Exist as an actor, and add to the score when touched
    Specifics -
        Make a method that takes the current score, adds one to it, and returns the new score
    """
    def __init__(self):
        super().__init__()
        self.new_score = 0

    def get_score(self):
        return self.new_score


    def add_score(self, score):
        return score + 100


