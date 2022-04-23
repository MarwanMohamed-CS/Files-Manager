class Tree():
    def __init__(self):
        self.obj = Dir(1)

    def return_dir(self):
        return self.obj


class Dir():
    def __init__(self, num):
        self.num = num

tree = Tree()
obj  = tree.return_dir()
print(tree.obj.num)
obj.num = 5
print(tree.obj.num)
