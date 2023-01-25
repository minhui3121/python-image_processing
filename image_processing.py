# Student name: Minhui Roh
# McGill ID: 261120462

def is_valid_image(n_list):
    """ (list<list>) -> bool
    Takes a nested list as inputs and returns a boolean indicating if the nested list represents valid
    PGM image matrix.
    
    >>> is_valid_image([[1,2,3], [4,5,6], [7,8,9]])
    True
    >>> is_valid_image([[1,2], [3,4,5]])
    False
    >>> is_valid_image([["25"], ["26"]])
    False
    >>> is_valid_image([[0], [0, 0]])
    False
    >>> is_valid_image([["0x5", "200x2"], ["111x7"]])
    False
    """
    for i in range (len(n_list)):
        for j in range (len(n_list[i])):
            if type(n_list[i][j]) != int or n_list[i][j] < 0 or n_list[i][j] > 255:
                return False
    for i in range (len(n_list)):
        if i == len(n_list)-1:
            break
        if (len(n_list[i]) != len(n_list[i+1])):
            return False
    return True

def is_valid_compressed_image(n_list):
    """ (list<list>) -> bool
    Takes a nested list as inputs and returns a boolean indicating if the nested list represents valid
    compressed PGM image matrix.
    
    >>> is_valid_compressed_image([["0x5", "200x2"], ["111x7"]])
    True
    >>> is_valid_compressed_image([["0x4", "200x2"], ["111x7"]])
    False
    >>> is_valid_compressed_image([[15, 16], [17, 18]])
    False
    >>> is_valid_compressed_image([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    False
    >>> is_valid_compressed_image([[0], [0, 0]])
    False
    """
    sum_B1 = 0
    sum_B2 = 0
    for i in range (len(n_list)):
        sum_B2 = sum_B1
        sum_B1 = 0
        for j in range (len(n_list[i])):
            if type(n_list[i][j]) != str or ("x" not in n_list[i][j]) or n_list[i][j].count("x") != 1:
                return False
            AB_list = n_list[i][j].split("x")
            for k in range (len(AB_list)):
                if not AB_list[k].isdecimal():
                    return False
            if int(AB_list[0]) < 0 or int(AB_list[0]) > 255 or int(AB_list[1]) <= 0:
                return False
            sum_B1 += int(AB_list[1])
        if sum_B1 != sum_B2 and i != 0:
            return False
    return True

def load_regular_image(filename):
    """ (str) -> list<list<int>>
    Takes a filename of a PGM image file as an input and returns the image as an image matrix.
    If the image matrix is not be in PGM format, raise AssertionError.
    
    >>> load_regular_image("comp.pgm")
    [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 51, 51, 51, 51, 51, 0, 119, 119, 119, 119, 119, 0, 187, 187, 187, 187, 187, 0, 255, 255, 255, 255, 0], [0, 51, 0, 0, 0, 0, 0, 119, 0, 0, 0, 119, 0, 187, 0, 187, 0, 187, 0, 255, 0, 0, 255, 0], [0, 51, 0, 0, 0, 0, 0, 119, 0, 0, 0, 119, 0, 187, 0, 187, 0, 187, 0, 255, 255, 255, 255, 0], [0, 51, 0, 0, 0, 0, 0, 119, 0, 0, 0, 119, 0, 187, 0, 187, 0, 187, 0, 255, 0, 0, 0, 0], [0, 51, 51, 51, 51, 51, 0, 119, 119, 119, 119, 119, 0, 187, 0, 187, 0, 187, 0, 255, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    
    >>> save_regular_image([[0]*10, [255]*10, [0]*10], "test.pgm")
    >>> load_regular_image("test.pgm")
    [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [255, 255, 255, 255, 255, 255, 255, 255, 255, 255], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    
    >>> save_regular_image([[2]*2, [10]*2, [20]*2], "test.pgm")
    >>> load_regular_image("test.pgm")
    [[2, 2], [10, 10], [20, 20]]
    
    >>> save_compressed_image([["0x5", "200x2"], ["111x7"]], "test.pgm.compressed")
    >>> load_regular_image("test.pgm.compressed")
    Traceback (most recent call last):
    AssertionError: This isn't in PGM format
    """
    
    fobj = open(filename, "r")
    file_content = fobj.read()
    fobj.close()
    string = file_content.strip("\n")
    list = string.split("\n")
    if list[0] != "P2" or list[2] != "255":
        raise AssertionError ("This isn't in PGM format")
    AB_list = list[1].split()
    if AB_list[1] != str(len(list)-3) or AB_list[0] != str(len(list[3].split())):
        raise AssertionError ("This isn't in PGM format")
    n_list=[]
    for i in range (len(list)):
        string = list[i]
        n_list.append(string.split())
    if len(n_list) < 4:
        raise AssertionError ("This isn't in PGM format")
    for i in range (3):
        n_list.pop(0)
    for i in range(len(n_list)):
        for j in range(len(n_list[i])):
            n_list[i][j]=int(n_list[i][j])
    if not is_valid_image(n_list):
        raise AssertionError ("This isn't in PGM format")
    return n_list

