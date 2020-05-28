def process_time(f, *args, **kwargs):
    def func(*args, **kwargs):
        import timeit
        start = timeit.default_timer()
        val = f(*args, **kwargs)
        print(f"function time: {timeit.default_timer() - start}")
        return val
    return func


@process_time
def firstNonrepeat(char):
    common = list()
    unique = list()
    for letter in char:
        if letter in common:  # check if the letter is already repeating
            continue  # return to loop if the letter is already repeating
        elif letter in unique:  # check if clash with previous uniques
            unique.remove(letter)  # if so, remove from unique & add to common
            common.append(letter)
        else:
            unique.append(letter)  # if letter is unique then add to list
    return unique[0]  # return the first unique letter in a string


@process_time
def alternative_FNP(char):
    freq_dict = dict()
    for letter in char:
        freq_dict[letter] = char.count(letter)
    for k, v in freq_dict.items():
        if v == 1:
            return k


@process_time
def alternative_FNP_set(char):  # winner
    freq_dict = dict()
    for letter in set(char):
        freq_dict[letter] = char.count(letter)
    for letter in char:
        if freq_dict[letter] == 1:
            return letter


char = ('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris sitme'
        'augue in augue molestie euismod vitae vitae sem.'
        'Mauris placerat fringilla varius. Etiam vel iaculis sem.'
        'Cras auctor mi in ipsum malesuada posuere sed nec dui. Nullam'
        'volutpat tempor nunc, nec ultrices ligula. Praesent pharetra urna lac'
        'a commodo quam vestibulum et. Nunc neque dolor, tincidunt at nisl eu,'
        'ornare pharetra magna. Aliquamfeugiat nisl ipsum, pharetra suscipitel'
        'cursus sit amet. Nullam facilisis vivamus')


char = char.replace(' ', '')
char = char.replace(',', '')
char = char.replace('.', '')
char = char.lower()

x = firstNonrepeat(char)
y = alternative_FNP(char)
z = alternative_FNP_set(char)
print(x, y, z)
