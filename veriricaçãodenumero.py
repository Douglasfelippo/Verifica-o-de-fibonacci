def is_fibonacci_number(n):
    def is_perfect_square(x):
        s = int(x**0.5)
        return s*s == x
    
    return is_perfect_square(5*n*n + 4) or is_perfect_square(5*n*n - 4)

def fibonacci_sequence_up_to_n(n):
    sequence = [0, 1]
    while sequence[-1] < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

def main():
    num = int(input("Informe um número: "))
    
    sequence = fibonacci_sequence_up_to_n(num)
    
    if is_fibonacci_number(num):
        print(f"O número {num} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {num} NÃO pertence à sequência de Fibonacci.")
    
    print(f"Sequência de Fibonacci até {num}: {sequence}")

if __name__ == "__main__":
    main()
