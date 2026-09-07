# CSES Practice Problems

Optional preparation for the seven-week ICPC Training Program, with 10 CSES problems and a self-assessment guide.

This is independent practice, not a graded assignment or formal competition. You do not need to report your progress. Try as many problems as you can, using your preferred programming language. Starting with pseudocode is encouraged.

**Attempt the problems before opening the self-assessment table or reference code.** The problems are listed in the same order as the PDF, rather than in training-week order.

## Preparation guide

[Download or view ICPC_Self_Assessment.pdf](ICPC_Self_Assessment.pdf)

- Page 1: practice problems, account registration, and source-code submission instructions.
- Page 2: a reminder to attempt the problems first.
- Page 3: self-assessment ratings and the primary training week and topics for each problem.

## Practice problems

| # | Problem |
| --- | --- |
| 1 | [Counting Rooms](https://cses.fi/problemset/task/1192/) |
| 2 | [Factory Machines](https://cses.fi/problemset/task/1620/) |
| 3 | [Book Shop](https://cses.fi/problemset/task/1158/) |
| 4 | [Static Range Sum Queries](https://cses.fi/problemset/task/1646/) |
| 5 | [Course Schedule](https://cses.fi/problemset/task/1679/) |
| 6 | [Message Route](https://cses.fi/problemset/task/1667/) |
| 7 | [Counting Divisors](https://cses.fi/problemset/task/1713/) |
| 8 | [Shortest Routes I](https://cses.fi/problemset/task/1671/) |
| 9 | [Distinct Values Subarrays II](https://cses.fi/problemset/task/2428/) |
| 10 | [Road Reparation](https://cses.fi/problemset/task/1675/) |

## Getting started

1. [Create a CSES account](https://cses.fi/register/) if needed, and log in.
2. Open a problem and write a complete program that reads standard input and writes standard output.
3. Save it as a source-code file, such as `.py`, `.cpp`, or `.java`.
4. On the CSES problem page, choose the matching language, upload your file, and submit. Review the result and revise as needed.

For a local Python run, open a terminal in this folder and use, for example:

```sh
python "solutions/Counting Rooms.py"
```

Then enter the problem's input. You can also run the file in your editor with a configured Python interpreter.

## Reference code and explanations

All Python solution files are in the [solutions/](solutions/) folder.

Reference Python code and [approach explanations](SOLUTION_NOTES.md) are currently available for **Counting Rooms** and **Distinct Values Subarrays II**. The other eight Python files are empty placeholders, not completed solutions. The existing programs have not been verified as Accepted on CSES as part of this repository setup.

Use these resources after making your own attempt so that the self-assessment reflects your independent preparation.

<details>
<summary>After attempting the problems: open the reference code</summary>

- [Counting Rooms.py](solutions/Counting%20Rooms.py)
- [Distinct Values Subarrays II.py](solutions/Distinct%20Values%20Subarrays%20II.py)
- [Solution notes](SOLUTION_NOTES.md)

</details>

<details>
<summary>After attempting the problems: open the self-assessment guide</summary>

Choose a rating for each problem:

- **A - Independent:** I identified the approach and completed the solution independently.
- **B - Partial:** I identified the general approach or wrote pseudocode, but could not complete the implementation.
- **C - Guided:** I recognized the approach only after reviewing the week and topic information below.
- **D - Unfamiliar:** I am still unsure how to approach the problem or the related algorithm is unfamiliar to me.

| # | Problem | Primary week | Related topics |
| --- | --- | --- | --- |
| 1 | Counting Rooms | Week 3 | Grid graphs; DFS/BFS; connected components |
| 2 | Factory Machines | Week 2 | Binary search; constraint analysis |
| 3 | Book Shop | Week 6 | Dynamic programming; 0/1 knapsack |
| 4 | Static Range Sum Queries | Week 1 | Constraints; time complexity; prefix sums |
| 5 | Course Schedule | Week 5 | Directed graphs; DAGs; indegrees; topological sorting |
| 6 | Message Route | Week 4 | BFS; unweighted shortest paths; path reconstruction |
| 7 | Counting Divisors | Week 5 | Prime factorization; divisibility; counting divisors |
| 8 | Shortest Routes I | Week 4 | Weighted graphs; priority queues; Dijkstra's algorithm |
| 9 | Distinct Values Subarrays II | Week 2 | Hash maps; frequency counting; two pointers; sliding windows |
| 10 | Road Reparation | Week 5 | Sorting; greedy; DSU; Kruskal; minimum spanning trees |

A rating reflects preparation in only part of a week's material. Solving a problem does not demonstrate mastery of every topic or suggest that you should skip the session. Everyone is encouraged to attend the full program. Week 7 emphasizes algorithm recognition and competition strategy across the full set.

</details>

## Sources

Problem links and the training-week mapping come from the accompanying preparation PDF. Problem statements and judging are hosted by [CSES](https://cses.fi/problemset/).