def load_compressed_image(filename):
    """ (str) -> list<list<str>>
    Takes a filename of a compressed PGM image file as an input,returns the image as compressed image matrix.
    If the image matrix is not be in compressed PGM format, raise AssertionError.
    
    >>> load_compressed_image("comp.pgm.compressed")
    [['0x24'], ['0x1', '51x5', '0x1', '119x5', '0x1', '187x5', '0x1', '255x4', '0x1'], ['0x1', '51x1', '0x5', '119x1', '0x3', '119x1', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x1', '0x2', '255x1', '0x1'], ['0x1', '51x1', '0x5', '119x1', '0x3', '119x1', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x4', '0x1'], ['0x1', '51x1', '0x5', '119x1', '0x3', '119x1', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x1', '0x4'], ['0x1', '51x5', '0x1', '119x5', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x1', '0x4'], ['0x24']]
    
    >>> save_compressed_image([["0x5", "200x2"], ["111x7"]], "test.pgm.compressed")
    >>> load_compressed_image("test.pgm.compressed")
    [['0x5', '200x2'], ['111x7']]
    
    >>> save_regular_image([[2]*2, [10]*2, [20]*2], "test.pgm")
    >>> load_compressed_image("test.pgm")
    Traceback (most recent call last):
    AssertionError: This isn't in compressed PGM format
    
    >>> fobj = open("invalid_test.pgm", "w")
    >>> fobj.write("P2C\\n30 5\\n255\\nabc3x23 0x0x7\\n")
    27
    >>> fobj.close()
    >>> load_compressed_image("invalid_test.pgm")
    Traceback (most recent call last):
    AssertionError: This isn't in compressed PGM format
    """
    fobj = open(filename, "r")
    file_content = fobj.read()
    fobj.close()
    string = file_content.strip("\n")
    list = string.split("\n")
    if list[0] != "P2C" or list[2] != "255":
        raise AssertionError ("This isn't in compressed PGM format")
    n_list=[]
    for i in range (len(list)):
        string = list[i]
        n_list.append(string.split())
    if len(n_list) < 4:
        raise AssertionError ("This isn't in compressed PGM format")
    for i in range (3):
        n_list.pop(0)
    if not is_valid_compressed_image(n_list):
        raise AssertionError ("This isn't in compressed PGM format")
    return n_list

