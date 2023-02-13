import datetime
import uuid
from enum import Enum

def get_current_time():
	return str(datetime.datetime.utcnow().replace(microsecond=0).isoformat())

class User:

	def __init__(self):
		self.user_id = str(uuid.uuid4())
		self._shift_start_time = False
		self._break_start_time = False
		self._lunch_start_time = False
		self._shift_record = []

	def start_shift(self):
		# If this user is not already in a shift
		if self._shift_start_time == False:
			self._shift_start_time = get_current_time()
			print(f"User with id {self.user_id} started shift at time {self._shift_start_time}")
		else:
			raise Exception(f"User is already in an active shift that started at {self._shift_start_time}")

	def end_shift(self):

		if self._shift_start_time == False:
			raise Exception('Cannot end shift because user is not in a shift')
		elif self._break_start_time != False:
			raise Exception('Cannot end shift because user is currently on break')
		elif self._lunch_start_time != False:
			raise Exception('Cannot end shift because user is currently on lunch')
		else:
			current_time = get_current_time()
			self._shift_record.append(["shift", self._shift_start_time, current_time])

			self._shift_start_time = False

			print(f"User with id {self.user_id} ended shift at {current_time}")

	def start_break(self):
		if self._shift_start_time == False:
			raise Exception('Cannot start break because user is not on a shift')
		elif self._break_start_time != False:
			raise Exception('Cannot start break because user is already on a break')
		else:
			self._break_start_time = get_current_time()
			print(f"User with id {self.user_id} started break at time {self._break_start_time}")

	def end_break(self):

		if self._shift_start_time == False:
			raise Exception('Cannot end break because user is not on a shift')
		elif self._break_start_time == False:
			raise Exception('Cannot end break because user is not on a break')
		else:
			current_time = get_current_time()
			self._shift_record.append(["break", self._break_start_time, current_time])

			self._break_start_time = False

			print(f"User with id {self.user_id} ended break at {current_time}")

	def start_lunch(self):
			if self._shift_start_time == False:
				raise Exception('Cannot start lunch because user is not on a shift')
			elif self._lunch_start_time != False:
				raise Exception('Cannot start lunch because user is already on a lunch')
			else:
				self._lunch_start_time = get_current_time()
				print(f"User with id {self.user_id} started lunch at time {self._lunch_start_time}")

	def end_lunch(self):

		if self._shift_start_time == False:
			raise Exception('Cannot end lunch because user is not on a shift')
		elif self._lunch_start_time == False:
			raise Exception('Cannot end lunch because user is not on a lunch')
		else:
			current_time = get_current_time()
			self._shift_record.append(["lunch", self._lunch_start_time, current_time])

			self._lunch_start_time = False

			print(f"User with id {self.user_id} ended lunch at {current_time}")

	def print_shift_record(self):

		for type, start, stop in self._shift_record:

			print(f'Type:{type} Start: {start} Stop: {stop}')