from treenode import TreeNode

def main():
    tn = TreeNode(7)
    duck = TreeNode(2)
    cake = TreeNode(1)
    poop = TreeNode(0)
    howard = TreeNode(3)
    dirk = TreeNode(2)
    tn.add(duck)
    duck.add(cake)
    tn.print_tree()
    #tn.add(poop)
    #poop.add(howard)
    #howard.add(dirk)
    #dirk.add(TreeNode(3))
    #tn.print_tree()


    #tn.add(TreeNode(5))
    #tn.add(TreeNode(1))
    #print(tn.get_lvl())


if __name__ == "__main__":
    main()