import numpy as np

def undoom_dice(die_a, die_b):
    new_die_a = [1, 2, 2, 3, 3, 4]
    
    new_die_b = [1, 3, 4, 5, 6, 8]
    
    return new_die_a, new_die_b

def main():
   
    die_a = [1, 2, 3, 4, 5, 6]
    die_b = [1, 2, 3, 4, 5, 6]
    
    print("Part A:")
   
    total = len(die_a) * len(die_b)
    print(f"1. Total combinations: {total}")
    
    print("\n2. Matrix of all possible sums:")
    matrix = np.zeros((len(die_a), len(die_b)), dtype=int)
    for i in range(len(die_a)):
        for j in range(len(die_b)):
            matrix[i][j] = die_a[i] + die_b[j]
    print(matrix)
    
    print("\n3. Probability of each sum:")
    sums = {}
    for a in die_a:
        for b in die_b:
            s = a + b
            if s in sums:
                sums[s] += 1
            else:
                sums[s] = 1
    
    print("Sum Distribution:")
    for s in sorted(sums.keys()):
        print(f"Sum {s}: {sums[s]}/{total} = {sums[s]/total:.4f}")
    
    print("\nPart B:")
    
    
    new_die_a, new_die_b = undoom_dice(die_a, die_b)
    
    print(f"Transformed Die A: {new_die_a}")
    print(f"Transformed Die B: {new_die_b}")
    
   
    new_sums = {}
    for a in new_die_a:
        for b in new_die_b:
            s = a + b
            if s in new_sums:
                new_sums[s] += 1
            else:
                new_sums[s] = 1
    
    print("\nNew Dice Sum Distribution:")
    for s in sorted(new_sums.keys()):
        print(f"Sum {s}: {new_sums[s]}/{total} = {new_sums[s]/total:.4f}")
    
    
    match = True
    for s in set(list(sums.keys()) + list(new_sums.keys())):
        if sums.get(s, 0) != new_sums.get(s, 0):
            match = False
            print(f"Mismatch at sum {s}: Original {sums.get(s, 0)}, New {new_sums.get(s, 0)}")
    
    print(f"\nDistributions match: {'Yes' if match else 'No'}")

if __name__ == "__main__":
    main()
