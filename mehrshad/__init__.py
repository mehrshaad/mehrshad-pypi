import os
import turtle
from collections import Counter
from math import factorial, gcd, sqrt

from tqdm import tqdm  # progress feature in loops


def Binomial_Theorem(power: int, print_input: bool = False, print_output: bool = False, return_str: bool = False, sup_power: bool = True, sign: str = ' + ', alphas=['x', 'y']):
    """This Function is Used For Getting Binomial Theorem:
       Example: (x+y)² = x² + 2xy + y²

    Args:
        power (int) -> Power of Binomial Theorem
        print_input (bool, optional) -> If you set this true you'll see binomial theorem with power before anything. Defaults to False.
        print_output (bool, optional) -> This optional bool will prints output if you make it true. Defaults to False.
        return_str (bool, optional) -> By setting this option to true you will. Defaults to False.
        sup_power (bool, optional) -> This option is used for making the power of output list, like you write on paper! Defaults to True.
        sign (str, optional) -> This is the sign that takes place between the output elements (this item works if return_str is True). Defaults to ' + '.
        alphas (list/tuple/set, optional) -> You can change the 2 alphas that used for output elements (this item must've 2 characters otherwise it'll give error). Defaults to ['x', 'y'].

    Returns:
        str -> If return_str sets to True you'll get str instead a list.
        list -> By the default setting of function you'll get a list of output elements.
    """
    try:
        if print_input:  # printing (x+y)^power
            if sup_power:
                print(f'({alphas[0]}+{alphas[1]}){Number_to_Power(power)}')
            else:
                print(f'({alphas[0]}+{alphas[1]})^{power}')
        output = []  # an empty list that we place the output things in it

        for k in range(power+1):  # adding all elements to output list
            C = Combination(power, k)
            if sup_power:
                # making number power like (some os's might not support)
                NP1 = Number_to_Power(k)
                NP2 = Number_to_Power(power-k)
            else:
                NP1 = f'^{k}'
                NP2 = f'^{power-k}'
            if C == 1:  # if the multilayer equals 1 don't showing it
                C = ''

            if k == 0:
                output.append(f'{C}{alphas[1]}{NP2}')
            elif power-k == 0:
                output.append(f'{C}{alphas[0]}{NP1}')
            else:
                if (NP1 == '¹' and NP2 == '¹') or (NP1 == '^1' and NP2 == '^1'):
                    output.append(f'{C}{alphas[0]}{alphas[1]}')
                elif NP1 == '¹' or NP1 == '^1':
                    output.append(f'{C}{alphas[0]}{alphas[1]}{NP2}')
                elif NP2 == '¹' or NP2 == '^1':
                    output.append(f'{C}{alphas[0]}{NP1}{alphas[1]}')
                else:
                    output.append(f'{C}{alphas[0]}{NP1}{alphas[1]}{NP2}')

        # reversing the final output list because it's not like what we've seen in books!
        output.reverse()
        if print_output:
            print(sign.join(output))

        if return_str:
            return sign.join(output)
        return output
    except:
        return 'error!'


def Combination(n: int, r: int):
    """Tarkib! :)"""
    if r > n:
        raise ValueError('Wrong Input!')
    return factorial(n) // (factorial(r) * factorial(n - r))


def Complement_0_1(String_0_1: str):
    """This Function Can Be Used For Complement of a Binary Number (Motamam Adad)"""
    Result = ''
    for i in String_0_1:
        if str(i) == '0':
            Result += '1'
        elif str(i) == '1':
            Result += '0'
    return Result


def BaseN_to_10(num: str, base: int):
    """This Function Can Be Used For Converting The Base of a Number
       to 10 (Taghir base b 10)"""
    return int(num, base)


