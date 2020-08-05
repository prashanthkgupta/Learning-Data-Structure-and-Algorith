def generate_all_possible_strings(n, k=2, s=''):
    if n == 0:
        print(s)
    else:
        for i in range(k):
            generate_all_possible_strings(n - 1, k, s + str(i))


# here I am printing only how can I return value here
def generate_all_possible_strings_book():
    pass


generate_all_possible_strings(3)
