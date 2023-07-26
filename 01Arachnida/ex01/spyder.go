package main

import "fmt"
// import "github.com/gocolly/colly"
import "os"

type codeReturn struct {
	code int
	url string
	n string
	location string
}

func printUsage() {
	fmt.Println("./spider [-rlp] URL")
	os.Exit(1)
}

func checkOptions(argc int, argv[] string) codeReturn {
	var ret codeReturn;
	if (argc == 3) { //case -r url
		if (argv[1] == "-r") { 
			ret.code = 1
			ret.url = argv[2]
			return ret
		}
	} else if (argc == 5) { 
		if (argv[1] == "-r" && argv[2] == "-l") { //case -r -l N url
			ret.code = 2
			ret.n = argv[3]
			ret.url = argv[4]
			return ret
		} else if (argv[1] == "-r" && argv[2] == "-p") { //case -r -p location url
			ret.code = 3
			ret.location = argv[3]
			ret.url = argv[4]
			return ret
		}
	} else if (argc == 7) {
		if (argv[1] == "-r" && argv[2] == "-l" && argv[4] == "-p") { //case -r -l N -p location url
			ret.code = 4
			ret.n = argv[3]
			ret.location = argv[5]
			ret.url = argv[6]
			return ret
		} else if (argv[1] == "-r" && argv[2] == "-p" && argv[4] == "-l") { //case -r -p location -l N url
			ret.code = 4
			ret.location = argv[3]
			ret.n = argv[5]
			ret.url = argv[6]
			return ret
		}
	}
	printUsage()
	return ret
}

func main() {

	var ret codeReturn;
	if (len(os.Args) < 3){
		printUsage()
	}
	ret = checkOptions(len(os.Args), os.Args)
	print(ret.code)
	// c := colly.NewCollector()

	// // Find and visit all links
	// c.OnHTML("img", func(e *colly.HTMLElement) {
	// 	e.Request.Visit(e.Attr("src"))
	// })

	// c.OnRequest(func(r *colly.Request) {
	// 	fmt.Println(r.URL)
	// })

	// c.Visit("http://go-colly.org/")
}