class Container:
    """
    This is class of the container
    """
    MAX_CONTAINER_SIZE = 128

    def __init__(self):
        """
        Initialization
        """
        self.size = 0
        self.max_size = Container.MAX_CONTAINER_SIZE
        self.data = []

    def add(self, transport) -> None:
        """
        Adds transport to container
        :param transport: transport to add
        :return: None
        """
        if self.size >= self.max_size:
            raise BufferError

        self.data.append(transport)

        self.size += 1

    def clear(self):
        """
        This function clears container
        :return: None
        """
        self.size = 0
        self.data.clear()

    def __str__(self) -> str:
        """
        This function prints container tmp
        :return: str: container tmp
        """
        data = f"Transport count: {self.size}."
        dividing_line = "-" * 93 + "\n"

        if self.size:
            data += " Transport:\n"
            data += dividing_line

            for i in range(self.size):
                data += f"{i + 1}: {self.data[i]}\n"
                data += dividing_line

        return data

