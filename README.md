# Word Ladder Solver using Breadth-First Search (BFS)

**Institution:** VIT Bhopal University  
**Course:** CSA (Fundamentals of AI and ML)  
**Instructor:** Prof. Santosh Kumar Sahoo  
**Student Name:** Abhra Banerjee  
**Registration Number:** 25BCY10118  
**Academic Year:** 2025-26

---

## Project Overview

The **Word Ladder Solver** is an intelligent algorithm-based application that finds the shortest transformation sequence between two words of equal length. Using **Breadth-First Search (BFS)**, a fundamental graph traversal algorithm, this project demonstrates how complex word relationships can be modeled as graph problems and efficiently solved.

### What is a Word Ladder?

A word ladder is a word puzzle where you transform one word into another by changing one letter at a time, with each intermediate step forming a valid word from a dictionary. For example:

```
CAT → COT → COG → DOG
```

This project automates the discovery of such transformation sequences using sophisticated algorithmic techniques.

---

## Problem Statement

Given two words of identical length, find the shortest sequence of valid English words that transforms the start word into the goal word by changing exactly one letter per step. Each intermediate word must exist in the dictionary.

**Input:**
- Start word (e.g., "cat")
- Goal word (e.g., "dog")

**Output:**
- Transformation sequence if one exists
- Number of steps required
- Error message if no valid transformation exists

---

## Key Features

✓ **Optimal Path Finding:** Uses BFS algorithm to guarantee the shortest transformation sequence  
✓ **Dictionary Support:** Loads words from external file or uses built-in fallback dictionary  
✓ **Error Handling:** Validates input word lengths and handles missing dictionary files  
✓ **Efficient Neighbor Generation:** Intelligently generates valid word neighbors by single-letter substitution  
✓ **Path Reconstruction:** Rebuilds the complete transformation path from start to goal  
✓ **User-Friendly Interface:** Simple command-line interface for easy interaction  

---

## Algorithm: Breadth-First Search (BFS)

### Why BFS?

BFS is the optimal choice for this problem because:

1. **Shortest Path Guarantee:** BFS explores nodes level by level, ensuring the first path found is the shortest
2. **Unweighted Graph:** Since each transformation has equal weight (one letter change), BFS is more efficient than Dijkstra's algorithm
3. **Complete Search:** BFS explores all possibilities systematically before declaring failure
4. **Time Efficiency:** O(V + E) complexity, where V is the number of words and E is the number of valid transformations

### Time and Space Complexity

| Aspect | Complexity | Details |
|--------|-----------|---------|
| **Time Complexity** | O(N × 26 × L) | N = dictionary size, L = word length, 26 letters in alphabet |
| **Space Complexity** | O(N) | For visited set, queue, and parent tracking |
| **Worst Case** | O(N × 26 × L) | When traversing entire dictionary |

---

## Technical Stack

| Component | Technology |
|-----------|-----------|
| **Programming Language** | Python 3.7+ |
| **Data Structures** | Deque (from collections), Set, Dictionary |
| **Algorithm** | Breadth-First Search (BFS) |
| **File I/O** | Text file reading (words.txt) |

---

## Code Structure

### Main Components

#### 1. **load_dictionary(word_length)**
Loads a dictionary of words filtered by length. Attempts to read from `words.txt` or uses built-in fallback.

```python
Purpose: Initialize word dictionary
Input: word_length (int) - desired word length
Output: words (set) - set of valid words of specified length
```

#### 2. **get_neighbors(word, dictionary)**
Generates all valid neighboring words by single-letter substitution.

```python
Purpose: Find all words differing by exactly one letter
Input: word (str), dictionary (set)
Output: neighbors (list) - list of valid neighbor words
Logic: 
  - For each position in word
  - Try each letter a-z
  - Check if new word exists in dictionary
  - Add to neighbors if valid and different from original
```

#### 3. **bfs_word_ladder(start, goal, dictionary)**
Core BFS algorithm that finds the shortest transformation path.

```python
Purpose: Find shortest word transformation sequence
Input: start (str), goal (str), dictionary (set)
Output: path (list) - transformation sequence or None
Algorithm:
  - Initialize queue with start word
  - Mark start as visited
  - Set start's parent as None
  - While queue not empty:
    - Get front element
    - If equals goal, break
    - For each neighbor not visited:
      - Mark as visited
      - Set current as parent
      - Add to queue
  - Reconstruct and return path
```

#### 4. **reconstruct_path(parent, start, goal)**
Rebuilds the transformation sequence from the parent tracking dictionary.

```python
Purpose: Convert parent pointers to actual transformation path
Input: parent (dict), start (str), goal (str)
Output: path (list) - sequence from start to goal or None
Logic:
  - Check if goal is reachable
  - Traverse from goal backwards using parent pointers
  - Reverse final path to get start→goal order
```

