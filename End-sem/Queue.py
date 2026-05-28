from collections import deque

q = deque([1, 2, 3, 4, 5, 6])

odd = deque()
even = deque()

position = 1

while q:

    element = q.popleft()

    if position % 2 != 0:
        odd.append(element)

    else:
        even.append(element)

    position += 1

# Combine queues
result = odd + even

print("Final Queue:")

for i in result:
    print(i, end=" ")