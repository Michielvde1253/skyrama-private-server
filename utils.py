def get_level_by_xp(current_xp, level_caps):
    current_level = 100 # Handle the edge case when you're at the last level
    j = 0
    for i in level_caps:
      if int(i) > current_xp:
        current_level = j
        return current_level
      j = j + 1