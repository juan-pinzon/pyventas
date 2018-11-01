clients = ['Juan', 'Carlos']

def create_client(client_name):
	global clients
	if client_name not in clients:
		clients.append(client_name)
	else:
		print('Client already is in the client\'s list')


def list_clients():
	global clients
	
	for idx, client in enumerate(clients):
	    print('{}: {}'.format(idx, client))


def update_client(client_name, update_client_name):
	global clients

	if client_name in clients:
		index = clients.index(client_name)
		clients[index] = update_client_name
	else:
		_client_not_found()


def delete_client(client_name):
	global clients

	if client_name in clients:
		clients.remove(client_name)
	else:
		_client_not_found()


def search_client(client_name):
	global clients

	for client in clients:
		if client != client_name:
			continue
		else:
			return True


def _get_client_name():
	return input('What is the name client\n')

def _client_not_found():
	return input('Client is not in clients list')


def print_welcome():
	print('W E L C O M E   T O   P Y V E N T A S')
	print('*' * 50)
	print("What would you like to do today?")
	print('[L]ist clients')
	print('[C]reate client')
	print('[U]pdate client')
	print('[D]elete client')
	print('[S]earch client')


if __name__ == '__main__':
	print_welcome()
	command = input()
	command = command.upper()
	
	if command == 'L':
	    list_clients()
	elif command == 'C':
		client_name = _get_client_name()
		create_client(client_name)
		list_clients()
	elif command == 'D':
		client_name = _get_client_name()
		delete_client()
		list_clients()
	elif command == 'U':
		client_name = _get_client_name()
		updated_client_name = input('What is the updated client name\n')
		update_client(client_name, updated_client_name)
		list_clients()
	elif command == 'S':
		client_name = _get_client_name()
		found = search_client(client_name)
		if found:
			print('The client is in the client\'s list')
		else:
			_client_not_found()
	else: print('comando inválido')
