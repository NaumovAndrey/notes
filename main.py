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
