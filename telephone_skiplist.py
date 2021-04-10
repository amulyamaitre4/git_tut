#######################
# Name: Amulya Maitre #
# Roll No. FYMTC08    #
#######################

import random


class Node(object):  # Node class
    def __init__(self, key, level):
        self.key = key
        self.forward = [None] * (level + 1)  # list to hold references to node of different level


class Telephone_SkipList(object):  # Skip list
    def __init__(self, max_lvl, p):
        self.maxlvl = max_lvl  # Maximum level for this skip list
        self.p = p  # p is the fraction of the nodes with level
        self.header = self.createNode(self.maxlvl, -1)  # create header node and initialize key to -1
        self.level = 0

    def randomLevel(self):  # create random level for node
        lvl = 0
        while random.random() < self.p and lvl < self.maxlvl:
            lvl += 1
        return lvl

    def createNode(self, lvl, key):  # create new node
        n = Node(key, lvl)
        return n

    def insertElement(self, key):  # insert given key in skip list
        update = [None] * (self.maxlvl + 1)  # create update array and initialize it
        current = self.header

        ''' 
        Start from highest level of skip list move the current reference forward while key  
        is greater than key of node next to current. 
        Otherwise inserted current in update and move one level down and continue search.
        '''
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
            update[i] = current

        '''  
        Reached level 0 and forward reference to right, which is desired position to  
        insert key. 
        '''
        current = current.forward[0]

        ''' 
        If current is NULL that means we have reached to end of the level or current's key is not equal 
        to key to insert that means we have to insert node between update[0] and current node. 
       '''
        if current == None or current.key != key:
            rlevel = self.randomLevel()  # Generate a random level for node

            ''' 
            If random level is greater than list's current level (node with highest level inserted in  
            list so far), initialize update value with reference to header for further use.
            '''
            if rlevel > self.level:
                for i in range(self.level + 1, rlevel + 1):
                    update[i] = self.header
                self.level = rlevel

            n = self.createNode(rlevel, key)  # create new node with random level generated

            for i in range(rlevel + 1):
                n.forward[i] = update[i].forward[i]  # insert node by rearranging references
                update[i].forward[i] = n

            print("Successfully phone number {}".format(key))
            choice = input("Do you want to add another contact?")
            return choice

    def searchElement(self, key):
        current = self.header

        ''' 
        Start from highest level of skip list move the current reference forward while key  
        is greater than key of node next to current. 
        Otherwise inserted current in update and move one level down and continue search.
        '''
        for i in range(self.level, -1, -1):
            while (current.forward[i] and current.forward[i].key < key):
                current = current.forward[i]

        current = current.forward[0]  # reached level 0 and advance reference to right, which is our desired node

        if current and current.key == key:  # If key of current node is equal to search key, we have found our node
            print("Found phone number ", key)
        else:
            print("Phone Number {} not in the telephone book!".format(key))
            print("Try inserting the Phone Number")

        choice = input("Do you want to search another contact?")
        return choice

    def deleteElement(self, search_key):
        update = [None] * (self.maxlvl + 1)  # create update array and initialize it
        current = self.header

        ''' 
        Start from highest level of skip list move the current reference forward while key  
        is greater than key of node next to current. 
        Otherwise inserted current in update and move one level down and continue search. 
        '''
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].key < search_key:
                current = current.forward[i]
            update[i] = current

        '''  
        reached level 0 and advance reference to right, which is prssibly our desired node. 
        '''
        current = current.forward[0]

        if current is not None and current.key == search_key: # If current node is target node

            ''' 
            Start from lowest level and rearrange references just like we do in singly linked list 
            to remove target node.
            '''
            for i in range(self.level + 1):

                ''' 
                If at level i, next node is not target node, break the loop, no need to move  
                further level.
                '''
                if update[i].forward[i] != current:
                    break
                update[i].forward[i] = current.forward[i]

            while self.level > 0 and self.header.forward[self.level] is None: # Remove levels having no elements
                self.level -= 1
            print("Successfully deleted phone number {}".format(search_key))
        else:
            print("Phone Number {} not found! So can't delete anything!".format(search_key))

        choice = input("Do you want to delete another contact?")
        return choice

    def displayList(self):
        print("\n*****Telephone Book******")
        head = self.header
        for lvl in range(self.level + 1):
            print("Level {}: ".format(lvl), end=" ")
            node = head.forward[lvl]
            while node is not None:
                print(node.key, end=" ")
                node = node.forward[lvl]
            print("")


def main():
    lst = Telephone_SkipList(4, 0.5)
    ch = True
    while ch:
        print("Operations to perform: \n 1. Insert Contact \n 2. Search Contact \n 3. Delete Contact \n 4. Exit")
        op = int(input("Enter your choice: "))
        if op == 1:
            flag = True
            while flag:
                print("\nInsert your contact numbers in the Telephone Book")
                phno = int(input("Enter the phone number: "))
                choice = lst.insertElement(phno)
                lst.displayList()
                if choice == 'N' or choice == 'n':
                    flag = False

        elif op == 2:
            flag = True
            while flag:
                print("\nSearch a contact number in the Telephone Book")
                phno = int(input("Enter the phone number you want to search: "))
                choice = lst.searchElement(phno)
                if choice == 'N' or choice == 'n':
                    flag = False

        elif op == 3:
            flag = True
            while flag:
                print("\nDelete a contact number in the Telephone Book")
                phno = int(input("Enter the phone number you want to delete: "))
                choice = lst.deleteElement(phno)
                lst.displayList()
                if choice == 'N' or choice == 'n':
                    flag = False

        elif op == 4:
            ch = False

main()
