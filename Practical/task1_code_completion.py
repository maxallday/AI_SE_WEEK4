"""
🧠 Task 1: AI-Powered Code Completion

This script compares an AI-generated Python function (simulated using GitHub Copilot-style logic)
with a manually written version. The goal is to sort a list of dictionaries by a specific key
and evaluate which version is more efficient and readable.
"""

# Sample dataset: list of people with names and ages
people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]

# 🤖 AI-generated version (simulated Copilot-style suggestion)
def ai_version(data, key):
    return sorted(data, key=lambda x: x[key])

# ✍️ Manual version with docstring and error handling
def manual_sort(data, key):
    """
    Sorts a list of dictionaries by a specified key.

    Parameters:
        data (list): List of dictionaries.
        key (str): Key to sort by.

    Returns:
        list: Sorted list of dictionaries.
    """
    try:
        return sorted(data, key=lambda x: x[key])
    except KeyError:
        print(f"Key '{key}' not found in one or more dictionaries.")
        return data
    except TypeError:
        print("Invalid data format. Expected a list of dictionaries.")
        return data

# 🔍 Compare outputs
print("=== AI Version Output ===")
print(ai_version(people, "age"))

print("\n=== Manual Version Output ===")
print(manual_sort(people, "age"))

# ⏱️ Performance Benchmarking
import timeit

ai_time = timeit.timeit(lambda: ai_version(people, "age"), number=1000)
manual_time = timeit.timeit(lambda: manual_sort(people, "age"), number=1000)

print(f"\n⏱️ AI version time: {ai_time:.6f} seconds")
print(f"⏱️ Manual version time: {manual_time:.6f} seconds")

# 📝 200-Word Analysis
analysis = """
Both the AI-generated and manual functions successfully sort a list of dictionaries by a specified key.
The AI version, simulated using GitHub Copilot-style logic, is concise and uses Python’s built-in
sorted() function with a lambda expression. It performs well and is syntactically correct, but lacks
documentation and error handling.

The manual version includes a docstring and basic error handling for missing keys and incorrect data types,
making it more robust and user-friendly. In terms of performance, both versions are nearly identical for
small datasets, though the AI version may be slightly faster due to its minimal structure.

Overall, the AI-generated code is efficient and saves time, especially for simple tasks. However, it still
requires human oversight to ensure readability, maintainability, and resilience to edge cases. In a real-world
project, I would use the AI suggestion as a starting point and refine it to meet production standards.
This exercise shows how AI can accelerate development while still benefiting from human review and refinement.
"""

print("\n📝 Analysis:\n")
print(analysis)
