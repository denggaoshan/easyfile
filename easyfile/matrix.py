#encoding:utf-8
import re

__version__ = 't_1.0'

def load_matrix(filename,spliter=' |\n|\t|,'):
    ret = []
    with open(filename,'r') as f:
        lines = f.readlines()
        for line in lines:
            result = re.split(spliter,line)
            result = [item for item in filter(lambda x:x != '', result)]
            ret.append(result)
    return ret

def load_matrix_row(filename,row_number,spliter=' |\n|\t|,'):
    with open(filename,'r') as f:
        lines = f.readlines()
        line = lines[row_number]
        result = re.split(spliter,line)
        result = [item for item in filter(lambda x:x != '', result)]
        return result

if __name__ == '__main__':
    load_matrix('datas/type1.csv')
