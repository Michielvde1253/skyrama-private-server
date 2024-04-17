player_list = [0]

own_user_id = 0
#player_list2 = [ x if x != own_user_id else player_list[8] for x in player_list[0:8] ]
player_list2 = [ x for x in player_list[0:(9 if own_user_id in player_list else 8)] if x != own_user_id ]

print(player_list2)