from Bien.Barkable import Barkable
from Bien.Runnable import Runnable


class Dog(Barkable, Runnable):
	def bark(self):
		print("Dog is barking")

	def run(self):
		print("Dog is running")