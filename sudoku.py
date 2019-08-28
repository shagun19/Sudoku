import sys
import copy

A=[
[[0],[1],[2],[0],[0],[8],[4],[0],[0]],
[[0],[0],[0],[2],[9],[7],[0],[0],[0]],
[[7],[0],[0],[0],[0],[0],[0],[0],[0]],
[[0],[0],[7],[0],[0],[6],[0],[0],[1]],
[[4],[3],[0],[0],[2],[0],[0],[9],[5]],
[[8],[0],[0],[3],[0],[0],[7],[0],[0]],
[[0],[0],[0],[0],[0],[0],[0],[0],[3]],
[[0],[0],[0],[5],[7],[4],[0],[0],[0]],
[[0],[0],[5],[8],[0],[0],[6],[7],[0]]
]
def display(arr):
    for x in range(0,9):
        if (x % 3 == 0) and not ( x == 0 ):
            print "-------------------------"
        val=''
        for y in range(0,9):
            if (y % 3 == 0) and not ( y == 0 ) :
                 val = val + " | "
            val = val +' '+ str(arr[x][y])
        print val
    print "\n\n\n"

def getcell(arr,x,y):
    cell=[]
    for l in range(3 * (x / 3), (3 * (x / 3)) + 3):
        for m in range(3 * (y / 3), (3 * (y / 3)) + 3):
            cell.append(arr[l][m])
    return cell

def del_row_Junk(arr,x,y):
    if len(arr[x][y]) > 1:
        for elem in [item for item in arr[x] if item != arr[x][y]]:
            if len(elem) == 1 and (elem[0] in arr[x][y]) and not (elem == [0]) :
                print "del_row_list"
                arr[x][y].remove(elem[0])
                if arr[x][y] == [] :
                    #display(arr)
                    return -1
def del_col_Junk(arr,x,y):
    if len(arr[x][y]) > 1:
        for elem in [arr[l][y] for l in range(0,9) if arr[l][y] != arr[x][y]]:
            if len(elem) == 1 and (elem[0] in arr[x][y]) and not (elem == [0]):
                print "del_col_list"
                arr[x][y].remove(elem[0])
                if arr[x][y] == [] :
                    #display(arr)
                    return -1

def del_cell_Junk(arr,x,y):
    if len(arr[x][y]) > 1:
        for elem in [item for item in getcell(arr,x,y) if item != arr[x][y]]:
            if len(elem) == 1 and (elem[0] in arr[x][y]) and not (elem == [0]):
                print "del_cell_list"
                arr[x][y].remove(elem[0])
                if arr[x][y] == [] :
                    #display(arr)
                    return -1


def replace_col_list(arr,x,y):
    if len(arr[x][y]) > 1:
        for elem in arr[x][y]:
            ycount = 0
            val=[]
            for l in range(0,9):
                val.append(arr[l][y])
            for alist in val :
                if (len(alist) > 1)  :
                    if elem in alist :
                        ycount = ycount+1
            if ycount==1:
                print "replace_col_list"
                arr[x][y]=[elem]
                return

def replace_cell_list(arr,x,y):
    if len(arr[x][y]) > 1:
        for elem in arr[x][y]:
            zcount = 0
            for alist in getcell(arr,x,y) :
                if (len(alist) > 1)  :
                    if elem in alist :
                        zcount = zcount+1
            if zcount==1:
                print "replace_cell_list"
                arr[x][y]=[elem]
                return
def replace_row_list(arr,x,y):
    if len(arr[x][y]) > 1:
        for elem in arr[x][y] :
            vcount = 0
            for alist in arr[x] :
                if (len(alist) > 1)  :
                    if elem in alist :
                        vcount = vcount+1
            if vcount==1 :
                print "replace_row_list"
                arr[x][y]=[elem]
                return


def scan(arr):
    B = copy.deepcopy(arr)
    count=0
    for x in range(0,9):
        for y in range(0,9):
            if len(arr[x][y]) > 1 :
                display(arr)
                xval = del_row_Junk(arr,x,y)
                if xval == -1 :
                    print 'xval',xval
                    return
                yval = del_col_Junk(arr,x,y)
                if yval == -1 :
                    print 'yval',yval
                    return
                zval = del_cell_Junk(arr,x,y)
                if zval == -1 :
                    print 'zval',zval
                    return
                replace_row_list(arr,x,y)
                replace_col_list(arr,x,y)
                replace_cell_list(arr,x,y)
                if check_dups(arr) == -1 :
                    print "value Dups"
                    return
            else :
                count = count + 1
    if count == 81 :
        print "I am done$"
        display(arr)
        verify(arr)
        sys.exit(0)
    if B == arr :
        print "Going in loop "
        for m in range(0,9):
		for n in range(0,9):
                	if len(arr[m][n]) > 1:
                    		print "trying for ",m,n,arr[m][n]
                    		for elem in arr[m][n]:
                        		arr_bkp=copy.deepcopy(arr)
                        		arr_bkp[m][n] = [elem]
                        		print "setting a[m][n] = ",elem
                        		scan(arr_bkp)
                    			print "Wrong Choice. done with ",m,n,arr[m][n]
                    			return
    	print "calling new turn"
    	scan(arr)



def verify(arr):
    for x in range(0,9):
        val=[]
        for element in arr[x]:
            val.append(element)
        val.sort()
        if val != [[1], [2], [3], [4], [5], [6], [7], [8], [9]]:
            print "xerror",x
            return -1
    for y in range(0,9):
        val=[]
        for x in range(0,9):
            val.append(arr[x][y])
        val.sort()
        if val != [[1], [2], [3], [4], [5], [6], [7], [8], [9]]:
            print "yerror",y
            return -1
    for x in [0,3,6]:
        for y in [0,3,6]:
            val = [item for item in getcell(arr,x,y)]
            val.sort()
            if val != [[1], [2], [3], [4], [5], [6], [7], [8], [9]]:
                print "cerror",x,y
                return -1
    if not arr==B:
        print "value mismatch error"
        return -1

def check_dups(arr):
    for x in range(0,9):
        val=[]
        for elem in arr[x] :
            if len(elem) == 1:
                if elem in val:
                    return -1
                else :
                    val.append(elem)

    for y in range(0,9):
        val =[]
        ylist=[]
        for x in range(0,9):
            ylist.append(arr[x][y])
        for elem in ylist :
            if len(elem) == 1 :
                if elem in val:
                                    return -1
                else:
                                    val.append(elem)

    for x in [0,3,6]:
                for y in [0,3,6]:
            val=[]
                        cell = [item for item in getcell(arr,x,y)]
            for elem in cell :
                if len(elem) == 1:
                    if elem in val:
                        return -1
                    else :
                        val.append(elem)
    return 0


display(A)
for x in range(0,9):
    for y in range(0,9):
        if A[x][y] == [0] :
            for l in range(1,10):
                A[x][y].append(l)
            A[x][y].remove(0)


scan(A)
