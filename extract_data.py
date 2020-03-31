import ast
import os


class PrintClass(ast.NodeVisitor):
    def __init__(self, file_name):
        self.file_name = file_name

    def validate_file(self):  # returns true if the file exits and is .txt
        try:
            if os.path.exists(self.file_name):
                if ".py" in self.file_name[-3:]:
                    with open(self.file_name) as file:
                        file.close()
                        return True
                else:
                    print("incorrect file format!")
            else:
                print("File not fount")
        except FileNotFoundError as err:
            print(f'The error is, {err}')

    def reader(self):
        if self.validate_file():
            with open(self.file_name) as f:
                mod = ast.parse(f.read())
                self.visit(mod)

    def visit_ClassDef(self, node):
        print(f'Class: {node.name}')


class PrintFunc(ast.NodeVisitor):
    def __init__(self, file_name):
        self.file_name = file_name

    def validate_file(self):  # returns true if the file exits and is .txt
        try:
            if os.path.exists(self.file_name):
                if ".py" in self.file_name[-3:]:
                    with open(self.file_name) as file:
                        file.close()
                        return True
                else:
                    print("incorrect file format!")
            else:
                print("File not fount")
        except FileNotFoundError as err:
            print(f'The error is, {err}')

    def reader(self):
        if self.validate_file():
            with open(self.file_name) as f:
                mod = ast.parse(f.read())
                self.visit(mod)

    def visit_FunctionDef(self, node):
        print(f'function: {node.name}')


if __name__ == "__main__":
    counter = PrintClass("src_code.py")
    counter.reader()
    c = PrintFunc("src_code.py")
    c.reader()
