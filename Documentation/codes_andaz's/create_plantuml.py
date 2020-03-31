"""
Create diagram from dot file using Plantuml
to-do: <option> -filename "%filename%" is not working in plantuml. Cannot give name to png file.
validate data: checking is source file exists or is python or correct
"""
import os


class DiagramCreator:
    def __init__(self, file_name):
        self.file_name = file_name

    def validate_file(self):  # returns true if the file exits and is .txt
        try:
            if ".txt" in self.file_name[-4:]:
                with open(self.file_name) as file:
                    file.close()
                    return True
            else:
                print("incorrect file format!")
        except FileNotFoundError as err:
            print(f'The error is, {err}')

    def create_diagram(self):  # create dot txt file into png using Plantuml
        if self.validate_file():  # deals with file directory and should work for any os
            java = "java -jar plantuml.jar "
            script_dir = os.getcwd()
            directory = "DE321_assignment_2-master"
            file_location = (script_dir + "\\" or "//" + directory + "\\")
            destination = (script_dir + "\\" or "//" + directory)
            os.system(f'{java} -o {destination} {file_location}{self.file_name}')

    def load_dot_file(self):
        if self.validate_file():
            script_dir = os.getcwd()  # directory path should work for any os
            file_to_open = (script_dir + "\\" + self.file_name)
            f = open(file_to_open)
            print(f.read())
       
    def delete_png(self):
        if os.path.exists(self.file_name):
            if ".png" in self.file_name[-4:]:
                os.remove(self.file_name)
                print("Png file deleted.")
            else:
                print("Incorrect file format.")
        else:
            print("File not fount")
