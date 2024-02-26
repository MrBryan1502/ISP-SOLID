from abc import ABC, abstractmethod

class Animal(ABC):
	@abstractmethod
	def fly(self):
		pass

	@abstractmethod
	def run(self):
		pass

	@abstractmethod
	def bark(self):
		pass
