import pandas as pd
import numpy as np

from scipy.stats import expon


chat_id = 1121374935 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    time = 62
    alpha = 1 - p
    return (expon.ppf(alpha / 2)/len(x) + x.min() - 1/2)*2/time**2, (expon.ppf(1 - alpha / 2)/len(x) + x.min() - 1/2)*2/time**2
