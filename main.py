'''
Solve 2 specific types of dynamic programming problems
1. prompt user for type of problem to be solved - X
2. prompt user for dimensions of problem - X
3. prompt user for function values. Save in array - 
4. Calculate and display returns and decisions - 
5. Calculate and display optimal return and decisions - 
6. Give opportunity to run program again - 
'''

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
def get_values():
    try:
        pass;
    except:
        return [[]];

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
        
if __name__ == '__main__':
    prob_type = -1;
    while prob_type != 0 and prob_type != 1:
        prob_type = get_problem_type();
    n, m = 0, 0;
    while not valid_dimensions(n, m):
        (n, m) = get_dimensions();
    values = init_array(n, m);
    while not valid_values(values):
        print('get valid values');
        break;
