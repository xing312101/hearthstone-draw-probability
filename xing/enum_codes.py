####################################################################
# 作者：李俞興 (LEE, YU-XING)
# 功能：資料定義
####################################################################
#from enum import IntEnum, unique

class StartingHandChoice():
    # 起手換牌選擇
    NoSwap = 0 # 不換牌
    KeepOneCard = 1 # 只留一張
    KeepTwoCard = 2 # 只留兩張
    KeepThreeCard = 3 # 只留三張，先手不會用到


class GameCatagory():
    NoneStarting = 0 # 沒有起手，遊戲中途
    FrontStart = 1 # 起手，先手
    BackStart = 2 # 起手，後手


class MaxNumOfStartingSwap():
    FrontStart = 3 # 爐石先手可以換3張牌
    BackStart = 4 # 爐石後手可以換4張牌