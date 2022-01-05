"""
File: todo.py
------------------
Simple command-line to-do list manager. See README.md for getting started 
and how to use the program. 
"""

import sys 

LIST_FILE_PATH = "list.txt"


def length(file_obj):
	"""
	Function that takes in the file object 
	(pointing to list.txt) and returns the number of
	items in the list. 
	"""
	count = 0

	for line in file_obj:
		count += 1 

	return count


def add(item_string):
	"""
	Function that appends the item based on what the 
	user specified as a command line argument to list.txt. 
	"""
	curr_num_items = length(open(LIST_FILE_PATH))
	curr_index = curr_num_items + 1
	og_string = item_string  # for printing purposes 
	item_string = str(curr_index) + ". " + item_string + '\n'
	file = open(LIST_FILE_PATH, "a")
	file.write(item_string)
	file.close()

	print('Added "' + og_string + '" to the to-do list.') 


def show():
	"""
	Function that prints out the list. It also displays 
	the number of items in the list. 
	"""

	file = open(LIST_FILE_PATH)

	for line in file:
		print(line, end='')  # use end to avoid printing \n 

	print("Number of items:", length(open(LIST_FILE_PATH)))


def complete(idx):
	"""
	Function that completes (deletes) the line (item) at the 
	specified index from the list. 
	"""

	# store list of lines to use later (since we will overwrite these lines) 
	temp_file_obj = open(LIST_FILE_PATH, "r") 
	line_list = temp_file_obj.readlines()
	temp_file_obj.close()
	

	updated_list = open(LIST_FILE_PATH, "w") 
	curr_idx = 1
	line_count = 0  # num lines appended to new list 
	for line in line_list:
		if curr_idx < idx:
			updated_list.write(line)
			line_count += 1
		if curr_idx > idx:
			line_count += 1 
			dot_idx = line.find(".")
			line = str(line_count) + line[dot_idx:]
			updated_list.write(line)

		curr_idx += 1 


def erase():
	"""
	Function that erases the contents of the list. 
	"""

	file = open(LIST_FILE_PATH, "w")
	file.close() 


def main():
	user_arguments = sys.argv[1:]
	arg_count = len(user_arguments)  # num user arguments 

	# exit program if no user arguments were specified 
	if arg_count == 0:
		show()  # show the list 
		sys.exit() 

	# add item to list if 'add' argument is specified 
	if (user_arguments[0] == "add" or user_arguments[0] == "a") and arg_count > 1:
		add(' '.join(user_arguments[1:]))

	# print out list if 'show' argument is specified
	if user_arguments[0] == "show" or user_arguments[0] == "s":
		show()

	# print out list if 'show' argument is specified
	if user_arguments[0] == "len" or user_arguments[0] == "l":
		print("Number of items:", length(open(LIST_FILE_PATH)))

	# complete (delete) specific item from list 
	if (user_arguments[0] == "complete" or user_arguments[0] == "c") and arg_count == 2:
		specified_idx = int(user_arguments[1]) 
		if specified_idx > length(open(LIST_FILE_PATH)) or specified_idx <= 0:
			print("Item index out of bounds")
			sys.exit() 
		complete(specified_idx)

	# erase items from list 
	if user_arguments[0] == "erase" or user_arguments[0] == "e":
		erase()


if __name__ == '__main__':
    main()
