'''
Created on 24 Jan 2016

@author: chris
'''

def main():
    
    txt = 'banana'
    
    naiveSuffixArray = buildSuffixArray(txt)
    
    print "Naive suffix array construction, O(N**2logN)"
    for i in naiveSuffixArray:
        print i
    
    
    


# Naive version

def buildSuffixArray(txt):
    
    def substring(i):
        return txt[i:]
    
    indexArray = range(len(txt))
    
    suffixArray = sorted(indexArray,key=substring)
    
    return suffixArray
        

if __name__ == '__main__':
    main()