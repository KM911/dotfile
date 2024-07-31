package tools

import (
	"fmt"
	"os"
)

func Args() {
	for i := range os.Args {
		fmt.Println(i, os.Args[i])
	}
	// auto gen the main function
}
