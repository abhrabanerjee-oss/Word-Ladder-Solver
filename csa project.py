from collections import deque
def load_dictionary(word_length):
    """Load a built-in mini dictionary filtered by length."""
    words = set()
    try:
        with open("words.txt", "r") as file:
            for w in file.read().split():
                if len(w) == word_length:
                    words.add(w.lower())
    except FileNotFoundError:
        words = {"cat", "cot", "cog", "dog", "dot", "dat", "bat", "bag"}
    return words
def get_neighbors(word, dictionary):
    """Generate valid next words differing by one letter."""
    neighbors = []
    for i in range(len(word)):
        for ch in "abcdefghijklmnopqrstuvwxyz":
            new_word = word[:i] + ch + word[i+1:]
            if new_word in dictionary and new_word != word:
                neighbors.append(new_word)
    return neighbors
def bfs_word_ladder(start, goal, dictionary):
    """Perform BFS to find shortest transformation sequence."""
    queue = deque([start])
    visited = set([start])
    parent = {start: None}

    while queue:
        current = queue.popleft()

        if current == goal:
            break

        for neighbor in get_neighbors(current, dictionary):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)

    return reconstruct_path(parent, start, goal)
def reconstruct_path(parent, start, goal):
    """Rebuild the path from goal to start."""
    if goal not in parent:
        return None

    path = []
    current = goal
    while current:
        path.append(current)
        current = parent[current]
    return list(reversed(path))
if __name__ == "__main__":
    print("_Word Ladder Solver (BFS)__")

    start = input("Enter start word: ").lower()
    goal = input("Enter target word: ").lower()

    if len(start) != len(goal):
        print("Error: Words must be the same length!")
        exit()

    dictionary = load_dictionary(len(start))

    path = bfs_word_ladder(start, goal, dictionary)

    if path:
        print("\n Transformation found!")
        print(" → ".join(path))
        print(f"Steps required: {len(path) - 1}")
    else:
        print("\n No valid transformation path found!")