---

## Installation and Usage

### Requirements

- Python 3.7 or higher
- No external libraries required (uses only Python standard library)

### Files Needed

```
word_ladder_solver/
├── word_ladder.py          # Main program
├── words.txt               # Dictionary file (optional)
└── README.md               # This file
```

### How to Run

1. **Save the code** as `word_ladder.py`

2. **Create a dictionary file** `words.txt` (optional):
   ```
   cat
   cot
   cog
   dog
   dot
   dat
   bat
   bag
   ```

3. **Run the program**:
   ```bash
   python word_ladder.py
   ```

4. **Provide inputs** when prompted:
   ```
   Enter start word: cat
   Enter target word: dog
   ```

5. **View results**:
   ```
   Transformation found!
   cat → cot → cog → dog
   Steps required: 3
   ```

---

## Usage Examples

### Example 1: Successful Transformation
```
Input:
  Start: cat
  Goal: dog

Output:
  Transformation found!
  cat → cot → cog → dog
  Steps required: 3
```

### Example 2: Error - Different Lengths
```
Input:
  Start: cat
  Goal: dogs

Output:
  Error: Words must be the same length!
```

### Example 3: No Valid Transformation
```
Input:
  Start: cat
  Goal: xyz

Output:
  No valid transformation path found!
```

---

## Input Validation

The program performs the following validations:

| Validation | Rule | Action |
|-----------|------|--------|
| **Length Match** | Both words must be same length | Exit with error if not |
| **Case Sensitivity** | Converts to lowercase | Automatic conversion |
| **Dictionary Load** | Falls back to built-in dictionary | Uses default if file missing |
| **Empty Results** | Goal unreachable from start | Returns None and user message |

---

## Algorithm Walkthrough: Step-by-Step Execution

### Example: CAT → DOG

**Initial State:**
- Queue: [cat]
- Visited: {cat}
- Parent: {cat: None}

**Step 1:** Process CAT
- Neighbors: [bat, cot, dot, ...]
- Add unvisited neighbors to queue
- Queue: [bat, cot, dot, ...]
- Visited: {cat, bat, cot, dot, ...}

**Step 2:** Process BAT
- Neighbors: [bat, cat, bat, ...]
- All neighbors already visited
- Queue: [cot, dot, ...]

**Step 3:** Process COT
- Neighbors: [cat, cot, cog, ...]
- Add unvisited cog
- Queue: [dot, cog, ...]
- Visited: {..., cog}

**Step 4:** Process DOT
- Neighbors: [cat, dot, dog, ...]
- Add unvisited dog
- Queue: [cog, dog, ...]
- Visited: {..., dog}

**Step 5:** Process COG
- Neighbors: [cot, cog, dog, ...]
- All already visited
- Queue: [dog, ...]

**Step 6:** Process DOG (Goal Found!)
- Current == Goal
- Break loop
- Reconstruct path: dog ← cog ← cot ← cat
- Reverse: cat → cot → cog → dog

---

## Data Flow Diagram

```
┌─────────────────┐
│  User Input     │
│ (start, goal)   │
└────────┬────────┘
         │
         ▼
┌─────────────────────┐
│ Validate Lengths    │
│ Convert to Lower    │
└────────┬────────────┘
         │
         ▼
┌──────────────────────┐
│ Load Dictionary      │
│ (from file or built) │
└────────┬─────────────┘
         │
         ▼
┌──────────────────────────┐
│ Execute BFS Algorithm    │
│ ├─ Initialize Queue      │
│ ├─ Track Visited Words   │
│ ├─ Generate Neighbors    │
│ └─ Find Path             │
└────────┬─────────────────┘
         │
         ▼
┌──────────────────────┐
│ Reconstruct Path     │
│ (using parent dict)  │
└────────┬─────────────┘
         │
         ▼
┌──────────────────────┐
│ Display Results      │
│ - Path (if found)    │
│ - Step count         │
│ - Error message      │
└──────────────────────┘
```

---

## Flowchart