def load_image(filename):
    """ (str) -> list<list>
    Takes a filename of a file as input. If the first line of the file is "P2", then loads the file in
    PGM format. If the first line of the file is "P2C", then loads the file in compressed PGM format.
    If anything else, raise AssertionError.

    >>> load_image("comp.pgm.compressed")
    [['0x24'], ['0x1', '51x5', '0x1', '119x5', '0x1', '187x5', '0x1', '255x4', '0x1'], ['0x1', '51x1', '0x5', '119x1', '0x3', '119x1', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x1', '0x2', '255x1', '0x1'], ['0x1', '51x1', '0x5', '119x1', '0x3', '119x1', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x4', '0x1'], ['0x1', '51x1', '0x5', '119x1', '0x3', '119x1', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x1', '0x4'], ['0x1', '51x5', '0x1', '119x5', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x1', '0x4'], ['0x24']]
    >>> load_image("comp.pgm")
    [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 51, 51, 51, 51, 51, 0, 119, 119, 119, 119, 119, 0, 187, 187, 187, 187, 187, 0, 255, 255, 255, 255, 0], [0, 51, 0, 0, 0, 0, 0, 119, 0, 0, 0, 119, 0, 187, 0, 187, 0, 187, 0, 255, 0, 0, 255, 0], [0, 51, 0, 0, 0, 0, 0, 119, 0, 0, 0, 119, 0, 187, 0, 187, 0, 187, 0, 255, 255, 255, 255, 0], [0, 51, 0, 0, 0, 0, 0, 119, 0, 0, 0, 119, 0, 187, 0, 187, 0, 187, 0, 255, 0, 0, 0, 0], [0, 51, 51, 51, 51, 51, 0, 119, 119, 119, 119, 119, 0, 187, 0, 187, 0, 187, 0, 255, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    
    >>> save_regular_image([[0]*10, [255]*10, [0]*10], "test.pgm")
    >>> load_image("test.pgm")
    [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [255, 255, 255, 255, 255, 255, 255, 255, 255, 255], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    
    >>> save_compressed_image([["0x5", "200x2"], ["111x7"]], "test.pgm.compressed")
    >>> load_image("test.pgm.compressed")
    [['0x5', '200x2'], ['111x7']]
    """
    fobj = open(filename, "r")
    file_content = fobj.read()
    fobj.close()
    list = []
    list.append (file_content)
    string = list[0]
    list = string.split("\n")
    if list[0] == "P2":
        return load_regular_image(filename)
    elif list[0] == "P2C":
        return load_compressed_image(filename)
    else:
        raise AssertionError ("This is neither in PGM format nor in compressed PGM format")

def save_regular_image(n_list, filename):
    """ (list<list>, str) -> NoneType
    Takes a nested list and a filename as inputs and returns nothing.
    Saves the nested list into a PGM format file with given filename.
    AssertionError is raised when the inputs are invalid.
    
    >>> save_regular_image([[0]*10, [255]*10, [0]*10], "test.pgm")
    >>> fobj = open("test.pgm", 'r')
    >>> fobj.read()
    'P2\\n10 3\\n255\\n0 0 0 0 0 0 0 0 0 0\\n255 255 255 255 255 255 255 255 255 255\\n0 0 0 0 0 0 0 0 0 0\\n'
    >>> fobj.close()
    
    >>> save_regular_image([[2]*2, [10]*2, [20]*2], "test.pgm")
    >>> fobj = open("test.pgm", 'r')
    >>> fobj.read()
    'P2\\n2 3\\n255\\n2 2\\n10 10\\n20 20\\n'
    >>> fobj.close()
    
    >>> save_regular_image([[0, 0, 0], [1, 1, 1], [2, 2, 2]], "test.pgm")
    >>> fobj = open("test.pgm", 'r')
    >>> fobj.read()
    'P2\\n3 3\\n255\\n0 0 0\\n1 1 1\\n2 2 2\\n'
    
    >>> save_regular_image([["0x5", "200x2"], ["111x7"]], "test.pgm")
    Traceback (most recent call last):
    AssertionError: This is not a valid PGM image matrix
    """
    if not is_valid_image(n_list):
        raise AssertionError ("This is not a valid PGM image matrix")
    fobj = open(filename, "w")
    
    n_row = len(n_list)
    n_column = len(n_list[0])
    list_1 = []
    for e in n_list:
        new_e = []
        for n in e:
            new_e.append(n)
        list_1.append(new_e)
    for i in range (len(n_list)):
        for j in range(len(n_list[i])):
            list_1[i][j] = str(n_list[i][j])
    max_white_list = ["255"]
    row_column_list = [str(n_column), str(n_row)]
    indication_list = ["P2"]
    empty_list=[]
    list_1.insert(0, max_white_list)
    list_1.insert(0, row_column_list)
    list_1.insert(0, indication_list)
    list_1.insert(len(list_1), empty_list)
    d=" "
    line_break = "\n"
    list_2=[]
    string = ""
    for i in range (len(list_1)):
        list_2.append(d.join(list_1[i]))
        string = line_break.join(list_2)
    fobj.write(string)
    fobj.close()
    
