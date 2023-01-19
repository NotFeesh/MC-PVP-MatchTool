class PoolEd:
  def __init__(self, pool1, pool2, pool3, pool4, pool5):
    self.pools = [pool1, pool2, pool3, pool4, pool5]

class PoolVar:
  def __init__(self, map1, map2, map3, map4, map5):
    self.maps = [map1, map2, map3, map4, map5]

firstedition = PoolEd(PoolVar("Ruins", "Fortress", "Endstone", "Pillars", "Atlantis"), PoolVar("Glowstone", "StoneBurg", "StoneBurg 2.0", "Landscape", "Dust V"), PoolVar("Themepark", "Darkgrove", "Draze", "Tropical", "Slime"), PoolVar("Library", "Barnyard", "Subway", "Concrete", "Logs"), PoolVar("Icy", "Trainwreck", "Playground", "Hut", "Quartz"))

secondedition = PoolEd(PoolVar("Subway", "Glowstone", "Library", "Slime", "Trainyard"), PoolVar("Ruins", "Endstone", "Tropical", "Blackstone", "Logs"), PoolVar("Quartz", "Trainwreck", "Playground", "Stoneburg", "Subway 2.0"), PoolVar("Icy", "Atlantis", "Hut", "Concrete", "Themepark"), PoolVar("Pillars", "Draze", "Barnyard", "Fortress", "Darkgrove"))

editions = [firstedition, secondedition]

print("Enter Player 1 Name:")
player1 = input()

print("Enter " + player1 + "'s current elo rating:")
elo1 = int(input())

print("Enter Player 2 Name:")
player2 = input()

print("Enter " + player2 + "'s current elo rating:")
elo2 = int(input())

elo_difference = abs(elo1 - elo2)

p1_win = 20
p1_loss = 20
p2_win = 20
p2_loss = 20

if elo_difference > 100:
  if elo1 < elo2: #p1 underdog
    p1_win += round(elo_difference / 10)

    a = p1_loss - round(elo_difference / 10)
    p1_loss = p1_loss - round(elo_difference / 10) if a > 0 else 0

    b = p2_win - round(elo_difference / 20)
    p2_win = p2_win - round(elo_difference / 20) if b > 0 else 0

    p2_loss += round(elo_difference / 20)

    print(player1 + " is the underdog! " + player1 + " will win " + str(p1_win) + " or lose " + str(p1_loss) + ". " + player2 + " will win " + str(p2_win) + " or lose " + str(p2_loss) + ".")
  else: #p2 underdog
    p1_loss += round(elo_difference / 20)

    a = p1_win - round(elo_difference / 20)
    p1_win = p1_win - round(elo_difference / 20) if a > 0 else 0

    b = p2_loss - round(elo_difference / 10)
    p2_loss = p2_loss - round(elo_difference / 10) if b > 0 else 0

    p2_win += round(elo_difference / 10)
    print(player2 + " is the underdog! " + player1 + " will win " + str(p1_win) + " or lose " + str(p1_loss) + ". " + player2 + " will win " + str(p2_win) + " or lose " + str(p2_loss) + ".")
else:
  #"even" match  
  if elo1 < elo2:
    p1_win += 2
    p1_loss -= 2
    p2_win += 2
    p2_loss -= 2
  else:
    p1_win -= 2
    p1_loss += 2
    p2_win -= 2
    p2_loss += 2


minpool = 1
maxpool = 2

print("Enter Map Pool Edition Used: (" + str(minpool) + "-" + str(maxpool) + ")")
ed = int(input())
ed -= 1

#p1 bans a pool; p2 bans a pool; p1 picks a pool to play first; p2 picks a pool to play second; 3rd pool automatically added;
temp = [1, 2, 3, 4, 5]
usedpools = []

print(player1 + " bans a pool (1-5):")
poolban1 = int(input())

usedpools.append(poolban1)
temp.remove(poolban1)

print(player2 + " bans a pool (1-5)")
poolban2 = poolban1
while poolban2 in usedpools:
  poolban2 = int(input())

usedpools.append(poolban2)
temp.remove(poolban2)

print("Pools Banned: " + str(poolban1) + ", " + str(poolban2))

print(player1 + " chooses to play pool (1-5) first:")
poolpick1 = poolban1
while poolpick1 in usedpools:
  poolpick1 = int(input())

usedpools.append(poolpick1)
temp.remove(poolpick1)

print(player2 + " chooses to play pool (1-5) second:")
poolpick2 = poolban1
while poolpick2 in usedpools:
  poolpick2 = int(input())

usedpools.append(poolpick2)
temp.remove(poolpick2)

pools = [poolpick1, poolpick2, temp[0]]

