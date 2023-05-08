def solution(mat):
    length = len(mat)
    new_list=[]
    i = 0
    j = length-1
    while i < length:
        if length % 2 != 1:
            new_list.append(mat[i][i])
            new_list.append(mat[i][j])
        else:
            if i != j:
                new_list.append(mat[i][i])
                new_list.append(mat[i][j])
            else:
                new_list.append(mat[i][i])
            
        j-=1
        i+=1
    
    return print(sum(new_list))

    
# mat = [[1,2,3],[4,5,6],[7,8,9]]

# mat =  [[10,11,12,1],
#         [9,5,13,22],
#         [6,4,21,42],
#         [4,3,7,2]]
mat = [[1,2,3,4,5,6,7],
       [8,9,10,11,12,13,14],
       [15,16,17,18,19,20,21],
       [22,23,24,25,26,27,28],
       [29,30,31,32,33,34,35],
       [36,37,38,39,40,41,42],
       [43,44,45,46,47,48,49]]
solution(mat)