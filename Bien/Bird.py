from Bien.Flyable import Flyable
from Bien.Runnable import Runnable


class Bird(Flyable, Runnable):
	def fly(self):
		print("Bird is flying")

	def run(self):
		print("Bird is running")