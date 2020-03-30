import os
from pathlib import Path


class DiagramCreator:
    def __init__(self, file_name):
        self.file_name = file_name

    def validate_file(self):
        try:
            with open(self.file_name) as file:
                file.close()
                return True
        except FileNotFoundError as err:
            print(f'The error is, {err}')

    def create_diagram(self):
        if self.validate_file():
            java = "java -jar plantuml.jar "
            destination = Path("./Documentation/")
            os.system(f'{java} -o {destination} {self.file_name}')
    
    def load_dot_file(self):
        print(self.file_name.read_text())


# print(DiagramCreator("a").load_dot_file())
