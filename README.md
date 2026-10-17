# Data Structures and Algorithms in Python

A structured, continuously updated collection of **Data Structures and
Algorithms (DSA)** concepts, Python implementations, and problem-solving
practice.

The goal of this repository is to understand how algorithms work, learn
when to use them, analyze their efficiency, and write clear, correct
Python code.

> **Status:** Work in progress. Add a topic to the "Completed" list only
> after you have studied and implemented it.

------------------------------------------------------------------------

## Table of Contents

1.  [Repository Goals](#repository-goals)
2.  [Folder Structure](#folder-structure)
3.  [Topics and Concepts](#topics-and-concepts)
4.  [Complexity Analysis](#complexity-analysis)
5.  [Recommended Format for
    Solutions](#recommended-format-for-solutions)
6.  [How to Run the Code](#how-to-run-the-code)
7.  [Learning Roadmap](#learning-roadmap)
8.  [Progress Tracker](#progress-tracker)

------------------------------------------------------------------------

## Repository Goals

-   Build strong foundations in problem-solving with Python.
-   Understand the logic behind common data structures and algorithms.
-   Learn to choose an appropriate approach for a given problem.
-   Analyze time and space complexity.
-   Practice edge cases, testing, and clean code.
-   Keep solutions organized by topic for revision and interview
    preparation.

## Folder Structure

``` text
DSA_PYTHON/
├── README.md
├── 01_Basics/
├── 02_Arrays_and_Lists/
├── 03_Sorting_Algorithms/
├── 04_Strings/
├── 05_Linked_Lists/
├── 06_Stacks_and_Queues/
├── 07_Binary_Trees/
├── 08_Heaps/
└── 10_Sliding_Window_and_Two_Pointers/
```

The numbering is for navigation and learning order. The missing number
`09` is intentional for now; you can use it for a future topic such as
hashing, or renumber folders later if you prefer.

------------------------------------------------------------------------

# Topics and Concepts

## 01 --- Basics

**Purpose:** Build the Python and algorithmic foundations needed to
solve DSA problems.

-   **Variables and data types:** Store values using names. Common types
    include `int`, `float`, `str`, `bool`, and `None`.
-   **Operators:** Perform arithmetic, comparisons, logical operations,
    assignment, and bitwise operations.
-   **Input and output:** Read input and display results using `input()`
    and `print()`.
-   **Conditionals:** Use `if`, `elif`, and `else` to choose which
    instructions execute.
-   **Loops:** Use `for` and `while` to repeat operations.
-   **Functions:** Package reusable logic, accept parameters, and return
    results.
-   **Scope:** Understand local and global names and where variables can
    be accessed.
-   **Recursion fundamentals:** A function calls itself to solve a
    smaller version of a problem. Every recursive solution needs a base
    case and progress toward it.
-   **Basic number problems:** Practice digit extraction, reversing
    numbers, checking primes, factorials, and GCD/LCM.
-   **Algorithm tracing:** Follow variable values and execution order by
    hand.
-   **Edge cases:** Consider empty input, one element, duplicates,
    negative values, and boundary values.

**Practice:** Write small programs first, then solve problems involving
loops, functions, number properties, and simple patterns. Explain the
approach before coding.

## 02 --- Arrays and Lists

**Purpose:** Store and process sequences of values.

-   **Array:** A sequence-like structure whose elements are typically
    stored contiguously in memory in lower-level languages. Python lists
    are dynamic arrays of object references.
-   **Python list:** An ordered, mutable collection that can grow or
    shrink and can contain values of different types.
-   **Indexing:** Access an element by position. Python uses zero-based
    indexing.
-   **Slicing:** Select a range with `sequence[start:stop:step]`; the
    stop index is excluded.
-   **Traversal:** Visit elements one by one to calculate totals, find
    values, or build a result.
-   **Insertion and deletion:** Add or remove elements. Inserting near
    the beginning or middle of a Python list generally requires shifting
    references.
-   **Searching:** Find an element or its position. Linear search checks
    elements one by one.
-   **Prefix sums:** Store cumulative sums so range-sum queries can be
    answered efficiently after preprocessing.
-   **Frequency counting:** Count occurrences using a dictionary or
    `collections.Counter`.
-   **In-place operations:** Modify a collection without constructing a
    complete replacement when appropriate.
-   **Subarrays:** Contiguous portions of an array. A subarray differs
    from a subsequence, whose elements need not be adjacent.
-   **Two-dimensional lists:** Represent grids and matrices using nested
    lists; be careful when creating independent rows.

**Common problems:** Find a maximum or minimum, remove duplicates,
rotate an array, merge sorted arrays, calculate prefix sums, solve
subarray problems, and use frequency maps.

**Complexity reminders:** Indexing a Python list by position is
typically **O(1)**; searching an unsorted list is **O(n)**; appending is
**O(1) amortized**; inserting or deleting near the beginning is
**O(n)**.

## 03 --- Sorting Algorithms

**Purpose:** Arrange elements in an order so that later operations
become easier.

-   **Sorting:** Rearrange values in ascending or descending order.
-   **Bubble sort:** Repeatedly compare adjacent elements and swap them
    when out of order. Usually O(n²); useful mainly for learning.
-   **Selection sort:** Repeatedly select the smallest remaining element
    and put it in its final position. O(n²) comparisons.
-   **Insertion sort:** Insert each new element into the correct
    position in an already-sorted prefix. Worst-case O(n²), but
    effective on small or nearly sorted inputs.
-   **Merge sort:** Divide the sequence, sort the halves, and merge
    them. O(n log n) time, generally with O(n) auxiliary space for
    arrays.
-   **Quicksort:** Partition values around a pivot and recursively sort
    the partitions. Average O(n log n), worst-case O(n²) with poor
    partitions.
-   **Heap sort:** Build a heap and repeatedly extract the next extreme
    element. O(n log n) time.
-   **Python's `sort()` and `sorted()`:** Python uses Timsort, a stable
    sorting algorithm. `list.sort()` modifies the list; `sorted()`
    returns a new list.
-   **Custom sorting:** Use `key=` to specify the value or tuple that
    determines order.
-   **Stability:** A stable sort preserves the relative order of items
    with equal keys.
-   **In-place sorting:** Uses little additional storage, although the
    exact memory usage depends on the algorithm and implementation.

**How to compare algorithms:** Consider time complexity, extra memory,
stability, input size, and whether the data is already partially sorted.
In practical Python code, built-in sorting is often preferable to a
hand-written algorithm.

## 04 --- Strings

**Purpose:** Process text and sequences of characters.

-   **String immutability:** Python strings cannot be changed in place.
    Operations such as concatenation create new strings.
-   **Indexing and slicing:** Access individual characters and
    substrings.
-   **Traversal:** Examine characters to count, compare, or transform
    them.
-   **Character properties:** Use methods such as `isalpha()`,
    `isdigit()`, `isalnum()`, `lower()`, and `upper()` when appropriate.
-   **Palindrome:** A sequence that reads the same forward and backward.
-   **Anagrams:** Strings containing the same character counts, possibly
    in different orders.
-   **Frequency maps:** Count characters with a dictionary or `Counter`.
-   **Substring vs. subsequence:** A substring is contiguous; a
    subsequence preserves order but may skip characters.
-   **String building:** Use `"".join(parts)` when combining many string
    fragments.
-   **Two-pointer string processing:** Compare characters from opposite
    ends or advance through two strings.
-   **Pattern matching:** Learn basic substring search first; more
    advanced topics include KMP and rolling hashes.

**Common problems:** Reverse a string, validate a palindrome, check
anagrams, find the first non-repeating character, count character
frequencies, and find the longest substring satisfying a condition.

## 05 --- Linked Lists

**Purpose:** Learn a node-based structure where each node refers to
another node rather than storing all elements in one contiguous array.

-   **Node:** Usually contains a value and a reference to another node.
-   **Head:** Reference to the first node. An empty list has no head
    (`None`).
-   **Singly linked list:** Each node points to the next node.
-   **Doubly linked list:** Each node points to both the next and
    previous nodes.
-   **Circular linked list:** The last node points back to a node in the
    list, often the head.
-   **Traversal:** Follow node references until the end or until a
    target is found.
-   **Insertion and deletion:** Update links carefully so nodes are not
    lost.
-   **Reversal:** Change the direction of links, commonly using
    `previous`, `current`, and `next_node`.
-   **Fast and slow pointers:** Move pointers at different speeds to
    detect cycles or find a middle node.
-   **Cycle detection:** Floyd's tortoise-and-hare algorithm detects a
    cycle in O(n) time and O(1) auxiliary space.
-   **Merge sorted lists:** Reuse or create nodes while preserving
    sorted order.
-   **Dummy/sentinel node:** A temporary node that simplifies edge cases
    near the head.
-   **Intersection:** Determine whether two linked lists share the same
    node objects, not merely equal values.

**Key trade-off:** Accessing an arbitrary position requires traversal
and is O(n). Inserting or deleting a node can be O(1) when the relevant
node or predecessor is already known.

**Edge cases:** Empty list, one node, deleting the head, deleting the
tail, absent target, and cyclic lists.

## 06 --- Stacks and Queues

**Purpose:** Learn structures that control the order in which items are
processed.

### Stack --- Last In, First Out (LIFO)

The most recently added item is removed first.

-   **Push:** Add an item.
-   **Pop:** Remove the top item.
-   **Peek/top:** Inspect the top item without removing it.
-   **Typical uses:** Function-call stacks, undo operations, expression
    evaluation, parentheses validation, and monotonic-stack problems.
-   **Python implementation:** A list supports efficient `append()` and
    `pop()` at the end.

### Queue --- First In, First Out (FIFO)

The earliest added item is removed first.

-   **Enqueue:** Add an item to the back.
-   **Dequeue:** Remove an item from the front.
-   **Front/peek:** Inspect the next item to be removed.
-   **Typical uses:** Scheduling, buffering, simulations, and
    breadth-first search.
-   **Python implementation:** Use `collections.deque` for efficient
    operations at both ends. Repeatedly removing index zero from a list
    is inefficient.

### Related concepts

-   **Deque:** A double-ended queue that supports insertion and removal
    at either end.
-   **Circular queue:** Reuses fixed-capacity storage by wrapping
    indices around.
-   **Monotonic stack:** Maintains increasing or decreasing values to
    solve next-greater/smaller-element problems.
-   **Monotonic queue:** Maintains candidates in order, often for
    sliding-window minimum or maximum problems.
-   **BFS:** A graph/tree traversal that typically uses a queue.
-   **DFS:** A traversal that can use recursion or an explicit stack.

**Common problems:** Valid parentheses, next greater element, stock
span, implement a queue using stacks, implement a stack using queues,
and level-order traversal.

## 07 --- Binary Trees

**Purpose:** Represent hierarchical data using nodes with up to two
children.

-   **Node:** Holds a value and references to a left child and a right
    child.
-   **Root:** The top node of the tree.
-   **Parent and child:** A parent has a direct connection to a child
    node.
-   **Leaf:** A node with no children.
-   **Depth:** Number of edges from the root to a node.
-   **Height:** Number of edges on the longest downward path from a node
    to a leaf. Some definitions count nodes instead, so state your
    convention.
-   **Subtree:** A node and all its descendants.
-   **Recursive structure:** Each child can itself be the root of a
    smaller tree.
-   **Preorder traversal:** Root, left, right.
-   **Inorder traversal:** Left, root, right.
-   **Postorder traversal:** Left, right, root.
-   **Level-order traversal:** Visit nodes level by level, generally
    using a queue.
-   **Recursive DFS:** A function visits a node and recursively
    processes its children.
-   **Iterative traversal:** Use an explicit stack or queue rather than
    the call stack.
-   **Tree diameter:** The longest path between any two nodes; it need
    not pass through the root.
-   **Balanced tree:** A tree whose height remains controlled according
    to a specified balance condition.
-   **Lowest common ancestor (LCA):** The deepest node that is an
    ancestor of two target nodes.
-   **Path problems:** Calculate root-to-leaf sums, test whether a path
    meets a condition, or collect path values.
-   **Serialization:** Convert a tree into a representation that can
    later reconstruct it.

### Binary Search Tree (BST)

A BST is a binary tree with an ordering rule. A common rule is that
values in the left subtree are smaller than the node and values in the
right subtree are larger, but duplicate handling varies by
implementation.

-   **Search:** Follow the ordering rule to choose a subtree.
-   **Insertion:** Find the appropriate location and attach a node.
-   **Deletion:** Handle a leaf, a node with one child, or a node with
    two children.
-   **Minimum/maximum:** Follow left/right child links.
-   **Inorder traversal:** Produces sorted order for a BST under the
    usual ordering rule.
-   **Complexity:** Search, insertion, and deletion are O(h), where h is
    tree height. They are O(log n) in a balanced tree and can degrade to
    O(n) in a skewed tree.

**Common problems:** Tree height, maximum depth, diameter, symmetry,
path sum, invert a tree, validate a BST, search/insert/delete in a BST,
and lowest common ancestor.

## 08 --- Heaps

**Purpose:** Efficiently retrieve the smallest or largest item without
fully sorting all values.

-   **Heap:** A complete binary tree that satisfies a heap-order
    property.
-   **Min-heap:** Every parent is no greater than its children, so the
    minimum is at the root.
-   **Max-heap:** Every parent is no smaller than its children, so the
    maximum is at the root.
-   **Array representation:** For zero-based indexing, the children of
    index `i` are `2*i + 1` and `2*i + 2`; the parent of a non-root
    index `i` is `(i - 1) // 2`.
-   **Sift up:** Move a newly inserted value toward the root while the
    heap property is violated.
-   **Sift down:** Move a root or replacement value downward to restore
    the heap property.
-   **Insertion:** O(log n).
-   **Peek at the extreme element:** O(1).
-   **Extract the extreme element:** O(log n).
-   **Heap construction:** Bottom-up heapification can build a heap in
    O(n) time.
-   **Heap sort:** Repeatedly extract elements to produce sorted order,
    typically O(n log n).
-   **Top K problems:** Use a heap to find the K largest/smallest values
    without sorting every value when beneficial.
-   **K-way merge:** Use a heap to repeatedly select the next smallest
    item from multiple sorted sequences.
-   **Priority queue:** A structure that removes items according to
    priority rather than insertion order.

### Python's `heapq`

Python's `heapq` implements a min-heap. To simulate a max-heap for
numeric values, negating values is a common technique; take care with
how values are stored and returned.

**Common problems:** Kth largest element, top K frequent elements, merge
K sorted lists, task scheduling, and maintaining a running median with
two heaps.

## 10 --- Sliding Window and Two Pointers

**Purpose:** Solve many sequence and string problems by maintaining a
small amount of state instead of repeatedly examining every possible
range.

### Sliding window

A window is a contiguous range of elements. Its left and right
boundaries move as the algorithm processes the input.

-   **Fixed-size window:** The window length stays constant, such as
    finding the maximum sum of any `k` consecutive values.
-   **Variable-size window:** The boundaries move according to a
    condition, such as finding the shortest valid range.
-   **Window state:** Maintain a running sum, frequency map, count, or
    other information about the current window.
-   **Expand and shrink:** Move the right boundary to include new
    elements and the left boundary to remove elements when required.
-   **Frequency-map windows:** Track how often values or characters
    appear.
-   **Amortized reasoning:** In many linear-time solutions, each pointer
    moves forward at most O(n) times, giving O(n) total pointer
    movement.
-   **Important limitation:** The usual shrink-while-invalid pattern
    often relies on a monotonic property. Negative numbers can
    invalidate some common sliding-window sum strategies; prefix sums or
    other methods may be needed.

### Two pointers

Two indices process a sequence together.

-   **Opposite-direction pointers:** Start at opposite ends and move
    inward, as in sorted two-sum or palindrome checking.
-   **Same-direction pointers:** Advance through a sequence at different
    rates.
-   **Fast and slow pointers:** Useful for linked-list cycle detection
    and removing duplicates in sorted arrays.
-   **Sorted-array techniques:** Sorting can enable efficient pair or
    triplet searches, but remember that sorting changes the original
    order.
-   **Partitioning:** Move elements into groups based on a condition.
-   **In-place updates:** Overwrite or rearrange elements while using
    little extra storage.

**Common problems:** Maximum average subarray, maximum points from
cards, longest substring without repeating characters, fruit into
baskets, minimum-size subarray sum, two sum in a sorted array, container
with most water, and trapping rain water.

### How to choose the pattern

1.  Is the problem about a **contiguous** subarray or substring?
    Consider sliding window or prefix sums.
2.  Is the input sorted, or can sorting help? Consider two pointers.
3.  Do two indices need to move at different speeds? Consider fast/slow
    pointers.
4.  Can each pointer move only forward without missing a valid answer?
    Prove this before relying on a linear-time solution.

------------------------------------------------------------------------

# Complexity Analysis

Complexity describes how resource requirements grow as the input size
`n` grows.

  Complexity   Name           Typical example
  ------------ -------------- -------------------------------------------
  O(1)         Constant       Access a list element by index
  O(log n)     Logarithmic    Binary search on sorted data
  O(n)         Linear         Scan a list once
  O(n log n)   Linearithmic   Efficient comparison sorting
  O(n²)        Quadratic      Compare every pair using two nested loops
  O(2ⁿ)        Exponential    Many brute-force subset explorations
  O(n!)        Factorial      Generate all permutations

These are typical examples, not universal guarantees. Actual complexity
depends on the algorithm and its assumptions.

-   **Time complexity:** How the number of operations grows with input
    size.
-   **Auxiliary space:** Extra memory used by an algorithm, often
    excluding the input itself.
-   **Best case:** The most favorable input behavior.
-   **Average case:** Expected behavior under an assumed input
    distribution.
-   **Worst case:** The maximum cost for inputs of a given size.
-   **Amortized complexity:** Average cost per operation over a sequence
    of operations, even if some individual operations are expensive.

For recursive algorithms, consider the recursion stack as part of space
complexity.

------------------------------------------------------------------------

# Recommended Format for Solutions

Use a consistent format for substantial problems. It helps you revise
the idea later and makes your code easier for other people to
understand.

``` python
"""
Problem: Maximum sum of a fixed-size subarray

Approach:
Maintain the sum of the current window. Add the incoming
element and remove the element that leaves the window.

Time Complexity: O(n)
Auxiliary Space: O(1)
"""

def max_window_sum(nums, k):
    if k <= 0 or k > len(nums):
        raise ValueError("k must be between 1 and len(nums)")

    window_sum = sum(nums[:k])
    best = window_sum

    for right in range(k, len(nums)):
        window_sum += nums[right]
        window_sum -= nums[right - k]
        best = max(best, window_sum)

    return best
```

For each important solution, try to include:

1.  **Problem statement:** Describe the task in your own words.
2.  **Example:** Show input and expected output.
3.  **Approach:** Explain the key idea.
4.  **Correctness reasoning:** Explain why the approach returns the
    right answer.
5.  **Complexity:** State time and auxiliary space.
6.  **Implementation:** Use meaningful variable names and avoid
    unnecessary code.
7.  **Tests:** Include normal cases and edge cases.

The example assumes `nums` contains numeric values. If your solution
must follow a specific platform's function signature, preserve that
signature.

------------------------------------------------------------------------

# How to Run the Code

1.  Install Python 3.
2.  Open a terminal in the repository or relevant topic folder.
3.  Run a Python file, for example:

``` bash
python 03_Sorting_Algorithms/example.py
```

On some Windows installations, this command may be:

``` bash
py 03_Sorting_Algorithms/example.py
```

Use the actual file name that exists in your folder.

## Testing checklist

For each solution, consider:

-   Empty input, if the problem allows it.
-   One element.
-   Duplicate values.
-   Already sorted and reverse-sorted input.
-   Negative, zero, and positive values where relevant.
-   Minimum and maximum allowed input sizes.
-   A case where the answer does not exist, if allowed by the problem.

------------------------------------------------------------------------

# Learning Roadmap

The repository is organized by topic, but DSA learning is iterative. A
useful progression is:

1.  Python basics, arrays, and strings.
2.  Searching and sorting.
3.  Hashing and frequency counting.
4.  Two pointers and sliding window.
5.  Linked lists, stacks, and queues.
6.  Recursion and backtracking.
7.  Trees, BSTs, and heaps.
8.  Greedy algorithms.
9.  Graph traversal and graph algorithms.
10. Dynamic programming.

Revisit earlier topics while solving new problems. Many problems combine
several techniques.

## Progress Tracker

Update this checklist honestly as you learn and implement each topic.

-   [ ] Basics
-   [ ] Arrays and Lists
-   [ ] Sorting Algorithms
-   [ ] Strings
-   [ ] Linked Lists
-   [ ] Stacks and Queues
-   [ ] Binary Trees
-   [ ] Heaps
-   [ ] Sliding Window and Two Pointers
-   [ ] Hashing
-   [ ] Binary Search
-   [ ] Recursion and Backtracking
-   [ ] Bit Manipulation
-   [ ] Greedy Algorithms
-   [ ] Graphs
-   [ ] Dynamic Programming

------------------------------------------------------------------------

## About

This repository is a personal learning resource for Data Structures and
Algorithms using Python. It is intended for practice, revision, and
continuous improvement.

**Language:** Python 3\
**Status:** Actively maintained as new concepts and solutions are
learned.
