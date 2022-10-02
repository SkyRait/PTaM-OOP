from libr.Conteiner.Conteiner import Container
from libr.Transport.Train import Train
from libr.Transport.Ship import Ship
from libr.Transport.Airplane import Plane
from libr.Transport.base_transport import Transport
import sys


class Worker:
    """
    Application worker
    """

    def __init__(self):
        self.__container = Container()

    def run(self, file_in, file_out):
        self.__read_data_from_file(file_in)
        self.print_filtered_data()
        self.__container.sort_by_transit_time()
        self.__write_data_to_file(file_out)
        self.__container.clear()

    def print_filtered_data(self):
        for transport_class in [Plane]:
            print(f"\nFilter by {transport_class.__name__}")
            filtered_data = self.__container.filter_by(transport_class)

            for transport in filtered_data:
                print(transport)

    def __read_data_from_file(self, file_in: str):
        """
        This function reads input file and puts tmp to container
        :param file_in: path to the file
        :return: None
        """
        errors_log = []
        errors_count = 0
        try:
            with open(file_in) as file:
                lines = file.readlines()

                for index, line in enumerate(lines):
                    try:
                        self.__container.add(self.__parse_line(line))
                    except (ValueError, NameError, KeyError, TypeError) as error:
                        errors_log.append(f"line {index + 1}: {str(error)}")
                        errors_count += 1
                    except BufferError:
                        print(f"! Warning: Container is full. Read only {self.__container.max_size} lines.")
                        break
            print(f"File read with {errors_count} errors.")
            if errors_log:
                print("Errors info:")
                print("\n".join(errors_log))

        except FileNotFoundError:
            print("Incorrect command line: No such input file.")
            sys.exit()

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
        if line[0].lower() == "transport":
            raise NameError("Class 'Transport' can be only inherited")
        elif line[0].lower() not in ["plane", "train", "ship"]:
            raise NameError(f"Class {line[0]} undefined")

        if len(line) == 5:
            if line[0].lower() == "train":
                common_fields = {value: line[index + 1] for index, value in enumerate(Transport.DEFAULT_FIELDS)}

                description = {
                    "class_name": line[0],
                    "common_fields": common_fields,
                    "unique_features": line[-1]
                }

                transport_class = globals()[description["class_name"]]

                return transport_class.create_class_with_description(description)
            else:
                raise ValueError("Incorrect number of parameters")

        elif len(line) == 6:

            if line[0].lower() == "ship":
                common_fields = {value: line[index + 1] for index, value in enumerate(Transport.DEFAULT_FIELDS)}
                unique_features = {value: line[index + 4] for index, value in enumerate(Ship.ALLOWED_Ship)
                                   }
                description = {
                    "class_name": line[0],
                    "common_fields": common_fields,
                    "unique_features": unique_features
                }

                transport_class = globals()[description["class_name"]]

                return transport_class.create_class_with_description(description)

            elif line[0].lower() == "plane":
                common_fields = {value: line[index + 1] for index, value in enumerate(Transport.DEFAULT_FIELDS)}
                unique_features = {value: line[index + 4] for index, value in enumerate(Plane.ALLOWED_Airplane_TYPES)
                                   }
                description = {
                    "class_name": line[0],
                    "common_fields": common_fields,
                    "unique_features": unique_features
                }

                transport_class = globals()[description["class_name"]]

                return transport_class.create_class_with_description(description)
            else:
                raise ValueError("Incorrect number of parameters")

        else:
            raise ValueError("Incorrect number of parameters")
