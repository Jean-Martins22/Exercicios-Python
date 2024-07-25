#A Fila de Desempregados

class Node:
    def __init__(self, id):
        self.id = id
        self.prev = None
        self.next = None

def fill(size):
    start = None
    node_prev = None

    for i in range(1, size + 1):
        node = Node(i)

        if start is None:
            start = node
        else:
            node_prev.next = node
            node.prev = node_prev

        node_prev = node

    start.prev = node
    node.next = start

    return start

def delete(list, reg):
    node_prev = reg.prev
    node_next = reg.next

    if reg == list:
        list = list.next
        node_prev.next = list
        list.prev = reg.prev
    else:
        node_prev.next = node_next
        node_next.prev = node_prev

    del reg
    return list

def count(list):
    i = 1
    node = list
    while list != node.next:
        i += 1
        node = node.next

    return i

def traverse(list, n, direction):
    node = list
    if direction == 0:
        while n > 1:
            node = node.next
            n -= 1
    else:
        while n > 1:
            node = node.prev
            n -= 1

    return node

def main():
    n, k, m = map(int, input().split())

    while n:
        list = fill(n)
        K = list
        M = list.prev

        while count(list) > 2:
            K = traverse(K, k, 0)
            M = traverse(M, m, 1)

            if K.next == M:
                auxK = M.next
            else:
                auxK = K.next

            if M.prev == K:
                auxM = K.prev
            else:
                auxM = M.prev

            if K == M:
                print(f"{M.id:3d},", end="")
                list = delete(list, K)
            else:
                print(f"{K.id:3d}{M.id:3d},", end="")
                list = delete(list, M)
                list = delete(list, K)

            K = auxK
            M = auxM

        if count(list) == 2:
            K = traverse(K, k, 0)
            M = traverse(M, m, 1)

            if K == M:
                print(f"{K.id:3d},{K.next.id:3d}")
            else:
                print(f"{K.id:3d}{K.next.id:3d}")
        else:
            print(f"{list.id:3d}")

        n, k, m = map(int, input().split())

if __name__ == "__main__":
    main()
