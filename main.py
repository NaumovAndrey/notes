import json
import datetime
class Note:
    def __init__(self, id, title, body, created_at, updated_at):
        self.id = id
        self.title = title
        self.body = body
        self.created_at = created_at
        self.updated_at = updated_at
class NotesApp:
    def __init__(self):
        self.notes = []
        self.load_notes()

    def load_notes(self):
        try:
            with open('notes.json', 'r') as f:
                notes_data = json.load(f)
                for note_data in notes_data:
                    note = Note(note_data['id'], note_data['title'], note_data['body'], note_data['created_at'],
                                note_data['updated_at'])
                    self.notes.append(note)
        except:
            pass

    def save_notes(self):
        notes_data = []
        for note in self.notes:
            note_data = {'id': note.id, 'title': note.title, 'body': note.body, 'created_at': note.created_at,
                         'updated_at': note.updated_at}
            notes_data.append(note_data)
        with open('notes.json', 'w') as f:
            json.dump(notes_data, f)
    def create_note(self):
        id = len(self.notes) + 1
        title = input('Enter note title: ')
        body = input('Enter note body: ')
        created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        updated_at = created_at
        note = Note(id, title, body, created_at, updated_at)
        self.notes.append(note)
        self.save_notes()

    def read_notes(self):
        for note in self.notes:
            print('ID:', note.id)
            print('Title:', note.title)
            print('Body:', note.body)
            print('Created at:', note.created_at)
            print('Updated at:', note.updated_at)
            print()

    def update_note(self):
        id = int(input('Enter note ID: '))
        for note in self.notes:
            if note.id == id:
                title = input('Enter new note title: ')
                body = input('Enter new note body: ')
                note.title = title
                note.body = body
                note.updated_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.save_notes()
                break

    def delete_note(self):
        id = int(input('Enter note ID: '))
        for note in self.notes:
            if note.id == id:
                self.notes.remove(note)
                self.save_notes()
                break

    def show_menu(self):
        print('Notes App\n')
        print('1. Create note')
        print('2. Read notes')
        print('3. Update note')
        print('4. Delete note')
        print('5. Exit\n')

    def run(self):
        while True:
            self.show_menu()
            choice = input('Enter your choice: ')
            if choice == '1':
                self.create_note()
            elif choice == '2':
                self.read_notes()
            elif choice == '3':
                self.update_note()
            elif choice == '4':
                self.delete_note()
            elif choice == '5':
                break
            else:
                print('Invalid choice\n')


if __name__ == '__main__':
    app = NotesApp()
    app.run()