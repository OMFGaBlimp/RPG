'''
Created on 07/10/2014

@author: 22491
'''
import functions, entities

def setmap_world_map(player_gridx, player_gridy):
    map = ["MFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF",
           "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF",
           "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF",
           "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF",
           "FFFWWWWWWWFFFFFFFFFFFFFFFFFFFFF",
           "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF",
           "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF",
           "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF",
           "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF",
           "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF",
           "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF",
           "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF",
           "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF",
           "FFFFFFFFFFFFFFFFFFFWMMMMFFFFFFF",
           "FFFFFFFFFFFFFFFFFFFWMWWMFFFFFFF",
           "FFFFFFFFFFFFFFFFFFFWMMMMFFFFFFF",
           "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF",
           "FFFFFFFFFFWWWWFFFFFFFFFFFFFFFFF",
           "FFFFFFFFFFWWWWFFFFFFFFFFFFFFFFF",
           "FFFFFFFFFFWWWWFFFFFFFFFFFFFFFFF",
           "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF",
           "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF",
           "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF",
           "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF",
           "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF",
           "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF",
           "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF",
           "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF",
           "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF",
           "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF"]
    return map
    
def load_map(map):
    for rowindex, row in enumerate(map):
        for columnindex, column in enumerate(row):
            if column == "F":
                walkabletile = entities.walkable_map(columnindex, rowindex)
            elif column == "W":
                watertile = entities.water_map(columnindex, rowindex)
            elif column == "M":
                mountaintile = entities.mountain_map(columnindex, rowindex)
                 