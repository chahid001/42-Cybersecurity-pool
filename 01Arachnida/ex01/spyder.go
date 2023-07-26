package main

import (
	"fmt"
	"os"
	"github.com/gocolly/colly"
	"flag"
	"strings"
	"net/http"
	"io"
	"path"
)

func printUsage() {
	fmt.Println("./spider [-rlp] URL")
	os.Exit(1)
}

func checkNum(nb int) bool {
	if (nb < 1) {
		return false
	}
	return true
}

func checkPath(location string) string {
	if (strings.HasSuffix(location, "/")) {
		filename := location
		return filename
	}
	filename := location + "/"
	return filename
}	

func downloadImage(location string, url string, max_depth int) error {
	os.MkdirAll(location, os.ModePerm);
	
	if (i == max_depth) {
		os.Exit(0)
	}
	res, err := http.Get(url)

	if (err != nil) {
		println("An error kharij 3an saytara")
		os.Exit(1)
	}

	defer res.Body.Close()
	filename := checkPath(location)
	filename = filename + path.Base(url)

	out, err := os.Create(filename)
	if (err != nil) {
		println("An error kharij 3an saytara")
		os.Exit(1)
	}

	defer out.Close()

	_, err = io.Copy(out, res.Body)
	i :+= 1
	println(i)
	return err
}

func checkLink(link string) bool {
	if (strings.HasSuffix(link, "jpg") ||
		strings.HasSuffix(link, "jpeg") ||
		strings.HasSuffix(link, "png") ||
		strings.HasSuffix(link, "gif") ||
		strings.HasSuffix(link, "bmp")) {
			if (strings.HasPrefix(link, "http://") ||
				strings.HasPrefix(link, "https://")) {
					return true
			}
			return false
	} 
	return false
}

func scrapPic(url string, max_depth int, location string) {
	c := colly.NewCollector()

	c.OnHTML("img", func(e *colly.HTMLElement) {
		link := e.Attr("src")
		file := checkLink(link)

		if (file == true) {
			downloadImage(location, link, max_depth)
		}
	})

	c.OnError(func(_ *colly.Response, err error) {
		fmt.Println("Something went wrong:", err)
		os.Exit(1)
	})

	c.Visit(url)
}

func main() {

	recursive := flag.Bool("r", false, "download images recursively")
	max_depth := flag.Int("l", 5, "max depth level of recursive downloads")
	location := flag.String("p", "./data/", "the path where the downloaded files will be saved")

	flag.Parse()
	args := flag.Args()

	if (len(args) < 1 || !*recursive) {
		flag.Usage()
		printUsage()
	}

	url := args[0]
	if (!checkNum(*max_depth)) {
		println("Invalid option: max depth number")
		printUsage()
	}
	scrapPic(url, *max_depth, *location)
}