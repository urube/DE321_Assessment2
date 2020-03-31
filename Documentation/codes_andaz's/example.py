import ast


class CountClass(ast.NodeVisitor):
    def __init__(self, file_name):
        self.file_name = file_name
        self.class_count = 0
        with open(self.file_name) as f:
            mod = ast.parse(f.read())
            self.visit(mod)

    def visit_ClassDef(self, node):
        print(f'Class: {node.name}')
        self.class_count += 1


class CountFunc(ast.NodeVisitor):
    def __init__(self, file_name):
        self.func_count = 0
        with open(file_name) as f:
            mod = ast.parse(f.read())
            self.visit(mod)

    def visit_FunctionDef(self, node):
        print(f'function: {node.name}')
        self.func_count += 1


if __name__ == "__main__":
    print(CountClass("src_code.py").class_count)
    print(CountFunc("src_code.py").func_count)
