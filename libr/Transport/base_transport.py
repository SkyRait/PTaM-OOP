class Transport:
    """
        This is the base transport class
    """
    # Here must be listed all Transport default fields
    DEFAULT_FIELDS = ["speed", "distance", "weight_now"]

    def __init__(self, **kwargs):
        """
        Initialization
        """
        speed = kwargs.pop("speed")
        self.speed = int(speed)

        distance = kwargs.pop("distance")
        self.distance = int(distance)

        weight_now = kwargs.pop("weight_now")
        self.weight_now = int(weight_now)

    def __str__(self) -> str:
        """
        To string conversion
        """
        return f"Type: {self.__class__.__name__.lower()}\t|\t" \
               f"Speed: {self.speed}\t|\t" \
               f"Distance: {self.distance}\t|\t" \
               f"weight_now:{self.weight_now}\t|\t" \
               f"{self.unique_features()}"

    def unique_features(self) -> str:
        """
        To string conversion of unique fields, must be defined in child classes
        """

    @staticmethod
    def create_class_with_description(description):
        """
        Parse data and create Transport class with given description,
        Raises error when his method not defined in child class
        :param description: Transport description
        """
        raise ValueError("create_class_with_description: unknown action")
