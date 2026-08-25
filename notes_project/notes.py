
def add_note():
    note_title = input("Enter the title of the note: ")
    note = input("Enter the note: ")
    note_data = note_title + '|' + note + '\n'

    with open("data.txt", 'a') as file:
        file.write(note_data)

    print("Note Added Successfully!")

def view_note():

    with open("data.txt", 'r') as file:
        content = file.readlines()

    if not content:
        print("Currently no data present to view!")
        return

    print()
    print("=" * 20)
    print("    Notes    ")
    print("=" * 20)

    for index,line in enumerate(content, start=1):
        title, note = line.split('|', 1)
        print(f'{index}. {title}')
        print(f'   {note}')


def search_note():

    with open("data.txt", 'r') as file:
        content = file.readlines()

    if not content:
        print("There is no value present to search.")
        return

    search_title = input("Enter the note title to search: ").lower()
    index = 0

    print("=" * 20)
    print("    Search Results    ")
    print("=" * 20)

    for line in content:
        title, note = line.split('|', 1)
        if search_title in title.lower():
            index +=1
            print(f'{index}. {title}')
            print(f'   {note}')

    if index == 0:
        print("No notes found.")

def delete_note():

    with open("data.txt", 'r') as file:
        content = file.readlines()

    if not content:
        print("There is no value present to delete.")
        return

    try:
        note_no = int(input("Enter the note number to delete: "))
    except ValueError:
        print("Enter a Valid number.")
        return

    total_notes = len(content)
    if note_no < 1 or note_no > total_notes:
        print("Invalid input! Enter a available index number.")
        return

    removed_note = content.pop(note_no - 1)

    with open("data.txt", 'w') as file:
        file.writelines(content)

    print("Note Deleted Successfully!")
    print("Deleted note: " + removed_note.strip())


def edit_note():

    with open("data.txt") as file:
        content = file.readlines()

    if not content:
        print("There is no value present to edit.")
        return

    try:
        note_no = int(input("Enter the note number to edit: "))
    except ValueError:
        print("Enter a Valid number.")
        return

    if len(content) < note_no or note_no <= 0:
        print("Invalid input! Enter a available index number.")
        return

    new_title = input("Enter new title: ")
    new_note = input("Enter new note: ")

    content[note_no-1] = new_title + '|' + new_note + '\n'
    with open("data.txt", 'w') as file:
        file.writelines(content)

    print("Note Updated Successfully!")

if __name__ == '__main__':

    print()
    print('*' * 20)
    print(f'   Notes App:   ')
    print('*' * 20)

    choice = 0

    with open("data.txt", 'a') as data_file:
        pass

    while choice != 6:
        print("\nMenu")
        print("1.Add Note")
        print("2.View Notes")
        print("3.Search Note")
        print("4.Delete Note")
        print("5.Edit Note")
        print("6.Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a number.")
            continue

        if choice == 1:
            add_note()
        elif choice == 2:
            view_note()
        elif choice == 3:
            search_note()
        elif choice == 4:
            delete_note()
        elif choice == 5:
            edit_note()
        elif choice == 6:
            break
        else:
            print("Invalid Choice!")

    print("App exited..")