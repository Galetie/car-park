class Display:
    """
    A display unit for showing car park information.
    
    This class represents a physical or virtual display that shows
    information about the car park such as available bays, temperature,
    and current time to users.
    
    Attributes:
        id (int): Unique identifier for the display.
        message (str): Current message being displayed.
        is_on (bool): Whether the display is powered on.
    """
    
    def __init__(
            self,
            id: int = None,
            message: str = "",
            is_on: bool = False
    ):
        self.id = id
        self.message = message
        self.is_on = is_on

    def __str__(self):
        return f"Display {self.id}: Welcome to the car park."

    def update(self, data: dict):
        messages = []

        for key, value in data.items():
            messages.append(f"{key}: {value}")

        self.message = "\n".join(messages)