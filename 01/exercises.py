# Exercicio 01
def max_consecutive_sum(nums):
    soma_total = float('-inf')
    
    soma = 0
    for num in nums:
        soma = max(num, soma + num) 
        soma_total = max(soma_total, soma) 
    
    return soma_total

# Testes 01
def test_max_consecutive_sum():
    print(max_consecutive_sum([1, -3, 2, 1, -1]) == 3)
    print(max_consecutive_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6)
    print(max_consecutive_sum([5, -1, -2, 3, -1, 2, -4]) == 7)
    print(max_consecutive_sum([1]) == 1)
    print(max_consecutive_sum([-1, -2, -3, -4, -5]) == -1)


# Exercício 02
def is_palindrome(word):
    word = word.replace(" ", "").lower()
    return word == word[::-1]

# Testes 02
def text_is_palindrome():
    print(is_palindrome("radar") == True)
    print(is_palindrome("racecar") == True)
    print(is_palindrome("level") == True)
    # Testes negativos
    print(is_palindrome("python") == False)
    print(is_palindrome("hello") == False)
    print(is_palindrome("12321") == False)
    print(is_palindrome("abccbaa") == False)


# Exercício 03
def count_increasing_subsets(nums):
    def count_subsets_recursive(index, prev_num):
        if index == len(nums):
            return 1  
        
        count_with_current = 0
        if nums[index] > prev_num:
            count_with_current = count_subsets_recursive(index + 1, nums[index])
        
        count_without_current = count_subsets_recursive(index + 1, prev_num)
        
        return count_with_current + count_without_current
    
    return count_subsets_recursive(0, float('-inf'))

# Testes 03
def test_count_increasing_subsets():
    # Teste com lista vazia
    print(count_increasing_subsets([]) == 0)
    # Teste com uma lista de um elemento
    print(count_increasing_subsets([1]) == 1)
    # Teste com uma lista de números aleatórios
    print(count_increasing_subsets([1, 3, 2, 4]) == 8)
    # Teste com uma lista de números ordenados
    print(count_increasing_subsets([1, 2, 3, 4, 5]) == 31)
    # Teste com uma lista de números em ordem decrescente
    print(count_increasing_subsets([5, 4, 3, 2, 1]) == 0)
    # Teste com uma lista contendo números repetidos
    print(count_increasing_subsets([1, 2, 2, 3, 3, 3, 4]) == 16)


# Run the tests
if __name__ == "__main__":
    test_max_consecutive_sum()
    text_is_palindrome()
    test_count_increasing_subsets()
