from game.casting.actor import Actor


class Artifact(Actor):
    """
    A rock or a gem. 
    
    The responsibility of an Artifact is to provide a value for the player
    to win or lose a point. Rock(o) == -1. Gem(*) == +1

    Attributes:
        _value (int): The value of the artifact [-1 / +1].
    """
    def __init__(self, value):
        super().__init__()
        self._value = value
        
    def get_value(self):
        """Gets the artifact's value [-1 / +1].
        
        Returns:
            int: The value.
        """
        return self._value