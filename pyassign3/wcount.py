import sys
from urllib.request import urlopen

def d(a):
    b=[i for i in a]
    for i in range(0,len(b)-1):
        if 65>ord(b[i]) or ord(b[i])>122 or 97>ord(b[i])>90 or b[i]==',':
            del b[i]
    return ''.join(b)
        
def wcount(lines, topn=10):
    m=lines.split()
    for i in m:
        i=d(i)
    n={}
    for i in m:
        if i in n:
            n[i]=n[i]+1
        else:
            n[i]=1
    c=list((i,n[i]) for i in n)
    d=sorted(c,key=lambda x:x[1],reverse=True)
    e=d[:topn-1]
    print(e)

if __name__ == '__main__':

    if  len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)

    try:
        topn = 10
        if len(sys.argv) == 3:
            topn = int(sys.argv[2])
    except ValueError:
        print('{} is not a valid topn int number'.format(sys.argv[2]))
        sys.exit(1)

    try:
        with urlopen(sys.argv[1]) as f:
            contents = f.read()
            lines   = contents.decode()
            wcount(lines, topn)
    except Exception as err:
        print(err)
        sys.exit(1)