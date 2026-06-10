import fastf1

print("Welcome to your Formula 1 AI!")
print("Powered by FastF1 - The go-to python package for all things Formula 1")
print("R = Race")
print("Q = Qualifying")
print("SQ = Sprint Qualifying")
print("S = Sprint")
print("FP1 = Free Practice 1")
print("FP2 = Free Practice 2")
print("FP3 = Free Practice 3")
year = int(input("Enter year of the session you want to analyze (e.g. 2024): "))
round_num = int(input("Enter round number (e.g. 1): "))
session_type = input(
    "Enter session type (R, Q, FP1, FP2, FP3, S, SQ): ").strip().upper()

session = fastf1.get_session(year, round_num, session_type)

# Only load session metadata and results, not lap timing data.
# This avoids FastF1 lap accuracy validation issues in some sessions.
session.load(laps=False)

print(session.results[['Abbreviation', 'TeamName', 'Position']])
