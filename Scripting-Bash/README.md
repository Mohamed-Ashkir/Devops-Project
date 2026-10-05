### Challenge 1: Basic Arithmetic Calculator

Create a script that takes two numbers as input and performs basic arithmetic operations (addition, subtraction, multiplication, division).

Requirements:

- Prompt user for two numbers
- Perform all four operations
- Display the results
- Handle division by zero

Example output:

Enter first number: 10 Enter second number: 5

Results: 10 + 5 = 15 10 - 5 = 5 10 × 5 = 50 10 ÷ 5 = 2

!image.png

### Challenge 2: File Operations Script

Create a script that automates directory and file creation.

Requirements:

- Create a directory called bash_demo
- Navigate into the directory
- Create a file called demo.txt
- Write text to the file (include current date)
- Display the file contents

Example output:

Directory 'bash_demo' created. File 'demo.txt' created.

File contents: This file was created by a Bash script on 2024-11-29

!image.png

### Challenge 3: File Checker with Permissions

Create a script that checks if a file exists and displays its permissions.

Requirements:

- Prompt user for a filename
- Check if the file exists
- If it exists, check if it's readable, writable, and executable
- Display appropriate messages for each permission

Example output:

Enter filename to check: /etc/passwd

File '/etc/passwd' exists. ✓ File is readable ✓ File is writable ✗ File is not executable

---

!Screenshot 2026-09-24 at 19.49.18.png

### Challenge 4: Backup Script for Text Files

Create a script that backs up all .txt files from one directory to another.

Requirements:

- Prompt user for source directory
- Create a backup directory if it doesn't exist
- Copy all .txt files to the backup directory
- Add timestamp to backup directory name
- Display count of files backed up

Example output:

Enter source directory: /home/user/documents

Backup directory created: backup_2024-11-29_14-30 Copying .txt files...

Backup complete! Files backed up: 5

!image.png

# **Bash Battle Arena**

## Level 2: Variables and Loops

**Mission**: Create a script that outputs the numbers 1 to 10, one number per line.

!image.png

Solution: For loops
for num in {0..9} tells the script to repeat an action exactly 10 times, ((num++)) this add one to the variable num and it prints number 1 till 10 in a line.

## Level 3: Conditional Statements

**Mission**: Write a script that checks if a file named `hero.txt` exists in the `Arena` directory. If it does, print `Hero found!`; otherwise, print `Hero missing!`.

!image.png

the -f flag is used to look for a file name hero.txt 

## Level 4: File Manipulation

**Mission**: Create a script that copies all `.txt` files from the `Arena` directory to a new directory called `Backup`.

!Screenshot 2026-09-25 at 17.17.10.png

mkdir -p the flag option -p is used create a parent directory with sub directory. Using the -p in a script ensure your script doesn’t crash.

## Level 5: The Boss Battle - Combining Basics

**Mission**: Combine what you've learned! Write a script that:

```
1. Creates a directory names 'Battlefield'
2. Inside Battlefield, create files named knight.txt, sorcerer.txt, and rogue.txt.
3. Check if knight.txt exists; if it does, move it to a new directory called Archive.
4. List the contents of both Battlefield and Archive.
```

!Screenshot 2026-09-25 at 17.46.39.png

Thought process- i created a directory using the -p flag, then instead of creating file one at a time i managed to do it in one line. Putting the directory/filename i was able to tell the computer Go inside the  battlefield folder right next to me, and create a brand new file.  I used IF statement to check if the file knight.txt inside the directory battlefield exist; then move it to another directory i created called archive. This is how my terminal should look like when i run the script:

!image.png

## Level 6: Argument Parsing

**Mission**: Write a script that accepts a filename as an argument and prints the number of lines in that file. If no filename is provided, display a message saying 'No file provided'.

!image.png

Solution- we used if statement to check if the argument is a file and if it is then prints the number of lines in that file. No  argument or no filename it will print no file provided

## Level 7: File Sorting Script

**Mission**: Write a script that sorts all `.txt` files in a directory by their size, from smallest to largest, and displays the sorted list.

!image.png

Solution- This script first listed all the file with the .txt and then used pipe to connect the output from previous command to the next one. sort is used with the flag option -k as i want to specifically sort out the size of the file but that information is in the fifth column.  Sort -k is used to the fifth column and the -n flag sort it in numerical order from smallest to largest.

## Level 8: Multi-File Searcher

**Mission**: Create a script that searches for a specific word or phrase across all `.log` files in a directory and outputs the names of the files that contain the word or phrase.

!image.png

grep -l is used to tell the computer *"Just give me the names of the files that contain this word, and skip showing me the actual lines of text”* 

## **Level 9: Script to Monitor Directory Changes**

**Mission**: Write a script that monitors a directory for any changes (file creation, modification, or deletion) and logs the changes with a timestamp.

!image.png

Solution- inotifywait is a command that is used to monitor **directories and files for real-time changes** directly through the Linux kernel. Using the -m flag to monitor continuously and -e flag stands for event. It tells the command **exactly what kind of actions to listen for**. The **`create`**, **`modify`**, and **`delete`** keywords are **event names** used to filter out noise so you only log a timestamp when a file is added, edited, or removed. The **`--timefmt`** flag defines what your clock looks like, while the **`--format`** flag chooses exactly where to print that clock along with the event details on your screen.

### Test to see if Level 9 script works:

!image.png

### Live Test- Developed a live filesystem event monitor utilizing `inotifywait` to capture real-time creation, modification, and deletion logs. Testing was conducted using parallel terminal sessions; execution was initiated in the primary shell environment while test file payloads were generated and altered in a secondary shell. The primary interface successfully validated the pipeline by capturing and printing all real-time events.

## **Level 10: Boss Battle 2 - Intermediate Scripting**

**Mission**: Write a script that:

```
1. Creates a directory called Arena_Boss.
2. Creates 5 text files inside the directory, named file1.txt to file5.txt.
3. Generates a random number of lines (between 10 and 20) in each file.
4. Sorts these files by their size and displays the list.
5. Checks if any of the files contain the word 'Victory', and if found, moves the file to a directory called Victory_Archive.
```

!image.png

## **Level 11: Automated Disk Space Report**

**Mission**: Create a script that checks the disk space usage of a specified directory and sends an alert if the usage exceeds a given threshold.

!Screenshot 2026-09-28 at 18.41.41.png

## **Level 12: Simple Configuration File Parser**

**Mission**: Write a script that reads a configuration file in the format `KEY=VALUE` and prints each key-value pair.
