### Question 1
How many processes are currently running on your system? Use ps and wc, the first line of output of ps is not a process!

1 process
`ps -r | expr $(wc -l) - 1`


### Question 3
Which command would you use in order to create an empty file in the current directory, let's say empty.txt?

`touch empty.txt`


### Question 4
You are in /home/icipe/  suppose this directory is empty. How do you create in only one command the whole path /home/icipe/Work/mini-project/RNA-Seq/?

`mkdir -p /home/icipe/Work/mini-project/RNA-Seq/?`

### Question 5
Suppose your current working directory contains a file named seqs.txt. How do you rename this file into sequences.fasta? 
Does this have any effect on the content of the file, and if yes, what does it do?

`mv seqs.txt sequences.fasta`
This does not affect the contents of the file


### Question 17
Try this with the command "expr 1 / 0", whose purpose is to calculate the integer result of 1 divided by 0. What happens? Why?



### Question 18
How can you separately redirect the standard output and the standard error streams into two separate files?

`command 1> capture.txt 2> error.txt`


### Question 20
Suppose your current working directory is /home/icipe/Linux/Exercises/. What is the command that will enable to move to /home/icipe/Fun_stuff/?

`cd ~/Fun_stuff/`
