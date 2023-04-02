import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 1121374935 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    time = 62
    alpha = 1 - p
    loc = (2*x/time**2).mean()
    scale = np.sqrt(np.var(x)) / np.sqrt(len(x))
    return loc - scale * norm.ppf(1 - alpha / 2), \
           loc - scale * norm.ppf(alpha / 2)
