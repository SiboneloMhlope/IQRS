from django.db import models


class Faculties(models.Model):
    faculty_id = models.AutoField(primary_key=True)
    faculty_name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'faculties'


class Programmes(models.Model):
    programme_id = models.AutoField(primary_key=True)
    faculty = models.ForeignKey(Faculties, models.DO_NOTHING)
    programme_name = models.CharField(max_length=255)
    duration_years = models.IntegerField()
    minimum_points = models.IntegerField()
    qualification_type = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'programmes'


class Subjects(models.Model):
    subject_id = models.AutoField(primary_key=True)
    subject_name = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'subjects'


class Requirements(models.Model):
    requirement_id = models.AutoField(primary_key=True)
    programme = models.ForeignKey(Programmes, models.DO_NOTHING)
    subject = models.ForeignKey(Subjects, models.DO_NOTHING)
    minimum_level = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'requirements'