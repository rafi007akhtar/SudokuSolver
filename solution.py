assignments = []

rows = 'ABCDEFGHI'
cols = '123456789'

def assign_value(values, box, value):
    """
    Please use this function to update your values dictionary!
    Assigns a value to a given box. If it updates the board record it.
    """

    # Don't waste memory appending actions that don't actually change any values
    if values[box] == value:
        return values

    values[box] = value
    if len(value) == 1:
        assignments.append(values.copy())
    return values

def delete(key1, key2, unit, values):
    val = list[values[key1]]
    for i in val:
        for key in unit:
            p = values[key]
            if i in p and key not in (key1, key2): 
                values.update({key: p.replace(i, "")})

def cross(A, B):
    # Given two strings — a and b — will return the list formed by all the possible concatenations of a letter "s" in string "a" with a letter "t" in string "b".
    return [s+t for s in A for t in B]

boxes = cross(rows, cols)
#print(boxes)

row_units = [cross(r, cols) for r in rows]
#print(row_units)
column_units = [cross(rows, c) for c in cols]
square_units = [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]
unitlist = row_units + column_units + square_units
units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
#print(unitlist)
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)

def naked_twins(values):
    """Eliminate values using the naked twins strategy.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        the values dictionary with the naked twins eliminated from peers.
    """

    # Find all instances of naked twins
    # Eliminate the naked twins as possibilities for their peers  
    for unit in unitlist:
        for key in unit:
            if len(values[key]) == 2:
                one = key
                for key2 in unit:
                    if key2 is not one and values[key2] is values[one]:
                        two = key2
                        values = delete(one, two, unit, values)
                        break

    return values              

def puff(grid):
    i = 0
    dict = {}
    for key in boxes:
        num = grid[i]
        if num == '.':
            dict.update({key: "."})
        else:
            dict.update({key: num})
        i += 1
    return dict

def grid_values(grid):
    """
    Convert grid into a dict of {square: char} with '123456789' for empties.
    Args:
        grid(string) - A grid in string form.
    Returns:
        A grid in dictionary form
            Keys: The boxes, e.g., 'A1'
            Values: The value in each box, e.g., '8'. If the box has no value, then the value will be '123456789'.
    """
    i = 0
    dict = {}
    for key in boxes:
        num = grid[i]
        if num == '.':
            dict.update({key: "123456789"})
        else:
            dict.update({key: num})
        i += 1
    return dict

def display(values):
    """
    Display the values as a 2-D grid.
    Args:
        values(dict): The sudoku in dictionary form
    """
    width = 1+max(len(values[s]) for s in boxes)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print(''.join(values[r+c].center(width)+('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF': print(line)
    return

def eliminate(puzzle):
    for key, val in puzzle.items():
        if len(val) == 1:
            # run  a row check
            row = []
            for i in row_units: # fetch the row to which the key row belongs
                if key in i:
                    row = i
                    break
            for i in row: # now perform a scan in the row containing the key row and eliminate val
                if i != key: # that is, don't remove val from key itself!
                    if val in puzzle[i]:
                        # puzzle[i] is the value of the current key, and the condition checks if this value has val
                        # if so, remove it, or, replace it with a blank space
                        assign_value(puzzle, i, puzzle[i].replace(val, ""))

            # now run a column check
            col = []
            for i in column_units: # fetch the column to which the key column belongs
                if key in i:
                    col = i
                    break
            for i in col: # now perform a scan in the column containing the key column and eliminate val
                if i != key: # that is, don't remove val from key itself!
                    if val in puzzle[i]:
                        # puzzle[i] is the value of the current key, and the condition checks if this value has val
                        # if so, remove it, that is, replace it with a blank space
                        assign_value(puzzle, i, puzzle[i].replace(val, ""))
            
            # lastly, perform the square-block check to complete the elimination process
            sq = []
            for i in square_units: # fetch the square_unit to which the key square_unit belongs
                if key in i:
                    sq = i
                    break
            for i in sq: # now perform a scan in the square_unit containing the key square_unit and eliminate val
                if i != key: # that is, don't remove val from key itself!
                    if val in puzzle[i]:
                        # puzzle[i] is the value of the current key, and the condition checks if this value has val
                        # if so, remove it, that is, replace it with a blank space
                        assign_value(puzzle, i, puzzle[i].replace(val, ""))
           
    return puzzle

def only_choice(values):
    # unitlist is a list of all units - rows, columns and 3x3 grids
    # traverse each unit in a unitlist
    for unit in unitlist:
        digits = "123456789"
        # for each digit, check if it is there in a unit EXACTLY ONCE
        for digit in digits:
            # make a list of those boxes where digit is occuring
            boxes = [box for box in unit if digit in values[box]]
            # if this list has exactly one box where the digit is occuring, it means that digit is the box's only choice
            # so assign it
            if len(boxes) == 1:
                values[boxes[0]] = digit
                assign_value(values, boxes[0], digit)
    return values

def reduce_puzzle(values):
    stalled = False
    while not stalled:
        # Check how many boxes have a determined value
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])

        # Your code here: Use the Eliminate Strategy
        values = eliminate(values)

        # Eliminate naked twins
        values = naked_twins(values)

        # Your code here: Use the Only Choice Strategy
        values = only_choice(values)

        # Check how many boxes have a determined value, to compare
        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
        # If no new values were added, stop the loop.
        stalled = solved_values_before == solved_values_after
        # Sanity check, return False if there is a box with zero available values:
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False
    
    return values

def search(values):
    "Using depth-first search and propagation, create a search tree and solve the sudoku."

    # First, reduce the puzzle using the previous function
    values = reduce_puzzle(values)
    if values is False:
        return False
    if all(len(values[s]) == 1 for s in boxes): 
        return values

    # Choose one of the unfilled squares with the fewest possibilities
    n, val = min((len(values[box]), box) for box in boxes if len(values[box]) > 1)
    
    # Now use recursion to solve each one of the resulting sudokus, and if one returns a value (not False), return that answer!
    for i in values[val]:
        temp = values.copy()
        temp[val] = i
        assign_value(temp, val, i)
        trial = search(temp)
        if trial:
            return trial

def solve(grid):
    """
    Find the solution to a Sudoku grid.
    Args:
        grid(string): a string representing a sudoku grid.
            Example: '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    Returns:
        The dictionary representation of the final sudoku grid. False if no solution exists.
    """
    values = puff(grid)
    print("Original board")
    display(values)

    values = grid_values(diag_sudoku_grid)
    values = search(values)

    print("\nSolved board")
    display(values)
        
    return values

if __name__ == '__main__':
    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    #diag_sudoku_grid = '.2.986.1.6...5...9...1.3...3.1...6.285.....412.6...9.3...8.5...5...2...4.6.437.9.'
    solve(diag_sudoku_grid)

    try:
        from visualize import visualize_assignments
        visualize_assignments(assignments)

    except SystemExit:
        pass
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')
