from django.db import models
from djangoratings.fields import AnonymousRatingField, RatingField


__all__ = ['RatingTestModel', ]


class RatingTestModel(models.Model):
    rating = AnonymousRatingField(range=2, can_change_vote=True)
    rating2 = RatingField(range=2, can_change_vote=False)
    
    class Meta:
        db_table = "djangoratings_ratingtestmodel"

    def __unicode__(self):
        return unicode(self.pk)
