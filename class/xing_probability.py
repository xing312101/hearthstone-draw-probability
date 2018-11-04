####################################################################
# 作者：李俞興 (LEE, Yu-Xing)
# 功能：排列組合機率
####################################################################

import math

class XingProbability(object):
    # 優化: 可以考慮把階乘結果在記憶體紀錄，須先確認在python能加快不然沒有意義。

    @staticmethod
    def cal(num_samples, num_sample_space):
        # 機率計算
        # num_sample: 樣本數量
        # num_sample_space: 樣本空間內樣本總數量

        return (num_samples / num_sample_space)

    @staticmethod
    def factorial(n):
        # 階乘計算

        return math.factorial(n)

    @staticmethod
    def permutations(num_samples, num_sampling, reduplicate = False):
        # 排列
        # 目前不考慮環狀，只是來算爐石抽牌用不到
        # num_sample: 樣本數量
        # num_sample_space: 樣本空間內樣本總數量
        # reduplicate: 重複抽取

        if reduplicate:
            return math.pow(num_samples, num_sampling)
        else:
            # 優化: 可以考慮自己運算減少乘法運算，須先確認在python能加快不然沒有意義。
            return math.factorial(num_samples) / math.factorial(num_samples - num_sampling)


    @staticmethod
    def combinations(num_samples, num_sampling, reduplicate = False):
        # 組合
        # 目前不考慮環狀，只是來算爐石抽牌用不到
        # num_sample: 樣本數量
        # num_sample_space: 樣本空間內樣本總數量
        # reduplicate: 重複抽取

        if reduplicate:
            return math.factorial(num_samples + num_sampling - 1) / (math.factorial(num_sampling) * math.factorial(num_sampling - 1))
        else:
            # 優化: 可以考慮自己運算減少乘法運算，須先確認在python能加快不然沒有意義。
            return math.factorial(num_samples) / (math.factorial(num_samples - num_sampling) * math.factorial(num_sampling))
