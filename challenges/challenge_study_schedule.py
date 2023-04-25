def study_schedule(permanence_period, target_time="a"):
    count = 0
    try:
        for element in permanence_period:
            if int(target_time) in range(element[0], element[1] + 1):
                count += 1
    except (TypeError, ValueError, AssertionError):
        return None
    return count
