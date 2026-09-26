import json
import re

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from core.models import Programmes, RequirementRules
from core.services.recommender import get_recommendations


def extract_marks(message):
    """
    Extract common subject + level patterns from a learner's message.

    Examples:
    "English 4, Maths 5, Physical Sciences 5"
    "I got level 5 Mathematics and level 4 English"
    """

    subject_aliases = {
        "english": "English",
        "maths": "Mathematics",
        "math": "Mathematics",
        "mathematics": "Mathematics",
        "maths literacy": "Mathematical Literacy",
        "mathematical literacy": "Mathematical Literacy",
        "physical sciences": "Physical Sciences",
        "physical science": "Physical Sciences",
        "life sciences": "Life Sciences",
        "life science": "Life Sciences",
        "agricultural sciences": "Agricultural Sciences",
        "agricultural science": "Agricultural Sciences",
        "geography": "Geography",
        "history": "History",
        "economics": "Economics",
        "tourism": "Tourism",
        "dramatic art": "Dramatic Art",
        "visual art": "Visual Art",
        "isizulu": "IsiZulu",
    }

    marks = {}

    # "level 5 Mathematics"
    pattern_one = re.findall(
        r"level\s*(\d+)\s*(?:in\s*)?([A-Za-z]+(?:\s+[A-Za-z]+){0,2})",
        message,
        re.IGNORECASE,
    )

    for level, raw_subject in pattern_one:
        subject_key = raw_subject.strip().lower()

        if subject_key in subject_aliases:
            marks[subject_aliases[subject_key]] = int(level)

    # "Mathematics 5", "English 4"
    for raw_subject, subject_name in subject_aliases.items():

        pattern_two = re.search(
            rf"\b{re.escape(raw_subject)}\s*(?:level\s*)?(\d+)\b",
            message,
            re.IGNORECASE,
        )

        if pattern_two:
            marks[subject_name] = int(pattern_two.group(1))

    return marks


def programme_search(message):
    """
    Find programmes using useful words from the user's message.
    """

    message_lower = message.lower()

    stop_words = {
        "what",
        "are",
        "the",
        "requirements",
        "requirement",
        "for",
        "tell",
        "me",
        "about",
        "can",
        "i",
        "study",
        "with",
        "please",
        "do",
        "does",
        "this",
        "programme",
        "program",
        "course",
        "courses",
        "qualification",
        "qualifications",
        "in",
        "at",
        "unizulu",
    }

    words = set(re.findall(r"\b[a-zA-Z]+\b", message_lower))

    search_words = words - stop_words

    programmes = Programmes.objects.all()

    scored_matches = []

    for programme in programmes:

        name_words = set(
            re.findall(
                r"\b[a-zA-Z]+\b",
                programme.programme_name.lower()
            )
        )

        matched_words = search_words.intersection(name_words)

        if matched_words:
            scored_matches.append(
                (len(matched_words), programme)
            )

    scored_matches.sort(
        key=lambda item: item[0],
        reverse=True
    )

    return [programme for _, programme in scored_matches]

@csrf_exempt
def recommend(request):

    if request.method != "POST":
        return JsonResponse(
            {"error": "Only POST requests are allowed."},
            status=405
        )

    try:
        data = json.loads(request.body)
        marks = data.get("marks", {})

        result = get_recommendations(marks)

        return JsonResponse(result)

    except json.JSONDecodeError:
        return JsonResponse(
            {"error": "Invalid JSON."},
            status=400
        )

    except Exception as e:
        return JsonResponse(
            {"error": str(e)},
            status=500
        )


