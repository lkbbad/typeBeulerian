from numpy.polynomial import polynomial as np

p_1_x_pos = (1)
p_1_x_neg = (1)
p_1_x_pos_d = np.Polynomial(np.polyder(p_1_x_pos))
p_1_x_neg_d = np.Polynomial(np.polyder(p_1_x_neg))

p_2_x_pos = 