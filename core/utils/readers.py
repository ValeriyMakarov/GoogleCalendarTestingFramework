import csv
import json
import os.path as path
from dotenv import load_dotenv
from os import getenv


class EnvManager:
    __loaded = False
    @classmethod
    def get_variable(cls, variable_name: str) -> str:
        if not cls.__loaded:
            load_dotenv()
        return getenv(variable_name)


class DeviceConfigManager:
    CONFIGS_DIRECTORY_PATH: str = path.abspath(
        path.join(path.dirname(__file__), r"../configs")
    )

    def __init__(self, device_config_name: str):
        config_path: str = rf"{self.CONFIGS_DIRECTORY_PATH}\{device_config_name}"

        with open(file=config_path, mode='r') as config_file:
            self.__configs: dict[str, str] = json.load(config_file)

    @property
    def configs(self) -> dict[str, str]:
        return self.__configs


class POMManager:
    def __init__(self, file_path: str):
        self.__xpath_dict: dict = {}
        page_csv_path: str = file_path.replace(".py", ".csv")
        with open(page_csv_path, newline='') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                if row["name"] in self.__xpath_dict:
                    raise ValueError(
                        f"There is duplicated name { row['name'] } in "
                        f"{ page_csv_path } file.")
                self.__xpath_dict[row["name"]] = row["xpath"]

    def __getitem__(self, element_name: str) -> str:
        return self.__xpath_dict[element_name]

    def __str__(self):
        return str(self.__xpath_dict)