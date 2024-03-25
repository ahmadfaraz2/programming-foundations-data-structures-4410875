user_preferences = {
    "timezone": "GMT",
    "language": "English",
    "notifications": None,
    "currency": "USD",
    "theme": None,
}


# def update_preferences(user_pref):
#     for key, value in user_pref.items():
#         if value is None:
#             del user_pref[key]
#     return {user_pref}


def update_preferences(user_perf):
    updated_preferences = {}
    for key, value in user_perf.items():
        if value is not None:
            updated_preferences[key] = value
    return updated_preferences


def update_preferences_v2(user_perf):
    return {key: value for key, value in user_perf.items() if value is not None}


print(update_preferences(user_preferences))
print(update_preferences_v2(user_preferences))