def save_compressed_image(n_list, filename):
    """ (list<list>, str) -> NoneType
    Takes a nested list and a filename as inputs and returns nothing.
    Saves the nested list into a compressed PGM format file with given filename.
    AssertionError is raised when the inputs are invalid.
    
    >>> save_compressed_image([["0x5", "200x2"], ["111x7"]], "test.pgm.compressed")
    >>> fobj = open("test.pgm.compressed", 'r')
    >>> fobj.read()
    'P2C\\n7 2\\n255\\n0x5 200x2\\n111x7\\n'
    >>> fobj.close()
    
    >>> image = [["0x5", "200x2"], ["111x7"]]
    >>> save_compressed_image(image, "test.pgm")
    >>> image2 = load_compressed_image("test.pgm")
    >>> image == image2
    True
    
    >>> save_compressed_image([[2]*2, [10]*2, [20]*2], "test.pgm.compressed")
    Traceback (most recent call last):
    AssertionError: This is not a valid compressed PGM image matrix
    
    >>> save_compressed_image([["0x4", "220x2"], ["111x6"]], "test.pgm.compressed")
    >>> fobj = open("test.pgm.compressed", 'r')
    >>> fobj.read()
    'P2C\\n6 2\\n255\\n0x4 220x2\\n111x6\\n'
    >>> fobj.close()
    """
    if not is_valid_compressed_image(n_list):
        raise AssertionError ("This is not a valid compressed PGM image matrix")
    fobj = open(filename, "w")
    
    n_row = len(n_list)
    n_column = 0
    for i in range (len(n_list)):
        for j in range (len(n_list[i])):
            AB_list = n_list[i][j].split("x")
    n_column += int(AB_list[1])
    
    list_1 = []
    for e in n_list:
        new_e = []
        for n in e:
            new_e.append(n)
        list_1.append(new_e)
    max_white_list = ["255"]
    row_column_list = [str(n_column), str(n_row)]
    indication_list = ["P2C"]
    empty_list=[]
    list_1.insert(0, max_white_list)
    list_1.insert(0, row_column_list)
    list_1.insert(0, indication_list)
    list_1.insert(len(list_1), empty_list)
    d=" "
    line_break = "\n"
    list_2=[]
    string = ""
    for i in range (len(list_1)):
        list_2.append(d.join(list_1[i]))
        string = line_break.join(list_2)
    fobj.write(string)
    fobj.close()
    
def save_image(n_list, filename):
    """ (list<list>, str) -> NoneType
    Takes a nested list and a filename as inputs and returns nothing.
    If the elements in the list are integers, saves the list as PGM image matrix into a file with given name.
    If the elements are strings, saves the list as compressed PGM image matrix into a file with given name.
    If the inputs are invalid, raise AssertionError.
    
    >>> save_image([["0x5", "200x2"], ["111x7"]], "test.pgm.compressed")
    >>> fobj = open("test.pgm.compressed", 'r')
    >>> fobj.read()
    'P2C\\n7 2\\n255\\n0x5 200x2\\n111x7\\n'
    >>> fobj.close()
    
    >>> save_image([[2]*2, [10]*2, [20]*2], "test.pgm")
    >>> fobj = open("test.pgm", 'r')
    >>> fobj.read()
    'P2\\n2 3\\n255\\n2 2\\n10 10\\n20 20\\n'
    >>> fobj.close()
    
    >>> save_image([["0x5", 0]], "test.pgm")
    Traceback (most recent call last):
    AssertionError: There are mix of integers and strings
    """
    for i in range (len(n_list)):
        for j in range (len(n_list[i])):
            if type(n_list[i][j]) != int and type(n_list[i][j]) != str:
                raise AssertionError ("The elements are neither integers nor strings")
            
    for i in range (len(n_list)):
        for j in range (len(n_list[i])):
            if j == len(n_list[i])-1:
                break
            elif type(n_list[i][j]) != type(n_list[i][j+1]):
                raise AssertionError ("There are mix of integers and strings")
    if type(n_list[0][0]) == int:
        return save_regular_image(n_list, filename)
    else:
        return save_compressed_image(n_list, filename)

