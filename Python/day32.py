# Set .discard(), .remove() & .pop()

n = int(input())
s = set(map(int, input().split()))
n1 = int(input())
for i in range(n1):
    command = input()
    if command == "pop":
        s.pop()
    elif command[0:6] == "remove":
        s.remove(int(command[-1]))
    elif command[0:7] == "discard":
        s.discard(int(command[-1]))

print(sum(s))
