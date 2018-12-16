####################################################################
# 作者：李俞興 (LEE, YU-XING)
# 功能：爐石抽牌機率
####################################################################
import xing.xing_math as XingMath
import xing.enum_codes as GameEnums
import xing.game_structure as GameStructure

class HearthstoneDrawProbability:

    def __init__(self,
                num_max_card = 30 ,
                num_wanted_card = 1,
                num_dup_card_wanted_one = 0,
                b_starting = True):
        # num_max_card: 卡牌總數量或者當下剩餘牌堆張數
        # num_wanted_card： 想抽到的卡牌數量
        # num_dup_card_wanted_one： 在牌組中有重複的卡牌種類裡有幾種只需要抽到一張的，比如牌堆有兩張小斧但只想抽一張
        # b_starting：是否新的牌局，判斷要不要算起手的機率
        self.__num_max_card = num_max_card
        self.__num_wanted_card = num_wanted_card
        self.__num_dup_card_wanted_one = num_dup_card_wanted_one
        self.__b_starting = b_starting

        self.games = [] # collection all games

    def valid(self):
        pass

    def play(self):
        if (self.__b_starting):
            # 先手
            for num_swap in range(GameEnums.MaxNumOfStartingSwap.FrontStart):
                game = GameStructure.Game(GameEnums.GameCatagory.FrontStart, num_swap)
                self.games.append(game)

                front_start_probability = self.starting_hand_probability()
                self.round_draw_probability(game, 1, None, self.__num_max_card, front_start_probability, self.__num_wanted_card, self.__num_dup_card_wanted_one)

            # 後手
            for num_swap in range(GameEnums.MaxNumOfStartingSwap.BackStart):
                game = GameStructure.Game(GameEnums.GameCatagory.BackStart, num_swap)
                self.games.append(game)

                back_start_probability = self.starting_hand_probability()
                self.round_draw_probability(game, 1, None, self.__num_max_card, back_start_probability, self.__num_wanted_card, self.__num_dup_card_wanted_one)


        else:
            game = GameStructure.Game(GameEnums.GameCatagory.NoneStarting)
            self.games.append(game)
            self.round_draw_probability(game, 1, None, self.__num_max_card, 1, self.__num_wanted_card, self.__num_dup_card_wanted_one)

    def starting_hand_probability(self):
        pass

    def round_draw_probability(self,
                                game,
                                round_number,
                                last_node,
                                num_remaining_card,
                                base_probability,
                                num_wanted_card,
                                num_dup_card_wanted_one):

        round = game.get_round(round_number)

        if (None == round):
            round = round.new()

        # calculate this node probability
        probability_node = GameStructure.ProbabilityNode(
            last_node,
            round_number,
            num_remaining_card,
            base_probability,
            num_wanted_card,
            num_dup_card_wanted_one)

        success_probability = probability_node.calculate_probability
        unsuccess_probability = 1 - success_probability

        # next nodes of next round
        next_round_number = round_number + 1
        next_num_remaining_card = num_remaining_card - 1
        next_num_wanted_card = num_wanted_card - 1
        if (0 < num_remaining_card):
            ## success_probability and num_wanted_card > 0 and num_remaining_card > 0
            if (0 < next_num_wanted_card):
                self.round_draw_probability(game,
                                            next_round_number,
                                            probability_node,
                                            next_num_remaining_card,
                                            success_probability,
                                            next_num_wanted_card,
                                            num_dup_card_wanted_one)

            ## unsuccess_probability and num_remaining_card > 0
            self.round_draw_probability(game,
                                        next_round_number,
                                        probability_node,
                                        next_num_remaining_card,
                                        unsuccess_probability,
                                        num_wanted_card,
                                        num_dup_card_wanted_one)

