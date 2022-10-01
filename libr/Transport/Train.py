from libr.Transport.base_transport import Transport


class Train(Transport):
    """
        Class of the Train
    """
    ALLOWED_Train_TYPES = ["wagons"]

    def __init__(self, **kwargs):
        """
            Initialization
        """
        wagons = kwargs.pop("wagons")

        super().__init__(**kwargs)
        self.wagons = int(wagons)

    def unique_features(self) -> str:
        """
        To string conversion of Train type
        :return: readable string with Train info
        """
        return f"Wagons: {self.wagons}\t|\t"

    @staticmethod
    def create_class_with_description(description):
        """
        Parse data and create Transport class with given description
        :param description: Transport description
        :return: class instance
        """
        # Unpacking Transport fields
        train_fields = {**description["common_fields"]}

        # Parse unique Train fields
        allowed_train_types = description["unique_features"]

        # Add unique Train fields
        train_fields["wagons"] = allowed_train_types

        # Create Train class with unpacked kwargs
        return Train(**train_fields)
