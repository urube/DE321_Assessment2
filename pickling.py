"""
Using pickle for object-persistence.
to-do: Make cmd robust for when users enter unknown codes
validate data: checking is source file exists or is python or correct
"""
import pickle
import os
from src_code import Hospital


def pickle_it():  # pickle each class by class
    try:
        # create object
        details = Hospital('John Wick', 'Doctor')
        # create pickle file
        pickle_file = open('details', 'wb')
        # pickle the details and write it to the file
        pickle.dump(details, pickle_file)
        # close the file
        pickle_file.close()
    except ValueError as e:
        print(f'The exception is: {e}')


def un_pickle_it():
    try:
        # read the pickle file
        pickle_file = open('details', 'rb')
        # unpickle the data_frame
        details = pickle.load(pickle_file)
        # close pickle file
        pickle_file.close()

        # print the data_frame
        print(type(details))
        details.__str__()
    except FileNotFoundError:
        print('File not found')


if __name__ == "__main__":
    un_pickle_it()


class Pickling:  # pickle whole .py file
    def __init__(self, to_pickle, file_name):
        self.to_pickle = to_pickle
        self.file_name = file_name

    def pickle_it(self):  # pickle the file for object-persistence
        a_file = open(self.file_name, 'wb')
        pickle.dump(self.to_pickle, a_file)
        a_file.close()

    def validate_file(self):
        try:
            if os.path.exists(self.file_name):
                if ".pickle" in self.file_name[-7:]:
                    with open(self.file_name) as file:
                        file.close()
                        return True
                else:
                    print("Incorrect file format.")
            else:
                print("File not fount")
        except FileNotFoundError as err:
            print(f'The error is, {err}')

    def unpickle_it(self):  # unpickle the pickled file
        if self.validate_file():
            a_file = open(self.file_name, 'rb')
            load_file = pickle.load(a_file)
            print(load_file)  # loads just the name of the pickled file
            f = open(load_file, 'r')  # Reads and prints pickled file line by line
            print(f.read())
            a_file.close()
    
    def delete_it(self):
        if os.path.exists(self.file_name):
            if ".pickle" in self.file_name[-7:]:
                os.remove(self.file_name)
                print("Pickle file deleted.")
            else:
                print("Incorrect file format.")
        else:
            print("File not fount")
