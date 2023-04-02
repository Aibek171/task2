import pandas as pd
import numpy as np

from scipy.stats import t


chat_id = 1121374935 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    time = 62
    alpha = 1 - p
    n=len(x)
    z = x*2/time**2
    loc = np.mean(x)*2/time**2
    se = np.sqrt(np.sum((z - loc)**2)/(n-1)) / np.sqrt(n)
    return loc + se * t.ppf(alpha/2, n-1), loc + se * t.ppf(1 - alpha/2, n-1)