def Base10_to_N(num: int, base: int, numerals: str = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    return ((num == 0) and numerals[0]) or (Base10_to_N(num // base, base, numerals).lstrip(numerals[0]) + numerals[num % base])


def Count_Digit(number):
    """This Function is Used For Counting Digits"""
    return len(str(number))


def createTxt(text, address: str = '.', fileName: str = 'Text', clearTxt: bool = True):
    """Used For Creating a .txt file in your address"""
    try:
        with open(f'{address}\{fileName}.txt', 'a+') as file:
            if clearTxt:
                file.truncate(0)
            file.write(str(text))
    except FileNotFoundError:
        os.makedirs(address)
        createTxt(text, address, fileName, clearTxt)


def Diamond_Pattern(Number_of_Rows):
    """For Creating Diamond Patterns Built From ' * '"""

    def Star_Shapes(Num):
        return '*' * Num

    DP1 = 1
    DP2 = Number_of_Rows / 2
    DP3 = int(DP2) - 1
    for iDP in range(1, Number_of_Rows + 1):
        if iDP < DP2:
            print(" " * DP3, Star_Shapes(DP1))
            DP1 += 2
            DP3 -= 1
        elif iDP == (DP2 + 0.5):
            print(Star_Shapes(Number_of_Rows))
            DP1 = DP1 - 2
            DP3 = 0
        else:
            print(" " * DP3, Star_Shapes(DP1))
            DP1 = DP1 - 2
            DP3 += 1


def Divisor_Counter(number):
    cnt = 0
    for i in range(1, (int)(sqrt(number)) + 1):
        if (number % i == 0):
            if (number / i == i):
                cnt = cnt + 1
            else:
                cnt = cnt + 2
    return cnt


def Divisor_Sigma(number: int):
    SumDS = number
    for iDC in range(1, number // 2 + 1):
        if number % iDC == 0:
            SumDS += iDC
    return SumDS


def Divisors(number: int):
    Divisors_List = []
    for iDL in range(1, number // 2 + 1):
        if number % iDL == 0:
            Divisors_List.append(iDL)
    Divisors_List.append(number)
    return Divisors_List


def Draw_Shape_Turtle(sides, length, Done=False):
    if sides >= 3:
        angle = 360.0 / sides
        for sides in range(sides):
            turtle.forward(length)
            turtle.left(angle)
        if Done:
            turtle.done()
    else:
        return "Slides Should be >= 3!"


def Factorial(number):
    if number == 0:
        return 1
    if number > 0:
        SUMf = 1
        for iF in range(1, number + 1):
            SUMf *= iF
        return SUMf
    else:
        return "Wrong Number!"


def Fibonacci_Sequence(number):
    v1, v2, v3 = 1, 1, 0  # initialise a matrix [[1,1],[1,0]]
    # perform fast exponentiation of the matrix (quickly raise it to the nth power)
    for rec in bin(number)[3:]:
        calc = v2 * v2
        v1, v2, v3 = v1 * v1 + calc, (v1 + v3) * v2, calc + v3 * v3
        if rec == '1':
            v1, v2, v3 = v1 + v2, v1, v2
    return v2


def GCD_of_List(List):
    counter_g = 1
    temp_g = List[0]
    while counter_g != len(List):
        temp_g = gcd(temp_g, List[counter_g])
        if temp_g == 1:
            return 1
        else:
            counter_g = counter_g + 1
    return temp_g


def Hanoi_Tower(num_of_moves, source, destination, temp):
    if num_of_moves == 1:
        print('Move Disk %d From %s to %s' %
              (num_of_moves, source, destination))
    else:
        Hanoi_Tower(num_of_moves - 1, source, temp, destination)
        print('Move Disk %d From %s to %s' %
              (num_of_moves, source, destination))
        Hanoi_Tower(num_of_moves - 1, temp, destination, source)


def is_Sum_of_Digit_Power(number, power):
    SumDP = 0
    mioDP = abs(number)
    while mioDP > 0:
        SumDP += (mioDP % 10) ** power
        mioDP //= 10
    if int(SumDP) == int(abs(number)):
        return True
    else:
        return False


def isComplete(number):
    SumiC = 0
    for iIc in range(1, number // 2 + 1):
        if number % iIc == 0:
            SumiC += iIc
    if SumiC == number:
        return True
    return False


def isEqual_to_Dingit_Factorial(number):
    if number >= 0:
        def F(number):
            if number == 0:
                return 1
            if number > 0:
                SUMf = 1
                for iF in range(1, number + 1):
                    SUMf *= iF
                return SUMf

        SumitDF = 0
        number = str(number)
        for i in number:
            SumitDF += F(int(i))
        if SumitDF == int(number):
            return True
        else:
            return False
    else:
        return 'Wrong Number!'


def isPalindrom(string):
    return str(string) == str(string)[::-1]


def isPrime(number):
    if number >= 2:
        prime_list = []
        for num in range(2, round(sqrt(number)) + 1):
            prime_flag = True
            for prime_item in prime_list:
                if num % prime_item == 0:
                    prime_flag = False
                    break
            if prime_flag:
                prime_list.append(num)
        for prime_item in prime_list:
            if number % prime_item == 0:
                return False
        return True
    if number == 1:
        return False
    return 'Number Most Be Bigger Than 0!'


def LCM_of_List(List):
    return Multiply_of_List(List) // GCD_of_List(List)


def Magic_Square_Generator(row_column: int, only_sum=False):
    if only_sum:
        return row_column * (row_column * row_column + 1) / 2
    MagicSquare = [[0 for x in range(row_column)] for y in range(row_column)]
    i = row_column / 2
    j = row_column - 1
    num = 1
    while num <= (row_column * row_column):
        if i == -1 and j == row_column:
            j = row_column - 2
            i = 0
        else:
            if j == row_column:
                j = 0
            if i < 0:
                i = row_column - 1
        if MagicSquare[int(i)][int(j)]:
            j = j - 2
            i = i + 1
            continue
        else:
            MagicSquare[int(i)][int(j)] = num
            num = num + 1
        j = j + 1
        i = i - 1
    return MagicSquare


def Mex_of_List(List: list, Return=list):
    mex = [counter for counter in range(1, max(List)) if counter not in List]
    if mex == []:
        return 'there is no mex!'
    try:
        return Return(mex)
    except:
        return "'Return' value error"


def Min_Step_To_Target_Elephant_Chess(first_pos: list, target_pos: list, board: int):
    """this function returns minimum step to reach target position
    in chess elephant piece.

    Arguments:
        first_pos (list) -> first position of elephant.
        target_pos (list) -> target position of elephant.
        board (int) -> chess board width and column.

    Returns:
        int -> returns the minimum step of elephant to reach target in board.
    """
    class cell:
        """Python3 code to find minimum steps to reach
        to specific cell in minimum moves by Knight"""

        def __init__(self, x=0, y=0, dist=0):
            self.x = x
            self.y = y
            self.dist = dist

    def isInside(x, y, board):
        """checks whether given position is
        inside the board"""
        if x >= 1 and x <= board and y >= 1 and y <= board:
            return True
        return False
    # all possible moves for the elephant
    dx = [2, 2, -2, -2, 1, 1, -1, -1]
    dy = [1, -1, 1, -1, 2, -2, 2, -2]
    queue = []
    # push starting position of elephant
    # with 0 distance
    queue.append(cell(first_pos[0], first_pos[1], 0))
    # make all cell unvisited
    visited = [[False for i in range(board + 1)] for j in range(board + 1)]
    # visit starting state
    visited[first_pos[0]][first_pos[1]] = True
    # loop until we have one element in queue
    while(len(queue) > 0):
        t = queue[0]
        queue.pop(0)
        # if current cell is equal to target
        # cell, return its distance
        if(t.x == target_pos[0] and
           t.y == target_pos[1]):
            return t.dist
        # iterate for all reachable states
        for i in range(8):
            x = t.x + dx[i]
            y = t.y + dy[i]
            if(isInside(x, y, board) and not visited[x][y]):
                visited[x][y] = True
                queue.append(cell(x, y, t.dist + 1))


def Multiply_of_List(List):
    ans_M = 1
    for items_of_list in List:
        if type(items_of_list) == List:
            Multiply_of_List(items_of_list)
        try:
            ans_M *= int(items_of_list)
        except:
            continue
    return ans_M


def Next_Bigger_Number_With_Same_Digits(number):
    numlist = [int(i) for i in str(number)]

    index_of_replace_num = -1
    i = len(numlist) - 1
    while i > 0:
        if numlist[i] > numlist[i - 1]:
            index_of_replace_num = i - 1
            break
        i -= 1

    if index_of_replace_num == -1:
        return 0
    else:
        firstlist = numlist[:index_of_replace_num]
        replaced_num = numlist[index_of_replace_num]
        secondlist = numlist[index_of_replace_num + 1:]
        new_replaced_num = 9
        i = 0
        delindex = 0
        while i < len(secondlist):
            if replaced_num < secondlist[i] < new_replaced_num:
                new_replaced_num = secondlist[i]
                delindex = i
            i += 1

        secondlist.pop(delindex)
        secondlist.append(replaced_num)
        firstlist.append(new_replaced_num)
        output = firstlist + sorted(secondlist)
        return int(''.join(str(x) for x in output))


def Num_to_Weekday(num, first_day="Saturday", all_week_days=False):
    first_day = first_day[0].upper() + first_day[1:].lower()
    week_days = ["Saturday", "Sunday", "Monday",
                 "Tuesday", "Wednesday", "Thursday", "Friday"]
    if not first_day in week_days:
        return "Please Choose a Correct first_day!"
    while week_days[0] != first_day:
        week_days.insert(0, week_days[-1])
        del week_days[-1]
    if all_week_days:
        return week_days
    return week_days[num % len(week_days)]


def Number_to_Power(number):
    def to_Power_1_10(number):
        if number == 0:
            return '⁰'
        if number == 1:
            return '¹'
        if number == 2:
            return '²'
        if number == 3:
            return '³'
        if number == 4:
            return '⁴'
        if number == 5:
            return '⁵'
        if number == 6:
            return '⁶'
        if number == 7:
            return '⁷'
        if number == 8:
            return '⁸'
        if number == 9:
            return '⁹'

    NP = []
    while number > 0:
        NP.append(to_Power_1_10(number % 10))
        number //= 10
    NP.reverse()
    NP = ''.join(NP)
    return NP


def Permutation(n, r):
    if r > n:
        return 'Wrong Input!'

    def F(number):
        if number == 0:
            return 1
        if number > 0:
            SUMf = 1
            for iF in range(2, number + 1):
                SUMf *= iF
            return SUMf

    return F(n) // (F(n - r))


def Permutation_Print(lst: list):
    if len(lst) == 1:
        return [lst]
    return_list = []
    for element in lst:
        temp = [var for var in lst if var != element]
        for t in Permutation_Print(temp):
            return_list.append([element] + t)
    return return_list


def Prime_Factors_List(number):
    listPF = []
    iPF = 1
    while iPF <= number:
        kPF = 0
        if number % iPF == 0:
            jPF = 1
            while jPF <= iPF:
                if iPF % jPF == 0:
                    kPF = kPF + 1
                jPF = jPF + 1
            if kPF == 2:
                listPF.append(iPF)
        iPF = iPF + 1
    return listPF


def Prime_Roots_With_Power_List(number):
    def Number_to_Power(number):
        def to_Power_1_10(number):
            if number == 0:
                return '⁰'
            if number == 1:
                return '¹'
            if number == 2:
                return '²'
            if number == 3:
                return '³'
            if number == 4:
                return '⁴'
            if number == 5:
                return '⁵'
            if number == 6:
                return '⁶'
            if number == 7:
                return '⁷'
            if number == 8:
                return '⁸'
            if number == 9:
                return '⁹'

        NP = []
        while number > 0:
            NP.append(to_Power_1_10(number % 10))
            number //= 10
        NP.reverse()
        NP = ''.join(NP)
        return NP

    def def1(D1, D2):
        isP = [False] * (D1 + 1)
        for iD1 in range(2, D1 + 1, 2):
            D2[iD1] = 2
        for iD1 in range(3, D1 + 1, 2):
            if not isP[iD1]:
                D2[iD1] = iD1
                for j in range(iD1, int(D1 / iD1) + 1, 2):
                    if not isP[iD1 * j]:
                        isP[iD1 * j] = True
                        D2[iD1 * j] = iD1

    SA = [0] * (number + 1)
    ListNR = []
    def1(number, SA)
    NUM = SA[number]
    POW = 1
    while number > 1:
        number //= SA[number]
        if NUM == SA[number]:
            POW += 1
            continue
        POW = Number_to_Power(POW)
        ListNR.append(str(NUM) + str(POW))
        NUM = SA[number]
        POW = 1
    ListNR = ' × '.join(ListNR)
    return ListNR


def Primes_Before_List(number):
    if number >= 1:
        prime_list = []
        for num in range(2, number):
            prime_flag = True
            for prime_item in prime_list:
                if num % prime_item == 0:
                    prime_flag = False
                    break
            if prime_flag:
                prime_list.append(num)
        if len(prime_list) == 0:
            return 'None'
        return prime_list
    return 'Number Must Be >= 1!'


def Reverse_Number(number):
    reverse = 0
    while number > 0:
        digit = number % 10
        reverse = reverse * 10 + digit
        number = number // 10
    return reverse


def Sequence_of_Triangle(number: int):
    """this sequence is like: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

    Arguments:
        number (int) -> limit of your wanted members in sequence of triangle.

    Returns:
        generator -> all numbers in sequence in range of your entered number.
    """
    List_Seq = 1
    while List_Seq <= number:
        yield sum(range(List_Seq + 1))
        List_Seq += 1


def Sudoku_Solver(num_list_9x9: list, blank: str = '0'):
    """this function is used for solving a 9x9 sudoku table.

    Arguments:
        num_list_9x9 (list) -> the 9x9 table of sudoku.

    Keyword Arguments:
        blank (str) -> the element that you want to use for blanked spaces. (default: {'0'})

    Returns:
        list -> if everything goes well you'll get your 9x9 sudoku table solved in 2D list.
        str -> if something goes wrong it returns 'error'.
    """
    try:
        for i in range(len(num_list_9x9)):
            for j in range(len(num_list_9x9[i])):
                try:
                    num_list_9x9[i][j] = str(num_list_9x9[i][j])
                except:
                    continue
        lns = {}
        rgns = {
            'rgn1': ['ln1 0', 'ln1 1', 'ln1 2', 'ln2 0', 'ln2 1', 'ln2 2', 'ln3 0', 'ln3 1', 'ln3 2'],
            'rgn2': ['ln1 3', 'ln1 4', 'ln1 5', 'ln2 3', 'ln2 4', 'ln2 5', 'ln3 3', 'ln3 4', 'ln3 5'],
            'rgn3': ['ln1 6', 'ln1 7', 'ln1 8', 'ln2 6', 'ln2 7', 'ln2 8', 'ln3 6', 'ln3 7', 'ln3 8'],
            'rgn4': ['ln4 0', 'ln4 1', 'ln4 2', 'ln5 0', 'ln5 1', 'ln5 2', 'ln6 0', 'ln6 1', 'ln6 2'],
            'rgn5': ['ln4 3', 'ln4 4', 'ln4 5', 'ln5 3', 'ln5 4', 'ln5 5', 'ln6 3', 'ln6 4', 'ln6 5'],
            'rgn6': ['ln4 6', 'ln4 7', 'ln4 8', 'ln5 6', 'ln5 7', 'ln5 8', 'ln6 6', 'ln6 7', 'ln6 8'],
            'rgn7': ['ln7 0', 'ln7 1', 'ln7 2', 'ln8 0', 'ln8 1', 'ln8 2', 'ln9 0', 'ln9 1', 'ln9 2'],
            'rgn8': ['ln7 3', 'ln7 4', 'ln7 5', 'ln8 3', 'ln8 4', 'ln8 5', 'ln9 3', 'ln9 4', 'ln9 5'],
            'rgn9': ['ln7 6', 'ln7 7', 'ln7 8', 'ln8 6', 'ln8 7', 'ln8 8', 'ln9 6', 'ln9 7', 'ln9 8']
        }
        for i in range(9):
            lns["ln" + str(len(lns)+1)] = num_list_9x9[i]

        def locate_vars(lst, item):
            return [i for i, x in enumerate(lst) if x == item]

        locs = [ln + " " + str(item)
                for ln in lns for item in locate_vars(lns[ln], blank)]
        possible_nums = {loc: ['1', '2', '3', '4',
                               '5', '6', '7', '8', '9'] for loc in locs}

        def naked_single(loc):
            ln_of_loc = loc.split()[0]
            col_of_loc = loc.split()[1]

            temp_list_1 = [lns[ln][int(col_of_loc)] for ln in lns]
            temp_list_2 = temp_list_1 + lns[ln_of_loc]
            for rgn in rgns:
                if loc in rgns[rgn]:
                    for item in rgns[rgn]:
                        temp_list_2.append(
                            lns[item.split()[0]][int(item.split()[1])])

            impossible_nums = list(dict.fromkeys(temp_list_2))
            impossible_nums.remove(blank)
            for item in impossible_nums:
                while item in possible_nums[loc]:
                    possible_nums[loc].remove(item)

        def hidden_single(loc):
            locs_of_the_vars_of_the_same_ln = [
                item for item in locs if item.split()[0] == loc.split()[0] and item != loc]
            locs_of_the_vars_of_the_same_col = [
                item for item in locs if item.split()[1] == loc.split()[1] and item != loc]
            for rgn in rgns:
                if loc in rgns[rgn]:
                    locs_of_the_vars_of_the_same_rgn = [
                        item for item in rgns[rgn] if item in locs and item != loc]

            possible_nums_of_the_vars_of_the_same_ln = [
                item2 for item1 in locs_of_the_vars_of_the_same_ln for item2 in possible_nums[item1]]
            possible_nums_of_the_vars_of_the_same_col = [
                item2 for item1 in locs_of_the_vars_of_the_same_col for item2 in possible_nums[item1]]
            possible_nums_of_the_vars_of_the_same_rgn = [
                item2 for item1 in locs_of_the_vars_of_the_same_rgn for item2 in possible_nums[item1]]

            temps = {
                'possible_nums_1': [item for item in possible_nums[loc] if not item in possible_nums_of_the_vars_of_the_same_ln],
                'possible_nums_2': [item for item in possible_nums[loc] if not item in possible_nums_of_the_vars_of_the_same_col],
                'possible_nums_3': [item for item in possible_nums[loc] if not item in possible_nums_of_the_vars_of_the_same_rgn]
            }

            for item1 in temps:
                if len(temps[item1]) == 1:
                    possible_nums[loc] = [temps[item1][0]]

        def naked_pairs(loc):
            impossible_nums = []
            categories = {
                'locs_of_the_vars_of_the_same_ln': [item for item in locs if item.split()[0] == loc.split()[0] and item != loc],
                'locs_of_the_vars_of_the_same_col': [item for item in locs if item.split()[1] == loc.split()[1] and item != loc],
                'locs_of_the_vars_of_the_same_rgn': []
            }
            for rgn in rgns:
                if loc in rgns[rgn]:
                    categories['locs_of_the_vars_of_the_same_rgn'] = [
                        item for item in rgns[rgn] if item in locs and item != loc]
            for item1 in categories:
                temp = categories[item1]
                for item2 in temp:
                    for item3 in temp:
                        if item2 != item3:
                            if possible_nums[item2] == possible_nums[item3] and len(possible_nums[item2]) == 2:
                                for num in possible_nums[item2]:
                                    while num in possible_nums[loc]:
                                        possible_nums[loc].remove(num)

        def hidden_pairs(loc):
            categories = {
                'locs_of_the_vars_of_the_same_ln': [item for item in locs if item.split()[0] == loc.split()[0] and item != loc],
                'locs_of_the_vars_of_the_same_col': [item for item in locs if item.split()[1] == loc.split()[1] and item != loc],
                'locs_of_the_vars_of_the_same_rgn': []
            }
            for rgn in rgns:
                if loc in rgns[rgn]:
                    categories['locs_of_the_vars_of_the_same_rgn'] = [
                        item for item in rgns[rgn] if item in locs and item != loc]
            for item1 in categories:
                if len(categories[item1]) != 0:
                    possible_nums_of_the_vars_of_the_same_neighborhood = [
                        item for location in categories[item1] for item in possible_nums[location]]
                    frequencies_of_the_possible_nums_of_the_vars_of_the_same_neighborhood = dict(
                        Counter(possible_nums_of_the_vars_of_the_same_neighborhood))
                    for item2 in categories[item1]:
                        num_of_duplicates = len(possible_nums[loc] + possible_nums[item2]) - len(
                            list(dict.fromkeys(possible_nums[loc] + possible_nums[item2])))
                        temp_dict = dict(
                            Counter(possible_nums[loc] + possible_nums[item2]))
                        if num_of_duplicates == 2:
                            nums_held_in_common = [
                                item for item in temp_dict if temp_dict[item] == 2]
                            temp_list = [
                                item for item in nums_held_in_common if frequencies_of_the_possible_nums_of_the_vars_of_the_same_neighborhood[item] == 1]
                            if len(temp_list) == 2:
                                for item3 in possible_nums[loc] + possible_nums[item2]:
                                    if not item3 in temp_list:
                                        while item3 in possible_nums[loc]:
                                            possible_nums[loc].remove(item3)
                                        while item3 in possible_nums[item2]:
                                            possible_nums[item2].remove(item3)

        def naked_triples(loc):
            impossible_nums = []
            categories = {
                'locs_of_the_vars_of_the_same_ln': [item for item in locs if item.split()[0] == loc.split()[0] and item != loc],
                'locs_of_the_vars_of_the_same_col': [item for item in locs if item.split()[1] == loc.split()[1] and item != loc],
                'locs_of_the_vars_of_the_same_rgn': []
            }
            for rgn in rgns:
                if loc in rgns[rgn]:
                    categories['locs_of_the_vars_of_the_same_rgn'] = [
                        item for item in rgns[rgn] if item in locs and item != loc]
            for item1 in categories:
                temp = categories[item1]
                for item2 in temp:
                    for item3 in temp:
                        for item4 in temp:
                            if item2 != item3 and item2 != item4 and item3 != item4:
                                if len(possible_nums[item2]) == 2 and len(possible_nums[item3]) == 2 and len(possible_nums[item4]) == 2:
                                    temp_2 = possible_nums[item2] + \
                                        possible_nums[item3] + \
                                        possible_nums[item4]
                                    if len(temp_2) - len(list(dict.fromkeys(temp_2))) == 3:
                                        for item5 in list(dict.fromkeys(temp_2)):
                                            impossible_nums.append(item5)
                                elif possible_nums[item2] == possible_nums[item3] and possible_nums[item2] == possible_nums[item4] and len(possible_nums[item2]) == 3:
                                    for nums in possible_nums[item2]:
                                        impossible_nums.append(nums)
            for item in impossible_nums:
                while item in possible_nums[loc]:
                    possible_nums[loc].remove(item)

        lst = []
        while len(locs) != 0:
            for loc in locs:
                naked_single(loc)
                hidden_single(loc)
                naked_pairs(loc)
                hidden_pairs(loc)
                naked_triples(loc)
                if len(possible_nums[loc]) == 1:
                    lns[loc.split()[0]][int(loc.split()[1])
                                        ] = possible_nums[loc][0]
                    locs.remove(loc)
                    for ln in lns:
                        lst.append(lns[ln])
        return lst[-9:]
    except:
        return 'error'


def Sum_of_Digit(number):
    SumD = 0
    for iSD in str(number):
        SumD += int(iSD)
    return SumD


def Weekday_to_Num(weekday, first_day='saturday'):
    first_day = first_day.lower()
    week_days = ['saturday', 'sunday', 'monday',
                 'tuesday', 'wednesday', 'thursday', 'friday']
    try:
        if not first_day in week_days:
            return "Please Choose a Correct first_day!"
        while week_days[0] != first_day:
            week_days.insert(0, week_days[-1])
            del week_days[-1]
        tempWN = weekday.lower()
        return week_days.index(tempWN) + 1
    except:
        return 'Wrong Entered Weekday!'
