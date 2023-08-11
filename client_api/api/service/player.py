import os 
import sys
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from typing import List
## from ..struct.player import Player
from .. import struct
# talk to Charlie about how these import statements work. 
import xml.etree.ElementTree as ET

root_dir = os.path.realpath(os.path.join(os.path.dirname(__file__), '../'))
source_dir = os.path.join(root_dir, '../src')
xml_file_path = f"{source_dir}/fantasy.xml"

def get_list() -> List[struct.player.Player]:
    players = []
    tree = ET.parse(xml_file_path)
    root = tree.getroot()
    id_counter = 1 # initialize id counter to 1
    for dataitem in root.findall('dataitem'):
        player = struct.player.Player() # Uses Player object from Struct 
        player.id = id_counter # set player id to the current value of id_counter
        id_counter += 1 # increment id_counter for the next player
        player.rank = int(dataitem.find('RK').text)
        player.name = dataitem.find('PLAYER-NAME').text.strip()
        player.team = dataitem.find('TEAM').text.strip()
        player.position = dataitem.find('POS').text.strip()
        player.bye = int(dataitem.find('BYE-WEEK').text)
        players.append(player)
    return players

# just for testing 
get_list()

# only two functions needed for PoC, can easily create others if needed
def get(id: int) -> struct.player.Player:
    players = get_list()
    for player in players:
        if player.id == id:
            return player
    return None



# def get(id:int, players: List[struct.player.Player]) -> struct.player.Player: 
#     # Load the player data from the XML file
#     tree = ET.parse('players.xml')
#     root = tree.getroot()

#     players = get_list("/home/jlo/projects/test-project/src/fantasy.xml")

#     # Find the player element with the given ID
#     player_elem = None
#     for elem in root:
#         if elem.attrib['id'] == str(id):
#             player_elem = elem
#             break

#     if player_elem is None:
#         return None

#     # Extract the player data from the element
#     player = {}
#     for child in player_elem:
#         player[child.tag] = child.text.strip()

#     player['id'] = id
#     return player

    # return {
    #         'id': 456,
    #         'name': 'Test Player',
    #         'team': 'Some Team',
    #         # rank, bye, position, etc
    #     }

# def create(player):
#     # @todo: Insert the player to the database, return id
#     # @todo: Return the complete player object with updated id
#     # (may want to select the new player from the database, rather than modifying the input player)


#     tree = parse_player_data("/home/jlo/projects/test-project/src/fantasy.xml")
#     root = tree.getroot()

#     # Generate a new player ID by incrementing the last ID in the file
#     player_id = int(root[-1].attrib['id']) + 1
#     print(player_id)

#     # Create a new player element and populate it with the given data
#     new_player = ET.Element('dataitem', {'id': str(player_id)})
#     for key, value in player.items():
#         elem = ET.Element(key)
#         elem.text = str(value)
#         new_player.append(elem)

#     # Add the new player element to the root element and write the changes to the file
#     root.append(new_player)
#     tree.write()

#     # Return the complete player object with updated ID
#     player['id'] = player_id
#     return player

# def update(id, player):
#     # @todo: Check that a player with this id already exists
#     # @todo: Update the database, and get the latest player data
#     # Load the player data from the XML file
#     tree = ET.parse('players.xml')
#     root = tree.getroot()

#     # Find the player element with the given ID
#     player_elem = None
#     for elem in root:
#         if elem.attrib['id'] == str(id):
#             player_elem = elem
#             break

#     if player_elem is None:
#         raise ValueError("Player with ID {} not found".format(id))

#     # Update the player element with the new data
#     for key, value in player.items():
#         elem = player_elem.find(key)
#         if elem is None:
#             elem = ET.Element(key)
#             player_elem.append(elem)
#         elem.text = str(value)

#     # Write the changes to the XML file
#     tree.write('players.xml')

#     # Return the updated player object
#     player['id'] = id
#     return player



# def get_list():
#     # @todo: Get all the players from the database

#     # Load the player data from the XML file
#     tree = ET.parse('players.xml')
#     root = tree.getroot()

#     # Extract the player data from each element and add it to a list
#     player_list = []
#     for elem in root:
#         player = {}
#         for child in elem:
#             player[child.tag] = child.text.strip()
#         player['id'] = int(elem.attrib['id'])
#         player_list.append(player)

#     return player_list
    
    # return [
    #         {
    #             'id': 456,
    #             'name': 'Test Player',
    #             'team': 'Some Team',
    #             # rank, bye, position, etc
    #         },
    #     ]
