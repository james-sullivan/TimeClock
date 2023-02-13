import argparse
import jsonpickle
import json
from User import User

# Create the main parser
parser = argparse.ArgumentParser(prog='time_clock')
subparsers = parser.add_subparsers(title='Commands', dest='command')

parser_create_user = subparsers.add_parser('create_user', help='Create a new user')

parser_start_shift = subparsers.add_parser('start_shift', help='Start a users shift')
parser_start_shift.add_argument('--id', type=str, help='The ID of the user')

parser_end_shift = subparsers.add_parser('end_shift', help='End a users shift')
parser_end_shift.add_argument('--id', type=str, help='The ID of the user')

parser_start_break = subparsers.add_parser('start_break', help='Start a users break')
parser_start_break.add_argument('--id', type=str, help='The ID of the user')

parser_end_break = subparsers.add_parser('end_break', help='End a users break')
parser_end_break.add_argument('--id', type=str, help='The ID of the user')

parser_start_lunch = subparsers.add_parser('start_lunch', help='Start a users lunch')
parser_start_lunch.add_argument('--id', type=str, help='The ID of the user')

parser_end_lunch = subparsers.add_parser('end_lunch', help='End a users lunch')
parser_end_lunch.add_argument('--id', type=str, help='The ID of the user')

parser_shift_record = subparsers.add_parser('print_record', help='Prints the record of a users past shifts, lunches, and breaks')
parser_shift_record.add_argument('--id', type=str, help='The ID of the user')

# Parse the arguments
args = parser.parse_args()

# Load user data from JSON file
with open('users.json', 'r') as f:
	json_string = f.read()

users = jsonpickle.decode(json_string)

if args.command == 'start_shift':

	users[args.id].start_shift()

elif args.command == 'end_shift':

	users[args.id].end_shift()

elif args.command == 'start_break':

	users[args.id].start_break()

elif args.command == 'end_break':

	users[args.id].end_break()

elif args.command == 'start_lunch':

	users[args.id].start_lunch()

elif args.command == 'end_lunch':

	users[args.id].end_lunch()

elif args.command == 'print_record':

	users[args.id].print_shift_record()

elif args.command == 'create_user':

	new_user = User()
	users[new_user.user_id] = new_user
	print(f'New user with id {new_user.user_id} was created')

# Write the user's data to a json file
json_string = jsonpickle.encode(users)

with open('users.json', 'w') as file:
	file.write(json_string)
