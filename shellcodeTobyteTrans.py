#-*- coding:utf-8 -*-

f = open('e:/outputshellcode64','rb')
f.seek(0,0)
i=0
fw = open('e:/outputbyteshellcode64','wb')
while True:
    byte = f.read(1)
    if byte == '':
        break
    else:
        hexstr = "%s" % byte.encode('hex')
        decnum = int(hexstr,16)
    fw.write(r'\x')
    fw.write(hexstr)
    i=i+1
    print hexstr
f.close()
fw.close()
print 'finish'
print i