def invert(matrix):
    """ (list<list>) -> list<list<int>>
    Takes a nested list representing PGM image matrix as input and returns the inverted image.
    If the input is not PGM image matrix, raises AssertionError.
    
    >>> image = [[0, 100, 150], [200, 200, 200], [255, 255, 255]]
    >>> invert(image)
    [[255, 155, 105], [55, 55, 55], [0, 0, 0]]
    
    >>> image == [[0, 100, 150], [200, 200, 200], [255, 255, 255]]
    True
    
    >>> image = [[255, 155, 105], [55, 55, 55], [0, 0, 0]]
    >>> invert(image)
    [[0, 100, 150], [200, 200, 200], [255, 255, 255]]
    
    >>> image = [[15, 215], [215, 15]]
    >>> invert(image)
    [[240, 40], [40, 240]]
    
    >>> image = [["0x5", "200x2"], ["111x7"]]
    >>> invert(image)
    Traceback (most recent call last):
    AssertionError: The input is not a PGM matrix
    """
    if not is_valid_image(matrix):
        raise AssertionError ("The input is not a PGM matrix")
    
    matrix_copy = []
    for e in matrix:
        new_e = []
        for n in e:
            new_e.append(abs(n-255))
        matrix_copy.append(new_e)
    return matrix_copy

def flip_horizontal(matrix):
    """ (list<list>) -> list<list<int>>
    Takes a nested list representing PGM image matrix as input and returns horizontally flipped image.
    If the input is not PGM image matrix, raises AssertionError.
    
    >>> image = [[1, 2, 3, 4, 5], [0, 0, 5, 10, 10], [5, 5, 5, 5, 5]]
    >>> flip_horizontal(image)
    [[5, 4, 3, 2, 1], [10, 10, 5, 0, 0], [5, 5, 5, 5, 5]]
    >>> image == [[1, 2, 3, 4, 5], [0, 0, 5, 10, 10], [5, 5, 5, 5, 5]]
    True
    
    >>> image = [[5, 10, 15, 20], [55, 60, 65, 70], [105, 110, 115, 120]]
    >>> flip_horizontal(image)
    [[20, 15, 10, 5], [70, 65, 60, 55], [120, 115, 110, 105]]
    
    >>> image = [["0x5", "200x2"], ["111x7"]]
    >>> flip_horizontal(image)
    Traceback (most recent call last):
    AssertionError: The input is not a PGM matrix
    """
    if not is_valid_image(matrix):
        raise AssertionError ("The input is not a PGM matrix")
    
    matrix_copy = []
    for e in matrix:
        new_e = []
        for n in e:
            new_e.insert(0, n)
        matrix_copy.append(new_e)
    return matrix_copy
    
def flip_vertical(matrix):
    """ (list<list>) -> list<list<int>>
    Takes a nested list representing PGM image matrix as input and returns vertically flipped image.
    If the input is not PGM image matrix, raises AssertionError.
    
    >>> image = [[1, 2, 3, 4, 5], [0, 0, 5, 10, 10], [5, 5, 5, 5, 5]]
    >>> flip_vertical(image)
    [[5, 5, 5, 5, 5], [0, 0, 5, 10, 10], [1, 2, 3, 4, 5]]
    >>> image == [[1, 2, 3, 4, 5], [0, 0, 5, 10, 10], [5, 5, 5, 5, 5]]
    True
    
    >>> image = [[5, 10, 15, 20], [55, 60, 65, 70], [105, 110, 115, 120]]
    >>> flip_vertical(image)
    [[105, 110, 115, 120], [55, 60, 65, 70], [5, 10, 15, 20]]
    
    >>> image = [["0x5", "200x2"], ["111x7"]]
    >>> flip_horizontal(image)
    Traceback (most recent call last):
    AssertionError: The input is not a PGM matrix
    """
    if not is_valid_image(matrix):
        raise AssertionError ("The input is not a PGM matrix")
    
    matrix_copy = []
    for e in matrix:
        new_e = []
        for n in e:
            new_e.append(n)
        matrix_copy.insert(0, new_e)
    return matrix_copy
    
