#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here

    errors = list( (net_worths - predictions)**2 )
    cleaned_data = zip(ages, net_worths, errors)
    cleaned_data = sorted(cleaned_data, key = lambda tup: tup[2])

    #for i in range(0, int(len(cleaned_data) * 0.1)):
     #   cleaned_data.pop()
    cleaned_data = cleaned_data[:80]
    return cleaned_data

