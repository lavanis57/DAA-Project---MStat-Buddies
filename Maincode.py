import time


def median_of_two_sorted_iterative(A, B):
    if len(A) > len(B):
        A, B = B, A
    n, m = len(A), len(B)

    if n == 0:
        mid = m // 2
        if m % 2 == 0:
            return (B[mid - 1] + B[mid]) / 2.0
        else:
            return B[mid]

    lo, hi = 0, n
    half = (n + m + 1) // 2

    while lo <= hi:
        i = (lo + hi) // 2
        j = half - i

        l1 = A[i - 1] if i > 0 else float('-inf')
        r1 = A[i] if i < n else float('inf')
        l2 = B[j - 1] if j > 0 else float('-inf')
        r2 = B[j] if j < m else float('inf')

        if l1 <= r2 and l2 <= r1:
            if (n + m) % 2 == 0:
                return (max(l1, l2) + min(r1, r2)) / 2.0
            else:
                return max(l1, l2)

        elif l1 > r2:
            hi = i - 1
        else:
            lo = i + 1


def median_of_two_sorted_recursive(A, B):
    if len(A) > len(B):
        A, B = B, A
    n, m = len(A), len(B)

    if n == 0:
        mid = m // 2
        if m % 2 == 0:
            return (B[mid - 1] + B[mid]) / 2.0
        else:
            return B[mid]

    half = (n + m + 1) // 2

    def recurse(lo, hi):
        if lo > hi:
            return None
        i = (lo + hi) // 2
        j = half - i

        l1 = A[i - 1] if i > 0 else float('-inf')
        r1 = A[i] if i < n else float('inf')
        l2 = B[j - 1] if j > 0 else float('-inf')
        r2 = B[j] if j < m else float('inf')

        if l1 <= r2 and l2 <= r1:
            if (n + m) % 2 == 0:
                return (max(l1, l2) + min(r1, r2)) / 2.0
            else:
                return max(l1, l2)
        elif l1 > r2:
            return recurse(lo, i - 1)
        else:
            return recurse(i + 1, hi)

    return recurse(0, n)


def main():
    print("=== Median of Two Sorted Arrays Calculator ===")
    print()

    # Input first array
    print("Enter elements for Array A (space-separated):")
    try:
        A = list(map(float, input().split()))
    except ValueError:
        print("Invalid input! Please enter numbers only.")
        return

    # Input second array
    print("Enter elements for Array B (space-separated):")
    try:
        B = list(map(float, input().split()))
    except ValueError:
        print("Invalid input! Please enter numbers only.")
        return

    # Sort the arrays
    A_sorted = sorted(A)
    B_sorted = sorted(B)

    print("\n" + "=" * 50)
    print(f"Array A (sorted): {A_sorted}")
    print(f"Array B (sorted): {B_sorted}")
    print("=" * 50)

    # Calculate median using iterative method and measure time
    start_time = time.perf_counter()
    median_iter = median_of_two_sorted_iterative(A_sorted, B_sorted)
    iter_time = time.perf_counter() - start_time

    # Calculate median using recursive method and measure time
    start_time = time.perf_counter()
    median_rec = median_of_two_sorted_recursive(A_sorted, B_sorted)
    rec_time = time.perf_counter() - start_time

    print("\nRESULTS:")
    print("-" * 30)
    print(f"Median using iteration: {median_iter}")
    print(f"Median using recursion: {median_rec}")
    print(f"Time using iteration: {iter_time:.8f} seconds")
    print(f"Time using recursion: {rec_time:.8f} seconds")
    print("-" * 30)

    # Verification
    if median_iter == median_rec:
        print("✓ Both methods produced the same result!")
    else:
        print("✗ Methods produced different results!")

    # Performance comparison
    if iter_time < rec_time:
        faster = "Iterative"
        speedup = rec_time / iter_time
        print(f"✓ Iterative method was {speedup:.2f}x faster")
    else:
        faster = "Recursive"
        speedup = iter_time / rec_time
        print(f"✓ Recursive method was {speedup:.2f}x faster")


if __name__ == "__main__":
    main()
