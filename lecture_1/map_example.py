def return_with_ending_a(s):
    return s + 'a'


lst_of_strs = ['af', 'bae', 'cre', 'd', 'e', 'f', 'g']

# Option A
# for s in lst_of_strs:
#     print_with_ending_a(s)

# Option B
print(map(return_with_ending_a, lst_of_strs))


# Filter:
def is_even(x):
    if x % 2 == 0:
        return True
    return False


lst = [i for i in range(1, 11)]
lst_of_evens=list(filter(is_even,lst))
print(lst,lst_of_evens)
