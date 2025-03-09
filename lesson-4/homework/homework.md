### Question 2
Break: This statement is used to exit a loop immediately. 
When Python encounters a break, it stops the loop entirely and moves on to the next part of the program.
Continue: This statement is used to skip the current iteration of the loop and move directly to the next one. 
It doesn’t stop the loop — it just skips whatever comes after it in the current cycle.

### Question 3
Difference between for loop and while loop in Python
For loop:
A for loop is used to iterate over a sequence (like a list, tuple, string, or range). It runs a fixed number of times — usually determined by the size of the sequence.

Best used when you know how many times the loop should run.
While loop:
A while loop runs as long as a condition is true. It doesn’t rely on sequences — instead, it keeps looping until the condition becomes false.

Best used when you don’t know in advance how many times the loop should run.
Key difference:

For loops are count-controlled — you use them when the number of iterations is predetermined.
While loops are condition-controlled — they run until something specific happens.

### Question 4
A nested for loop is simply a for loop inside another for loop. The outer loop controls how many times the inner loop runs completely, so for each iteration of the outer loop, the inner loop will execute all its iterations.

Here’s a simple explanation in words:

The outer loop starts and picks a value.
The inner loop runs fully for each outer loop iteration.
Once the inner loop finishes, control goes back to the outer loop, moving to the next value.
This repeats until the outer loop is done.
Example scenario:
Imagine you want to print a grid — like rows and columns in a table.

Step-by-step process:

The outer loop represents rows.
The inner loop represents columns.
For each row, the program goes through all the columns.