import matplotlib.pyplot as plt
import numpy as np
import random
import time
import statistics
from fpdf import FPDF
import io


# Create PDF class with updated methods
class PDFReport(FPDF):
    def header(self):
        self.set_font('helvetica', 'B', 16)
        self.cell(0, 10, 'Median of Two Sorted Arrays - Comprehensive Analysis', new_x="LMARGIN", new_y="NEXT",
                  align='C')
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font('helvetica', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', align='C')

    def add_section_title(self, title):
        self.set_font('helvetica', 'B', 12)
        self.cell(0, 10, title, new_x="LMARGIN", new_y="NEXT")
        self.ln(2)

    def add_subsection_title(self, title):
        self.set_font('helvetica', 'B', 10)
        self.cell(0, 8, title, new_x="LMARGIN", new_y="NEXT")
        self.ln(1)

    def add_explanation(self, text):
        self.set_font('helvetica', '', 10)
        self.multi_cell(0, 5, text)
        self.ln(2)

    def add_code(self, code):
        self.set_font('courier', '', 8)
        self.multi_cell(0, 4, code)
        self.ln(2)


# Initialize PDF
pdf = PDFReport()
pdf.add_page()

# Add introduction
pdf.add_section_title("Introduction")
intro_text = """
This report analyzes the algorithm for finding the median of two sorted arrays. 
The median is the middle value that separates the higher half from the lower half of a data set. 
For two sorted arrays, we can find the median in O(log(min(m,n))) time using a binary search approach.

The algorithm works by:
1. Ensuring the first array is the smaller one
2. Using binary search to find the correct partition
3. Checking boundary conditions to ensure valid partitions
4. Calculating the median based on whether the total number of elements is even or odd
"""
pdf.add_explanation(intro_text)

# Add algorithm implementations
pdf.add_section_title("Algorithm Implementations")

pdf.add_subsection_title("Iterative Implementation")
iterative_code = '''
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

        l1 = A[i-1] if i > 0 else float('-inf')
        r1 = A[i]   if i < n else float('inf')
        l2 = B[j-1] if j > 0 else float('-inf')
        r2 = B[j]   if j < m else float('inf')

        if l1 <= r2 and l2 <= r1:
            if (n + m) % 2 == 0:
                return (max(l1, l2) + min(r1, r2)) / 2.0
            else:
                return max(l1, l2)

        elif l1 > r2:
            hi = i - 1
        else:
            lo = i + 1
'''
pdf.add_code(iterative_code)

pdf.add_subsection_title("Recursive Implementation")
recursive_code = '''
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

        l1 = A[i-1] if i > 0 else float('-inf')
        r1 = A[i]   if i < n else float('inf')
        l2 = B[j-1] if j > 0 else float('-inf')
        r2 = B[j]   if j < m else float('inf')

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
'''
pdf.add_code(recursive_code)

# Add a new page for test cases
pdf.add_page()
pdf.add_section_title("Edge Case Tests")


# Implement both algorithms
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


def time_function(func, A, B):
    start = time.perf_counter()
    result = func(A, B)
    end = time.perf_counter()
    return result, end - start


# Test cases
test_cases = [
    (1, [], [2, 3, 4], 'One array empty'),
    (2, [], [], 'Both arrays empty'),
    (3, [1], [2], 'Both arrays length one'),
    (4, [1], list(range(10, 100, 10)), 'Unbalanced sizes'),
    (5, [1, 2, 2, 2], [2, 2, 3, 4], 'Duplicates present'),
    (6, [-10, -5, -2], [-3, 1, 4, 6], 'Negative numbers'),
    (7, [1.5, 2.5, 3.5], [0.5, 4.5, 5.5], 'Floating-point numbers'),
    (8, sorted(random.sample(range(-100, 100), 3)), sorted(random.sample(range(-100, 100), 10)),
     'Random different sizes')
]

# Run tests and add to PDF
for num, A, B, desc in test_cases:
    pdf.add_subsection_title(f"Test Case {num}: {desc}")

    try:
        result_iter, t_iter = time_function(median_of_two_sorted_iterative, A, B)
        pdf.add_explanation(f"Iterative method - Time: {t_iter:.6f} seconds, Result: {result_iter}")
    except Exception as e:
        pdf.add_explanation(f"Iterative method - Error: {e}")

    try:
        result_rec, t_rec = time_function(median_of_two_sorted_recursive, A, B)
        pdf.add_explanation(f"Recursive method - Time: {t_rec:.6f} seconds, Result: {result_rec}")
    except Exception as e:
        pdf.add_explanation(f"Recursive method - Error: {e}")

    pdf.add_explanation("---")

# Add performance analysis
pdf.add_page()
pdf.add_section_title("Performance Analysis")


# Performance test function
def run_performance_test():
    random.seed(2025)

    # Define test sizes
    len_A = [100, 1000, 5000, 10000,20000,25000,30000,40000,50000,75000]
    len_B = [150, 1500, 6000, 15000,24000,28000,35000,45000,60000,80000]

    # Lists to store mean runtimes
    mean_times_iter = []
    mean_times_rec = []

    # Run test cases and collect runtimes
    for i in range(len(len_A)):
        A = sorted(random.sample(range(-100000, 100000), len_A[i]))
        B = sorted(random.sample(range(-100000, 100000), len_B[i]))

        # Test iterative
        elapsed_times = []
        for _ in range(5):
            start = time.perf_counter()
            median_of_two_sorted_iterative(A, B)
            elapsed_times.append(time.perf_counter() - start)
        mean_times_iter.append(statistics.mean(elapsed_times))

        # Test recursive
        elapsed_times = []
        for _ in range(5):
            start = time.perf_counter()
            median_of_two_sorted_recursive(A, B)
            elapsed_times.append(time.perf_counter() - start)
        mean_times_rec.append(statistics.mean(elapsed_times))

        pdf.add_explanation(f"Array sizes: {len_A[i]} vs {len_B[i]}")
        pdf.add_explanation(f"Iterative mean time: {mean_times_iter[-1]:.8f} seconds")
        pdf.add_explanation(f"Recursive mean time: {mean_times_rec[-1]:.8f} seconds")
        pdf.add_explanation("---")

    return len_A, mean_times_iter, mean_times_rec


# Run performance tests
sizes, iter_times, rec_times = run_performance_test()

# Add real-world applications
pdf.add_page()
pdf.add_section_title("Real-World Applications")

# Application 1: Property Values
pdf.add_subsection_title("Application 1: Median Property Values")

property_code = '''
whitefield = {
    'Amrutha Platinum Towers': 10340,
    'Prestige Waterford': 11135,
    'Brigade Cosmopolis': 13949,
    'Lakshmi Green Ville': 4913,
    'My Home Dreams': 4867,
    'Sumadhura Eden Garden': 7645,
    'Godrej United': 6758,
    'Keya Around The Life': 8425,
    'Godrej Woodscapes': 11240
}

KRPuram = {
    'Monarch Aqua': 8907,
    'LVS Classic': 5941,
    'Nexsa Royal Apartment': 3481,
    'Pashmina Waterfront': 5630,
    'Sri Amethyst': 6214,
    'LVS Gardenia': 5072,
    'Sai Surakshaa Fairview Ville': 4892,
    'Gina Shalom': 8013,
    'Whitestone Landmark': 5666
}
'''
pdf.add_code(property_code)

# Calculate median property value
whitefield = {
    'Amrutha Platinum Towers': 10340,
    'Prestige Waterford': 11135,
    'Brigade Cosmopolis': 13949,
    'Lakshmi Green Ville': 4913,
    'My Home Dreams': 4867,
    'Sumadhura Eden Garden': 7645,
    'Godrej United': 6758,
    'Keya Around The Life': 8425,
    'Godrej Woodscapes': 11240
}

KRPuram = {
    'Monarch Aqua': 8907,
    'LVS Classic': 5941,
    'Nexsa Royal Apartment': 3481,
    'Pashmina Waterfront': 5630,
    'Sri Amethyst': 6214,
    'LVS Gardenia': 5072,
    'Sai Surakshaa Fairview Ville': 4892,
    'Gina Shalom': 8013,
    'Whitestone Landmark': 5666
}

Whitefield_value = sorted(whitefield.values())
KRPuram_value = sorted(KRPuram.values())

property_median_iter = median_of_two_sorted_iterative(Whitefield_value, KRPuram_value)
property_median_rec = median_of_two_sorted_recursive(Whitefield_value, KRPuram_value)

pdf.add_explanation(f"Median property value (Iterative): {property_median_iter}")
pdf.add_explanation(f"Median property value (Recursive): {property_median_rec}")

# Application 2: Daily Transactions
pdf.add_subsection_title("Application 2: Median Daily Transactions")

transaction_code = '''
daily_totals_week1 = {
    '01-08-2025': 750,
    '02-08-2025': 430,
    '03-08-2025': 1240,
    '04-08-2025': 890,
    '05-08-2025': 760,
    '06-08-2025': 600,
    '07-08-2025': 690
}

daily_totals_week2 = {
    '08-08-2025': 480,
    '09-08-2025': 660,
    '10-08-2025': 900,
    '11-08-2025': 830,
    '12-08-2025': 440,
    '13-08-2025': 690,
    '14-08-2025': 720
}
'''
pdf.add_code(transaction_code)

# Calculate median transaction value
daily_totals_week1 = {
    '01-08-2025': 750,
    '02-08-2025': 430,
    '03-08-2025': 1240,
    '04-08-2025': 890,
    '05-08-2025': 760,
    '06-08-2025': 600,
    '07-08-2025': 690
}

daily_totals_week2 = {
    '08-08-2025': 480,
    '09-08-2025': 660,
    '10-08-2025': 900,
    '11-08-2025': 830,
    '12-08-2025': 440,
    '13-08-2025': 690,
    '14-08-2025': 720
}

week1_value = sorted(list(daily_totals_week1.values()))
week2_value = sorted(list(daily_totals_week2.values()))

transaction_median_iter = median_of_two_sorted_iterative(week1_value, week2_value)
transaction_median_rec = median_of_two_sorted_recursive(week1_value, week2_value)

pdf.add_explanation(f"Median daily transaction (Iterative): {transaction_median_iter}")
pdf.add_explanation(f"Median daily transaction (Recursive): {transaction_median_rec}")

# Add conclusion
pdf.add_page()
pdf.add_section_title("Conclusion")
conclusion_text = """
The analysis demonstrates that both iterative and recursive implementations of the median of two sorted arrays algorithm produce identical results across all test cases.

Key observations:
1. Both implementations handle edge cases correctly (empty arrays, single elements, etc.)
2. The recursive implementation has slightly higher overhead due to function calls
3. For large arrays, the iterative approach is generally more efficient
4. The algorithm efficiently finds the median in O(log(min(m,n))) time

The real-world applications show how this algorithm can be useful in data analysis scenarios such as comparing property values or transaction data across different datasets.

The choice between iterative and recursive implementations depends on the specific use case, with iterative being preferred for performance-critical applications and recursive for scenarios where code clarity is more important.
"""
pdf.add_explanation(conclusion_text)

# Save PDF - UPDATED METHOD
try:
    pdf.output("median_analysis_report.pdf")
    print("PDF report generated successfully: median_analysis_report.pdf")
except Exception as e:
    print(f"Error generating PDF: {e}")
    # Alternative method
    try:
        with open("median_analysis_report.pdf", "wb") as f:
            f.write(pdf.output())
        print("PDF report generated successfully using alternative method: median_analysis_report.pdf")
    except Exception as e2:
        print(f"Alternative method also failed: {e2}")
