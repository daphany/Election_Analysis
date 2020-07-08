




counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county, values in counties_dict.items():
        message_to_me = (f"{county} county has {values:,} registered voters.")
        print(message_to_me)

voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]
for counties_dict in voting_data:
    for county, registered_voters in counties_dict.items():
        message = (f'{county} county has {registered_voters:,} registered voters.')
        print(message)
