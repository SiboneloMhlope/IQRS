from core.models import Programmes, RequirementRules
from core.services.aps import calculate_aps


def get_recommendations(marks):

    aps = calculate_aps(marks)

    programmes = Programmes.objects.all()

    recommendations = []

    for programme in programmes:

        # APS must meet the programme minimum
        if aps < programme.minimum_points:
            continue

        # A programme without imported rules is NOT considered
        # qualified. This prevents incomplete data from producing
        # false recommendations.
        rules = list(
            RequirementRules.objects
            .filter(programme=programme)
            .prefetch_related("requirementoptions_set__subject")
        )

        if not rules:
            continue

        qualified = True
        matched_rules = []

        for rule in rules:

            options = rule.requirementoptions_set.all()

            satisfied_options = []

            for option in options:

                subject_name = option.subject.subject_name
                required_level = option.minimum_level

                learner_level = marks.get(subject_name)

                if (
                    learner_level is not None
                    and learner_level >= required_level
                ):
                    satisfied_options.append({
                        "subject": subject_name,
                        "required": required_level,
                        "learner_level": learner_level
                    })

            # The learner must satisfy the required number
            # of options in this rule.
            if len(satisfied_options) < rule.required_count:
                qualified = False
                break

            matched_rules.append({
                "rule": rule.rule_description,
                "required_count": rule.required_count,
                "matched": satisfied_options
            })

        if not qualified:
            continue

        recommendations.append({
            "programme_id": programme.programme_id,
            "programme": programme.programme_name,
            "faculty": programme.faculty.faculty_name,
            "qualification_type": programme.qualification_type,
            "duration_years": programme.duration_years,
            "minimum_points": programme.minimum_points,
            "aps": aps,
            "requirements": matched_rules
        })

    return {
        "aps": aps,
        "recommendations": recommendations
    }