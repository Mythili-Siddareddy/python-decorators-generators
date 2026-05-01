# Python Generator Example

def count_up(n):
    for i in range(n):
        yield i

print("Generator Output:")
for value in count_up(5):
    print(value)