print("The map pools will be played in the following order: " + str(pools[0]) + ", " + str(pools[1]) + ", and " + str(pools[2]))

#P1-POOL: p2 bans a map; p1 bans a map; p2 picks a map to play first; p1 picks a map to play second; 3rd map automatically added;

winner = 0

pool_num = 1

p1_poolscore = 0
p2_poolscore = 0

while p1_poolscore < 2 and p2_poolscore < 2:
  print("PICK & BAN PHASE: POOL #" + str(pools[pool_num - 1]))

  print(editions[ed].pools[pools[pool_num - 1] - 1].maps)

  print(player2 + " bans a map: ")
  mapban2 = 0
  while mapban2 not in editions[ed].pools[pools[pool_num - 1] - 1].maps:
    mapban2 = input()
  editions[ed].pools[pools[pool_num - 1] - 1].maps.remove(mapban2)

  print(player1 + " bans a map: ")
  mapban1 = 0
  while mapban1 not in editions[ed].pools[pools[pool_num - 1] - 1].maps:
    mapban1 = input()
  editions[ed].pools[pools[pool_num - 1] - 1].maps.remove(mapban1)

  print("Maps Banned: " + mapban2 + ", " +  mapban1)

  print(player2 + " chooses to play a map first: ")
  mappick2 = 0
  while mappick2 not in editions[ed].pools[pools[pool_num - 1] - 1].maps:
    mappick2 = input()
  editions[ed].pools[pools[pool_num - 1] - 1].maps.remove(mappick2)

  print(player1 + " chooses to play a map second: ")
  mappick1 = 0
  while mappick1 not in editions[ed].pools[pools[pool_num - 1] - 1].maps:
    mappick1 = input()
  editions[ed].pools[pools[pool_num - 1] - 1].maps.remove(mappick1)

  maps = [mappick2, mappick1, editions[ed].pools[pools[pool_num - 1] - 1].maps[0]]
  print("Maps for Map Pool " + str(pools[pool_num - 1]) + " will be played in the following order: " + maps[0] + ", " + maps[1] + " & " + maps[2])

  #Pool
  print("Pool " + str(pool_num) + " : Match Score " + str(p1_poolscore) + " - " + str(p2_poolscore) + " : Map Pool " + str(pools[pool_num - 1]))
  pool_winner = 0
  #Map
  map_num = 1

  p1_mapscore = 0
  p2_mapscore = 0

  while p1_mapscore < 2 and p2_mapscore < 2:
    #Map
    print("Map " + str(map_num) + " : Map Score " + str(p1_mapscore) + " - " + str(p2_mapscore) + " : " + maps[map_num - 1])
    mapwinner = 0
    #Game
    game_num = 1

    p1_gamescore = 0
    p2_gamescore = 0

    while p1_gamescore < 2 and p2_gamescore < 2:
      print("Game " + str(game_num) + " : Game Score " + str(p1_gamescore) + " - " + str(p2_gamescore))
      print("Enter Game " + str(game_num) + " Winner")
      gamewinner = input()
      if gamewinner == player1:
        p1_gamescore += 1
      else:
        p2_gamescore += 1
      game_num += 1

    if p1_gamescore > p2_gamescore:
      mapwinner = player1
    else:
      mapwinner = player2

    print(mapwinner + " wins " + str(p1_gamescore) + " - " + str(p2_gamescore) + " on " + maps[map_num - 1])
    #Map
    if mapwinner == player1:
      p1_mapscore += 1
    else:
      p2_mapscore += 1
    map_num += 1

  if p1_mapscore > p2_mapscore:
    poolwinner = player1
  else:
    poolwinner = player2

  print(poolwinner + " wins " + str(p1_mapscore) + " - " + str(p2_mapscore) + " on map pool " + str(pools[pool_num - 1]))
  if poolwinner == player1:
    p1_poolscore += 1
  else:
    p2_poolscore += 1
  pool_num += 1

if p1_poolscore > p2_poolscore:
  winner = player1
  elo1 += p1_win
  elo2 -= p2_loss
else:
  winner = player2
  elo2 += p2_win
  elo1 -= p1_loss

print(winner + " wins! " + player1 + "'s new elo rating: " + str(elo1) + ". " + player2 + "'s new elo rating: " + str(elo2) + ".")



  



#MAP1: BO3; MAP2: BO3; MAP3: BO3;
#P2-POOL: p1 bans a map; p2 bans a map; p1 picks a map to play first; p2 picks a map to play second; 3rd map automatically added;
#MAP1: BO3; MAP2: BO3; MAP3: BO3;
#Default-POOL: p1 bans a map; p2 bans a map; MAP1 picked randomly; MAP2 picked randomly; MAP3 picked randomly
#MAP1: BO3; MAP2: BO3; MAP3: BO3;





