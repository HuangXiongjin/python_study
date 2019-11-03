"""---author==hxj---"""
import random


def new_poker():
    pokers = []
    nums = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    colors = ['♥', '♠', '♣', '♦']
    for num in nums:
        for color in colors:
            pokers.append({'num': num, 'color': color})
    pokers.extend({'num': '小王', 'color': 'black'}, {'nun': '大王', 'color': 'red'})
    return pokers


def shuffle(pokers):
    """洗牌"""
    random.shuffle(pokers)


def deal(pokers):
    poker_iter = iter(pokers)