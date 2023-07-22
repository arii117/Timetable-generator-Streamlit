import streamlit as st
import random
import numpy as np

st.title("Timetable Generator")

st.write("YOU CAN USE THE FOLLOWING ABBREVIATIONS FOR THE SUBJECTS:")
st.write("PHYSICS ---->PHY")

lst = []
d = 0
p = 0

subnum = st.number_input("Enter number of subjects:", min_value=0, step=1, value=0)

for i in range(0, subnum):
    sub = st.text_input(f"Enter subject abbreviation {i+1}:")  # Use i+1 as a unique identifier for the key
    f = st.number_input(f"Enter hours in a Week {i+1}:", min_value=1, step=1, value=1)  # Use i+1 as a unique identifier for the key
    d = d + f
    for i in range(0, f):
        lst.append(sub)

if (d > 30):
    st.write("Invalid input")
else:
    for i in range(0, 30 - d):
        ele = "CCA"
        lst.append(ele)

R = 6
C = 5

k = st.number_input("Enter number of timetables:", min_value=1, step=1, value=1)

for p in range(k):
    lst1 = []
    matrix = []
    m = []
    time = ["8-9   ", "9-10  ", "10-11 ", "11-12 ", "12-1  ", "1-2   "]

    for i in range(R):
        a = []
        for j in range(C):
            item = lst[0]
            a.append(item)
            lst.remove(item)
            lst1.append(item)

        matrix.append(a)
        m = np.array(matrix)
        matrix1 = m.T
        for e in range(5):
            random.shuffle(matrix1[e])
        m1 = np.array(matrix1)
        matrix2 = m1.T

    for m in range(30):
        lst.append(lst1[m])

    st.write(f"-----FE {p + 1} ------")
    table_data = np.column_stack((time, matrix2))
    st.table(table_data)
