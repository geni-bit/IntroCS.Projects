def get_data(file_name:str) -> list:
    """Takes a file name, and returns a list of strings,
    containing all of the data from the file."""

    #Opening the file in read mode
    data_file = open(file_name, "r")
    
    #Read all lines of the file into a list
    data_read = data_file.readlines()

    #Closing the file
    data_file.close()

    return data_read

def parse_data(data:list) -> list:
    """Takes the list of strings returned by the
    get data function, and parses this data into a more usable format."""

    #create an empty list to the variable parsed data
    parsed_data = []
    
    #Using a loop through each line in the provided data (paramter) list
    for line in data:
        #Split each line by commas and strip any surrounding whitespace
        parsed_line = line.strip().split(',')
        #Only keep lines that have exactly 3 elements
        if len(parsed_line) == 3:
            parsed_data.append(parsed_line)
    
    return parsed_data

def get_populations(parsed_data: list) -> list:
    """Takes a list of lists (parsed data)
    and returns a list of strings containing only the populations."""

    #create an empty list to the variable populations
    populations = []

    #Iterate over each entry in the parsed data paramater 
    for entry in parsed_data:
        #Append the population value (third number) to the list
        populations.append(entry[2])

    return populations

def leading_digits(frequency_data:list) -> None:
    """Takes a list of strings and prints the frequency for 1, 2, 3, ...9
    as the first digits in the strings."""

    #An empty dictionary to store count of each leading digit
    counts = {}

    #Total number of items in the frequency data
    total_items = len(frequency_data)

    #Initializing the counts for digits 1 to 9 
    for index in range(1,10):
        counts[str(index)] = 0

   #Count occurrences of each leading digit in the strings 
    for item in frequency_data:
        for number in item:
            if number in '123456789':
                counts[number] += 1

    #Calculating the frequency for each leading digit (1-9)
    for digit in range(1,10):
        count_for_digit = counts[str(digit)]
        frequency = count_for_digit / (total_items + 1)

        #Create a varible for format of frequency
        formatted_string = "Frequency of " + str(digit) + ": " + str(frequency)

        #Printing the frequency for each leading digit (1-9)
        print(formatted_string)
