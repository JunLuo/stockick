import urllib2

day_1 = 10
month_1 = 11
year_1 = 2014
day_2 = 9
month_2 = 3
year_2 = 2015

url_base = "http://table.finance.yahoo.com/table.csv?a=%d&b=%d&c=%d&d=%d&e=%d&f=%d&s=" % (month_1, day_1, year_1, month_2, day_2, year_2)
stoke_file = open("./stoke_number.txt", "r")
stoke_list = {}
for line in stoke_file:
    if line.find("(") != -1:
        stoke_list[line[line.index("(") + 1:line.index(")")]] = line[0:line.index("(")]
for stoke in stoke_list.keys():
    if stoke[0] == '6':
        url = url_base + stoke + '.ss'
    else:
        url = url_base + stoke + '.sz'
    try:
        print url
        f = urllib2.urlopen(url)        
        open("./%s.csv" % stoke, "w").write(f.read())
    except Exception as e:
        print e
        print stoke + "fail"


#f = urllib2.urlopen(url)
#open("./test.csv","w").write(f.read())


#stoke_file = open("d:\\test\\stoke\\stoke_number.txt", "r")
#stoke_list = {}
#for line in stoke_file:
#    if line.find("(") != -1:
#        stoke_list[line[line.index("(") + 1:-2]] = line[0:line.index("(")]

#for key in stoke_list.keys():
#    if len(key) < 6 or (key.find("60") == -1 and key.find("00") == -1):
#        print key

