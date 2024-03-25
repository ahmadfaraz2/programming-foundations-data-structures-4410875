user_preferences = {
    "language": "English",
    "font_size": "14px",
    "timezone": "GMT",
    "currency": "USD",
    "enable_location": False,
    "volume_level": 80,
    "date_format": "MM/DD/YYYY",
}


# changing keys values
user_preferences["language"] = "Spanish"

user_preferences["volume_level"] = 43

# Adding new keys and values
user_preferences["highlight_color"] = "Blue"

# Deleting for dictionary
del user_preferences["currency"]  # does not return value

removed_item = user_preferences.pop("date_format", "N/A")


print(user_preferences)
