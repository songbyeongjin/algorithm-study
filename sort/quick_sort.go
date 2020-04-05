package main

import "fmt"

func main() {
	arr := []int{10, 30, 27, 5, 60, 4, 1, 90, 60, 3}

	sortedArr := QuickSort(arr)

	fmt.Println(sortedArr)
}

func QuickSort(arr []int) []int {
	if len(arr) <= 1 {
		return arr
	}

	pivot := len(arr) - 1
	i := 0
	j := pivot - 1

	for i <= j {
		if arr[i] < arr[pivot] {
			i++
		} else {
			if arr[j] >= arr[pivot] {
				j--
			} else {
				arr[i], arr[j] = arr[j], arr[i]
				i++
				j--
			}
		}
	}
	arr[pivot], arr[i] = arr[i], arr[pivot]
	QuickSort(arr[:i])
	QuickSort(arr[i+1:])

	return arr
}
