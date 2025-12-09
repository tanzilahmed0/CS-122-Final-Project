# Simple functions to compute report stats


def count_by_status(tasks):
    """
    Compute status counts from a list of tasks.
    
    """
    counts = {}
    
    for task in tasks:
        status = task.status
        if status in counts:
            counts[status] += 1
        else:
            counts[status] = 1
    
    return counts


def count_by_category(tasks):
    """
    Compute category counts from a list of tasks.
    
    """
    counts = {}
    
    for task in tasks:
        category = task.category
        if category in counts:
            counts[category] += 1
        else:
            counts[category] = 1
    
    return counts

