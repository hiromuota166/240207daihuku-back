from django.db import models


class Meal(models.Model):
    mealid = models.SmallIntegerField(db_column='MealID', primary_key=True)  # Field name made lowercase.
    date = models.DateField(db_column='Date')  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=300, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Meal'


class Mealdetail(models.Model):
    mealdetailid = models.SmallIntegerField(db_column='MealDetailID', primary_key=True)  # Field name made lowercase.
    item = models.CharField(db_column='Item', max_length=30)  # Field name made lowercase.
    mealid = models.ForeignKey(Meal, models.DO_NOTHING, db_column='MealID')  # Field name made lowercase.
    price = models.SmallIntegerField(db_column='Price', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MealDetail'


class Mealparticipant(models.Model):
    mealid = models.ForeignKey(Meal, models.DO_NOTHING, db_column='MealID')  # Field name made lowercase.
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='UserID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MealParticipant'


class User(models.Model):
    userid = models.SmallIntegerField(db_column='UserID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'User'
