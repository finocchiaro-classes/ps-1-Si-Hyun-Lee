prior_arrests = int(input("Prior arrests: "))
local_ordinance = input("Prior arrests for local ordinance (Y/N): ")
age_release = int(input("Age at release: "))

recidivism_score = 0

if 2 <= prior_arrests < 5:
    recidivism_score += 1
elif prior_arrests >= 5:
    recidivism_score += 2

if local_ordinance == 'Y':
    recidivism_score += 1

if 18 < age_release < 24:
    recidivism_score += 1
elif age_release >= 40:
    recidivism_score -= 1

print(f"The recidivism risk score is {recidivism_score}")

