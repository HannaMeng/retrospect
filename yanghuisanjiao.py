#-*-coding:utf-8 -*-
#@author:HM

def triangle(num):
    triangle = [[1]]
    for i in range(2, num + 1):
        triangle.append([1] * i)
        for j in range(1, i - 1):
            triangle[i - 1][j] = triangle[i - 2][j] + triangle[i - 2][j - 1]
    return triangle


def printtriangle(triangle, width):
    column = len(triangle[-1]) * width
    for sublist in triangle:
        result = []
        for contents in sublist:
            result.append('{0:^{1}}'.format(str(contents), width))
        print('{0:^{1}}'.format(''.join(result), column))


if __name__ == '__main__':
    num = int(input('num:'))
    triangle = triangle(num)
    width = len(str(triangle[-1][len(triangle[-1]) // 2])) + 3
    printtriangle(triangle, width)