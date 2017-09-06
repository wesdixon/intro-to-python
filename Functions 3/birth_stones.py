def get_month_season(month):

    seasons = {"mar" : "Spring", "apr" : "Spring", "may" : "Spring", "jun" : "Summer", "jul" : "Summer", "aug" : "Summer",
                "sep" : "Fall", "oct" : "Fall", "nov" : "Fall", "dec" : "Winter", "jan" : "Winter", "feb" : "Winter"}

    return seasons[month]

def month_info(month, category):
    #  '''
    #  Input:  Str - Abbreviation of month, Str - information category to get for month
    #  Output: Str - category information for the specified month
     #
    #  Categories supported: 'full name'   ex: month_info('jan', 'full_name') -----> 'January'
    #                        'num_month'   ex: month_info('may', 'num_month') ----->  5
    #                        'birth_stone' ex: month_info('jul', 'birth_stone') ---> 'Ruby'
    #                        'season'      ex: month_info('oct', 'season') --------> 'Fall'
    #  '''
    full_names = {'jan': 'January', 'feb': 'February', 'mar': 'March', 'apr': 'April', 'may': 'May', 'jun': 'June', 'jul': 'July', 'aug': 'August', 'sep': 'September', 'oct': 'October', 'nov': 'November', 'dec': 'December'}

    month_nums = {'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6, 'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12}

    birth_stones = {'jan': 'Garnet', 'feb': 'Amethyst', 'mar': 'Aquamarine', 'apr': 'Diamond', 'may': 'Emerald', 'jun': 'Pearl', 'jul': 'Ruby', 'aug': 'Peridot', 'sep': 'Sapphire', 'oct': 'Opal', 'nov': 'Topaz', 'dec': 'Turquoise'}

    if category == "full_name":
        return full_names[month]

    elif category == "num_month":
        return month_nums[month]

    elif category == "birth_stone":
        return birth_stones[month]

    elif category == "season":
        return get_month_season(month)

    else:
        return "Incorrect input..."

input_month = raw_input("Please enter three letter lowercase month: ")
input_action = raw_input("Please enter full_name, num_month, birth_stone, season: ")
print month_info(input_month, input_action)
