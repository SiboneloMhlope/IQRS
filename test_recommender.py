from core.services.recommender import get_recommendations


marks = {
    "English": 4,
    "Mathematics": 5,
    "Physical Sciences": 5
}

result = get_recommendations(marks)

print("APS:", result["aps"])
print("\nRecommendations:")

for programme in result["recommendations"]:
    print(
        f"- {programme['programme']} "
        f"({programme['faculty']})"
    )