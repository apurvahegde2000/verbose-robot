/**
(This problem is an interactive problem.)

A binary matrix means that all elements are 0 or 1. For each individual row of the matrix, this row is sorted in non-decreasing order.

Given a row-sorted binary matrix binaryMatrix, return leftmost column index(0-indexed) with at least a 1 in it. If such index doesn't exist, return -1.

You can't access the Binary Matrix directly.  You may only access the matrix using a BinaryMatrix interface:

BinaryMatrix.get(x, y) returns the element of the matrix at index (x, y) (0-indexed).
BinaryMatrix.dimensions() returns a list of 2 elements [n, m], which means the matrix is n * m.
Submissions making more than 1000 calls to BinaryMatrix.get will be judged Wrong Answer.  Also, any solutions that attempt to circumvent the judge will result in disqualification.

For custom testing purposes you're given the binary matrix mat as input in the following four examples. You will not have access the binary matrix directly.

 

Example 1:



Input: mat = [[0,0],[1,1]]
Output: 0
Example 2:

Input: mat = [[0,0],[0,1]]
Output: 1
Example 3:



Input: mat = [[0,0],[0,0]]
Output: -1
Example 4:



Input: mat = [[0,0,0,1],[0,0,1,1],[0,1,1,1]]
Output: 1
 

Constraints:

1 <= mat.length, mat[i].length <= 100
mat[i][j] is either 0 or 1.
mat[i] is sorted in a non-decreasing way.

Explanation: 
*Lets start from the top right corner(since we can make only 1000 binaryMatrix.get calls according to the question so we need
an optimal solution).
*Since the rows are sorted if the rightmost element of the row has a 0 then all the elememts have 0's.
*if the rightmost element has a 0 we move down 
*if the rightmost element has a 1 we may find more 1's in that row so we move left to find the leftmost column with 1.
eg:
    0 0----->0 so we move down
    1 1----->1 so we move left
    |
    |
   \ / 
    1------->leftmost column with 1 so the column number is returned
    
/


/**
 * // This is the BinaryMatrix's API interface.
 * // You should not implement it, or speculate about its implementation
 * interface BinaryMatrix {
 *     public int get(int x, int y) {}
 *     public List<Integer> dimensions {}
 * };
 */

class Solution{
    public int leftMostColumnWithOne(BinaryMatrix binaryMatrix) {
        List<Integer> a = binaryMatrix.dimensions();
        //System.out.println(a);
        int i=a.get(0);
        int j=a.get(1);
        int rc=0,cc=j-1,colno=-1;
        while(rc<i && cc>=0)
        {
            int e = binaryMatrix.get(rc,cc);
            if(e==1)
            {
                colno=cc;
                cc--;
            }
            else
                rc++;
        }
        return colno;
    }
}
