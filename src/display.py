class Display:
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