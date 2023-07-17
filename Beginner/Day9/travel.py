travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
def add_new_country(country_visitied, times_visited, cities_visitied):
    new_travel = {}
    new_travel["country"] = country_visitied
    new_travel["visits"] = times_visited
    new_travel["cities"] = cities_visitied
    return new_travel

new_travel = add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
travel_log.append(new_travel)
# print(new_travel)
print(travel_log)
