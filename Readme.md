# ccwc

A simplified version of one of the most valuabe Unix command line tools `wc` written in Python.

`ccwc` just like the original `wc` is a command line tool that allows you to count the number of lines, words, bytes, and characters in the file specified by the `File` parameter.

## Install
Create a conda environment

`conda create -n wc-tool python=3.10`

Activate the conda environment

`conda activate wc-tool`

If you don't have poetry installed on your system
`pip install poetry`

And then install the package

`poetry install`

## Usage

`ccwc [OPTION] [FILE]`

If `OPTION` is not specified, it prints the line, word, and byte count in this same order of the file specified by the `FILE` parameter.

### Example usage
`ccwc test.txt` 

`ccwc` supports the following `Flags` as of this time:

|    Flag     |        Description         |      
| ----------- |:--------------------------:|
|    -c       | print the byte count       |
|    -m       | print the character count  |
|    -w       | print the word count       |
|    -l       | print the newline count    |
|   --help    | display help info and exit |

### Example usage

`ccwc -c test.txt`

The above command prints the number of bytes in `test.txt`



## License

Copyright (c) 2023 [Himanshu Barak](https://github.com/HimanshuBarak)

Licensed under [MIT License](./LICENSE)
