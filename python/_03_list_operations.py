"""
insert i e: Insert integer e at position i.
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
"""

list_items = []
lines = []

if __name__ == '__main__':
    N = int(input())
    for i in range(N):
        line = input()
        lines.append(line)

    for line in lines:
        if "insert" == line.split(" ")[0]:
            index = int(line.split(" ")[1])
            element = int(line.split(" ")[2])
            list_items.insert(index, element)
        if "print" == line.split(" ")[0]:
            print(list_items)
        if "remove" == line.split(" ")[0]:
            element = int(line.split(" ")[1])
            list_items.remove(element)
        if "append" == line.split(" ")[0]:
            element = int(line.split(" ")[1])
            list_items.append(element)
        if "sort" == line.split(" ")[0]:
            list_items.sort()
        if "pop" == line.split(" ")[0]:
            list_items.pop()
        if "reverse" == line.split(" ")[0]:
            list_items.reverse()