@csrf_exempt
def chat(request):

    if request.method != "POST":
        return JsonResponse(
            {"error": "Only POST requests are allowed."},
            status=405
        )

    try:
        data = json.loads(request.body)
        message = data.get("message", "").strip()

        if not message:
            return JsonResponse({
                "reply": "Hi! Tell me your subjects and levels, or ask me about a UNIZULU programme."
            })

        message_lower = message.lower()

        # Basic conversation
        if message_lower in ["hi", "hello", "hey", "hiya"]:

            return JsonResponse({
                "reply": (
                    "Hey! 👋 I'm IQRS, the UNIZULU programme assistant. "
                    "Tell me your subject levels and I can check which "
                    "programmes you may qualify for."
                )
            })

        if "help" in message_lower:

            return JsonResponse({
                "reply": (
                    "You can ask me things like:\n\n"
                    "• What can I study with English 4, Maths 5 and Physical Sciences 5?\n"
                    "• What are the requirements for Computer Science?\n"
                    "• Which programmes can I qualify for?\n"
                    "• Tell me about B Laws."
                )
            })

        # Extract subject marks from the message
        marks = extract_marks(message)

        # If the user supplied marks, run the recommendation engine
        if marks:

            result = get_recommendations(marks)

            recommendations = result.get("recommendations", [])

            if recommendations:

                programme_lines = []

                for programme in recommendations[:10]:

                    programme_lines.append(
                        f"• {programme['programme']} "
                        f"({programme['qualification_type']}, "
                        f"{programme['duration_years']} years)"
                    )

                reply = (
                    f"I detected these results: {marks}\n\n"
                    f"Your APS is {result['aps']}.\n\n"
                    "Based on the currently loaded UNIZULU requirements, "
                    "these programmes match:\n\n"
                    + "\n".join(programme_lines)
                )

            else:

                reply = (
                    f"I detected these results: {marks}\n\n"
                    f"Your APS is {result['aps']}.\n\n"
                    "I couldn't find a matching programme in the "
                    "currently loaded requirements."
                )

            return JsonResponse({
                "reply": reply,
                "marks": marks,
                "aps": result["aps"],
                "recommendations": recommendations
            })

        # Programme lookup
        matches = programme_search(message)

        if matches:

            programme = matches[0]

            rules = list(
                RequirementRules.objects
                .filter(programme=programme)
                .prefetch_related("requirementoptions_set__subject")
            )

            requirement_lines = []

            for rule in rules:

                options = list(rule.requirementoptions_set.all())

                if len(options) == 1:
                    option = options[0]

                    requirement_lines.append(
                        f"• {option.subject.subject_name}: "
                        f"Level {option.minimum_level}"
                    )

                elif rule.required_count == len(options):
                    option_text = " AND ".join(
                        f"{option.subject.subject_name} Level {option.minimum_level}"
                        for option in options
                    )

                    requirement_lines.append(
                        f"• {option_text}"
                    )

                else:
                    option_text = " OR ".join(
                        f"{option.subject.subject_name} Level {option.minimum_level}"
                        for option in options
                    )

                    requirement_lines.append(
                        f"• {option_text}"
                    )

            if requirement_lines:
                requirements_text = (
                    "\n\nAdmission requirements:\n"
                    + "\n".join(requirement_lines)
                )
            else:
                requirements_text = (
                    "\n\nAdmission requirements are not currently "
                    "loaded into the system for this programme."
                )

            return JsonResponse({
                "reply": (
                    f"{programme.programme_name}\n\n"
                    f"Faculty: {programme.faculty.faculty_name}\n"
                    f"Qualification: {programme.qualification_type}\n"
                    f"Duration: {programme.duration_years} years\n"
                    f"Minimum APS: {programme.minimum_points}"
                    f"{requirements_text}"
                ),
                "programme": {
                    "programme_id": programme.programme_id,
                    "programme": programme.programme_name,
                    "faculty": programme.faculty.faculty_name,
                    "qualification_type": programme.qualification_type,
                    "duration_years": programme.duration_years,
                    "minimum_points": programme.minimum_points,
                },
                "requirements": [
                    {
                        "rule": rule.rule_description,
                        "required_count": rule.required_count,
                        "options": [
                            {
                                "subject": option.subject.subject_name,
                                "minimum_level": option.minimum_level,
                            }
                            for option in rule.requirementoptions_set.all()
                        ],
                    }
                    for rule in rules
                ],
            })
        return JsonResponse({
            "reply": (
                "I can help with UNIZULU programmes. "
                "Try giving me your subject levels, for example: "
                "\"I got English 4, Mathematics 5 and Physical Sciences 5.\""
            )
        })

    except json.JSONDecodeError:

        return JsonResponse(
            {"error": "Invalid JSON."},
            status=400
        )

    except Exception as e:

        return JsonResponse(
            {"error": str(e)},
            status=500
        )