def max_num(a, b, c):
    return max([a, b, c])

print(max_num(100, 44, 14))

def mult_list(a, b, c):
    return(a * b * c)

print(mult_list(4, 14, 3))

def rev_string(str):
    return str[::-1]

print(rev_string("pink"))

def num_within(a, b, c):
    return a in range(b, c+1)

print(num_within(14, 7, 8))
print(num_within(4, 7, 14))


triangle = [[1],[1,1]]
def pascal(n):
    if n < 1:
        print("Can not create rows")
    elif n == 1:
        print(triangle[0])
    else:
        row_num = 2
        while len(triangle) < n:
            row = []
            row_prev = triangle[row_num - 1]
            length = len(row_prev)+1
            for i in range(length):
                if i == 0:
                    row.append(1)
                elif i > 0 and i < length-1:
                    row.append(triangle[row_num-1][i-1]+triangle[row_num-1][i])
                else:
                    row.append(1)
                triangle.append(row)
                row_num += 1
            for row in triangle:
                print(row)

pascal(2)
pascal(5)