class TreeNode(object):

    # constructor
    def __init__(self, value):
        self.parent = None
        self.children = []
        self.value = value

    def add(self, child_node):
        child_node.parent = self
        self.children.append(child_node)


    def get_lvl(self):

        max_lvl = 0
        lvl = 0
        for i in self.children:
            if i.parent is not None:
                lvl = i.get_lvl() + 1

        return max(max_lvl, lvl)

    def print_tree(self, lvl = 0):
        print("Level {}: Node {}".format(lvl, self.value))
        lvl += 1
        if self.children:
            for child in self.children:
                child.print_tree(lvl)