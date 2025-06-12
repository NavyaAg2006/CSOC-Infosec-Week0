# OverTheWire: Bandit Walkthrough

## Bandit Level 00
To begin the Bandit wargame, connect to the host `bandit.labs.overthewire.org` on port `2220` using SSH. The username and password are both `bandit0`. You can connect using the command:
```
ssh bandit0@bandit.labs.overthewire.org -p 2220
```
Once logged in, you’ll find a file named `readme` in the home directory. To list all files including hidden ones, use:
```
ls -l
```
To read the content of the file and obtain the password for the next level:
```
cat readme
```
**Password:** `ZjLjTmM6FvvyRnrb2rfNWOZOTa6ip5If`

## Bandit Level 01
The file containing the password is named `-` and is located in the home directory. Since `-` usually refers to standard input, you need to specify its path explicitly.
Connect using:
```
ssh bandit1@bandit.labs.overthewire.org -p 2220
```
Then, to read the file:
```
cat ./-
```
**Password:** `263JGJPfgU6LtdEvgfWU1XP5yac29mFx`

## Bandit Level 02
The password is stored in a file with spaces in its name: `spaces in this filename`.
Connect using:
```
ssh bandit2@bandit.labs.overthewire.org -p 2220
```
You can read this file using either of the following commands:
```
cat "spaces in this filename"
```
**Password:** `MNk8KNH3Usiio41PRUEoDFPqfxLPlSmx`

## Bandit Level 03
The password is stored in a hidden file inside the `inhere` directory.
Connect using:
```
ssh bandit3@bandit.labs.overthewire.org -p 2220
```
Navigate to the directory and list all files, including hidden ones:
```
cd inhere
ls -la
```
Read the hidden file:
```
cat .hidden
```
**Password:** `2WmrDFRmJIq3IPxneAaMGhap0pFhF3NJ`

## Bandit Level 04
You need to find the only human-readable file in the `inhere` directory.
Connect using:
```
ssh bandit4@bandit.labs.overthewire.org -p 2220
```
Navigate to the directory:
```
cd inhere
```
Use the `file` command on each file to identify the human-readable file:
```
file ./-file0
```
And so on… Locate the file marked as ASCII text, and read it:
```
cat ./-file07
```
**Password:** `4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQw`

## Bandit Level 05
The password is hidden in a file somewhere inside the `inhere` directory. The file must be human-readable, exactly 1033 bytes in size, and not executable.
Connect using:
```
ssh bandit5@bandit.labs.overthewire.org -p 2220
```
Use the `find` command to search for the file:
```
find ./inhere/ -type f -readable ! -executable -size 1033c
```
Then, read the file identified by the command:
```
cat /home/bandit5/inhere/maybehere07/.file2
```
**Password:** `HWasnPhtq9AVKe0dmk45nxy20cvUa6EG`

## Bandit Level 06
The password is located somewhere on the server. The file is owned by `bandit7`, belongs to the group `bandit6`, and is exactly 33 bytes in size.
Connect using:
```
ssh bandit6@bandit.labs.overthewire.org -p 2220
```
Run a `find` command starting from the root directory, filtering by size, owner, and group. Suppress permission error messages:
```
find / -type f -size 33c -group bandit6 -user bandit7 2>/dev/null
```
Then, read the discovered file:
```
cat /var/lib/dpkg/info/bandit7.password
```
**Password:** `morbNTDkSW6jIlUc0ymOdMaLnOlFVAaj`

## Bandit Level 07
The password for the next level is stored in a file named `data.txt` located in the home directory. It contains many lines, and only one of them contains the word `millionth`.
Connect using:
```
ssh bandit7@bandit.labs.overthewire.org -p 2220
```
To extract the line containing the word `millionth`:
```
grep millionth data.txt
```
**Password:** `dfwvzFQi4mU0wfNbFOe9RoWskMLg7eEc`

## Bandit Level 08
The password is stored in the file `data.txt`, and it is the only line that occurs only once.
Connect using:
```
ssh bandit8@bandit.labs.overthewire.org -p 2220
```
Sort the file and use `uniq` to find the unique line:
```
sort data.txt | uniq -u
```
**Password:** `4CKMh1JI91bUIZZPXDqGanal4xvAg0JM`

## Bandit Level 09
The password is stored in the file `data.txt`, which contains multiple lines. It's in one of the few human-readable strings, preceded by several `=` characters.
Connect using:
```
ssh bandit9@bandit.labs.overthewire.org -p 2220
```
Use `strings` and `grep` to find the line with the different character:
```
strings data.txt | grep "=="
```
**Password:** `FGUW5ilLVJrxX9kMYMmlN4MgbpfMiqey`

## Bandit Level 10
The password is stored in `data.txt`, which contains base64 encoded text.
Connect using:
```
ssh bandit10@bandit.labs.overthewire.org -p 2220
```
To decode the password:
```
base64 -d data.txt
```
**Password:** `dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr`

## Bandit Level 11
The password is stored in `data.txt`, and it has been encoded with ROT13.
Connect using:
```
ssh bandit11@bandit.labs.overthewire.org -p 2220
```
To decode ROT13:
```
cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'
```
**Password:** `7x16WNeHIi5YkIhWsfFIqoognUTyj9Q4`

## Bandit Level 12
The password is stored in a file `data.txt` that was created by compressing a text file multiple times.
Connect using:
```
ssh bandit12@bandit.labs.overthewire.org -p 2220
```
First, create a working directory and copy the file:
```
mktemp -d
cp data.txt /tmp/tmp.vw0ltfgVJp
cd /tmp/tmp.vw0ltfgVJp
mv data.txt a1.txt
```
Now iteratively decompress it

**Password:** `FO5dwFsc0cbaIiH0h8J2eUks2vdTDwAn`

## Bandit Level 13
The password is stored in the `sshkey.private` file.
Connect using:
```
ssh bandit13@bandit.labs.overthewire.org -p 2220
```
Copy the ssh key to local machine:
```bash
# on local machine
scp -P 2220 bandit13@bandit.labs.overthewire.org:sshkey.private .
```
Make sure the key file has correct permissions:
```
chmod 400 sshkey.private
```
Then, log in to the next level using:
```
ssh -i sshkey.private bandit14@bandit.labs.overthewire.org -p 2220
```
