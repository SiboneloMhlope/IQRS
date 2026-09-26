def calculate_aps(marks):
    """
    Calculate APS using the best 6 subjects,
    excluding Life Orientation.
    """

    excluded_subjects = {"Life Orientation"}

    valid_levels = [
        level
        for subject, level in marks.items()
        if subject not in excluded_subjects
        and isinstance(level, int)
        and 1 <= level <= 7
    ]

    valid_levels.sort(reverse=True)

    return sum(valid_levels[:6])