def crop(matrix, row_index, column_index, n_row, n_column):
    """ (list<list>, int, int, int, int) -> list<list<int>>
    Takes a nested list representing PGM image matrix as input and returns cropped image.
    If the input is not PGM image matrix, raises AssertionError.
    
    >>> crop([[5, 5, 5], [5, 6, 6], [6, 6, 7]], 1, 1, 2, 2)
    [[6, 6], [6, 7]]
    
    >>> crop([[1, 2, 3, 4], [4, 5, 6, 7], [8, 9, 10, 11]], 1, 2, 2, 1)
    [[6], [10]]
    
    >>> crop([[11, 22, 33], [44, 55, 66], [77, 88, 99]], 2, 2, 1, 1)
    [[99]]
    
    >>> crop([["0x4", "200x2"], ["111x7"]], 1, 1, 1, 1)
    Traceback (most recent call last):
    AssertionError: The input is not a PGM matrix
    """
    if not is_valid_image(matrix):
        raise AssertionError ("The input is not a PGM matrix")
    
    matrix_copy = []
    i = row_index
    while i < row_index + n_row:
        new_e=[]
        j = column_index
        while j < column_index+ n_column:
            new_e.append(matrix[i][j])
            j += 1
        matrix_copy.append(new_e)
        i += 1
    return matrix_copy

def find_end_of_repetition (int_list, index, target):
    """ (list<int>, int, int) -> int
    Takes a list of integers and two non-negative integers, index and target number, as inputs.
    Returns the index of the last consecutive occurrence of the target in the list.
    
    >>> find_end_of_repetition([5, 3, 5, 5, 5, -1, 0], 2, 5)
    4
    >>> find_end_of_repetition([1, 2, 3, 4, 5, 6, 7], 6, 7)
    6
    >>> find_end_of_repetition([1, 2, 2, 2, 2, 3, 4], 2, 2)
    4
    >>> find_end_of_repetition([0, 0, 0], 0, 0)
    2
    """
    while index < len(int_list) -1:
        if int_list[index] != int_list[index + 1]:
            return index
        index += 1
    return index

def compress (n_list):
    """ (list<list>) -> list<list<str>>
    Takes a nested list representing a PGM image matrix as input.
    Returns the compressed matrix.
    If the input is not PGM image matrix, raises AssertionError.
    
    >>> compress([[11, 11, 11, 11, 11], [1, 5, 5, 5, 7], [255, 255, 255, 0, 255]])
    [['11x5'], ['1x1', '5x3', '7x1'], ['255x3', '0x1', '255x1']]
    
    >>> compress([[0, 10, 10, 10], [20, 10, 20, 20], [0, 10, 0, 10]])
    [['0x1', '10x3'], ['20x1', '10x1', '20x2'], ['0x1', '10x1', '0x1', '10x1']]
    
    >>> compress([["0x4", "200x2"], ["111x7"]])
    Traceback (most recent call last):
    AssertionError: The input is not a PGM matrix
    """
    if not is_valid_image(n_list):
        raise AssertionError ("The input is not a PGM matrix")
    i = 0
    compressed_list = []
    while i < len(n_list):
        j = 0
        new_e = []
        while j < len(n_list[i]):
            end_index = find_end_of_repetition(n_list[i], j, n_list[i][j])
            new_e.append(str(n_list[i][j])+"x"+str(end_index-j+1))
            j = end_index + 1
        compressed_list.append(new_e)
        i += 1
    return compressed_list
        
def decompress (compressed_list):
    """ (list<list>) -> list<list<int>>
    Takes a nested list representing a compressed PGM image matrix as input.
    Returns the uncompressed PGM matrix.
    If the input is not PGM image matrix, raises AssertionError.
    
    >>> decompress([['11x5'], ['1x1', '5x3', '7x1'], ['255x3', '0x1', '255x1']])
    [[11, 11, 11, 11, 11], [1, 5, 5, 5, 7], [255, 255, 255, 0, 255]]
    
    >>> image = [[11, 11, 11, 11, 11], [1, 5, 5, 5, 7], [255, 255, 255, 0, 255]]
    >>> compressed_image = compress(image)
    >>> image2 = decompress(compressed_image)
    >>> image == image2
    True
    
    >>> decompress([['0x1', '10x3'], ['20x1', '10x1', '20x2'], ['0x1', '10x1', '0x1', '10x1']])
    [[0, 10, 10, 10], [20, 10, 20, 20], [0, 10, 0, 10]]
    
    >>> decompress([[11, 11, 11, 11, 11], [1, 5, 5, 5, 7], [255, 255, 255, 0, 255]])
    Traceback (most recent call last):
    AssertionError: The input is not a compressed PGM matrix
    """
    if not is_valid_compressed_image(compressed_list):
        raise AssertionError ("The input is not a compressed PGM matrix")
    
    decompressed_list = []
    for i in range (len(compressed_list)):
        new_e = []
        for j in range (len(compressed_list[i])):
            AB_list = compressed_list[i][j].split("x")
            for k in range (int(AB_list[1])):
                new_e.append(int(AB_list[0]))
        decompressed_list.append(new_e)
    return decompressed_list

