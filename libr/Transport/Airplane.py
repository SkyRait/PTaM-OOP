from libr.Transport.base_transport import Transport


class Plane(Transport):
    """
        Class of the Airplane
    """
    ALLOWED_Airplane_TYPES = ["flying_range", "capacity"]

    def __init__(self, **kwargs):
        """
            Initialization
        """
        flying_range = kwargs.pop("Flying_range")

        super().__init__(**kwargs)
        self.flying_range = int(flying_range)

        capacity = kwargs.pop("Capacity")

        super().__init__(**kwargs)
        self.capacity = int(capacity)

    def unique_features(self) -> str:
        """
        To string conversion of Airplane type
        :return: readable string with Airplane info
        """
        return f"Flying_range: {self.flying_range}\t|\t" \
               f"Capacity: {self.capacity}\t|\t"

    @staticmethod
    def create_class_with_description(description):
        """
        Parse data and create Transport class with given description
        :param description: Transport description
        :return: class instance
        """
        # Unpacking Transport fields
        airplane_fields = {**description["common_fields"]}

        # Parse unique airplane fields
        allowed_airplane_types = description["unique_features"]

        # Add unique airplane fields
        airplane_fields["Flying_range"] = allowed_airplane_types["flying_range"]
        airplane_fields["Capacity"] = allowed_airplane_types["capacity"]

        return Plane(**airplane_fields)
