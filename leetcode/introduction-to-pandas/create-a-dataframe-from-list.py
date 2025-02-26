import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    dataframe = pd.DataFrame(student_data)
    dataframe.columns = ["student_id", "age"]
    return dataframe