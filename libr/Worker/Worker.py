from libr.Conteiner.Conteiner import Container
from libr.Transport.Train import Train
from libr.Transport.Airplane import Plane
from libr.Transport.base_transport import Transport


class Worker:
    """
    Application worker
    """

    def __init__(self):
        self.__container = Container()

    def run(self, file_in, file_out):
        self.__read_data_from_file(file_in)
        self.__container.sort_by_transit_time()
        self.__write_data_to_file(file_out)
        self.__container.clear()

    def __read_data_from_file(self, file_in: str):
        """
        This function reads input file and puts tmp to container
        :param file_in: path to the file
        :return: None
        """

        with open(file_in) as file:
            lines = file.readlines()

            for index, line in enumerate(lines):
                self.__container.add(self.__parse_line(line))

    def __write_data_to_file(self, file_out: str):
        """
        This function prints container data
        :param file_out: path to output file
        :return: None
        """
        with open(file_out, "w") as file:
            file.write(str(self.__container))

    def __parse_line(self, line):
        """
        This function parses string to right transport class
        :param line: description of transport
        :return: transport
        """
        line = line.replace("\n", "").split(" ")

        if len(line) == 4:
            common_fields = {value: line[index + 1] for index, value in enumerate(Transport.DEFAULT_FIELDS)}

            description = {
                "class_name": line[0],
                "common_fields": common_fields,
                "unique_features": line[-1]
            }

            transport_class = globals()[description["class_name"]]

            return transport_class.create_class_with_description(description)

        elif len(line) == 5:

            common_fields = {value: line[index + 1] for index, value in enumerate(Transport.DEFAULT_FIELDS)}
            unique_features = {value: line[index + 3] for index, value in enumerate(Plane.ALLOWED_Airplane_TYPES)
                               }
            description = {
                "class_name": line[0],
                "common_fields": common_fields,
                "unique_features": unique_features
            }

            transport_class = globals()[description["class_name"]]

            return transport_class.create_class_with_description(description)

        else:
            return print("Incorrect number of parameters")
