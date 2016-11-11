"""
The Base class with all the methods regarding app functionality.
"""
import psycopg2
import json
from firebase import firebase
from tabulate import tabulate
import csv
from time import sleep
from tqdm import tqdm

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
		note_id = cur.execute("""INSERT INTO notes_table(content) VALUES (%s) Returning id""", [json.dumps(json_data)])
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
		cur.execute("SELECT content->'title', content->'note' FROM notes_table where content->>'title' like (%s)", [param])
		result_rows = cur.fetchall()
		if result_rows:
			print('*** retrieving records matching your search! ***')

			for i in tqdm(range(200)):
				sleep(0.01)

			print tabulate(result_rows, headers=["Title", "Content"], tablefmt="fancy_grid")
		else:
			print ('*** There are no records matching your search! Try a different search ***')
		cur.close()
		self.conn.commit()

	# A method to implement synching notes with firebase
	def sync(self):
		cur = self.conn.cursor()
		cur.execute("SELECT content FROM notes_table")
		result_rows = cur.fetchall()
		fibase = firebase.FirebaseApplication('https://notes-74f87.firebaseio.com/')
		result = fibase.post('/', json.dumps(result_rows))
		print ('*** Just a moment your notes are being synced! ***')

		for i in tqdm(range(200)):
			sleep(0.01)

		print ('*** Done ***')

	# A method to implement exporting notes
	def export(self):
		file_name = raw_input("kindly provide a name to the notes: ")
		cur = self.conn.cursor()
		cur.execute("SELECT content->'title' as title, content->'note' as note from notes_table")
		result_rows = cur.fetchall()
		with open(file_name +'.csv', 'w') as f:
			writer = csv.writer(f)
			writer.writerow(['title', 'note'])
			writer.writerows(result_rows)
		print('*** Just a moment your notes are being exported ****')
		for i in tqdm(range(200)):
				sleep(0.01)
		cur.close()
		self.conn.commit()

	def import_file(self):
		# Check to see first the given directory is correct
		try:
			file_name = raw_input('kindly key in the file location: ')
			with open(file_name, 'rb') as csvfile:
				rows = csv.reader(csvfile, quotechar='|')
				for row in rows:
					self.save_imported_notes(row[0], row[1])
			# Just for a good UI
			print ('*** Just a moment your notes are being Imported! ***')
		
			for i in tqdm(range(200)):
				sleep(0.01)

			print ('*** Done ***')
		# if the directory given is wrong
		except IOError:
			print ('sorry buddy there is no such file in that directory')

	# A utility function to insert data read from a csv
	def save_imported_notes(self, title, note):
		cur = self.conn.cursor()
		json_data = {"note":note,"title":title}
		cur.execute("""INSERT INTO notes_table(content) VALUES (%s)""", [json.dumps(json_data)])
		cur.close()
		self.conn.commit()
