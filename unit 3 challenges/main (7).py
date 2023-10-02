def linear_search_product(arr,target):
  for i in range(len(arr)):
    if arr[i] == target:
       return i
#example usage
products = ['apple','banana','orange','mango','pear']
search_product = 'orange'
result = linear_search_product(products,search_product)
if result != -1:
  print(f"{search_product} found at index {result}")
else:
  print(f"{search_product} not found in the list")