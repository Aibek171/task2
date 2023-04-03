import pandas as pd
import numpy as np

from scipy.stats import t


chat_id = 1121374935 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    time = 62
    alpha = 1 - p
    loc = np.mean(x)*2/time**2
    return loc + 2/time**2 * (-1/2 + expon.ppf(alpha / 2)) , loc + 2/time**2 * (-1/2 + expon.ppf( 1 - alpha / 2))
