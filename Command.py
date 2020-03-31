"""
cli is the main user interface
"""
from cmd import Cmd


class CommandLineInterface(Cmd):
    intro = '======================================================================================== \n ' \
            'Simple Cli for Assessment2. Please Start by typing [introduce me] and follow the prompt.\n' \
            '======================================================================================== \n'
    prompt = '>>>'
    file = None

    def __init__(self):
        Cmd.__init__(self)
        self.name = "unknown"

    def default(self, arg):
        print(arg + ' is an incorrect command. Type ? or help to see command list')

    def do_introduce(self, unknown_name):
        """
        Syntax: introduce me
                Enter your name.
        then follow the prompt
        """
        if unknown_name == 'me':
            try:
                print('Welcome')
                if unknown_name:
                    unknown_name = (input("Please enter you name: "))
                    print('Hello ' + unknown_name)
                else:
                    print('Hello ' + self.name)
            except ValueError as e:
                print(f'The exception is: {e}')
            except KeyError as e:
                print(f'{e}: Not a command')
            finally:
                print('Type help or ? to see more available commands.')
        else:
            message = "Incorrect syntax. Type: [Introduce me]"
            print(message)

    def do_pickle(self, arg):
        """
        pickle a python file
        Syntax: pickle [file name]
                Enter the to_be name of the pickled file
        """
        try:
            from pickling import Pickling
            Pickling(arg, input("Please enter the name of file: ")).pickle_it()
        except TypeError as e:
            print(e)
        except():
            print("Error!!")

    def do_unpickle(self, arg):
        """
        load the pickled file of the classes
        Syntax: unpickle [pickled file_name]
        """
        try:
            from pickling import Pickling
            Pickling('', arg).unpickle_it()
            print('The pickled file has been un-pickled.')
        except FileNotFoundError as e:
            print(e)
        except():
            print("Error!!")

    def do_delete_pickle(self, arg):
        """
        Delete the pickled file
        Syntax:  pickle_delete [file name]
        :return:
        """
        try:
            from pickling import Pickling
            Pickling('', arg).delete_it()
        except FileNotFoundError as err:
            print(err)

    def do_create_dot_file(self, arg):
        """
        Create dot file using Pyreverse
        Syntax:
        """
        try:
            from runner import Runner
            # name = input("Enter diagram image name: ")
            Runner().make_dot_file()
        except ImportError as e:
            print(e)
        except():
            print("Error!!")

    def do_create_pyreverse_uml(self, arg):  # Daniel's uml diagram
        """
        Create uml diagram from dot file using Pyreverse
        Syntax:
        """
        try:
            from runner import Runner
            Runner().make_uml_diagram()
        except ImportError as e:
            print(e)
        except():
            print("Error!!")

    def do_load_database(self, name):
        """
        load the DOT file of uml diagram
        Syntax: load
        """
        try:
            from runner import Runner
            Runner().run()
        except ImportError as e:
            print(e)
        except():
            print('Loading failed')

    def do_create_plantuml(self, arg):
        """
        Create uml diagram from dot file using Plantuml
        Syntax:
        """
        try:
            from create_plantuml import DiagramCreator
            DiagramCreator(arg).create_diagram()
            print("Png file created.")
        except ImportError as e:
            print(e)
        except():
            print('Error!!')

    def do_dot_load(self, arg):
        """
        Load txt dot file
        syntax: dot_load [file name].txt
        """
        try:
            from create_plantuml import DiagramCreator
            DiagramCreator(arg).load_dot_file()
            print("Loading complete.")
        except ImportError as e:
            print(e)
        except():
            print("loading failed!!")

    def do_delete_png(self, arg):
        """
        delete png file created using plantuml
        Syntax: delete_png [file name]
        """
        try:
            from create_plantuml import DiagramCreator
            DiagramCreator(arg).delete_png()
        except ImportError as e:
            print(e)
        except():
            print("Delete failed!!")

    def do_extract_data(self, arg):
        """
        Extracts data from .py file to find the classes and function.
        Syntax: extract_data [file name].py
        """
        try:
            from extract_data import PrintClass, PrintFunc
            c = PrintClass(arg)
            c.reader()
            f = PrintFunc(arg)
            f.reader()
        except ImportError as e:
            print(e)
        except():
            print("Error!!")

    def do_exit(self, line):
        """
        Stop the program
        syntax: exit
        """
        print('Thank you for visiting.')
        return True


if __name__ == '__main__':
    CommandLineInterface().cmdloop()
