def find_magic_index_simple(arr):
  for i in range(len(arr)):
      if arr[i] == i:
          return i
  return -1  
# Ejemplo de uso:
arr = [-1, 0, 2, 4, 5]
print(find_magic_index_simple(arr))

