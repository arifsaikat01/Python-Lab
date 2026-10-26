
def display_resources(resources):
    if len(resources) == 0:
        print("No resources available.")
        return

    for r in resources:
        print("ID:", r[0])
        print("Name:", r[1])
        print("Category:", r[2])
        print("Quantity:", r[3])
        print()


def search_by_category(resources, category):
    found = False

    for r in resources:
        if r[2] == category:
            print(r)
            found = True

    if found == False:
        print("No resources found.")


def find_unavailable(resources):
    found = False

    for r in resources:
        if r[3] == 0:
            print(r)
            found = True

    if found == False:
        print("No unavailable resources.")


resources = [
    [101, "Laptop", "Electronics", 8],
    [102, "Projector", "Electronics", 0],
    [103, "Whiteboard", "Classroom", 5],
    [104, "Microphone", "Audio", 3],
    [105, "Camera", "Electronics", 2]
]


for r in resources:
    if r[3] < 0:
        print("Invalid quantity for:", r[1])

print("All Resources:")
display_resources(resources)

category = input("Enter category to search: ")
search_by_category(resources, category)

print("Unavailable Resources:")
find_unavailable(resources)


search_id = int(input("Enter resource ID to search: "))
found = False

for r in resources:
    if r[0] == search_id:
        print("Resource found:", r)
        found = True

if found == False:
    print("Resource ID not found.")
