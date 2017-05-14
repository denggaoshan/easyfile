#encoding:utf-8
import re

"""
"读取一个矩阵
"""
def load_matrix(filename,row=0,col=0,split=' |,|\t|\n'):
    ret = []
    with open(filename,'r') as f:
        lines = f.readlines()
        for line in lines[row:]:
            line = re.split(split,line)
            line = [item for item in filter(lambda x:x != '', line)]
            line = line[col:]
            try:
                line = [ float(x) for x in line ]
            except :
                pass
            ret.append(line) 
    return ret

"""
"读取一个图
"""
def load_gragh(filename):
    pass


"""
"读取训练样本，标签混杂的
"""
def load_sample(filename):
    pass


