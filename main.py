'''
Solve 2 specific types of dynamic programming problems
1. prompt user for type of problem to be solved - X
2. prompt user for dimensions of problem - X
3. prompt user for function values. Save in array - X
4. Calculate and display returns and decisions - X
5. Calculate and display optimal return and decisions - O
6. Give opportunity to run program again - O
'''

# Custom error class to handle incorrect number of column
#  inputs when retrieving values from user
class IncorrectColumnEntriesError(Exception):
    '''Raised when value is too small or large'''
    pass;

# Make it easier to view matrix as rows and coumns
def pretty_print(matrix):
    result = '\t';
    for i in range(len(matrix[0])):
        result += str(i) + '\t';
    result += '\n';
    for i in range(len(matrix)):
        result += '\n' + str(i) + '\t';
        for j in range(len(matrix[0])):
            result += str(matrix[i][j]) + '\t';
        result += '\n';
    print('\n', result);

def print_return_table(m_matrix, d_matrix):
    result = '\t\t';
    for i in range(len(m_matrix[0])):
        result += str(i) + '\t';
    result += '\n';
    for i in reversed(range(len(m_matrix))):
        result += '\n' + str(i) + '\tm_' + str(i) + '\t';
        for j in range(len(m_matrix[0])):
            result += str(m_matrix[i][j]) + '\t';
        result += '\n\td_' + str(i) + '\t';
        for j in range(len(m_matrix[0])):
            result += str(d_matrix[i][j]) + '\t';
        result += '\n';
    print('\n', result);

# Get user input to determine what type of problem
# we're going to be solving
def get_problem_type():
    try:
        return int(input('\nPlease Enter 0 for dynamic programming problem or 1 for stochastic dynamic programming problem: '));
    except:
        print("\nInvalid problem #");
        return -1;

# Get user input to determine number of companies
# and units of weight
# Then have user enter weight of product of companies
# and shipping cost of product
def get_dimensions():
    try:
        num_companies = int(input('\nEnter number of companies: '));
        money = int(input('\nEnter number of units of weight are available: '));
        weight_table = init_array(num_companies, 2);
        function_table = init_array(num_companies, money + 1);
        for i in range(len(weight_table)):
            print('\nEnter weight of product ' + str(i + 1) + ':', end = ' ');
            weight_table[i][0] = float(input(''));
            print('\nEnter shipping cost of product ' + str(i + 1) + ':', end = ' ');
            weight_table[i][1] = float(input(''));
        for i in range(len(function_table)):
            for j in range(len(function_table[0])):
                function_table[i][j] = int(j / weight_table[i][0]) * weight_table[i][1];
        print('\nWeight Table:\n');
        pretty_print(weight_table);
        print('\nFunction Table:\n');
        pretty_print(function_table);
        return function_table;
    except:
        print('\nInvalid input');
        return [];

# Initialize values matrix
def init_array(n, m):
    return [[0 for i in range(m)] for j in range(n)];

# Solve the dynamic programming problem using
# book problems as example
def solve_dynamic_programming_problem(values):
    # Test values
##    values = [[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
##              [0, 0, 25, 25, 50, 50, 75, 75, 100, 100, 125],
##              [0, 0, 0, 45, 45, 45, 90, 90, 90, 135, 135],
##              [0, 0, 0, 0, 60, 60, 60, 60, 120, 120, 120]];
    n, m = len(values), len(values[0]);
    # The j in f_j
    m_matrix = init_array(n, m);
    # The u in m_j(u)
    d_matrix = init_array(n, m);
    max_value = m_j(values, m_matrix, d_matrix, m, -1, 0);
    print('max_value:', max_value);
    print_return_table(m_matrix, d_matrix);

# this import is used to retrieve the index of the best next choice
import operator;
def m_j(values, m_matrix, d_matrix, u, j, counter):
    # base case: in last row of values matrix
    if j == len(values) - 1:
        m_matrix[j] = values[j];
        d_matrix[j] = [i for i in range(len(values[0]))];
        return max(values[j][:u]);
    # list of possible max values
    poss = [values[j][x] + m_j(values, m_matrix, d_matrix, u - x, j + 1, counter + 1)
            for x in range(u)];
    index, max_value = max(enumerate(poss), key = operator.itemgetter(1));
    # if counter == 0, we've finished our search
    # it's a return to the beginning
    if not counter == 0:
        m_matrix[j][u - 1] = max_value;
        d_matrix[j][u - 1] = index;
    return max_value;
    
if __name__ == '__main__':
    prob_type = -1;
    while prob_type != 0 and prob_type != 1:
        prob_type = get_problem_type();
    if prob_type == 0:
        function_table = [];
        while len(function_table) == 0:
            function_table = get_dimensions();
        solve_dynamic_programming_problem(function_table);
    else:
        print("Aarons code");
