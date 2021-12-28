from rando_modules.simulate import *

"""This file represents all edges of the world graph that have origin-nodes in the TIK (Toad Town Tunnels) area."""
edges_tik = [
    # TIK_01 Warp Zone 1 (B1)
    {"from": {"map": "TIK_01", "id": 0}, "to": {"map": "TIK_06", "id": 0}, "reqs": []}, # Warp Zone 1 (B1) Exit Right -> Sewer Entrance (B1) Exit Left
    {"from": {"map": "TIK_01", "id": 1}, "to": {"map": "TIK_03", "id": 0}, "reqs": []}, # Warp Zone 1 (B1) Exit Left -> Short Elevator Room (B1) Exit Right
    {"from": {"map": "TIK_01", "id": 2}, "to": {"map": "KMR_02", "id": 3}, "reqs": []}, # Warp Zone 1 (B1) Blue Warp Pipe (Right) -> Goomba Village Blue Warp Pipe
    {"from": {"map": "TIK_01", "id": 3}, "to": {"map": "NOK_02", "id": 2}, "reqs": []}, # Warp Zone 1 (B1) Blue Warp Pipe (Center) -> Koopa Village 2 Blue Pipe
    {"from": {"map": "TIK_01", "id": 4}, "to": {"map": "DRO_01", "id": 2}, "reqs": []}, # Warp Zone 1 (B1) Blue Warp Pipe (Left) -> Outpost 1 Blue Warp Pipe
    
    {"from": {"map": "TIK_01", "id": 0}, "to": {"map": "TIK_01", "id": 1}, "reqs": []}, #? Warp Zone 1 (B1) Exit Right -> Warp Zone 1 (B1) Exit Left
    {"from": {"map": "TIK_01", "id": 1}, "to": {"map": "TIK_01", "id": 0}, "reqs": []}, #? Warp Zone 1 (B1) Exit Left -> Warp Zone 1 (B1) Exit Right
    {"from": {"map": "TIK_01", "id": 0}, "to": {"map": "TIK_01", "id": 2}, "reqs": [require(flag="GF_TIK01_WarpPipes")]}, #? Warp Zone 1 (B1) Exit Right -> Warp Zone 1 (B1) Blue Warp Pipe (Right)
    {"from": {"map": "TIK_01", "id": 2}, "to": {"map": "TIK_01", "id": 0}, "reqs": []}, #? Warp Zone 1 (B1) Blue Warp Pipe (Right) -> Warp Zone 1 (B1) Exit Right
    {"from": {"map": "TIK_01", "id": 0}, "to": {"map": "TIK_01", "id": 3}, "reqs": [require(flag="GF_TIK01_WarpPipes")]}, #? Warp Zone 1 (B1) Exit Right -> Warp Zone 1 (B1) Blue Warp Pipe (Center)
    {"from": {"map": "TIK_01", "id": 3}, "to": {"map": "TIK_01", "id": 0}, "reqs": []}, #? Warp Zone 1 (B1) Blue Warp Pipe (Center) -> Warp Zone 1 (B1) Exit Right
    {"from": {"map": "TIK_01", "id": 0}, "to": {"map": "TIK_01", "id": 4}, "reqs": [require(flag="GF_TIK01_WarpPipes")]}, #? Warp Zone 1 (B1) Exit Right -> Warp Zone 1 (B1) Blue Warp Pipe (Left)
    {"from": {"map": "TIK_01", "id": 4}, "to": {"map": "TIK_01", "id": 0}, "reqs": []}, #? Warp Zone 1 (B1) Blue Warp Pipe (Left) -> Warp Zone 1 (B1) Exit Right
    
    {"from": {"map": "TIK_01", "id": 0}, "to": {"map": "TIK_01", "id": 0}, "reqs": [], "pseudoitems": ["GF_TIK01_WarpPipes"]}, #+ Warp Zone 1 (B1) Exit Right

    # TIK_02 Blooper Boss 1 (B1)
    {"from": {"map": "TIK_02", "id": 0}, "to": {"map": "TIK_18", "id": 1}, "reqs": []}, # Blooper Boss 1 (B1) Exit Left -> Hall to Blooper 1 (B1) Exit Right
    
    {"from": {"map": "TIK_02", "id": 0},        "to": {"map": "TIK_02", "id": "ChestA"}, "reqs": []}, #* Blooper Boss 1 (B1) Exit Left -> ChestA (ShrinkStomp)
    {"from": {"map": "TIK_02", "id": "ChestA"}, "to": {"map": "TIK_02", "id": 0},        "reqs": []}, #* ChestA (ShrinkStomp) -> Blooper Boss 1 (B1) Exit Left

    # TIK_03 Short Elevator Room (B1)
    {"from": {"map": "TIK_03", "id": 0}, "to": {"map": "TIK_01", "id": 1}, "reqs": []}, # Short Elevator Room (B1) Exit Right -> Warp Zone 1 (B1) Exit Left
    {"from": {"map": "TIK_03", "id": 1}, "to": {"map": "TIK_04", "id": 2}, "reqs": []}, # Short Elevator Room (B1) Green Pipe Left -> Scales Room (B2) Green Pipe TopLeft
    
    {"from": {"map": "TIK_03", "id": 0}, "to": {"map": "TIK_03", "id": 1}, "reqs": []}, #? Short Elevator Room (B1) Exit Right -> Short Elevator Room (B1) Green Pipe Left
    {"from": {"map": "TIK_03", "id": 1}, "to": {"map": "TIK_03", "id": 0}, "reqs": []}, #? Short Elevator Room (B1) Green Pipe Left -> Short Elevator Room (B1) Exit Right
    
    {"from": {"map": "TIK_03", "id": 0},         "to": {"map": "TIK_03", "id": "YBlockA"}, "reqs": []}, #* Short Elevator Room (B1) Exit Right -> YBlockA (SnowmanDoll)
    {"from": {"map": "TIK_03", "id": "YBlockA"}, "to": {"map": "TIK_03", "id": 0},         "reqs": []}, #* YBlockA (SnowmanDoll) -> Short Elevator Room (B1) Exit Right
    {"from": {"map": "TIK_03", "id": 0},         "to": {"map": "TIK_03", "id": "YBlockB"}, "reqs": []}, #* Short Elevator Room (B1) Exit Right -> YBlockB (Coin)
    {"from": {"map": "TIK_03", "id": "YBlockB"}, "to": {"map": "TIK_03", "id": 0},         "reqs": []}, #* YBlockB (Coin) -> Short Elevator Room (B1) Exit Right
    {"from": {"map": "TIK_03", "id": 0},         "to": {"map": "TIK_03", "id": "YBlockC"}, "reqs": []}, #* Short Elevator Room (B1) Exit Right -> YBlockC (Coin)
    {"from": {"map": "TIK_03", "id": "YBlockC"}, "to": {"map": "TIK_03", "id": 0},         "reqs": []}, #* YBlockC (Coin) -> Short Elevator Room (B1) Exit Right

    # TIK_04 Scales Room (B2)
    {"from": {"map": "TIK_04", "id": 0}, "to": {"map": "TIK_05", "id": 0}, "reqs": []}, # Scales Room (B2) Exit Left -> Spring Room (B2) Exit Right
    {"from": {"map": "TIK_04", "id": 1}, "to": {"map": "TIK_07", "id": 0}, "reqs": []}, # Scales Room (B2) Exit Right -> Elevator Attic Room (B2) Exit Left
    {"from": {"map": "TIK_04", "id": 2}, "to": {"map": "TIK_03", "id": 1}, "reqs": []}, # Scales Room (B2) Green Pipe TopLeft -> Short Elevator Room (B1) Green Pipe Left
    {"from": {"map": "TIK_04", "id": 3}, "to": {"map": "TIK_12", "id": 0}, "reqs": []}, # Scales Room (B2) Green Pipe BottomRight -> Metal Block Room (B3) Green Pipe Left
    
    {"from": {"map": "TIK_04", "id": 0}, "to": {"map": "TIK_04", "id": 1}, "reqs": []}, #? Scales Room (B2) Exit Left -> Scales Room (B2) Exit Right
    {"from": {"map": "TIK_04", "id": 1}, "to": {"map": "TIK_04", "id": 0}, "reqs": []}, #? Scales Room (B2) Exit Right -> Scales Room (B2) Exit Left
    {"from": {"map": "TIK_04", "id": 0}, "to": {"map": "TIK_04", "id": 2}, "reqs": []}, #? Scales Room (B2) Exit Left -> Scales Room (B2) Green Pipe TopLeft
    {"from": {"map": "TIK_04", "id": 2}, "to": {"map": "TIK_04", "id": 0}, "reqs": []}, #? Scales Room (B2) Green Pipe TopLeft -> Scales Room (B2) Exit Left
    {"from": {"map": "TIK_04", "id": 0}, "to": {"map": "TIK_04", "id": 3}, "reqs": []}, #? Scales Room (B2) Exit Left -> Scales Room (B2) Green Pipe BottomRight
    {"from": {"map": "TIK_04", "id": 3}, "to": {"map": "TIK_04", "id": 0}, "reqs": []}, #? Scales Room (B2) Green Pipe BottomRight -> Scales Room (B2) Exit Left

    # TIK_05 Spring Room (B2)
    {"from": {"map": "TIK_05", "id": 0}, "to": {"map": "TIK_04", "id": 0}, "reqs": []}, # Spring Room (B2) Exit Right -> Scales Room (B2) Exit Left
    
    {"from": {"map": "TIK_05", "id": 0},        "to": {"map": "TIK_05", "id": "ChestA"}, "reqs": []}, #* Spring Room (B2) Exit Right -> ChestA (PowerSmash1)
    {"from": {"map": "TIK_05", "id": "ChestA"}, "to": {"map": "TIK_05", "id": 0},        "reqs": []}, #* ChestA (PowerSmash1) -> Spring Room (B2) Exit Right

    # TIK_06 Sewer Entrance (B1)
    {"from": {"map": "TIK_06", "id": 0}, "to": {"map": "TIK_01", "id": 0}, "reqs": []}, # Sewer Entrance (B1) Exit Left -> Warp Zone 1 (B1) Exit Right
    {"from": {"map": "TIK_06", "id": 1}, "to": {"map": "TIK_18", "id": 0}, "reqs": []}, # Sewer Entrance (B1) Exit Right -> Hall to Blooper 1 (B1) Exit Left
    {"from": {"map": "TIK_06", "id": 2}, "to": {"map": "TIK_08", "id": 3}, "reqs": []}, # Sewer Entrance (B1) Green Pipe Left -> Second Level Entry (B2) Green Pipe Left
    {"from": {"map": "TIK_06", "id": 3}, "to": {"map": "MAC_02", "id": 4}, "reqs": []}, # Sewer Entrance (B1) Green Pipe Up -> Southern District Open Pipe
    {"from": {"map": "TIK_06", "id": 4}, "to": {"map": "TIK_08", "id": 2}, "reqs": []}, # Sewer Entrance (B1) Hole In Ground -> Second Level Entry (B2) Hole In Ceiling

    {"from": {"map": "TIK_06", "id": 3}, "to": {"map": "TIK_06", "id": 0}, "reqs": [require(hammer=1)]}, #? Sewer Entrance (B1) Green Pipe Up -> Sewer Entrance (B1) Exit Left
    {"from": {"map": "TIK_06", "id": 0}, "to": {"map": "TIK_06", "id": 3}, "reqs": []}, #? Sewer Entrance (B1) Exit Left -> Sewer Entrance (B1) Green Pipe Up
    {"from": {"map": "TIK_06", "id": 3}, "to": {"map": "TIK_06", "id": 1}, "reqs": [require(hammer=0)]}, #? Sewer Entrance (B1) Green Pipe Up -> Sewer Entrance (B1) Exit Right
    {"from": {"map": "TIK_06", "id": 1}, "to": {"map": "TIK_06", "id": 3}, "reqs": []}, #? Sewer Entrance (B1) Exit Right -> Sewer Entrance (B1) Green Pipe Up
    {"from": {"map": "TIK_06", "id": 3}, "to": {"map": "TIK_06", "id": 4}, "reqs": [require(boots=1)]}, #? Sewer Entrance (B1) Green Pipe Up -> Sewer Entrance (B1) Hole In Ground
    {"from": {"map": "TIK_06", "id": 4}, "to": {"map": "TIK_06", "id": 3}, "reqs": []}, #? Sewer Entrance (B1) Hole In Ground -> Sewer Entrance (B1) Green Pipe Up
    {"from": {"map": "TIK_06", "id": 2}, "to": {"map": "TIK_06", "id": 3}, "reqs": []}, #? Sewer Entrance (B1) Green Pipe Left -> Sewer Entrance (B1) Green Pipe Up

    # TIK_07 Elevator Attic Room (B2)
    {"from": {"map": "TIK_07", "id": 0}, "to": {"map": "TIK_04", "id": 1}, "reqs": []}, # Elevator Attic Room (B2) Exit Left -> Scales Room (B2) Exit Right
    {"from": {"map": "TIK_07", "id": 1}, "to": {"map": "TIK_07", "id": 2}, "reqs": []}, # Elevator Attic Room (B2) Green Pipe Left -> Elevator Attic Room (B2) Green Pipe Right
    {"from": {"map": "TIK_07", "id": 2}, "to": {"map": "TIK_07", "id": 1}, "reqs": []}, # Elevator Attic Room (B2) Green Pipe Right -> Elevator Attic Room (B2) Green Pipe Left
    
    {"from": {"map": "TIK_07", "id": 0}, "to": {"map": "TIK_07", "id": 2}, "reqs": []}, #? Elevator Attic Room (B2) Exit Left -> Elevator Attic Room (B2) Green Pipe Right
    {"from": {"map": "TIK_07", "id": 1}, "to": {"map": "TIK_07", "id": 0}, "reqs": []}, #? Elevator Attic Room (B2) Green Pipe Left -> Elevator Attic Room (B2) Exit Left
    
    {"from": {"map": "TIK_07", "id": 0},       "to": {"map": "TIK_07", "id": "ItemA"}, "reqs": [require(partner="PARTNER_Parakarry")]}, #* Elevator Attic Room (B2) Exit Left -> ItemA (StarPiece)
    {"from": {"map": "TIK_07", "id": "ItemA"}, "to": {"map": "TIK_07", "id": 0},       "reqs": []}, #* ItemA (StarPiece) -> Elevator Attic Room (B2) Exit Left

    # TIK_08 Second Level Entry (B2)
    {"from": {"map": "TIK_08", "id": 0}, "to": {"map": "TIK_09", "id": 1}, "reqs": []}, # Second Level Entry (B2) Exit Left -> Warp Zone 2 (B2) Exit Right
    {"from": {"map": "TIK_08", "id": 1}, "to": {"map": "TIK_20", "id": 0}, "reqs": []}, # Second Level Entry (B2) Exit Right -> Room with Spikes (B2) Exit Left
    {"from": {"map": "TIK_08", "id": 2}, "to": {"map": None, "id": None}, "reqs": []},  # Second Level Entry (B2) Hole In Ceiling
    {"from": {"map": "TIK_08", "id": 3}, "to": {"map": "TIK_06", "id": 2}, "reqs": []}, # Second Level Entry (B2) Green Pipe Left -> Sewer Entrance (B1) Green Pipe Left
    {"from": {"map": "TIK_08", "id": 4}, "to": {"map": "JAN_03", "id": 3}, "reqs": []}, # Second Level Entry (B2) Blue Warp Pipe -> Village Buildings Blue Warp Pipe
    
    {"from": {"map": "TIK_08", "id": 0}, "to": {"map": "TIK_08", "id": 1}, "reqs": [require(partner="PARTNER_Sushie")]}, #? Second Level Entry (B2) Exit Left -> Second Level Entry (B2) Exit Right
    {"from": {"map": "TIK_08", "id": 1}, "to": {"map": "TIK_08", "id": 0}, "reqs": [require(partner="PARTNER_Sushie")]}, #? Second Level Entry (B2) Exit Right -> Second Level Entry (B2) Exit Left
    {"from": {"map": "TIK_08", "id": 2}, "to": {"map": "TIK_08", "id": 0}, "reqs": []}, #? Second Level Entry (B2) Hole In Ceiling -> Second Level Entry (B2) Exit Left
    {"from": {"map": "TIK_08", "id": 0}, "to": {"map": "TIK_08", "id": 3}, "reqs": []}, #? Second Level Entry (B2) Exit Left -> Second Level Entry (B2) Green Pipe Left
    {"from": {"map": "TIK_08", "id": 3}, "to": {"map": "TIK_08", "id": 0}, "reqs": []}, #? Second Level Entry (B2) Green Pipe Left -> Second Level Entry (B2) Exit Left
    {"from": {"map": "TIK_08", "id": 1}, "to": {"map": "TIK_08", "id": 4}, "reqs": [require(flag="GF_TIK08_WarpPipe")]}, #? Second Level Entry (B2) Exit Right -> Second Level Entry (B2) Blue Warp Pipe
    {"from": {"map": "TIK_08", "id": 4}, "to": {"map": "TIK_08", "id": 1}, "reqs": []}, #? Second Level Entry (B2) Blue Warp Pipe -> Second Level Entry (B2) Exit Right
    
    {"from": {"map": "TIK_08", "id": 1}, "to": {"map": "TIK_08", "id": 1}, "reqs": [], "pseudoitems": ["GF_TIK08_WarpPipe"]}, #+ Second Level Entry (B2) Exit Right

    # TIK_09 Warp Zone 2 (B2) 
    {"from": {"map": "TIK_09", "id": 0}, "to": {"map": "TIK_10", "id": 0}, "reqs": []}, # Warp Zone 2 (B2) Exit Left -> Block Puzzle Room (B2) Exit Right
    {"from": {"map": "TIK_09", "id": 1}, "to": {"map": "TIK_08", "id": 0}, "reqs": []}, # Warp Zone 2 (B2) Exit Right -> Second Level Entry (B2) Exit Left
    {"from": {"map": "TIK_09", "id": 2}, "to": {"map": "MIM_11", "id": 3}, "reqs": []}, # Warp Zone 2 (B2) Blue Warp Pipe -> Outside Boo's Mansion Blue Warp Pipe
    
    {"from": {"map": "TIK_09", "id": 0}, "to": {"map": "TIK_09", "id": 1}, "reqs": []}, #? Warp Zone 2 (B2) Exit Left -> Warp Zone 2 (B2) Exit Right
    {"from": {"map": "TIK_09", "id": 1}, "to": {"map": "TIK_09", "id": 0}, "reqs": []}, #? Warp Zone 2 (B2) Exit Right -> Warp Zone 2 (B2) Exit Left
    {"from": {"map": "TIK_09", "id": 0}, "to": {"map": "TIK_09", "id": 2}, "reqs": [require(flag="GF_TIK09_WarpPipe")]}, #? Warp Zone 2 (B2) Exit Left -> Warp Zone 2 (B2) Blue Warp Pipe
    {"from": {"map": "TIK_09", "id": 2}, "to": {"map": "TIK_09", "id": 0}, "reqs": []}, #? Warp Zone 2 (B2) Blue Warp Pipe -> Warp Zone 2 (B2) Exit Left

    {"from": {"map": "TIK_09", "id": 0}, "to": {"map": "TIK_09", "id": 0}, "reqs": [], "pseudoitems": ["GF_TIK09_WarpPipe"]}, #+ Warp Zone 2 (B2) Exit Left

    # TIK_10 Block Puzzle Room (B2)
    {"from": {"map": "TIK_10", "id": 0}, "to": {"map": "TIK_09", "id": 0}, "reqs": []}, # Block Puzzle Room (B2) Exit Right -> Warp Zone 2 (B2) Exit Left
    
    {"from": {"map": "TIK_10", "id": 0},               "to": {"map": "TIK_10", "id": "HiddenYBlockA"}, "reqs": [require(partner="PARTNER_Watt")]}, #* Block Puzzle Room (B2) Exit Right -> HiddenYBlockA (Coin)
    {"from": {"map": "TIK_10", "id": "HiddenYBlockA"}, "to": {"map": "TIK_10", "id": 0},               "reqs": []}, #* HiddenYBlockA (Coin) -> Block Puzzle Room (B2) Exit Right
    {"from": {"map": "TIK_10", "id": 0},               "to": {"map": "TIK_10", "id": "HiddenYBlockB"}, "reqs": [require(partner="PARTNER_Watt")]}, #* Block Puzzle Room (B2) Exit Right -> HiddenYBlockB (Coin)
    {"from": {"map": "TIK_10", "id": "HiddenYBlockB"}, "to": {"map": "TIK_10", "id": 0},               "reqs": []}, #* HiddenYBlockB (Coin) -> Block Puzzle Room (B2) Exit Right
    {"from": {"map": "TIK_10", "id": 0},               "to": {"map": "TIK_10", "id": "HiddenYBlockC"}, "reqs": [require(partner="PARTNER_Watt")]}, #* Block Puzzle Room (B2) Exit Right -> HiddenYBlockC (Coin)
    {"from": {"map": "TIK_10", "id": "HiddenYBlockC"}, "to": {"map": "TIK_10", "id": 0},               "reqs": []}, #* HiddenYBlockC (Coin) -> Block Puzzle Room (B2) Exit Right

    # TIK_12 Metal Block Room (B3)
    {"from": {"map": "TIK_12", "id": 0}, "to": {"map": "TIK_04", "id": 3}, "reqs": []}, # Metal Block Room (B3) Green Pipe Left -> Scales Room (B2) Green Pipe BottomRight

    # TIK_14 Rip Cheato Antechamber (B3)
    {"from": {"map": "TIK_14", "id": 0}, "to": {"map": "TIK_21", "id": 2}, "reqs": []}, # Rip Cheato Antechamber (B3) Green Pipe Left -> Hidden Blocks Room (B2) Green Pipe BottomRight
    {"from": {"map": "TIK_14", "id": 1}, "to": {"map": "TIK_15", "id": 0}, "reqs": []}, # Rip Cheato Antechamber (B3) Bomb Wall Right -> Rip Cheato's Home (B3) Bomb Wall Left
    
    {"from": {"map": "TIK_14", "id": 0}, "to": {"map": "TIK_14", "id": 1}, "reqs": [require(partner="PARTNER_Bombette")]}, #? Rip Cheato Antechamber (B3) Green Pipe Left -> Rip Cheato Antechamber (B3) Bomb Wall Right
    {"from": {"map": "TIK_14", "id": 1}, "to": {"map": "TIK_14", "id": 0}, "reqs": []}, #? Rip Cheato Antechamber (B3) Bomb Wall Right -> Rip Cheato Antechamber (B3) Green Pipe Left

    # TIK_15 Rip Cheato's Home (B3)
    {"from": {"map": "TIK_15", "id": 0}, "to": {"map": "TIK_14", "id": 1}, "reqs": []}, # Rip Cheato's Home (B3) Bomb Wall Left -> Rip Cheato Antechamber (B3) Bomb Wall Right
    {"from": {"map": "TIK_15", "id": 1}, "to": {"map": "MAC_02", "id": 5}, "reqs": []}, # Rip Cheato's Home (B3) Green Pipe Right -> Southern District Blue House Pipe
    
    {"from": {"map": "TIK_15", "id": 0}, "to": {"map": "TIK_15", "id": 1}, "reqs": []}, #? Rip Cheato's Home (B3) Bomb Wall Left -> Rip Cheato's Home (B3) Green Pipe Right
    {"from": {"map": "TIK_15", "id": 1}, "to": {"map": "TIK_15", "id": 0}, "reqs": [require(partner="PARTNER_Bombette")]}, #? Rip Cheato's Home (B3) Green Pipe Right -> Rip Cheato's Home (B3) Bomb Wall Left

    {"from": {"map": "TIK_15", "id": 1},       "to": {"map": "TIK_15", "id": "GiftA"}, "reqs": []}, #* Rip Cheato's Home (B3) Green Pipe Right -> GiftA (StarPiece3F)
    {"from": {"map": "TIK_15", "id": "GiftA"}, "to": {"map": "TIK_15", "id": 1},       "reqs": []}, #* GiftA (StarPiece3F) -> Rip Cheato's Home (B3) Green Pipe Right
    {"from": {"map": "TIK_15", "id": 1},       "to": {"map": "TIK_15", "id": "GiftB"}, "reqs": []}, #* Rip Cheato's Home (B3) Green Pipe Right -> GiftB (LifeShroom)
    {"from": {"map": "TIK_15", "id": "GiftB"}, "to": {"map": "TIK_15", "id": 1},       "reqs": []}, #* GiftB (LifeShroom) -> Rip Cheato's Home (B3) Green Pipe Right
    {"from": {"map": "TIK_15", "id": 1},       "to": {"map": "TIK_15", "id": "GiftC"}, "reqs": []}, #* Rip Cheato's Home (B3) Green Pipe Right -> GiftC (BumpAttack)
    {"from": {"map": "TIK_15", "id": "GiftC"}, "to": {"map": "TIK_15", "id": 1},       "reqs": []}, #* GiftC (BumpAttack) -> Rip Cheato's Home (B3) Green Pipe Right
    {"from": {"map": "TIK_15", "id": 1},       "to": {"map": "TIK_15", "id": "GiftD"}, "reqs": []}, #* Rip Cheato's Home (B3) Green Pipe Right -> GiftD (RepelGel)
    {"from": {"map": "TIK_15", "id": "GiftD"}, "to": {"map": "TIK_15", "id": 1},       "reqs": []}, #* GiftD (RepelGel) -> Rip Cheato's Home (B3) Green Pipe Right
    {"from": {"map": "TIK_15", "id": 1},       "to": {"map": "TIK_15", "id": "GiftE"}, "reqs": []}, #* Rip Cheato's Home (B3) Green Pipe Right -> GiftE (StarPiece40)
    {"from": {"map": "TIK_15", "id": "GiftE"}, "to": {"map": "TIK_15", "id": 1},       "reqs": []}, #* GiftE (StarPiece40) -> Rip Cheato's Home (B3) Green Pipe Right
    {"from": {"map": "TIK_15", "id": 1},       "to": {"map": "TIK_15", "id": "GiftF"}, "reqs": []}, #* Rip Cheato's Home (B3) Green Pipe Right -> GiftF (SuperShroom)
    {"from": {"map": "TIK_15", "id": "GiftF"}, "to": {"map": "TIK_15", "id": 1},       "reqs": []}, #* GiftF (SuperShroom) -> Rip Cheato's Home (B3) Green Pipe Right
    {"from": {"map": "TIK_15", "id": 1},       "to": {"map": "TIK_15", "id": "GiftG"}, "reqs": []}, #* Rip Cheato's Home (B3) Green Pipe Right -> GiftG (Mushroom)
    {"from": {"map": "TIK_15", "id": "GiftG"}, "to": {"map": "TIK_15", "id": 1},       "reqs": []}, #* GiftG (Mushroom) -> Rip Cheato's Home (B3) Green Pipe Right
    {"from": {"map": "TIK_15", "id": 1},       "to": {"map": "TIK_15", "id": "GiftH"}, "reqs": []}, #* Rip Cheato's Home (B3) Green Pipe Right -> GiftH (DriedShroom)
    {"from": {"map": "TIK_15", "id": "GiftH"}, "to": {"map": "TIK_15", "id": 1},       "reqs": []}, #* GiftH (DriedShroom) -> Rip Cheato's Home (B3) Green Pipe Right
    {"from": {"map": "TIK_15", "id": 1},       "to": {"map": "TIK_15", "id": "GiftI"}, "reqs": []}, #* Rip Cheato's Home (B3) Green Pipe Right -> GiftI (DriedShroom)
    {"from": {"map": "TIK_15", "id": "GiftI"}, "to": {"map": "TIK_15", "id": 1},       "reqs": []}, #* GiftI (DriedShroom) -> Rip Cheato's Home (B3) Green Pipe Right
    {"from": {"map": "TIK_15", "id": 1},       "to": {"map": "TIK_15", "id": "GiftJ"}, "reqs": []}, #* Rip Cheato's Home (B3) Green Pipe Right -> GiftI (StarPiece41)
    {"from": {"map": "TIK_15", "id": "GiftJ"}, "to": {"map": "TIK_15", "id": 1},       "reqs": []}, #* GiftI (StarPiece41) -> Rip Cheato's Home (B3) Green Pipe Right
    {"from": {"map": "TIK_15", "id": 1},       "to": {"map": "TIK_15", "id": "GiftK"}, "reqs": []}, #* Rip Cheato's Home (B3) Green Pipe Right -> GiftK (DriedShroom)
    {"from": {"map": "TIK_15", "id": "GiftK"}, "to": {"map": "TIK_15", "id": 1},       "reqs": []}, #* GiftK (DriedShroom) -> Rip Cheato's Home (B3) Green Pipe Right

    # TIK_17 Frozen Room (B3)
    {"from": {"map": "TIK_17", "id": 0}, "to": {"map": "TIK_22", "id": 1}, "reqs": []}, # Frozen Room (B3) Green Pipe Left -> Path to Shiver City (B2) Green Pipe
    {"from": {"map": "TIK_17", "id": 1}, "to": {"map": "SAM_02", "id": 2}, "reqs": []}, # Frozen Room (B3) Green Pipe Right -> Shiver City Center Greep Pipe
    
    {"from": {"map": "TIK_17", "id": 0}, "to": {"map": "TIK_17", "id": 1}, "reqs": []}, #? Frozen Room (B3) Green Pipe Left -> Frozen Room (B3) Green Pipe Right
    {"from": {"map": "TIK_17", "id": 1}, "to": {"map": "TIK_17", "id": 0}, "reqs": []}, #? Frozen Room (B3) Green Pipe Right -> Frozen Room (B3) Green Pipe Left

    # TIK_18 Hall to Blooper 1 (B1)
    {"from": {"map": "TIK_18", "id": 0}, "to": {"map": "TIK_06", "id": 1}, "reqs": []}, # Hall to Blooper 1 (B1) Exit Left -> Sewer Entrance (B1) Exit Right
    {"from": {"map": "TIK_18", "id": 1}, "to": {"map": "TIK_02", "id": 0}, "reqs": []}, # Hall to Blooper 1 (B1) Exit Right -> Blooper Boss 1 (B1) Exit Left
    
    {"from": {"map": "TIK_18", "id": 0}, "to": {"map": "TIK_18", "id": 1}, "reqs": []}, #? Hall to Blooper 1 (B1) Exit Left -> Hall to Blooper 1 (B1) Exit Right
    {"from": {"map": "TIK_18", "id": 1}, "to": {"map": "TIK_18", "id": 0}, "reqs": []}, #? Hall to Blooper 1 (B1) Exit Right -> Hall to Blooper 1 (B1) Exit Left
    
    {"from": {"map": "TIK_18", "id": 0},               "to": {"map": "TIK_18", "id": "HiddenYBlockA"}, "reqs": [require(partner="PARTNER_Watt")]}, #* Hall to Blooper 1 (B1) Exit Left -> HiddenYBlockA (SuperShroom)
    {"from": {"map": "TIK_18", "id": "HiddenYBlockA"}, "to": {"map": "TIK_18", "id": 0},               "reqs": []}, #* HiddenYBlockA (SuperShroom) -> Hall to Blooper 1 (B1) Exit Left

    # TIK_19 Under the Toad Town Pond
    {"from": {"map": "TIK_19", "id": 0}, "to": {"map": "MAC_00", "id": 3}, "reqs": []}, # Under the Toad Town Pond Green Pipe Left -> Gate District Island Pipe

    # TIK_20 Room with Spikes (B2)
    {"from": {"map": "TIK_20", "id": 0}, "to": {"map": "TIK_08", "id": 1}, "reqs": []}, # Room with Spikes (B2) Exit Left -> Second Level Entry (B2) Exit Right
    {"from": {"map": "TIK_20", "id": 1}, "to": {"map": "TIK_21", "id": 0}, "reqs": []}, # Room with Spikes (B2) Exit Right -> Hidden Blocks Room (B2) Exit Left
    {"from": {"map": "TIK_20", "id": 2}, "to": {"map": "TIK_23", "id": 1}, "reqs": []}, # Room with Spikes (B2) Green Pipe Center -> Windy Path (B3) Green Pipe
    
    {"from": {"map": "TIK_20", "id": 0}, "to": {"map": "TIK_20", "id": 1}, "reqs": []}, #? Room with Spikes (B2) Exit Left -> Room with Spikes (B2) Exit Right
    {"from": {"map": "TIK_20", "id": 1}, "to": {"map": "TIK_20", "id": 0}, "reqs": []}, #? Room with Spikes (B2) Exit Right -> Room with Spikes (B2) Exit Left
    {"from": {"map": "TIK_20", "id": 0}, "to": {"map": "TIK_20", "id": 2}, "reqs": [require(partner="PARTNER_Lakilester")]}, #? Room with Spikes (B2) Exit Left -> Room with Spikes (B2) Green Pipe Center
    {"from": {"map": "TIK_20", "id": 2}, "to": {"map": "TIK_20", "id": 0}, "reqs": [require(partner="PARTNER_Lakilester")]}, #? Room with Spikes (B2) Green Pipe Center -> Room with Spikes (B2) Exit Left
    
    {"from": {"map": "TIK_20", "id": 1},         "to": {"map": "TIK_20", "id": "YBlockA"}, "reqs": [require(boots=2)]}, #* Room with Spikes (B2) Exit Right -> YBlockA (ShootingStar)
    {"from": {"map": "TIK_20", "id": "YBlockA"}, "to": {"map": "TIK_20", "id": 1},         "reqs": []}, #* YBlockA (ShootingStar) -> Room with Spikes (B2) Exit Right

    # TIK_21 Hidden Blocks Room (B2)
    {"from": {"map": "TIK_21", "id": 0}, "to": {"map": "TIK_20", "id": 1}, "reqs": []}, # Hidden Blocks Room (B2) Exit Left -> Room with Spikes (B2) Exit Right
    {"from": {"map": "TIK_21", "id": 1}, "to": {"map": "TIK_22", "id": 0}, "reqs": []}, # Hidden Blocks Room (B2) Top Right Door -> Path to Shiver City (B2) Left Door
    {"from": {"map": "TIK_21", "id": 2}, "to": {"map": "TIK_14", "id": 0}, "reqs": []}, # Hidden Blocks Room (B2) Green Pipe BottomRight -> Rip Cheato Antechamber (B3) Green Pipe Left
    
    {"from": {"map": "TIK_21", "id": 0}, "to": {"map": "TIK_21", "id": 1}, "reqs": [require(flag="GF_TIK21_HiddenItem_CoinA"),require(flag="GF_TIK21_HiddenItem_CoinB"),require(flag="GF_TIK21_HiddenItem_CoinC"),require(flag="GF_TIK21_HiddenItem_CoinD")]}, #? Hidden Blocks Room (B2) Exit Left -> Hidden Blocks Room (B2) Top Right Door
    {"from": {"map": "TIK_21", "id": 1}, "to": {"map": "TIK_21", "id": 0}, "reqs": []}, #? Hidden Blocks Room (B2) Top Right Door -> Hidden Blocks Room (B2) Exit Left
    {"from": {"map": "TIK_21", "id": 0}, "to": {"map": "TIK_21", "id": 2}, "reqs": []}, #? Hidden Blocks Room (B2) Exit Left -> Hidden Blocks Room (B2) Green Pipe BottomRight
    {"from": {"map": "TIK_21", "id": 2}, "to": {"map": "TIK_21", "id": 0}, "reqs": []}, #? Hidden Blocks Room (B2) Green Pipe BottomRight -> Hidden Blocks Room (B2) Exit Left
    
    {"from": {"map": "TIK_21", "id": 0},               "to": {"map": "TIK_21", "id": "YBlockA"},       "reqs": [require(boots=2)]}, #* Hidden Blocks Room (B2) Exit Left -> YBlockA (Coin)
    {"from": {"map": "TIK_21", "id": "YBlockA"},       "to": {"map": "TIK_21", "id": 0},               "reqs": []}, #* YBlockA (Coin) -> Hidden Blocks Room (B2) Exit Left
    {"from": {"map": "TIK_21", "id": 0},               "to": {"map": "TIK_21", "id": "HiddenYBlockA"}, "reqs": [require(boots=2),require(partner="PARTNER_Watt")], "pseudoitems": ["GF_TIK21_HiddenItem_CoinA"]}, #* Hidden Blocks Room (B2) Exit Left -> HiddenYBlockA (Coin)
    {"from": {"map": "TIK_21", "id": "HiddenYBlockA"}, "to": {"map": "TIK_21", "id": 0},               "reqs": []}, #* HiddenYBlockA (Coin) -> Hidden Blocks Room (B2) Exit Left
    {"from": {"map": "TIK_21", "id": 0},               "to": {"map": "TIK_21", "id": "HiddenYBlockB"}, "reqs": [require(boots=2),require(partner="PARTNER_Watt")], "pseudoitems": ["GF_TIK21_HiddenItem_CoinB"]}, #* Hidden Blocks Room (B2) Exit Left -> HiddenYBlockB (Coin)
    {"from": {"map": "TIK_21", "id": "HiddenYBlockB"}, "to": {"map": "TIK_21", "id": 0},               "reqs": []}, #* HiddenYBlockB (Coin) -> Hidden Blocks Room (B2) Exit Left
    {"from": {"map": "TIK_21", "id": 0},               "to": {"map": "TIK_21", "id": "HiddenYBlockC"}, "reqs": [require(boots=2),require(partner="PARTNER_Watt")], "pseudoitems": ["GF_TIK21_HiddenItem_CoinC"]}, #* Hidden Blocks Room (B2) Exit Left -> HiddenYBlockC (Coin)
    {"from": {"map": "TIK_21", "id": "HiddenYBlockC"}, "to": {"map": "TIK_21", "id": 0},               "reqs": []}, #* HiddenYBlockC (Coin) -> Hidden Blocks Room (B2) Exit Left
    {"from": {"map": "TIK_21", "id": 0},               "to": {"map": "TIK_21", "id": "HiddenYBlockD"}, "reqs": [require(boots=2),require(partner="PARTNER_Watt")], "pseudoitems": ["GF_TIK21_HiddenItem_CoinD"]}, #* Hidden Blocks Room (B2) Exit Left -> HiddenYBlockD (Coin)
    {"from": {"map": "TIK_21", "id": "HiddenYBlockD"}, "to": {"map": "TIK_21", "id": 0},               "reqs": []}, #* HiddenYBlockD (Coin) -> Hidden Blocks Room (B2) Exit Left

    # TIK_22 Path to Shiver City (B2)
    {"from": {"map": "TIK_22", "id": 0}, "to": {"map": "TIK_21", "id": 1}, "reqs": []}, # Path to Shiver City (B2) Left Door -> Hidden Blocks Room (B2) Top Right Door
    {"from": {"map": "TIK_22", "id": 1}, "to": {"map": "TIK_17", "id": 0}, "reqs": []}, # Path to Shiver City (B2) Green Pipe -> Frozen Room (B3) Green Pipe Left
    
    {"from": {"map": "TIK_22", "id": 0}, "to": {"map": "TIK_22", "id": 1}, "reqs": []}, #? Path to Shiver City (B2) Left Door -> Path to Shiver City (B2) Green Pipe
    {"from": {"map": "TIK_22", "id": 1}, "to": {"map": "TIK_22", "id": 0}, "reqs": []}, #? Path to Shiver City (B2) Green Pipe -> Path to Shiver City (B2) Left Door

    # TIK_23 Windy Path (B3)
    {"from": {"map": "TIK_23", "id": 0}, "to": {"map": "TIK_24", "id": 1}, "reqs": []}, # Windy Path (B3) Exit Left -> Hall to Ultra Boots (B3) Exit Right
    {"from": {"map": "TIK_23", "id": 1}, "to": {"map": "TIK_20", "id": 2}, "reqs": []}, # Windy Path (B3) Green Pipe -> Room with Spikes (B2) Green Pipe Center
    
    {"from": {"map": "TIK_23", "id": 0}, "to": {"map": "TIK_23", "id": 1}, "reqs": []}, #? Windy Path (B3) Exit Left -> Windy Path (B3) Green Pipe
    {"from": {"map": "TIK_23", "id": 1}, "to": {"map": "TIK_23", "id": 0}, "reqs": [require(hammer=1)]}, #? Windy Path (B3) Green Pipe -> Windy Path (B3) Exit Left
    
    {"from": {"map": "TIK_23", "id": 1},               "to": {"map": "TIK_23", "id": "HiddenYBlockA"}, "reqs": [require(partner="PARTNER_Watt")]}, #* Windy Path (B3) Green Pipe -> HiddenYBlockA (MapleSyrup)
    {"from": {"map": "TIK_23", "id": "HiddenYBlockA"}, "to": {"map": "TIK_23", "id": 1},               "reqs": []}, #* HiddenYBlockA (MapleSyrup) -> Windy Path (B3) Green Pipe
    {"from": {"map": "TIK_23", "id": 1},               "to": {"map": "TIK_23", "id": "HiddenYBlockB"}, "reqs": [require(partner="PARTNER_Watt")]}, #* Windy Path (B3) Green Pipe -> HiddenYBlockB (StopWatch)
    {"from": {"map": "TIK_23", "id": "HiddenYBlockB"}, "to": {"map": "TIK_23", "id": 1},               "reqs": []}, #* HiddenYBlockB (StopWatch) -> Windy Path (B3) Green Pipe
    {"from": {"map": "TIK_23", "id": 1},               "to": {"map": "TIK_23", "id": "HiddenYBlockC"}, "reqs": [require(partner="PARTNER_Watt")]}, #* Windy Path (B3) Green Pipe -> HiddenYBlockC (VoltShroom)
    {"from": {"map": "TIK_23", "id": "HiddenYBlockC"}, "to": {"map": "TIK_23", "id": 1},               "reqs": []}, #* HiddenYBlockC (VoltShroom) -> Windy Path (B3) Green Pipe
    {"from": {"map": "TIK_23", "id": 1},               "to": {"map": "TIK_23", "id": "YBlockA"},       "reqs": []}, #* Windy Path (B3) Green Pipe -> YBlockA (Coin)
    {"from": {"map": "TIK_23", "id": "YBlockA"},       "to": {"map": "TIK_23", "id": 1},               "reqs": []}, #* YBlockA (Coin) -> Windy Path (B3) Green Pipe

    # TIK_24 Hall to Ultra Boots (B3)
    {"from": {"map": "TIK_24", "id": 0}, "to": {"map": "TIK_25", "id": 0}, "reqs": []}, # Hall to Ultra Boots (B3) Exit Left -> Ultra Boots Room (B3) Exit Right
    {"from": {"map": "TIK_24", "id": 1}, "to": {"map": "TIK_23", "id": 0}, "reqs": []}, # Hall to Ultra Boots (B3) Exit Right -> Windy Path (B3) Exit Left
    
    {"from": {"map": "TIK_24", "id": 0}, "to": {"map": "TIK_24", "id": 1}, "reqs": []}, #? Hall to Ultra Boots (B3) Exit Left -> Hall to Ultra Boots (B3) Exit Right
    {"from": {"map": "TIK_24", "id": 1}, "to": {"map": "TIK_24", "id": 0}, "reqs": [require(hammer=2)]}, #? Hall to Ultra Boots (B3) Exit Right -> Hall to Ultra Boots (B3) Exit Left
    
    {"from": {"map": "TIK_24", "id": 1},               "to": {"map": "TIK_24", "id": "HiddenYBlockA"}, "reqs": [require(boots=2),require(partner="PARTNER_Watt")]}, #* Hall to Ultra Boots (B3) Exit Right -> HiddenYBlockA (LifeShroom)
    {"from": {"map": "TIK_24", "id": "HiddenYBlockA"}, "to": {"map": "TIK_24", "id": 1},               "reqs": []}, #* HiddenYBlockA (LifeShroom) -> Hall to Ultra Boots (B3) Exit Right
    {"from": {"map": "TIK_24", "id": 1},               "to": {"map": "TIK_24", "id": "YBlockA"},       "reqs": [require(boots=2)]}, #* Hall to Ultra Boots (B3) Exit Right -> YBlockA (Coin)
    {"from": {"map": "TIK_24", "id": "YBlockA"},       "to": {"map": "TIK_24", "id": 1},               "reqs": []}, #* YBlockA (Coin) -> Hall to Ultra Boots (B3) Exit Right
    {"from": {"map": "TIK_24", "id": 1},               "to": {"map": "TIK_24", "id": "YBlockB"},       "reqs": [require(boots=2)]}, #* Hall to Ultra Boots (B3) Exit Right -> YBlockB (Coin)
    {"from": {"map": "TIK_24", "id": "YBlockB"},       "to": {"map": "TIK_24", "id": 1},               "reqs": []}, #* YBlockB (Coin) -> Hall to Ultra Boots (B3) Exit Right

    # TIK_25 Ultra Boots Room (B3)
    {"from": {"map": "TIK_25", "id": 0}, "to": {"map": "TIK_24", "id": 0}, "reqs": []}, # Ultra Boots Room (B3) Exit Right -> Hall to Ultra Boots (B3) Exit Left

    {"from": {"map": "TIK_25", "id": 0}, "to": {"map": "TIK_25", "id": 0}, "reqs": [], "pseudoitems": ["EQUIPMENT_Boots_Progressive"]}, #+ Ultra Boots Room (B3) Exit Right
]
