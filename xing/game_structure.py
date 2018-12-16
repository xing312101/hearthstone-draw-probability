####################################################################
# 作者：李俞興 (LEE, YU-XING)
# 功能：output 資料結構
####################################################################

class ProbabilityOuput(object):
    pass

class ProbabilityNode(object):
    def __init__(self, parent_node, round_number, num_remaining_card, base_probability, num_wanted_card, num_dup_card_wanted_one):
        self.__parent_node = parent_node
        self.__round_number = round_number
        self.__num_remaining_card = num_remaining_card
        self.__base_probability = base_probability
        self.__num_wanted_card = num_wanted_card
        self.__num_dup_card_wanted_one = num_dup_card_wanted_one

    def calculate_probability(self):
        pass

class Round(object):
    def __init__(self):
        self.__round_number = 0
        self.__probability_nodes = []

    def get_probabilities(self):
        pass

    def get_probability(self):
        pass

class Game(object):
    def __init__(self, catagory, num_swap = 0):
        self.catagory = catagory
        self.num_swap = num_swap
        self.__round_now = 0
        self.__rounds = []

    def next_round(self):
        pass

    def last_round(self):
        pass

    def add_round(self, round):
        pass

    def get_round(self, round_number):
        pass

    def get_rounds(self):
        pass