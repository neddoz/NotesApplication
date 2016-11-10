import psycopg2
import json
from firebase import firebase


class Notes(object):
	def __init__(self):
		self.conn = psycopg2.connect(database = 'notes', user = 'postgres', password = 'postgres', host = 'localhost')
	
	def delete_note(self, id):
		cur = self.conn.cursor()
		cur.execute("DELETE FROM notes_table where id = %s", [id])
		print ('***A note with ID '+ id +' has been deleted!')
		cur.close()
		self.conn.commit()

	def view_note(self, id):
		cur = self.conn.cursor()
		cur.execute("SELECT * FROM notes_table where id = %s", [id])
		result_row = cur.fetchall()
		if (result_row):
			print json.dumps(result_row)
		else:
			print ('*** sorry you dont have a note to the given ID! ***')
		cur.close()
		self.conn.commit()

	def save_note(self, title):
		note = raw_input('type in the contents of your note>>>')
		json_data = {"note":note,"title":title}	
		cur = self.conn.cursor()
		cur.execute("""INSERT INTO notes_table(content) VALUES (%s)""", [json.dumps(json_data)])
		print ('*** Note saved successfully! ***')
		cur.close()
		self.conn.commit()

	def retrieve_notes(self):
		cur = self.conn.cursor()
		cur.execute("SELECT content FROM notes_table")
		result_rows = cur.fetchall()
		for row in result_rows:
			print json.dumps(row)
		cur.close()
		self.conn.commit()

	def search_note(self, param):
		cur = self.conn.cursor()
		cur.execute("SELECT * FROM notes_table where content->>'title' like (%s)", [param])
		result_rows = cur.fetchall()
		print json.dumps(result_rows)

	def sync(self):
		cur = self.conn.cursor()
		cur.execute("SELECT content FROM notes_table")
		result_rows = cur.fetchall()
		fibase = firebase.FirebaseApplication('https://notes-74f87.firebaseio.com/')
		print ('*** Just a moment your notes are being synced! ***')
		result = fibase.post('/', json.dumps(result_rows))
		print ('*** Done ***')

if __name__ == "__main__":
	k = Notes()
	k.retrieve_notes()