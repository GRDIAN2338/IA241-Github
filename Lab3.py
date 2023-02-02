'''

Lab3
List and Set

'''

str_list = ['a','d','e','b','c']
str_list.sort()

print(str_list)

str_list.append('f')
print(str_list)

str_list.remove('d')
print(str_list)

print(str_list[2])

my_list = ('a',' 123', 123, 'b', 'B', 'False', False, 123, None, 
'None')
print(len(my_list))

print(len('This is my third python lab.'.split()))

num_list = [12,32,43,35]
num_list.sort()

print(num_list[0])
print(num_list[-1])

game_board=[ [0,0,0], 
[0,0,0],
[0,0,0]]

game_board[1][1]=1
print(game_board)