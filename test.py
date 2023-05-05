import unittest
import pacman
class Testpacman(unittest.Testcase):
	def test_blocks_ahead_of(self):
		self.assertEqual(pacman.blocks_ahead_of((2,2),1,0),['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'])
		self.assertEqual(pacman.blocks_ahead_of((8,6),0,1),["=", "=", ".", ".", ".", ".", "=", ".", ".", ".", "=", ".", ".", "=", ".", ".", ".", "=", ".", "=", "=", "=", "=", "=", "=", "=", "=", "=", "="]