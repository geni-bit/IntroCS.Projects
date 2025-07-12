import random

def infect(infection: float) -> bool:
    """This function simulates the chance of an infection
    occurring based on a given probability."""
    
    # Generate a random value between 0 and 1
    random_value = random.uniform(0, 1)
    
    # Check if the random value is less than the infection probability 
    if random_value < infection:
        return True  # Infection occurs
    else:
        return False  # Infection does not occur

def recover(recovery: float) -> bool:
    """ This function simulates the chance of recovery for an
    infected person based on a given probability."""
    
    # Generate a random value between 0 and 1
    random_value = random.uniform(0, 1)
    
    # Check if the random value is less than the recovery probability
    if random_value < recovery:
        return True  # Recovery occurs
    else:
        return False  # Recovery does not occur

def contact_indices(pop_size: int, source: int, contact_range: int) -> list:
    """This function determines which people come into contact with an
    infected person based on the given contact range and returns the
    list of their indices."""
    
    # An empty list to store the indices of people in contact with the infected person 
    contact_list = []
    
    # Loop over the range of indices based on the contact range
    for num in range(source - contact_range, source + contact_range + 1):
        
        # Check if the number is valid (within the population size) and not the source person
        if num >= 0 and num < pop_size and num != source:
            contact_list.append(num)  # Add the person to the contact list

    return contact_list

def apply_recoveries(population: list, recovery: float) -> None:
    """This function iterates through the population and attempts to apply
    recovery to each infected person based on the given recovery probability."""
    
    # Iterate through the population list
    for i in range(len(population)):
        # Check if the person is infected
        if population[i] == 'I':
            # If the person is infected, check if they recover using the recover function
            if recover(recovery):
                population[i] = 'R'  # Change their status to 'R' (recovered)

def contact(population: list, source: int, contact_range: int, infect_chance: int) -> None:
    """This function simulates an infected person coming into contact with other
    people, possibly infecting them."""
    
    # Get the list of indices of people the infected person contacts
    contact_list = contact_indices(len(population), source, contact_range)
    
    # Iterate through the people in contact with the infected person
    for i in contact_list:
        
        # Check if the person is susceptible (healthy but can get infected)
        if population[i] == 'S':
            
            # Use the infect function to determine if they become infected
            if infect(infect_chance):
                population[i] = 'I'  # If infected, change their status to 'I' (infected)

def apply_contacts(population: list, contact_range: int, infect_chance: float) -> None:
    """This function simulates all infected people in the population coming into contact with others, 
    possibly infecting them."""
    
    # An empty list to store the indices of infected people
    infected_indices = []
    
    # Loop through each person in the population and check their status
    for i in range(len(population)):
        status = population[i]  # Get the status of the person at index 
        if status == 'I':  # Check if the person is infected
            infected_indices.append(i)  # Add the infected person's index to the list
    
    # For each infected person, use the contact function to try to infect their neighbors
    for source in infected_indices:
        contact(population, source, contact_range, infect_chance)

def population_SIR_counts(population: list) -> dict:
    """This function simulates one day in the progression of the disease."""
    
    # Initialize counts
    counts = {'susceptible': 0, 'infected': 0, 'recovered': 0}
    
    # Count each status in the population
    for status in population:
        if status == 'S':
            counts['susceptible'] += 1  # Count susceptible individuals
        elif status == 'I':
            counts['infected'] += 1  # Count infected individuals
        elif status == 'R':
            counts['recovered'] += 1  # Count recovered individuals
    
    return counts  # Return the count of each category

def initialize_population(pop_size: int) -> list:
    """This function initializes the population with all individuals as susceptible
    ('S'), except for the first person who is initially infected ('I')."""
    
    population = ['S'] * pop_size  # Create a population where all are susceptible
    population[0] = 'I'  # The first person is infected
    return population

def simulate_disease(pop_size: int, contact_range: int, infect_chance: float, recover_chance: float) -> list:
    """This function simulates the disease spread over multiple days until there are no more infected individuals."""
    
    population = initialize_population(pop_size)  # Initialize the population
    counts = population_SIR_counts(population)  # Get the initial counts
    all_counts = [counts]  # List to store daily counts of the population
    
    # Simulate days while there are still infected individuals
    while counts['infected'] > 0:
        simulate_day(population, contact_range, infect_chance, recover_chance)  # Simulate a day
        counts = population_SIR_counts(population)  # Get the new counts after the day
        all_counts.append(counts)  # Store the daily counts
    
    return all_counts  # Return the counts over all days

def peak_infections(all_counts: list) -> int:
    """This function finds the peak number of infections during the simulation."""
    
    max_infections = 0
    for day in all_counts:
        if day['infected'] > max_infections:
            max_infections = day['infected']  # Track the highest number of infections
    return max_infections  # Return the peak number of infections

def display_results(all_counts: list) -> None:
    """This function displays the results of the simulation."""
    
    num_days = len(all_counts)  # Get the number of days in the simulation
    # Print the header for the results table
    print("Day".rjust(12) + "Susceptible".rjust(12) + "Infected".rjust(12) + "Recovered".rjust(12))
    
    # Print the counts for each day
    for day in range(num_days):
        line = str(day).rjust(12)
        line += str(all_counts[day]["susceptible"]).rjust(12)
        line += str(all_counts[day]["infected"]).rjust(12)
        line += str(all_counts[day]["recovered"]).rjust(12)
        print(line)  # Print the day and the corresponding counts
    
    # Print the peak number of infections during the simulation
    print("\nPeak Infections: {}".format(peak_infections(all_counts)))

def simulate_day(population: list, contact_range: int, infect_chance: float, recover_chance: float) -> None:
    """This function simulates one day in the disease progression."""
    
    # Apply recoveries to infected people
    apply_recoveries(population, recover_chance)
    
    # Simulate contact between infected people and attempt to infect others
    apply_contacts(population, contact_range, infect_chance)
