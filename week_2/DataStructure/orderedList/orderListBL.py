# ---------------------------------- prg-----------------------------------------------
# linkedList.py
# date : 26/08/2019
# perform the linked list operation as a sorting order add operation


import random


# This class for create a new node when calling there constructor with passing data (item)
class LinkedList:
    def __init__(self, data):
        self.data = data
        self.next = None
        return


class singleLinkedList:

    # This function use to initialize the empty list
    def __init__(self):
        self.head = None
        return

    # Function to find the length of list
    def size(self):
        count = 0
        temp_list = self.head
        while temp_list is not None:
            count += 1
            temp_list = temp_list.next
        return count

    # Function for add the value in the list
    def add_list(self, item):

        if not isinstance(item, LinkedList):
            item = LinkedList(item)

        if self.head is None:
            self.head = item

        else:
            # if(self.head.data):
            temp = self.head

            if temp.data > item.data:
                item.next = temp
                self.head = item
                return

            # obj.print_List()
            while temp.next is not None and temp.next.data < item.data:
                temp = temp.next

            if temp.next is None:
                temp.next = item
                return

            item.next = temp.next
            temp.next = item
        return

    # Function for print the value of list
    def print_List(self):

        temp = self.head

        while temp is not None:
            if temp.next is None:
                print(temp.data, end='-> None')
            else:
                print(temp.data, end='-> ')
            temp = temp.next

        print()

    # function for searching in the list
    def searchItem(self, item):

        if self.head is None:
            return False

        else:
            temp = self.head

            while temp is not None:
                if temp.data == item:
                    return True

                temp = temp.next

        return False

    # Function for remove the item from list
    def removeItem(self, item):

        if self.head is None:
            print("List is empty.. ! ")
            return

        else:
            temp = self.head

            if temp.data == item:
                self.head = self.head.next
                print('DELETED1')
                return

            while temp.next is not None:
                temp1 = temp

                if temp.next.data == item:
                    print(temp.next.data, item)
                    temp1.next = temp.next.next
                    print('DELETED2')
                    return

                temp = temp.next
            print("Data not present in the list:!!")

    # Function to check list is empty or not..
    def isEmpty(self):
        return self.head is None

    # function to find the index of item in the list (assume item is present in the list)
    def itemIndex(self, item):

        if self.head is None:
            print("List is empty !!\n")
            return -1

        count = -1
        temp = self.head

        while temp is not None:
            count += 1
            if temp.data == item:
                return count

            temp = temp.next
        print("Data not present in the list !!\n")
        return -1

    # pop() function to remove last element if we pass position pop(position) then remove at the position of element
    # and return this element from the list
    def pop(self, pos=None):
        if self.head is None:
            print("List is Empty !!")
            return

        if pos is None:
            temp = self.head
            if temp.next is None:
                ans = temp.data
                self.head = None
                return ans

            temp1 = None

            while temp.next is not None:
                temp1 = temp
                temp = temp.next

            temp1.next = None
            return temp.data

        else:
            temp = self.head

            if pos == 0:
                ans = temp.data
                self.head = self.head.next
                return ans

            temp1 = None

            while pos > 0 and temp.next is not None:
                temp1 = temp
                temp = temp.next
                pos -= 1

            if pos > 0:
                print("Your position is grater than list size !! ")
                return -1

            ans = temp.data
            temp1.next = temp.next
            temp = temp1
            return ans

    #   function to insert the item at the position
    def insertAtPosition(self, item, position):

        item = LinkedList(item)

        if self.head is None and position > 0:
            print(
                "List is empty and your position is grater then size so we consider this is first element and position "
                "is 0 : ")

            # return
            if item is not isinstance(item, LinkedList):
                self.head = item
                return

        if position == 0:
            item.next = self.head
            self.head = item
            return

        temp = self.head
        while position > 1 and temp.next is not None:
            position -= 1
            temp = temp.next

        if temp.next is None and position > 1:
            print("your position is grater then size so we consider this is end element of list : ")
            temp.next = item
            return

        item.next = temp.next
        temp.next = item

    # Function to read the data
    def readFileData(self):

        with open('Number.txt', "r") as file_obj:
            fileData = file_obj.read()

        return fileData

    # Function write data in the file
    def writeFile(self):

        count = 0

        with open('Number.txt', "w") as file_obj:
            temp = self.head

            while temp is not None:
                count += 1
                file_obj.write(str(temp.data))
                if count % 15 == 0:
                    file_obj.write(' \n')

                else:
                    file_obj.write(' ')
                temp = temp.next


# Function to convert data into list of words
def wordToString(fileData):
    word = ''
    word_list = []

    for i in fileData:
        if i is ' ':
            word_list.append(int(word))
            word = ''

        else:
            word = word + i

    if word != '':
        word_list.append(str(word))

    return word_list
