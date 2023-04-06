import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 689606612 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    loc = x.max()
    low = loc
    high = (loc-0.053)/pow(alpha, 1/len(x))+0.053
    result = [low, high]
    return result
