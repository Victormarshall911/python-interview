import re
import psycopg2
import random
from collections import Counter
import statistics

# Using HTML table

data = {
    "Monday": "GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, BLUE, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN",
    "Tuesday": "ARSH, BROWN, GREEN, BROWN, BLUE, BLEW, PINK, PINK, ORANGE, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE",
    "Wednesday": "GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, RED, YELLOW, ORANGE, RED, ORANGE, RED, BLUE, BLUE, WHITE, BLUE, BLUE, WHITE",
    "Thursday": "BLUE, BLUE, GREEN, WHITE, BLUE, BROWN, PINK, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN",
    "Friday": "GREEN, WHITE, GREEN, BROWN, BLUE, BLUE, BLACK, WHITE, ORANGE, RED, RED, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, WHITE"
}

normalized_colors = []
for day, colors in data.items():
    colors_list = [color.strip().upper().replace('BLEW', 'BLUE').replace('ARSH', 'ASH') for color in colors.split(',')]
    normalized_colors.extend(colors_list)

color_counts = Counter(normalized_colors)
total_colors = sum(color_counts.values())
mean_value = statistics.mean(color_counts.values())
mean_color = min(color_counts, key=lambda c: abs(color_counts[c] - mean_value))
most_worn_color = color_counts.most_common(1)[0][0]
sorted_counts = sorted(color_counts.items(), key=lambda x: x[1])
median_color = sorted_counts[len(sorted_counts) // 2][0]

# Bonus

variance = statistics.variance(color_counts.values())
prob_red = color_counts['RED'] / total_colors

print("Color Frequency Table:")
for color, freq in color_counts.items():
    print(f"{color}: {freq}")

print("\n1. Mean color:", mean_color)
print("2. Most worn color:", most_worn_color)
print("3. Median color:", median_color)
print("4. Variance of colors:", variance)
print(f"5. Probability of RED: {prob_red:.2f}")

try:
    connection = psycopg2.connect(
        host="localhost",
        database="bincomdb",
        user="postgres",
        password="itswell77"
    )
    cursor = connection.cursor()
    cursor.execute("DROP TABLE IF EXISTS color_frequency")
    cursor.execute("""
        CREATE TABLE color_frequency (
            color VARCHAR(50),
            frequency INT
        )
    """)
    for color, freq in color_counts.items():
        cursor.execute("INSERT INTO color_frequency (color, frequency) VALUES (%s, %s)", (color, freq))
    connection.commit()
    print("\n Data saved to PostgreSQL successfully.")
except Exception as e:
    print("\n Could not connect to PostgreSQL:", e)
finally:
    if 'connection' in locals():
        cursor.close()
        connection.close()


def recursive_search(arr, target, index=0):
    if index >= len(arr):
        return False
    if arr[index] == target:
        return True
    return recursive_search(arr, target, index + 1)

nums = [1, 5, 9, 12, 15, 20]
target = int(input("\nEnter a number to search: "))
print("Found!" if recursive_search(nums, target) else "Not Found!")

binary = ''.join(random.choice('01') for _ in range(4))
decimal = int(binary, 2)
print(f"\nGenerated Binary: {binary}, Base-10: {decimal}")

def fibonacci(n):
    a, b = 0, 1
    seq = []
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
    return seq

fib_seq = fibonacci(50)
fib_sum = sum(fib_seq)
print("\nSum of first 50 Fibonacci numbers:", fib_sum)
