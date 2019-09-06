Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> players = [29, 58, 66, 71, 87]
>>> players[2]
66
>>> players[2] = 68
>>> players
[29, 58, 68, 71, 87]
>>> players = [90, 91, 98]
>>> players
[90, 91, 98]
>>> players = [29, 58, 66, 71, 87]
>>> players
[29, 58, 66, 71, 87]
>>> players + [90, 91, 98]
[29, 58, 66, 71, 87, 90, 91, 98]
>>> players
[29, 58, 66, 71, 87]
>>> players.append(120)
>>> players
[29, 58, 66, 71, 87, 120]
>>> players[:2]
[29, 58]
>>> players[:2] = [0, 0]
>>> players
[0, 0, 66, 71, 87, 120]
>>> players[:2] = []
>>> players
[66, 71, 87, 120]
>>> players[:] = []
>>> players
[]
>>> 
