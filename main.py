
clients = 'Juan,Carlos,'

def create_client(client_name):
	global clients
	if client_name not in clients:
		clients += client_name
		_add_comma()
	else:
		print('Client already is in the client\'s list')


def list_clients():
	global clients
	print(clients)


def update_client(client_name, update_client_name):
	global clients

	if client_name in clients:
		clients = clients.replace(client_name + ',', update_client_name + ',')
	else:
		_client_not_found()


def delete_client(client_name):
	global clients

	if client_name in clients:
		clients = clients.replace(client_name + ',', '')
	else:
		_client_not_found()

def _add_comma():
	global clients
	clients += ','


def _client_not_found():
	return input('Client is not in clients list')


def print_welcome():
	print('W E L C O M E   T O   P Y V E N T A S')
	print('*' * 50)
	print("What would you like to do today?")
	print('[C]reate cliente')
	print('[U]pdate cliente')
	print('[D]elete cliente')


if __name__ == '__main__':
	print_welcome()
	command = input()
	command = command.upper()

	if command == 'C':
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
	else: print('comando inválido')