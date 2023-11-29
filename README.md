# Arachnida

The Cybersecurity Piscine project is centered around web data manipulation and metadata analysis. This entails crafting two distinct programs.

## Spider (Golang)

This program is designed to extract images from a provided URL in a recursive manner. It allows for options like specifying depth levels for recursive downloads and defining the download path. Supported file extensions for download include .jpg/jpeg, .png, .gif, and .bmp

### Deployment

```bash
go build spyder.go
```

```bash
Usage of ./spyder:
  -l int
    	max depth level of recursive downloads (default 5)
  -p string
    	the path where the downloaded files will be saved (default "./data/")
  -r	download images recursively
./spider [-rlp] URL
```

#### Example

```bash
./spyder -r "https://www.geeksforgeeks.org/c-programming-language/"
```

after that you will find the images scrapped and placed in data directory inside your program folder.

```bash
./spyder -r -l 2 "https://www.geeksforgeeks.org/c-programming-language/"
```

i set the program to max the scraping to 2 images.

```bash
./spyder -r -l 2 -p "/Desktop/data/" "https://www.geeksforgeeks.org/c-programming-language/"
```

The download location will be '/Desktop/data/'

## Scorpion (Pyhton)

The Scorpion program parses the extracted images from Spider, focusing on fetching metadata, especially EXIF data. It displays fundamental attributes such as creation dates and other pertinent EXIF details.

### Deployment

```bash
pyhton3 scorpion.py
