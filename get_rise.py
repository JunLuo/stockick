import os

dir_name = "./stoke/"
file_list = os.listdir(dir_name)
wre = open("./lessrise_result.txt","w")

stoke_file = open("./stoke_number.txt", "r")
stoke_list = {}
for line in stoke_file:
    if line.find("(") != -1:
        stoke_list[line[line.index("(") + 1:line.index(")")]] = line[0:line.index("(")]

for file_name in file_list:
    code = file_name[:-4]
    f = open(dir_name+file_name, 'r')
    logs = [line.split(',') for line in f.read().split("\n")[1:-1]]
    f.close()    
    close = [float(log[-3]) for log in logs]    
    min_close = reduce(lambda x,y: x if x<y else y, close)
    max_close = reduce(lambda x,y: y if y>x else x, close)
    if (max_close / min_close) < 1.2:
        wre.write(stoke_list[code] + '\t' + code +'\n')