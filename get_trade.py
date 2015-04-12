import os

dir_name = "./stoke/"
file_list = os.listdir(dir_name)

trade = {}
for file_name in file_list:
    code = file_name[:-4]
    f = open(dir_name+file_name, 'r')
    logs = [line.split(',') for line in f.read().split("\n")[1:-1]]
    f.close()
    close = [float(log[-1]) for log in logs]
    mins = reduce(lambda x,y : x if x<y else y, close)
    maxs = reduce(lambda x,y : y if x<y else x, close)
    (min_index, max_index) = (close.index(mins), close.index(maxs))
    if min_index < max_index:
        continue
    sub_mins = maxs
    for i in xrange(max_index, min_index):
        if close[i] <= sub_mins:
            sub_mins = close[i]
        else:
            break
    trade_list = [close[i] for i in range(0, min_index+1)[::-1]]
    sub_mins_index = trade_list.index(sub_mins)
    slope_min = (sub_mins - mins) / (sub_mins_index if sub_mins_index > 0 else 1)
    slope_now = (trade_list[-1] - mins) / len(trade_list)
    weight = slope_now - slope_min
    if weight > 0:        
        for i in xrange(1,len(trade_list)):
            if ((trade_list[i] - mins) / i) - slope_min < 0:
                weight *= 0.9
    trade[code] = weight * 100

stoke_file = open("./stoke_number.txt", "r")
stoke_list = {}
for line in stoke_file:
    if line.find("(") != -1:
        stoke_list[line[line.index("(") + 1:line.index(")")]] = line[0:line.index("(")]
trade = sorted(trade.iteritems(), key=lambda d:d[1], reverse=True)
trade = [stoke_list[x[0]] + "\t" + x[0] + "\t" + str(x[1]) for x in trade]
w = open("./trend_result.txt","w").write("\n".join(trade))

