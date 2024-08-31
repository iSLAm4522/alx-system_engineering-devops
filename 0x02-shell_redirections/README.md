# Project: 0x02. Shell, I/O Redirections and filters

## Resources

#### Read or watch:

* [Shell, I/O Redirection](https://intranet.alxswe.com/rltoken/fGOQQXRKbvOcd1qLRxHzLQ)
* [Special Characters](https://intranet.alxswe.com/rltoken/c1pz13vke3HPH0S8iALbtw)
## Learning Objectives

### General

* What do the commands <code>head</code>, <code>tail</code>, <code>find</code>, <code>wc</code>, <code>sort</code>, <code>uniq</code>, <code>grep</code>, <code>tr</code> do
* How to redirect standard output to a file
* How to get standard input from a file instead of the keyboard
* How to send the output from one program to the input of another program
* How to combine commands and filters with redirections
## Tasks

| Task | Description |
| ---- | ----------- |
| <code>[0-hello_world](./0-hello_world)</code>| Write a script that prints “Hello, World”, followed by a new line to the standard output.|
| <code>[1-confused_smiley](./1-confused_smiley)</code> | Write a script that displays a confused smiley "(Ôo)'|
| <code>[2-hellofile](./2-hellofile)</code> | Display the content of the /etc/passwd file. |
| <code>[3-twofiles](./3-twofiles)</code> | Display the content of /etc/passwd and /etc/hosts |
| <code>[4-lastlines](./4-lastlines)</code> | Display the last 10 lines of /etc/passwd |
| <code>[5-firstlines](./5-firstlines)</code> | Display the first 10 lines of /etc/passwd |
| <code>[6-third_line](./6-third_line)</code> | Write a script that displays the third line of the file iacta.The file iacta will be in the working directory, You’re not allowed to use sed |
| <code>[7-file](./7-file)</code> | Write a shell script that creates a file named exactly \*\\'"Best School"\'\\*$\?\*\*\*\*\*:) containing the text Best School ending by a new line. |
| <code>[8-cwd_state](./8-cwd_state)</code> | Write a script that writes into the file ls_cwd_content the result of the command ls -la. If the file ls_cwd_content already exists, it should be overwritten. If the file ls_cwd_content does not exist, create it. |
| <code>[9-duplicate_last_line](./9-duplicate_last_line)</code> | Write a script that duplicates the last line of the file iacta The file iacta will be in the working directory. |
| <code>[10-no_more_js](./10-no_more_js)</code> | Write a script that deletes all the regular files (not the directories) with a .js extension that are present in the current directory and all its subfolders. |
| <code>[11-directories](./11-directories)</code> | Write a script that counts the number of directories and sub-directories in the current directory. The current and parent directories should not be taken into account Hidden directories should be counted |
| <code>[12-newest_files](./12-newest_files)</code> | Create a script that displays the 10 newest files in the current directory. |
| <code>[13-unique](./13-unique)</code> | Create a script that takes a list of words as input and prints only words that appear exactly once.Input format: One line, one word Output format: One line, one word Words should be sorted. |
| <code>[14-findthatword](./14-findthatword)</code> | Display lines containing the pattern “root” from the file /etc/passwd |
| <code>[15-countthatword](./15-countthatword)</code> | Display the number of lines that contain the pattern “bin” in the file /etc/passwd |
| <code>[16-whatsnext](./16-whatsnext)</code> | Display lines containing the pattern “root” and 3 lines after them in the file /etc/passwd. |
| <code>[17-hidethisword](./17-hidethisword)</code> | Display all the lines in the file /etc/passwd that do not contain the pattern “bin”. |
| <code>[18-letteronly](./18-letteronly)</code> | Display all lines of the file /etc/ssh/sshd_config starting with a letter. |
| <code>[19-AZ](./19-AZ)</code> | Replace all characters A and c from input to Z and e respectively. |
| <code>[20-hiago](./20-hiago)</code> | Create a script that removes all letters c and C from input. |
| <code>[21-reverse](./21-reverse)</code> | Write a script that reverse its input. |
| <code>[22-users_and_homes](./22-users_and_homes)</code> | Write a script that displays all users and their home directories, sorted by users. Based on the the /etc/passwd file |
