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
    errors = []
    for prediction, age, net_worth in zip(predictions, ages, net_worths):
        error = abs(prediction - net_worth)
        errors.append(error)

    cleaned_data = [(age, net_worth, error) for age, net_worth, error in zip(ages, net_worths, errors)]
    cleaned_data = sorted(cleaned_data, key=lambda x: x[2])
    remove_index = int((len(cleaned_data) * 0.1))
    cleaned_data = cleaned_data[:-remove_index]
    
    return cleaned_data
