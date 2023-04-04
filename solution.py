import pandas as pd
import numpy as np

from scipy.stats import expon


chat_id = 1121374935 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    time = 62
    alpha = 1 - p
    n = len(x)
    return (-min(-x) - 1/2)*2/time**2, (-np.log(alpha)/n - min(-x) - 1/2)*2/time**2
