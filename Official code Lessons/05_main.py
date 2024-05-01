unsorted_list = [17,8,4,5,22]

def bubble_sort(list):
  length = len(list)
  
  for row in range(length):
    for col in range(length - row - 1):
      print('Original list: ', list)
      print('Row: ', row)
      print('Col: ', col)
      print('Col Value: ', list[col])
      print('Col + 1 Value: ', list[col + 1])

      # list[col] <<< value of left
      # list[col + 1] <<< value of right
      if list[col] > list[col + 1]:
        print('Swap happened')
        jar = list[col]
        list[col] = list[col + 1]
        list[col + 1] = jar

      print('After list: ', list)
      print('\n')

  return list

print('Sorted list: ', bubble_sort(unsorted_list))