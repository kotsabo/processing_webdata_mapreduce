# Processing Web data - Relational Join using MAPREDUCE

# Tasks

## 1.1 Processing Web data

### Task 1
Take file webLarge.txt, and produce a version which is all lower-case. For example, the sentence "John
loves Mary." would become "john loves mary." Call this the lower-case version.

### Task 2
Using MAPREDUCE write a program that will filter the lower-case version (from task 1) such that only lines
that appear exactly once will be in the output. Call this the unique-only version. For example, for the file:

bob had a little lamb and a small cat

alice had one tiger

bob had a little lamb and a small cat

mary had some small dogs and a rabbit

mary had some small dogs and a rabbit

bob had a little lamb and a small cat

the output should be:

alice had one tiger

because alice had one tiger is the only line that appeared exactly once in the input.

### Task 3
In the unique-only version, compute the maximum length of a line in bytes and the maximum length of a
line in tokens. We define a token the same way Python’s split() function does: anything separated by
runs of whitespace (space ' ', tab '\t', carriage return '\r', new line '\n', or form feed '\f'). The length
of a line does not include the newline character. The output should be a single file on HDFS. For example, the following file example.txt:

bob had a little lamb and a small cat and a tiny fish

alice had one kangaroo, three small dogs, and a rabbit

mary had an inanimate kazoo

should have the following result (54 bytes in the middle line and 13 tokens in the first line): 54 13

### Task 4
On the unique-only version, find all four-token sequences and their counts. For example, the three sentences:

mary had a little lamb

bob had a little lamb

mary had a little tiger

have the following four-token sequences and counts:

Sequence            Count

mary had a little   2

had a little lamb   2

bob had a little    1

had a little tiger  1

The output should have a space-separated four-token sequence, one tab, and a count on each line.

### Task 5
For this task, we use the output that we obtained above in Task 4. What are the top twenty-five
most frequent four-token sequences? Produce a single output file. Each line in the output should contain a
count of a four-token sequence followed by a space followed by the actual four-token sequence. The output
should be sorted in decreasing frequency order (i.e. the most frequent four-token sequence should be first).

### Task 6
Using the four-token sequence counts you found in task 4, find the entropy of tokens for each three-token
context.

For example, consider the following four-token sequences with their respective counts:

Sequence                Count

big green apple pie     7

big green apple donut   4

big green apple candy   3

small red apple pie     1

small red apple tree    2

tiny grey mouse ears    5

There are three contexts: 

big green apple, 

small red apple and 

tiny grey mouse. 

The context big green apple can be followed by pie, donut or candy. The context small red apple can be followed by tree or pie and the context tiny grey mouse can be only followed by ears. The probability of a token depends on the context. For example,
the probability of pie in the context big green apple is:

p(pie | big green apple) = 7 / (7 + 4 + 3) = 1 / 2

whilst in the context of small red apple it is:

p(pie | small red apple) = 1 / (1 + 2) = 1 / 3

The entropy of tokens for the context big green apple would be:

H(big green apple) = - (1 / 2) * log2(1 / 2) - (2 / 7) * log2(2/7) - (3/14) * log2(3/14)

Finally, the output for the given example counts would be:

big green apple 1.4926

small red apple 0.9183

tiny grey mouse 0

## 1.2 Relational Join using MAPREDUCE
In this task we will perform a join operation in Hadoop. Let us assume that we have the relations student(studentId, name) and marks(studentId, courseId, mark) as shown below:

students

studentId   name

1           George

2           Anna

marks

studentId courseId mark

1           EXC     70

2           EXC     65

1           TTS     70

1           ADBS    80

and need to join them on the studentId field. Traditionally, this is an easy task when we deal with relational
databases and can be performed by using the relational join operator. However, the way this join operation
is performed drastically changes, when we assume our input is into a single file that stores information
from both relations.

Assume the format of such a single input file storing data from two relations is as follows:

student 1 George

mark 1 EXC 70

student 2 Anna

mark 1 ADBS 80

mark 2 EXC 65

mark 1 TTS 80

The first column is a tag that shows from which relation the data comes from. Depending on this tag,
we can assign meaning to the other columns. When the tag used is mark, we know that the second column
refers to the studentId, the third to the courseId and the fourth refers to the grade the student took in this
specific course. On the other hand, if the tag is student, we know that there are only two other columns,
one with the studentId and one with the student name.

### Task 7
Use the uniLarge.txt file perform a join operation on the studentId key and produce an output that will
have the grades of each student as follows:

studentID --> (mark1, course1) (mark2, course2) (mark3, course3) . . .

For example, for the previous input file your algorithm should return:

1 --> (80, ADBS) (70, EXC) (80, TTS)

2 --> (65, EXC) (3 marks)

### Task 8
What is the studentID (or students in case of equality) with the lowest average when the number of lessons
examined is greater than three? What is the average score for that student?