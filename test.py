import unittest

from model import personagemFactory
from model import enemyFactory

class TestGame(unittest.TestCase):

	def test_player_name(self):
		factory_personagem = personagemFactory.PersonagemFactory()
		personagem = factory_personagem.create_personagem('paulus IV')
		self.assertEqual(personagem.get_name(), 'paulus IV')

	# def test_upper(self):
	# 	self.assertEqual('foo'.upper(), 'FOO')

	# def test_isupper(self):
	# 	self.assertTrue('FOO'.isupper())
	# 	self.assertFalse('Foo'.isupper())

	# def test_split(self):
	# 	s = 'hello world'
	# 	self.assertEqual(s.split(), ['hello', 'world'])
	# 	# check that s.split fails when the separator is not a string
	# 	with self.assertRaises(TypeError):
	# 	s.split(2)

if __name__ == '__main__':
	unittest.main()