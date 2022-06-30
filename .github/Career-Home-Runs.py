import statsapi

def find_player():
  player = input('Enter a position player (Firstname Lastname): ')
  player_count = 0
  number = 1
  for player in statsapi.lookup_player(player):
      ++player_count
  if player_count > 1:
    for player in statsapi.lookup_player(player):
      print(f'{number}. Full name: {player['fullName']}, Position: {player['primaryPosition']['abbreviation']}')
      ++number
    player_num = input('Enter a number to specify desired player above: ')
    player = player[player_num - 1]['id'])
    return player
  else:
    if len(player.split()) != 2:
      return "Please enter player name in following format: Firstname Lastname"
    if statsapi.lookup_player(player).position == 'P' | 'SP' | 'RP':
      return "Player entered was not a position player"
  return player

def find_career_high_hrs(player):
  
