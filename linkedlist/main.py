from linkedlist import LinkedList


def main():
    ll = LinkedList()
    #print(ll.length())

    ll.push(3)
    #print(ll.length())
    #print(ll.get_head())
    #print(ll.contains(3))
    ll.push(2)
    ll.push(4)
    #print(ll.__str__())
    #ll.append(2)
    #ll.append(1)
    #ll.append(7)
    print(ll.__str__())
    print(ll.delete_instances(2))
    print(ll.__str__())


if __name__ == "__main__":
 main()
