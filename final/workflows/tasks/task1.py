import pandas as pd
import json
from pandas.io.json import json_normalize
import shutil

def task1(source_filepath, destination, filename):
    ''' ingest and find all the input file(s) that will be used in the preprocessing
        Args:
            Param1(str): Source File Path
            Param2(str): destination file path once finished processing
        Returns:
            dataframe 
    ''' 
    data = []
    with open((source_filepath+filename)) as f:
        for line in f:
            data.append(json.loads(line))        
    df = pd.DataFrame.from_dict(json_normalize(data), orient='columns')
    #df = df.sample(frac=0.002)
    shutil.move((source_filepath+filename), (destination+filename))
    return df