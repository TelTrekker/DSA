#kaylangan nasa sort ang binary
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def search(list, target):
  start = 0
  end = len(list) -1

  while start <= end: #start
    mid = (start + end) //2
    print(start, '-',mid, '-', end)
    if list[mid] == target: #mid
      return mid
    elif list[mid] > target: #finish
      end = mid -1
    else: #finish if start is equals to mid
      start = mid +1
  return -1

print(search(number_list, 8))




sorted_list = [8, 13, 24, 36, 42, 55, 67, 89, 100]


def binary_search_while(sorted_list, target):
  pass


result_binary_search = binary_search_while(sorted_list, 42)

print("Binary Search with While Loop:",
      result_binary_search)
