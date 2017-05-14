#encoding:utf-8
import re

DEFAULT_SPLITER = ' |\n|\t|,'

def load_matrix(filename,spliter=DEFAULT_SPLITER):
    ret = []
    with open(filename,'r') as f:
        lines = f.readlines()
        for line in lines:
            result = re.split(spliter,line)
            result = [item for item in filter(lambda x:x != '', result)]
            ret.append(result)
    return ret

def load_matrix_row(filename,row_number,spliter=DEFAULT_SPLITER,,empty='r'):
    with open(filename,'r') as f:
        lines = f.readlines()
        line = lines[row_number]
        result = re.split(spliter,line)
        result = [item for item in filter(lambda x:x != '', result)]
        return result


def load_matrix_col(filename,col_number,spliter=DEFAULT_SPLITER,empty='r'):
    with open(filename,'r') as f:
        lines = f.readlines()
        ret = []
        for line in lines:
            result = re.split(spliter,line)
            result = [item for item in filter(lambda x:x != '', result)]
            line.s
        line = lines[col_number]
        
        
        return result