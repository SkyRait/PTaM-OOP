from libr.Transport.base_transport import Transport


class Ship(Transport):
    """
        Class of the Train
    """
    ALLOWED_Ship = ["displacement", "ship_types"]
    ALLOWED_Ship_TYPES = ["liner", "tug", "tanker", "cruiser", "caravelle"]

    def __init__(self, **kwargs):
        """
            Initialization
        """
        displacement = kwargs.pop("displacement")

        super().__init__(**kwargs)
        self.displacement = int(displacement)

        ship_type = kwargs.pop("ship_type")

        super().__init__(**kwargs)
        self.ship_type = ship_type

    def unique_features(self) -> str:
        """
        To string conversion of Train type
        :return: readable string with Train info
        """
        return f"Displacement: {self.displacement}\t|\t" \
               f"Ship type: {', '.join(self.ship_type)}"

    @staticmethod
    def create_class_with_description(description):
        """
        Parse data and create Transport class with given description
        :param description: Transport description
        :return: class instance
        """
        # Unpacking Transport fields
        ship_fields = {**description["common_fields"]}

        # Parse unique ship fields
        successful_parsed_ship_types = []
        allowed_ship = description["unique_features"]
        ship_fields["displacement"] = allowed_ship["displacement"]
        ship_types = allowed_ship["ship_types"].split("+")

        for ship_type in ship_types:
            if ship_type in Ship.ALLOWED_Ship_TYPES:
                successful_parsed_ship_types.append(ship_type)
        if len(successful_parsed_ship_types) == 0:
            raise ValueError("Unknown ship types given")

        # Add unique ship fields
        ship_fields["ship_type"] = successful_parsed_ship_types

        # Create Ship class with unpacked kwargs
        return Ship(**ship_fields)
