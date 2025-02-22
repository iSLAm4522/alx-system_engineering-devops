# Project: 0x03. Shell, init files, variables and expansions

## Resources

#### Read or watch:

* [Expansions](https://intranet.alxswe.com/rltoken/oXnzBjLBA9t9dr7WuftdmQ)
* [Shell Arithmetic](https://intranet.alxswe.com/rltoken/PLSUQnBcKKU5eEgRfRDlug)
* [Variables](https://intranet.alxswe.com/rltoken/SvdGNZJjKsPghzZEhaWu4Q)
* [Shell initialization files](https://intranet.alxswe.com/rltoken/tqud57kjsSYgDfeZDlwl3g)
* [The alias Command](https://intranet.alxswe.com/rltoken/1Z3nYPjmidqQJXcWQ9Fkug)
* [Technical Writing](https://intranet.alxswe.com/rltoken/wYrZr3t3DeAE8PpYHYWGiw)
## Learning Objectives

### General

* What happens when you type <code>$ ls -l *.txt</code>
## Tasks

| Task | File |
| ---- | ---- |
|<code>[0-alias](./0-alias)</code>|Create a script that creates an alias. Name: ls , Value: rm *|
|<code>[1-hello_you](./1-hello_you)</code>|Create a script that prints hello user, where user is the current Linux user.|
|<code>[2-path](./2-path)</code>|Add /action to the PATH. /action should be the last directory the shell looks into when looking for a program.|
|<code>[3-paths](./3-paths)</code>|Create a script that counts the number of directories in the PATH. |
|<code>[4-global_variables](./4-global_variables)</code>|Create a script that lists environment variables.|
|<code>[5-local_variables](./5-local_variables)</code>|Create a script that lists all local variables and environment variables, and functions.|
|<code>[6-create_local_variable](./6-create_local_variable)</code>|Create a script that creates a new local variable. Name: BEST, Value: School.|
|<code>[7-create_global_variable](./7-create_global_variable)</code>|Create a script that creates a new global variable. Name: BEST, Value: School.|
|<code>[8-true_knowledge](./8-true_knowledge)</code>|Write a script that prints the result of the addition of 128 with the value stored in the environment variable TRUEKNOWLEDGE, followed by a new line.|
|<code>[9-divide_and_rule](./9-divide_and_rule)</code>| Write a script that prints the result of POWER divided by DIVIDE, followed by a new line.POWER and DIVIDE are environment variables|
|<code>[10-love_exponent_breath](./10-love_exponent_breath)</code>|Write a script that displays the result of BREATH to the power LOVE. BREATH and LOVE are environment variables The script should display the result, followed by a new line. |
|<code>[11-binary_to_decimal](./11-binary_to_decimal)</code>| Write a script that converts a number from base 2 to base 10. The number in base 2 is stored in the environment variable BINARY The script should display the number in base 10, followed by a new line. |
|<code>[12-combinations](./12-combinations)</code>|Create a script that prints all possible combinations of two letters, except oo .Letters are lower cases, from a to z.one combination per line The output should be alpha ordered, starting with aa Do not print oo Your script file should contain maximum 64 characters |
|<code>[13-print_float](./13-print_float)</code>|Write a script that prints a number with two decimal places, followed by a new line. The number will be stored in the environment variable NUM.|
|<code>[100-decimal_to_hexadecimal](./100-decimal_to_hexadecimal)</code>|Write a script that converts a number from base 10 to base 16. The number in base 10 is stored in the environment variable DECIMAL The script should display the number in base 16, followed by a new line |
|<code>[101-rot13](./101-rot13)</code>|Write a script that encodes and decodes text using the rot13 encryption. Assume ASCII.|
|<code>[102-odd](./102-odd)</code>|Write a script that prints every other line from the input, starting with the first line.|
|<code>[103-water_and_stir](./103-water_and_stir)</code>| Write a shell script that adds the two numbers stored in the environment variables WATER and STIR and prints the result WATER is in base water STIR is in base stir.The result should be in base bestchol |