# Get input for two sets of numbers
set1 = set(map(int, input("Enter numbers for set 1 (space-separated): ").split()))
set2 = set(map(int, input("Enter numbers for set 2 (space-separated): ").split()))

# Display set operations
print("\nSet Operations:")
print("Union:", set1.union(set2))
print("Intersection:", set1.intersection(set2))
print("Difference (A - B):", set1.difference(set2))
print("Symmetric Difference:", set1.symmetric_difference(set2))