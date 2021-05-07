'''
Problem Challenge 1

Given a binary matrix representing an image, we want to flip the image horizontally, then invert it.
To flip an image horizontally means that each row of the image is reversed. For example,
flipping [0, 1, 1] horizontally results in [1, 1, 0].
To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0.
For example, inverting [1, 1, 0] results in [0, 0, 1].

Example 1:
Input: [
  [1,0,1],
  [1,1,1],
  [0,1,1]
]
Output: [
  [0,1,0],
  [0,0,0],
  [0,0,1]
]
Explanation: First reverse each row: [[1,0,1],[1,1,1],[1,1,0]]. Then, invert the image: [[0,1,0],[0,0,0],[0,0,1]]

Example 2:
Input: [
  [1,1,0,0],
  [1,0,0,1],
  [0,1,1,1], 
  [1,0,1,0]
]
Output: [
  [1,1,0,0],
  [0,1,1,0],
  [0,0,0,1],
  [1,0,1,0]
]
Explanation: First reverse each row: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]].
Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
'''


def flip_an_invert_image(arrays):
    n = len(arrays[0])
    loops = int(n / 2)
    for a in arrays:
        for i in range(loops):
            a[i], a[n-1-i] = a[n-1-i], a[i]
            a[i] ^= 1
            a[n-1-i] ^= 1
            
        if n % 2 == 1:
            a[loops] ^= 1

    return arrays

def main():
    print(flip_an_invert_image([[1,0,1], [1,1,1], [0,1,1]]))
    print(flip_an_invert_image([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]))

main()



'''
Time Complexity 
The time complexity of this solution is O(n) as we iterate through all elements of the input.
Space Complexity 
The space complexity of this solution is O(1).
'''
