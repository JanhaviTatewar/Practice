Last login: Thu Jan 30 21:48:59 on ttys001
ITIN000016-MAC:~ itn.janhavi.tatewar$ pwd
/Users/itn.janhavi.tatewar
ITIN000016-MAC:~ itn.janhavi.tatewar$ ssh -i ~/Downloads/jahnavi-key.pem ubuntu@3.0.89.152
Welcome to Ubuntu 18.04.3 LTS (GNU/Linux 4.15.0-1051-aws x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Fri Jan 31 05:06:47 UTC 2020

  System load:  0.0               Processes:           86
  Usage of /:   20.6% of 7.69GB   Users logged in:     0
  Memory usage: 17%               IP address for eth0: 172.31.11.106
  Swap usage:   0%

 * Overheard at KubeCon: "microk8s.status just blew my mind".

     https://microk8s.io/docs/commands#microk8s.status

85 packages can be updated.
49 updates are security updates.


Last login: Thu Jan 30 17:03:16 2020 from 115.99.113.174
ubuntu@ip-172-31-11-106:~$ cat test.py
import requests

url = 'https://reqres.in/api/users?page=2'
r = requests.get( url)
print(r)
data = r.text
Dict=eval(data)
list1=Dict['data']
#print(list1[1])
for i in range(len(list1)):
    print(list1[i]['first_name']+' '+list1[i]['last_name'])


    
ubuntu@ip-172-31-11-106:~$ cat abcd.txt
cat: abcd.txt: No such file or directory
ubuntu@ip-172-31-11-106:~$ vim abcd.txt
ubuntu@ip-172-31-11-106:~$ cat abcd.txt
hi
i am janhavi
working in grab 
ubuntu@ip-172-31-11-106:~$ pr -x abcd.txt
pr: invalid option -- 'x'
Try 'pr --help' for more information.
ubuntu@ip-172-31-11-106:~$ pr -x abcd.txt
pr: invalid option -- 'x'
Try 'pr --help' for more information.
ubuntu@ip-172-31-11-106:~$  pr --help
Usage: pr [OPTION]... [FILE]...
Paginate or columnate FILE(s) for printing.

With no FILE, or when FILE is -, read standard input.

Mandatory arguments to long options are mandatory for short options too.
  +FIRST_PAGE[:LAST_PAGE], --pages=FIRST_PAGE[:LAST_PAGE]
                    begin [stop] printing with page FIRST_[LAST_]PAGE
  -COLUMN, --columns=COLUMN
                    output COLUMN columns and print columns down,
                    unless -a is used. Balance number of lines in the
                    columns on each page
  -a, --across      print columns across rather than down, used together
                    with -COLUMN
  -c, --show-control-chars
                    use hat notation (^G) and octal backslash notation
  -d, --double-space
                    double space the output
  -D, --date-format=FORMAT
                    use FORMAT for the header date
  -e[CHAR[WIDTH]], --expand-tabs[=CHAR[WIDTH]]
                    expand input CHARs (TABs) to tab WIDTH (8)
  -F, -f, --form-feed
                    use form feeds instead of newlines to separate pages
                    (by a 3-line page header with -F or a 5-line header
                    and trailer without -F)
  -h, --header=HEADER
                    use a centered HEADER instead of filename in page header,
                    -h "" prints a blank line, don't use -h""
  -i[CHAR[WIDTH]], --output-tabs[=CHAR[WIDTH]]
                    replace spaces with CHARs (TABs) to tab WIDTH (8)
  -J, --join-lines  merge full lines, turns off -W line truncation, no column
                    alignment, --sep-string[=STRING] sets separators
  -l, --length=PAGE_LENGTH
                    set the page length to PAGE_LENGTH (66) lines
                    (default number of lines of text 56, and with -F 63).
                    implies -t if PAGE_LENGTH <= 10
  -m, --merge       print all files in parallel, one in each column,
                    truncate lines, but join lines of full length with -J
  -n[SEP[DIGITS]], --number-lines[=SEP[DIGITS]]
                    number lines, use DIGITS (5) digits, then SEP (TAB),
                    default counting starts with 1st line of input file
  -N, --first-line-number=NUMBER
                    start counting with NUMBER at 1st line of first
                    page printed (see +FIRST_PAGE)
  -o, --indent=MARGIN
                    offset each line with MARGIN (zero) spaces, do not
                    affect -w or -W, MARGIN will be added to PAGE_WIDTH
  -r, --no-file-warnings
                    omit warning when a file cannot be opened
  -s[CHAR], --separator[=CHAR]
                    separate columns by a single character, default for CHAR
                    is the <TAB> character without -w and 'no char' with -w.
                    -s[CHAR] turns off line truncation of all 3 column
                    options (-COLUMN|-a -COLUMN|-m) except -w is set
  -S[STRING], --sep-string[=STRING]
                    separate columns by STRING,
                    without -S: Default separator <TAB> with -J and <space>
                    otherwise (same as -S" "), no effect on column options
  -t, --omit-header  omit page headers and trailers;
                     implied if PAGE_LENGTH <= 10
  -T, --omit-pagination
                    omit page headers and trailers, eliminate any pagination
                    by form feeds set in input files
  -v, --show-nonprinting
                    use octal backslash notation
  -w, --width=PAGE_WIDTH
                    set page width to PAGE_WIDTH (72) characters for
                    multiple text-column output only, -s[char] turns off (72)
  -W, --page-width=PAGE_WIDTH
                    set page width to PAGE_WIDTH (72) characters always,
                    truncate lines, except -J option is set, no interference
                    with -S or -s
      --help     display this help and exit
      --version  output version information and exit

GNU coreutils online help: <http://www.gnu.org/software/coreutils/>
Report pr translation bugs to <http://translationproject.org/team/>
Full documentation at: <http://www.gnu.org/software/coreutils/pr>
or available locally via: info '(coreutils) pr invocation'
ubuntu@ip-172-31-11-106:~$ pr -x abcd.txt
pr: invalid option -- 'x'
Try 'pr --help' for more information.
ubuntu@ip-172-31-11-106:~$ man pr
ubuntu@ip-172-31-11-106:~$ 
ubuntu@ip-172-31-11-106:~$ vim test.py

import requests
  
url = 'https://reqres.in/api/users?page=2'
r = requests.get( url)
print(r)  
data = r.text 
Dict=eval(data)
list1=Dict['data']
#print(list1[1])
for i in range(len(list1)):
    print(list1[i]['first_name']+' '+list1[i]['last_name'])
      

    
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
"test.py" 14L, 253C                                           11,53         All

