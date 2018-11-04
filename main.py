import csv
import os

CLIENT_TABLE = 'clients.csv'
CLIENT_SCHEMA = ['name', 'company', 'email', 'position']
clients = []


def _initialize_clients_from_storage():
	with open(CLIENT_TABLE, mode='r') as f:
		reader = csv.DictReader(f, fieldnames=CLIENT_SCHEMA)

		for row in reader:
			clients.append(row)

def _save_clients_to_storage():
	tmp_table_name = '{}.tmp'.format(CLIENT_TABLE)
	with open(tmp_table_name, mode='w') as f:
		writer = csv.DictWriter(f, fieldnames=CLIENT_SCHEMA)
		writer.writerows(clients)

		os.remove(CLIENT_TABLE)
	os.rename(tmp_table_name, CLIENT_TABLE)

def create_client(client):
	global clients
	if client not in clients:
		clients.append(client)
	else:
		print('Client already is in the client\'s list')


def list_clients():
	global clients
	
	print('uid |  name  | company  | email  | position ')
	print('*' * 50)
	for idx, client in enumerate(clients):
		print('{uid} | {name} | {company} | {email} | {position}'.format(
            uid = idx,
            name = client['name'],
            company = client['company'],
            email = client['email'],
            position = client['position']))


def update_client(client_id, updated_client):
	global clients

	if len(clients) - 1 >= client_id:
		clients[client_id] = update_client
	else:
		_client_not_found()


def delete_client(client_id):
	global clients

	for idx, client in enumerate(clients):
		if idx == client_id:
			del clients[idx] 
			break


def search_client(client_name):
	global clients

	for client in clients:
		if client['name'] != client_name:
			continue
		else:
			return True


def _get_client_field(name_field):
	field = None

	while not field:
		field = input('What is the client {}?\n'.format(name_field))

	return field

def _get_client_from_user():
	return {
			'name': _get_client_field('name'),
			'company': _get_client_field('company'),
			'email': _get_client_field('email'),
			'position': _get_client_field('position')
		}

def _client_not_found():
	return input('Client is not in clients list')


def _print_welcome():
	print('W E L C O M E   T O   P Y V E N T A S')
	print('*' * 50)
	print("What would you like to do today?")
	print('[L]ist clients')
	print('[C]reate client')
	print('[U]pdate client')
	print('[D]elete client')
	print('[S]earch client')


if __name__ == '__main__':
	_initialize_clients_from_storage()
	_print_welcome()
	command = input()
	command = command.upper()
	
	if command == 'L':
	    list_clients()
	elif command == 'C':
		client = _get_client_from_user()
		create_client(client)
	elif command == 'D':
		client_id = int(_get_client_field('id'))
		delete_client(client_id)
	elif command == 'U':
		client_id = int(_get_client_field('id'))
		updated_client = _get_client_from_user()
		update_client(client_id, updated_client)
	elif command == 'S':
		client_id = int(_get_client_field('id'))
		found = search_client(client_id)
		if found:
			print('The client is in the client\'s list')
		else:
			_client_not_found()
	else: print('comando inválido')

	_save_clients_to_storage()
