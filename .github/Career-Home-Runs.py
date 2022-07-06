import statsapi
import sqlalchemy as db
import pandas as pd

def validate_name(player):
  # Validates player from user to look up in the API
  while player.isdigit() or player == "":
    player = input("Please enter player name in following format: Lastname")
  return player

def get_player_ids(player):
  players = statsapi.lookup_player(player)
  player_ids = []
  for id_ in players:
    player_ids.append(id_['id'])
  return player_ids

def ids_to_stats(ids):
  player_stats_list = []

  for player_id in ids:
    try:
      stats = statsapi.player_stat_data(player_id, group = 'homeRuns', type = 'career')['stats'][0]['stats']
      stats.update({'player' : statsapi.lookup_player(player_id)[0]['fullName']})
      player_stats_list.append(stats)
    except:
      pass
    print(pd.DataFrame(player_stats_list))

def main():
  player_name = input('Enter an MLB player (Lastname): ')
  valid_name = validate_name(player_name)
  ids = get_player_ids(valid_name)
  ids_to_stats(ids)
  # print(statsapi.league_leaders('homeRuns', season=2019, playerPool = 'rookies', limit = 5))

if __name__ == "__main__":
  main()