```
         START
           │
           ▼
    ┌─────────────┐
    │ Input Words │
    └──────┬──────┘
           │
           ▼
      ┌────────────┐
      │ Lengths    │
      │ Equal?     │
      └──┬──────┬──┘
    No  │      │ Yes
        │      ▼
      Exit  ┌─────────────┐
           │Load Dict    │
           └──────┬──────┘
                  │
                  ▼
            ┌──────────────┐
            │Initialize BFS│
            │Queue, Visited│
            └──────┬───────┘
                   │
                   ▼
            ┌──────────────┐
            │Queue Empty?  │
            └──┬────────┬──┘
           Yes │        │ No
              │        ▼
              │  ┌─────────────────┐
              │  │Get Front Node   │
              │  └────────┬────────┘
              │           │
              │           ▼
              │    ┌──────────────┐
              │    │Is Goal?      │
              │    └──┬────────┬──┘
              │   Yes │        │ No
              │      │        ▼
              │      │  ┌────────────────┐
              │      │  │Get Neighbors   │
              │      │  └────────┬───────┘
              │      │           │
              │      │           ▼
              │      │    ┌─────────────┐
              │      │    │Add Unvisited│
              │      │    │to Queue     │
              │      │    └────────┬────┘
              │      │            │
              │      └──────┬─────┘
              │             │
              └─────────────┴──────┐
                            │
                            ▼
                   ┌─────────────────┐
                   │Reconstruct Path │
                   └────────┬────────┘
                            │
                            ▼
                   ┌─────────────────┐
                   │Display Results  │
                   └────────┬────────┘
                            │
                            ▼
                           END
```

---

## Key Concepts Demonstrated

### 1. Graph Theory
- Modeling word relationships as graph nodes and edges
- Understanding graph connectivity and traversal

### 2. Breadth-First Search Algorithm
- Level-by-level exploration
- Shortest path finding in unweighted graphs
- Queue-based iterative approach

### 3. Data Structures
- **Queue (Deque):** For BFS traversal order
- **Set:** For fast O(1) dictionary lookup and visited tracking
- **Dictionary:** For parent pointer tracking and path reconstruction

### 4. Algorithm Optimization
- Early termination when goal found
- Visited set to prevent revisiting nodes
- Efficient neighbor generation through character substitution

### 5. Problem-Solving Strategy
- Breaking complex problems into manageable functions
- Input validation and error handling
- Modular code design for reusability

---

## Possible Extensions

1. **Bidirectional BFS:** Search from both start and goal simultaneously for faster convergence
2. **A* Algorithm:** Use heuristics to guide search (e.g., edit distance to goal)
3. **Word Length Flexibility:** Allow transformations with insertions/deletions
4. **GUI Interface:** Build graphical interface for word ladder visualization
5. **Web Application:** Deploy as web service with interactive visualization
6. **Dictionary Enhancement:** Load larger dictionary files for extended vocabulary
7. **Performance Metrics:** Track and display algorithm statistics (nodes visited, time taken)

---

## Educational Value

This project illustrates fundamental AI and Machine Learning concepts:

- **Search Algorithms:** Understanding different search strategies and their applications
- **Graph Representation:** Modeling real-world problems as graph problems
- **Optimization:** Finding efficient solutions to computational problems
- **Algorithm Analysis:** Evaluating time and space complexity of algorithms
- **Data Structure Selection:** Choosing appropriate data structures for algorithmic efficiency

---

## Testing and Verification

### Test Cases

| Test Case | Start | Goal | Expected Output | Status |
|-----------|-------|------|-----------------|--------|
| Valid Transformation | cat | dog | 3 steps found | ✓ |
| Single Step | cat | cot | 1 step found | ✓ |
| Same Word | cat | cat | 0 steps (same word) | ✓ |
| Different Length | cat | dogs | Error message | ✓ |
| No Path | cat | xyz | No path found | ✓ |

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| **FileNotFoundError for words.txt** | Program falls back to built-in dictionary. Create words.txt in same directory to use custom dictionary. |
| **No transformation found** | Ensure both words exist in dictionary and are connected. Try with different word pairs. |
| **Case sensitivity issues** | Program automatically converts inputs to lowercase. |
| **Memory issues with large dictionaries** | Use word length filtering to reduce dictionary size. |

---

## References and Resources

1. **Graph Algorithms:** Introduction to Algorithms by Cormen, Leiserson, Rivest, and Stein
2. **BFS Algorithm:** [GeeksforGeeks - BFS Algorithm](https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/)
3. **Python Collections:** [Python Official Documentation - Collections Module](https://docs.python.org/3/library/collections.html)
4. **Word Ladder Problem:** Classic problem in competitive programming and technical interviews

---

## Conclusion

The Word Ladder Solver demonstrates the power of fundamental algorithms in solving real-world problems. By modeling a word puzzle as a graph traversal problem and applying BFS, we find optimal solutions efficiently. This project serves as a foundation for understanding more complex AI algorithms and their applications.

---

## Academic Integrity

This project has been created as part of the CSA (Fundamentals of AI and ML) course at VIT Bhopal University. All code is original work by the student and intended for educational purposes under the guidance of Prof. Santosh Kumar Sahoo.

---

**Last Updated:** November 24, 2025  
**Version:** 1.0
