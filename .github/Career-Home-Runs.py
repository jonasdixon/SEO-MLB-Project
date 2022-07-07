import statsapi
import sqlalchemy as db
import pandas as pd

def validate_name(player):
  # Validates player from user to look up in the API
  while player.isdigit() or player == "":
    player = input("Please enter player name in following format -> Lastname: ")
  return player

def get_player_ids(player):
  # Gets the IDs of all the players with the entered last name in the API
  players = statsapi.lookup_player(player)
  player_ids = []
  for id_ in players:
    player_ids.append(id_['id'])
  return player_ids

def ids_to_stats(ids):
  # Uses player IDs to retreive player stats and put them into a dataframe
  player_stats_list = []

  for player_id in ids:
    try:
      stats = statsapi.player_stat_data(player_id, group = 'hitting', type = 'career')['stats'][0]['stats']
      stats.update({'player' : statsapi.lookup_player(player_id)[0]['fullName']})
      player_stats_list.append(stats)
    except:
      pass
  
  return pd.DataFrame(player_stats_list)

def run_program(player_name):
  # Driver for the program. Reruns program if player name is not active / does not exist
  valid_name = validate_name(player_name)
  ids = get_player_ids(valid_name)
  
  hitting_stats = ids_to_stats(ids)
  try:
    grouped_hitting_stats = hitting_stats.groupby('player').sum()
    print(grouped_hitting_stats.sort_values('homeRuns', ascending = False)['homeRuns'])
  except (KeyError):
    player_name = input("There are no active MLB players with that last name. Please enter a new player: ")
    run_program(player_name)

def main():
  player_name = input('Enter an active MLB player (Lastname): ')
  run_program(player_name)
  
if __name__ == "__main__":
  main()