def process_command(command):
    """ (str) -> NoneType
    Takes a string containg commands to be executed as an input.
    Returns nothing but processes the commands.
    If there is an unrecognized command, raises AssertionError.
    
    >>> process_command("LOAD<comp.pgm> CP DC INV INV SAVE<comp2.pgm>")
    >>> image = load_image("comp.pgm")
    >>> image2 = load_image("comp2.pgm")
    >>> image == image2
    True
    
    >>> process_command("LOAD<comp.pgm> CP SAVE<comp.pgm.compressed>")
    >>> load_compressed_image("comp.pgm.compressed")
    [['0x24'], ['0x1', '51x5', '0x1', '119x5', '0x1', '187x5', '0x1', '255x4', '0x1'], ['0x1', '51x1', '0x5', '119x1', '0x3', '119x1', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x1', '0x2', '255x1', '0x1'], ['0x1', '51x1', '0x5', '119x1', '0x3', '119x1', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x4', '0x1'], ['0x1', '51x1', '0x5', '119x1', '0x3', '119x1', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x1', '0x4'], ['0x1', '51x5', '0x1', '119x5', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x1', '0x4'], ['0x24']]
    
    >>> process_command("LOAD<comp.pgm> INVI SAVE<comp2.pgm>")
    Traceback (most recent call last):
    AssertionError: The string command contains unrecognized command.
    
    >>> process_command("LOAD<comp.pgm> CRC SAVE<comp2.pgm>")
    Traceback (most recent call last):
    AssertionError: The string command contains unrecognized command.
    
    >>> save_regular_image([[0]*10, [255]*10, [0]*10], "test.pgm")
    >>> process_command("LOAD<test.pgm> CR<1,8,2,2> SAVE<test_1.pgm>")
    >>> load_image("test_1.pgm")
    [[255, 255], [0, 0]]
    
    """ 
    
    command_list = command.split()
    if "LOAD" not in command_list[0]:
        raise AssertionError ("The string command contains unrecognized command.")
    elif "SAVE" not in command_list[len(command_list)-1]:
        raise AssertionError ("The string command contains unrecognized command.")
        
    for e in command_list:
        if "LOAD" in e:
            if e[4]!="<" or e[len(e)-1] != ">":
                raise AssertionError ("The string command contains unrecognized command.")
            filename = e[5:len(e)-1]
            matrix = load_image(filename)
        elif "INV" == e:
            matrix = invert(matrix)
        elif "FH" == e:
            matrix = flip_horizontal(matrix)
        elif "FV" == e:
            matrix = flip_vertical(matrix)
        elif "CR" in e:
            if e[2]!="<" or e[len(e)-1] != ">":
                raise AssertionError ("The string command contains unrecognized command.")
            int_str = e[3:len(e)-1]
            if "," not in int_str:
                raise AssertionError ("The string command contains unrecognized command.")
            int_list = int_str.split(",")
            if len(int_list) != 4:
                raise AssertionError ("The string command contains unrecognized command.")
            row_index = int(int_list[0])
            column_index = int(int_list[1])
            n_row = int(int_list[2])
            n_column = int(int_list[3])
            matrix = crop(matrix, row_index, column_index, n_row, n_column)
        elif "CP" == e:
            matrix = compress(matrix)
        elif "DC" == e:
            matrix = decompress(matrix)
        elif "SAVE" in e:
            if e[4]!="<" or e[len(e)-1] != ">":
                raise AssertionError ("The string command contains unrecognized command.")
            filename = e[5:len(e)-1]
            save_image(matrix, filename)
        else:
            raise AssertionError ("The string command contains unrecognized command.")
        

