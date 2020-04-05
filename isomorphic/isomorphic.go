/*
Given two strings s and t, determine if they are isomorphic.
Two strings are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters.
 No two characters may map to the same character but a character may map to itself.
*/

package main

import (
	"fmt"
	"strings"
)

func isIsomorphic(s string, t string) bool {

	if len(s) != len(t) {
		return false
	}

	strLen := len(s)
	wordMap := make(map[byte]byte)

	for i := 0; i < strLen; i++ {
		_, ok := wordMap[t[i]]

		if !ok {
			if !strings.Contains(s[0:i], string(s[i])) {
				wordMap[t[i]] = s[i]
			} else {
				return false
			}

		} else {
			if s[i] != wordMap[t[i]] {
				return false
			}
		}
	}

	return true
}

func main() {
	fmt.Println(isIsomorphic("test", "abcd"))       // false
	fmt.Println(isIsomorphic("title", "paper"))     // true
	fmt.Println(isIsomorphic("title", "zaper"))     // false
	fmt.Println(isIsomorphic("add", "egg"))         // true
	fmt.Println(isIsomorphic("qazqazz", "rtyrtyy")) // true
}
