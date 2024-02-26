from abc import ABC, abstractmethod


class Barkable(ABC):
	@abstractmethod
	def bark(self):
		pass