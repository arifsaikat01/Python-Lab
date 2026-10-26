def display_resources(resources):
    for r in resources:
        print("ID:", r[0])
        print("Name:", r[1])
        print("Category:", r[2])
        print("Quantity:", r[3])
        print()


def search_by_category(resources, category):
    for r in resources:
        if r[2] == category:
            print(r)


def find_unavailable(resources):
    for r in resources:
        if r[3] == 0:
            print(r)


resources = [
    [101, "Laptop", "Electronics", 8],
    [102, "Projector", "Electronics", 0],
    [103, "Whiteboard", "Classroom", 5],
    [104, "Microphone", "Audio", 3],
    [105, "Camera", "Electronics", 2]
]

print("All Resources:")
display_resources(resources)

category = input("Enter category to search: ")
print("Resources in this category:")
search_by_category(resources, category)

print("Unavailable Resources:")
find_unavailable(resources)