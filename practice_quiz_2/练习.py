# load in necessary packages/libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



test_list = [150, None, "??", 172.5, 130, "error", 165]


#写一个循环，遇到不是数字的项就打印它在列表中的位置，其他数字则加到总和里。

index = 0
sum = 0

for test in test_list:
    index = index + 1
    if (type(test) != int) and (type(test) != float):
        print("not a number")
        print(index)
        continue
    sum = sum + test

print(sum)

    





#下面的代码想算 1+2+...+n，但是错了。修复它，让 n=25 时结果正确。

n = 25
total = 0
for i in range(1, n+1):
    total = total + i
print(total)

#从 HeightWeight DataFrame 中提取第 100–150 行（包含 150），保存成 subset，再按 "Weight_Pounds" 从低到高排序。

df = pd.read_csv('/Users/cynthia/Desktop/practice_quiz_2/data_folder/HeightWeight-quiz.csv')

subset = df.iloc[100:151, ]

sorted = subset.sort_values(by = "Weight_Pounds")

sorted.head()



#(d) Filtering 用布尔条件筛选，得到两个新的子集：

#Height_Inches 在 65 到 70（包含边界）之间的。

#qd = df[(df["Height_Inches"] >= 65) & df(df["Height_Inches"] <= 70)]
qd = df[(df["Height_Inches"] >= 65) & df(df["Height_Inches"] <= 70)]
print(qd)




#Weight_Pounds < 110 或者 Height_Inches > 72 的。




