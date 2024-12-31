from collections import deque

def fill_the_box(*args):
    height, length, width = args[0], args[1], args[2]
    finish = args.index("Finish")
    size = height*length*width
    result_deque = deque()

    def collect_data():
        for i in range(3, finish):
            result_deque.append(args[i])

    collect_data()

    for i in range(3, len(args)):
        while args[i] != "Finish":
            while result_deque:
                current_box = result_deque.popleft()
                if size >= current_box:
                    size -= current_box
                else:
                    to_remove = current_box - size
                    result_deque.appendleft(to_remove)
                    size = 0
                break
            break

    if size:
        return f"There is free space in the box. You could put {size} more cubes."
    return f"No more free space! You have {sum(result_deque)} more cubes."


# print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
# print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))