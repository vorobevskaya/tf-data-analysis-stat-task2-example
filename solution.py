import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 689606612 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    x_mean = x.mean()
    low = (x_mean-0.053)/p + 0.053
    high = (x_mean-0.053)/alpha + 0.053
    result = [low, high]
    return result
