#!/usr/bin/env python 

import numpy as np
import matplotlib.pyplot as plt
# from scipy.optimize import curve_fit

#Part IV: Introduce selection. Plot selection coefficient vs fixation time. 


#Update the Wright Fisher model with p = selection parameter given.
def wright_fisher_selection(population, a_count, selection):
    return np.random.binomial(n=2 * population, p=float(a_count * (1 + selection)) / (2 * population + a_count * selection))


#Same generation counter but with the updated Wright Fisher + selection. 
def update_count_selection(population, selection, a_freq= 0.5):
    a_count = int(2 * population * a_freq)
    b_count = int(2 * population - a_count) 

    count = 0 
    while a_count != 0 and b_count != 0: 
        a_count = wright_fisher_selection(population, a_count, selection) 
        b_count = int(2 * population - a_count)

        count += 1

    return count 



if __name__ == "__main__":
    population = 100
    select_coeff = np.linspace(0,1, num= 100) #Generate a range of selection coefficients from 0-1. 
    fixation_generation = []

    for selec in select_coeff:
        fixation_generation.append(update_count_selection(population, selec))


#Started trying to add a fit to the data.
# def fit(x, a, b, c):
#     return a*np.exp(-b * x) - c

# x_data, y_data = optimize.curve_fit(fit, select_coeff, fixation_generation)
# yEXP - fit()


plt.figure()
plt.scatter(select_coeff, fixation_generation, color='purple')
plt.xlabel('Selection Coefficient')
plt.ylabel('Time to Fixation')
plt.title('Selection vs Fixation', size = '16')
plt.savefig("part4.png")
plt.close()
