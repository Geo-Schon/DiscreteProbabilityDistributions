# В первом ящике находится 10 мячей, из которых 7 - белые. Во втором ящике - 11 мячей, из которых 9 белых.
# Из каждого ящика вытаскивают случайным образом по два мяча. Какова вероятность того, что все мячи белые?
# Какова вероятность того, что ровно два мяча белые? Какова вероятность того, что хотя бы один мяч белый?

from Combi import combination


allwhiteballs = combination(7, 2)*combination(3, 0)/combination(10, 2) * combination(9, 2)*combination(2, 0)\
           / combination(11, 2)
print(
    f"Вероятность того, что все мячи белые = {allwhiteballs :.4f} -> {allwhiteballs *100:0.2f}%")


twowhiteballs = combination(7, 2)*combination(3, 0)/combination(10, 2) * combination(9, 0)*combination(2, 2)/combination(11, 2) \
    + combination(7, 1)*combination(3, 1)/combination(10, 2) * combination(9, 1)*combination(2, 1)/combination(11, 2) \
    + combination(7, 0)*combination(3, 2)/combination(10, 2) * combination(9, 2)*combination(2, 0)/combination(11, 2)
print(
    f"Вероятность того, что ровно два мяча белые = {twowhiteballs:.4f} -> {twowhiteballs*100:0.2f}%")


onewhiteball = 1 - combination(7, 0)*combination(3, 2)/combination(10, 2) * combination(9, 0)*combination(2, 2)\
              / combination(11, 2)
print(
    f"Вероятность того, что хотя бы один мяч белый = {onewhiteball:.4f} -> {onewhiteball*100:0.2f}%")