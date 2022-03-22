import numpy as np
import random
import pandas as pd

part_1 = []
for i in range(0, 104, 6):
    random.seed(i)
    part_1.append(random.randrange(40, 100, 2))

np.random.seed(41)
part_2 = np.random.randint(30, 100, size=(3, 6))

part_1 = np.reshape(part_1, (3, 6))
weighted = np.rint(part_1*0.4 + part_2*0.6).astype(int)

person1_average = np.rint(np.average(weighted[0])).astype(int)
person2_average = np.rint(np.average(weighted[1])).astype(int)
person3_average = np.rint(np.average(weighted[2])).astype(int)

person1 = np.ndarray.tolist(weighted[0])
person1.append(person1_average)
person2 = np.ndarray.tolist(weighted[1])
person2.append(person2_average)
person3 = np.ndarray.tolist(weighted[2])
person3.append(person3_average)

meaned = np.array((person1,person2,person3))

scores_average = np.rint(np.average(meaned, axis=0)).astype(int)
scores_average = np.reshape(scores_average,(1,7))


df = pd.DataFrame(meaned, index=["person1", "person2", "person3"], columns=["Scores1", "Scores2", "Scores3", "Scores4",
                                                                            "Scores5", "Scores6", "AVG_person"])
avg = pd.DataFrame(scores_average, index=["AVG_scr"],  columns=["       ","       ","       ","       ","       ",
                                                                "       ","          "])


print(df)
print("-------------------------------------------------------------------------")
print(avg)

