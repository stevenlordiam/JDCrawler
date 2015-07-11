# JDCrawler

A simple Python web crawler, fetching pictures from http://jandan.net/ooxx

The status bar indicator is from the open source project code from [process](https://github.com/verigak/progress/)

###Usage
___________

Python jdcrawler.py `startpage` `endpage`

The program will save all the picture by page in different folder under `./image` folder

**Note:**
The website has deleted the pages before 900 to save server according to their statement, so you have to assign a start page after 900
(inclusive).

###Todo
___________

Recently this program can only save 10 pages, after 10 pages it will be forbidden by the server. I will add a function to change the location after 10 pages. Or save the files to my server instead of computer.


###License
___________

The MIT License (MIT)

Copyright (c) 2015 Steven Liu

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
