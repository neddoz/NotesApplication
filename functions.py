"""
The Base class with all the methods regarding app functionality.
"""
import psycopg2
import json
from firebase import firebase
from tabulate import tabulate

class Notes(object):

	def __init__(self):
		# initialize and acquire the connection to the Database for use by the various methods
		self.conn = psycopg2.connect(database = 'notes', user = 'postgres', password = 'postgres', host = 'localhost')
	
	# A method to implement deleting a note from the Database
	def delete_note(self, id):
		cur = self.conn.cursor()
		cur.execute("DELETE FROM notes_table where id = %s", [id])
		print ('***A note with ID '+ id +' has been deleted!')
		cur.close()
		self.conn.commit()

	# A method to implement retrieving a note from the Database
	def view_note(self, id):
		cur = self.conn.cursor()
		cur.execute("SELECT content->'title', content->'note' FROM notes_table where id = %s", [id])
		result_row = cur.fetchall()
		if (result_row):
			print tabulate(result_row, headers=["Title", "Content"], tablefmt="fancy_grid")
		else:
			print ('*** sorry you dont have a note to the given ID! ***')
		cur.close()
		self.conn.commit()

	# A method to implement creating a note from the Database
	def save_note(self, title):
		note = raw_input('type in the contents of your note>>>')
		json_data = {"note":note,"title":title}	
		cur = self.conn.cursor()
		cur.execute("""INSERT INTO notes_table(content) VALUES (%s)""", [json.dumps(json_data)])
		print ('*** Note saved successfully! ***')
		cur.close()
		self.conn.commit()

	# A method to implement retrieving all notes from the Database
	def retrieve_notes(self):
		cur = self.conn.cursor()
		cur.execute("SELECT content->'title', content->'note' from notes_table")
		result_rows = cur.fetchall()
		print tabulate(result_rows, headers=["Title", "Content"], tablefmt="fancy_grid")
		cur.close()
		self.conn.commit()

	# A method to implement searching a note from the Database
	def search_note(self, param):
		cur = self.conn.cursor()
		cur.execute("SELECT * FROM notes_table where content->>'title' like (%s)", [param])
		result_rows = cur.fetchall()
		print json.dumps(result_rows)

	# A method to implement synching notes with firebase
	def sync(self):
		cur = self.conn.cursor()
		cur.execute("SELECT content FROM notes_table")
		result_rows = cur.fetchall()
		fibase = firebase.FirebaseApplication('https://notes-74f87.firebaseio.com/')
		print ('*** Just a moment your notes are being synced! ***')
		result = fibase.post('/', json.dumps(result_rows))
		print ('*** Done ***')

	def export(self):
		pass

if __name__ == "__main__":
	k = Notes()
	k.view_note(1)