from django.core.management.base import BaseCommand
from core.models import Programmes, Subjects, RequirementRules, RequirementOptions


RULES = {

    # =========================================================
    # ENGINEERING
    # English 4 AND Mathematics 5 AND Physical Sciences 5
    # =========================================================

    "B Eng Electrical Engineering": [
        (3, [
            ("English", 4),
            ("Mathematics", 5),
            ("Physical Sciences", 5),
        ]),
    ],

    "B Eng Electrical Engineering and Computer Engineering": [
        (3, [
            ("English", 4),
            ("Mathematics", 5),
            ("Physical Sciences", 5),
        ]),
    ],

    "B Eng Mechanical Engineering": [
        (3, [
            ("English", 4),
            ("Mathematics", 5),
            ("Physical Sciences", 5),
        ]),
    ],

    "B Eng Mechatronic Engineering": [
        (3, [
            ("English", 4),
            ("Mathematics", 5),
            ("Physical Sciences", 5),
        ]),
    ],


    # =========================================================
    # NURSING
    #
    # English 4 AND Life Sciences 4
    # AND
    # Mathematics 3 OR Mathematical Literacy 4
    # =========================================================

    "B Nursing Science": [
        (2, [
            ("English", 4),
            ("Life Sciences", 4),
        ]),
        (1, [
            ("Mathematics", 3),
            ("Mathematical Literacy", 4),
        ]),
    ],


    # =========================================================
    # AGRICULTURE
    #
    # English 4 AND Mathematics 4 AND Physical Sciences 3
    # AND
    # Life Sciences 4 OR Agricultural Sciences 4
    # =========================================================

    "B Sc Agric: Agronomy": [
        (3, [
            ("English", 4),
            ("Mathematics", 4),
            ("Physical Sciences", 3),
        ]),
        (1, [
            ("Life Sciences", 4),
            ("Agricultural Sciences", 4),
        ]),
    ],

    "B Sc Agric: Animal Science": [
        (3, [
            ("English", 4),
            ("Mathematics", 4),
            ("Physical Sciences", 3),
        ]),
        (1, [
            ("Life Sciences", 4),
            ("Agricultural Sciences", 4),
        ]),
    ],

    "B Sc Agricultural Economics: Agribusiness Management": [
        (3, [
            ("English", 4),
            ("Mathematics", 4),
            ("Physical Sciences", 3),
        ]),
        (1, [
            ("Life Sciences", 4),
            ("Agricultural Sciences", 4),
        ]),
    ],


    # =========================================================
    # APPLIED MATHEMATICS
    # English 4 AND Mathematics 5 AND Physical Sciences 4
    # =========================================================

    "B Sc Applied Mathematics with Computer Sciences as Major 2": [
        (3, [
            ("English", 4),
            ("Mathematics", 5),
            ("Physical Sciences", 4),
        ]),
    ],

    "B Sc Applied Mathematics with Hydrology as Major 2": [
        (3, [
            ("English", 4),
            ("Mathematics", 5),
            ("Physical Sciences", 4),
        ]),
    ],

    "B Sc Applied Mathematics with Mathematics as Major 2": [
        (3, [
            ("English", 4),
            ("Mathematics", 5),
            ("Physical Sciences", 4),
        ]),
    ],

    "B Sc Applied Mathematics with Physics as Major 2": [
        (3, [
            ("English", 4),
            ("Mathematics", 5),
            ("Physical Sciences", 4),
        ]),
    ],

    "B Sc Applied Mathematics with Statistics as Major 2": [
        (3, [
            ("English", 4),
            ("Mathematics", 5),
            ("Physical Sciences", 4),
        ]),
    ],


    # =========================================================
    # CHEMISTRY
    # =========================================================

    "B Sc Chemistry with Computer Science as Major 2": [
        (3, [
            ("English", 4),
            ("Mathematics", 5),
            ("Physical Sciences", 4),
        ]),
    ],

    "B Sc Chemistry with Hydrology as Major 2": [
        (3, [
            ("English", 4),
            ("Mathematics", 5),
            ("Physical Sciences", 4),
        ]),
    ],

    "B Sc Chemistry with Mathematics as Major 2": [
        (3, [
            ("English", 4),
            ("Mathematics", 5),
            ("Physical Sciences", 4),
        ]),
    ],

    "B Sc Chemistry with Physics as Major 2": [
        (3, [
            ("English", 4),
            ("Mathematics", 5),
            ("Physical Sciences", 4),
        ]),
    ],


    # =========================================================
    # COMPUTER SCIENCE
    # =========================================================

    "B Sc Computer Science with Hydrology as Major 2": [
        (3, [
            ("English", 4),
            ("Mathematics", 5),
            ("Physical Sciences", 4),
        ]),
    ],

    "B Sc Computer Science with Mathematics as Major 2": [
        (3, [
            ("English", 4),
            ("Mathematics", 5),
            ("Physical Sciences", 4),
        ]),
    ],

    "B Sc Computer Science with Physics as Major 2": [
        (3, [
            ("English", 4),
            ("Mathematics", 5),
            ("Physical Sciences", 4),
        ]),
    ],

    "B Sc Computer Science with Statistics as Major 2": [
        (3, [
            ("English", 4),
            ("Mathematics", 5),
            ("Physical Sciences", 4),
        ]),
    ],


    # =========================================================
    # B SC4 FOUNDATION
    #
    # English 3 AND Mathematics 3 AND Physical Sciences 2
    # AND
    # Agricultural Sciences 3 OR Life Sciences 3
    # =========================================================

    "B Sc4 Foundation": [
        (3, [
            ("English", 3),
            ("Mathematics", 3),
            ("Physical Sciences", 2),
        ]),
        (1, [
            ("Agricultural Sciences", 3),
            ("Life Sciences", 3),
        ]),
    ],


    # =========================================================
    # CO-OPERATIVES / LOGISTICS / TRANSPORT
    #
    # English 3
    # AND
    # Mathematics 3 OR Mathematical Literacy 4
    # =========================================================

    "Dip Co-Operatives Management": [
        (1, [
            ("English", 3),
        ]),
        (1, [
            ("Mathematics", 3),
            ("Mathematical Literacy", 4),
        ]),
    ],

    "Dip Logistics Management": [
        (1, [
            ("English", 3),
        ]),
        (1, [
            ("Mathematics", 3),
            ("Mathematical Literacy", 4),
        ]),
    ],

    "Dip Transport Management": [
        (1, [
            ("English", 3),
        ]),
        (1, [
            ("Mathematics", 3),
            ("Mathematical Literacy", 4),
        ]),
    ],


    # =========================================================
    # HIGHER CERTIFICATE ACCOUNTANCY
    #
    # English 3
    # AND
    # Mathematics 3 OR Mathematical Literacy 4
    # =========================================================

    "H Cert Accountancy": [
        (1, [
            ("English", 3),
        ]),
        (1, [
            ("Mathematics", 3),
            ("Mathematical Literacy", 4),
        ]),
    ],
}


class Command(BaseCommand):

    help = "Import programme requirement rules."

    def handle(self, *args, **options):

        self.stdout.write("Clearing existing requirement rules...")

        RequirementOptions.objects.all().delete()
        RequirementRules.objects.all().delete()

        rules_created = 0
        options_created = 0

        for programme_name, programme_rules in RULES.items():

            try:
                programme = Programmes.objects.get(
                    programme_name=programme_name
                )
            except Programmes.DoesNotExist:
                self.stdout.write(
                    self.style.WARNING(
                        f"Programme not found: {programme_name}"
                    )
                )
                continue

            for required_count, subject_options in programme_rules:

                rule = RequirementRules.objects.create(
                    programme=programme,
                    rule_description=f"Requirement for {programme_name}",
                    required_count=required_count
                )

                rules_created += 1

                for subject_name, minimum_level in subject_options:

                    subject = Subjects.objects.get(
                        subject_name=subject_name
                    )

                    RequirementOptions.objects.create(
                        rule=rule,
                        subject=subject,
                        minimum_level=minimum_level
                    )

                    options_created += 1

        self.stdout.write("")
        self.stdout.write(
            self.style.SUCCESS(
                f"Import complete. Rules: {rules_created}, "
                f"Options: {options_created}"
            )
        )