import pandas as pd
import numpy as np

from scipy.stats import t


chat_id = 1121374935 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    time = 62
    n=len(x)
    z = x*2/time**2
    loc = np.mean(x)*2/time**2
    se = np.sqrt(np.sum((z - loc)**2)/(n-1)) / np.sqrt(n)
    t_val = t.ppf(1-p/2, n-1)
    return loc - se * t_val, loc + se * t_val
