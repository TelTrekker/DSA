# - array
# - queue
# - stack

numbers = [1,2,3,4,5,6,7,8,9,10]
fruits = ['apple', 'orange', 'banana']
grades = [1.5, 3, 5, 1, 2.5]
map = [
  [
    [1,2,3,4,'chris']
   ,2
   ,3
   ,4
   ,5
  ],
  [1,2,3,4,5],
  [1,2,3,4,5],
  [1,2,3,4,5],
  [1,2,3,4,5],
]

for i in range(5):
    print('parent iteration: ', map[i])
    for j in range(5):
        print('child iteration: ', map[i][j])
        if isinstance(map[i][j], list):
            for k in range(5):
                print('grandchild iteration: ', map[i][j][k])
                if map[i][j][k] == 'chris':
                    print('file found')
                    break