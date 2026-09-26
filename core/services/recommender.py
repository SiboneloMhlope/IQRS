from core.models import Programmes, Requirements
from core.services.aps import calculate_aps


def get_recommendations(marks):
    """
    Find UNIZULU programmes that the learner qualifies for.

    marks example:
    {
        "English": 4,
        "Mathematics": 5,
        "Physical Sciences": 5
    }
    """

    aps = calculate_aps(marks)

    programmes = Programmes.objects.all()

    recommendations = []

    for programme in programmes:

        # First check the programme's minimum APS
        if aps < programme.minimum_points:
            continue

        # Get simple subject requirements
        requirements = Requirements.objects.filter(
            programme=programme
        ).select_related("subject")

        qualified = True
        matched_requirements = []

        for requirement in requirements:
            subject_name = requirement.subject.subject_name
            required_level = requirement.minimum_level

            learner_level = marks.get(subject_name)

            if learner_level is None:
                qualified = False
                break

            if learner_level < required_level:
                qualified = False
                break

            matched_requirements.append({
                "subject": subject_name,
                "required": required_level,
                "learner_level": learner_level
            })

        if qualified:
            recommendations.append({
                "programme_id": programme.programme_id,
                "programme": programme.programme_name,
                "faculty": programme.faculty.faculty_name,
                "qualification_type": programme.qualification_type,
                "duration_years": programme.duration_years,
                "minimum_points": programme.minimum_points,
                "aps": aps,
                "requirements": matched_requirements
            })

    return {
        "aps": aps,
        "recommendations": recommendations
    }