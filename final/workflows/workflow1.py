from .tasks.task1 import task1
from .tasks.task2 import task2
from .tasks.task3 import task3
from .tasks.task4 import task4
import pandas as pd

def run_wf(source_folder, destination_folder, filename):
    df = task1(source_folder, destination_folder, filename)
    df = task2(df, destination_folder, (filename+'.pkl'))
    _task3 = task3(df.cleaned,df.con)
    _task4 = task4(df)
    
    
    