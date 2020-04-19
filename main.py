'''
Solve 2 specific types of dynamic programming problems
1. prompt user for type of problem to be solved - X
2. prompt user for dimensions of problem - X
3. prompt user for function values. Save in array - X
4. Calculate and display returns and decisions - O
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

# Get user input to determine what type of problem
# we're going to be solving
def get_problem_type():
    try:
        return int(input('\nPlease Enter 0 for dynamic programming problem or 1 for stochastic dynamic programming problem: '));
    except:
        print("\nInvalid problem #");
        return -1;

# Get user input to determine size of matrix
# that holds the values we'll be working with
def get_dimensions():
    try:
        n, m = 0, 0;
        n = int(input('\nEnter number of rows ( > 0): '));
        m = int(input('\nEnter number of columns ( > 0): '));
        return (n, m);
    except:
        print('\nInvalid dimensions');
        return (0, 0);

# Verify dimension validity
def valid_dimensions(n, m):
    return n > 0 and m > 0;

# Get user input to determine value of
# matrix at each row and column
def get_values(values):
    try:
        for i in range(len(values)):
            print('\nEnter values for row', i, 'seperated by a space:', end = ' ');
            row = [float(i) for i in str(input('')).split()];
            if len(row) != len(values[0]):
                raise IncorrectColumnEntriesError;
            values[i] = row;
            pretty_print(values);
    except IncorrectColumnEntriesError:
        print('\nInvalid number of column entries');
    except ValueError:
        print('\nInvalid values');

# Verify values validity
def valid_values(values):
    count = 0;
    for i in values:
        for j in i:
            if j == 0:
                count += 1;
    return count != len(values) * len(values[0]);

# Initialize values matrix
def init_array(n, m):
    return [[0] * m] * n;

# Solve the dynamic programming problem using
# book problems as example
def solve_dynamic_programming_problem(values):
    n, m = len(values), len(values[0]);
    # The j in f_j
    m_matrix = init_array(n, m);
    # The u in m_j(u)
    d_matrix = init_array(n, m);
    '''
    m_j(u) = max (0<=x<=u){f_j(x) + m_j+1(u-x)}
    m_4(u) = max (0<=x<=10){f_4(x)}
    call m_j from here
    '''

# Values is values matrix
# u is current column
# j is current row
def m_j(values, u, j):
    '''
    This is our base case, if we have reached the last row,
    We will find the function values here and return the max
    This is what happens at m_4(u)
    '''
    if j == len(values[0]) - 1:
        return max(values[j]);
    '''
    This is where we call this function again in order to
    create a recursive call. Here is an example:

    m = max(values[j][u] + m_j(values, u - x, j + 1))

    basically we're making another function call with
    an updated j value, representing row we're currently at
    This will return the max value from last column which
    we can use to update our current decision
    '''
    
if __name__ == '__main__':
    prob_type = -1;
    while prob_type != 0 and prob_type != 1:
        prob_type = get_problem_type();
    n, m = 0, 0;
    while not valid_dimensions(n, m):
        (n, m) = get_dimensions();
    values = init_array(n, m);
    while not valid_values(values):
        get_values(values);
    if prob_type == 0:
        # Do whatever needs to be done to calculate decisions
        # for normal dynamic programming problems
        solve_dynamic_programming_problem(values);
