#encoding:utf-8
import time

def write_data(data,file,before,after):
    type1 = [str,int,float]
    if type(data) in type1:
        file.write(before + str(data)+ after)
    if type(data) is list:
        if type(data[0]) is not list:
            file.write(before+'\n'+str(data)+'\n'+after)
        elif type(data[0]) is list: #2D array
            print data
            file.write(before+'\n')
            for row in data:
                file.write(str(row) + '\n')
            file.write(after)

"""
"保存数据，默认文件名叫做output.sav，默认是追加
"""
def save(data,before='',after='\n',mod='a+',filename="output.sav"):
    with open(filename,mod) as f:
        write_data(data,f,before,after)
                

def static_vars(**kwargs):
    def decorate(func):
        for k in kwargs:
            setattr(func, k, kwargs[k])
        return func
    return decorate


"""
"保存数据到Log.
"""
@static_vars(counter = 0)
def elog(data,before='',after='\n',mod='a+',filename='log'):
    elog.counter += 1
    if elog.counter == 1:
         with open(filename,mod) as f:
             f.write('-----'+time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))+'-----\n')
    save(data,before,after,mod,filename)



