a={0:[2,1,3,1,2],
   1:[1,2,3,5,3,2,5,7,9,1,2,3]
  }
def count_array(array):
    n = ([array[row]<= array[row+1]  for row in range(len(array)-1)]).count(False)
    print(f"input \n {array}")
    count= 0
    while n != 0:
        for row in range(len(array)-1):
            if  array[row] > array[row+1] :
                array[row+1] , array[row] = array[row] , array[row+1]
                count += 1
        n = ([array[row] <= array[row+1]  for row in range(len(array)-1)]).count(False)
    print(f"The inversion numbers was {count}, for the array lenght {len(array)} \n output \n {array}")

#[count_array(a[i]) for i in range(len(a))]

