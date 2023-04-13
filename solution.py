from scipy.stats import beta
import numpy as np
from calc_prob import calc_prob_between

chat_id = 611202811 # Ваш chat ID, не меняйте название переменной

def solution(convs_ctrl: int, 
             imps_ctrl: int, 
             convs_test: int, 
             imps_ctrl: int) -> bool:
    a_C, b_C = convs_ctrl+1, imps_ctrl-convs_ctrl+1
    beta_C = beta(a_C, b_C)
    a_T, b_T = convs_test+1, imps_test-convs_test+1
    beta_T = beta(a_T, b_T)

    #calculating the lift
    lift=(beta_T.mean()-beta_C.mean())/beta_C.mean()

    #calculating the probability for Test to be better than Control
    prob=calc_prob_between(beta_T, beta_C)
    if prob <= 0.07:
      return False
    else:
      return True
