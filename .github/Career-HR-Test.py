import unittest
from Career-Home-Runs import *


class TestFileName(unittest.TestCase):
    def test_validate_name(self):
        self.assertEqual(validate_name('Judge'), 'Judge')
        self.assertEqual(validate_name('Ramirez')), 'Ramirez')
    
    def test_active_players(self):
        self.assertEqual(ids_to_stats(get_player_ids('Ramirez')).groupby('player')
                         .sum().sort_values('homeRuns', ascending = False)['homeRuns'], 
                         'player
                          Jose Ramirez      179
                          Harold Ramirez     22
                          Erasmo Ramirez      0
                          Noe Ramirez         0
                          Yohan Ramirez       0
                          Name: homeRuns, dtype: int64')
    
    def test_inactive_players(self):
        self.assertEqual()

    def test_matching_last_name(self):
        self.assertEqual(, 0)

if __name__ == '__main__':
    unittest.main()