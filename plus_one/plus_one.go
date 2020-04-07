/*

Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list,and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.

*/

package main

import (
	"fmt"
)

func plusOne(digits []int) []int {
	digitsLen := len(digits)

	for index := 0; index < digitsLen; index++ {
		digit := digits[digitsLen-index-1]

		if digit != 9 {
			digits[digitsLen-index-1] += 1
			break
		} else {
			digits[digitsLen-index-1] = 0

			if digitsLen == (index + 1) {
				digits = append([]int{1}, digits...)
				break
			}

			if digits[digitsLen-index-2] != 9 {
				digits[digitsLen-index-2] += 1
				break
			}
		}
	}

	return digits
}

func main() {
	fmt.Println(plusOne([]int{1, 2, 3}))          // 1234
	fmt.Println(plusOne([]int{1, 2, 2, 3}))       // 1224
	fmt.Println(plusOne([]int{5, 2, 3, 1, 1}))    // 52312
	fmt.Println(plusOne([]int{9, 9, 9}))          // 1000
	fmt.Println(plusOne([]int{9, 6, 9, 9}))       // 9700
	fmt.Println(plusOne([]int{1, 0, 0, 2, 0, 9})) // 100210
}
