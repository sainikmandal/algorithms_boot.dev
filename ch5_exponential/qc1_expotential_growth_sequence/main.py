def exponential_growth(n, factor, days):
    growth_sequence = []
    
    # Start with the initial followers count
    growth_sequence.append(n)
    
    # Calculate the number of followers for each day
    for i in range(1, days + 1):
        n *= factor  # Multiply the current followers count by the growth factor
        growth_sequence.append(n)
    
    return growth_sequence
