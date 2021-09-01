import numpy as np
grade2 = [4.3, 4.0, 4.5, 4.5, 4.3, 2.5, 4.3, 4.5]
grade3 = [3.3, 2.5, 4.5, 4.5, 4.5, 3.5, 4.5, 2.5, 4.3]
grade4 = [4.0, 4.5, 4.5, 4.5, 4.3, 4.0, 4.0, 4.3, 4.5, 3.5, 4.5, 4.3]
num2 = (3*np.array(grade2)).sum() / 3*len(grade2)
num3 = (3*np.array(grade3)).sum() / 3*len(grade3)
num4 = (3*np.array(grade4)).sum() / 3*len(grade4)
print('2학년: {}\n3학년: {}\n4학년: {}'.format(num2, num3, num4))
