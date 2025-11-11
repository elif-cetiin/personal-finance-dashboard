CATEGORY_RULES = {
    "STARBUCKS": "Coffee",
    "WALMART": "Groceries",
    "UBER": "Transport",
    "AMAZON": "Shopping",
    "SHELL": "Gas",
}

def categorize(description):
    desc = description.upper()
    for keyword, cat in CATEGORY_RULES.items():
        if keyword in desc:
            return cat
    return "Other"
