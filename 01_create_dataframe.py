import pandas as pd #my first leetcode solution

def createDataframe(student_data):
    return pd.DataFrame(student_data, columns=["student_id", "age"])

