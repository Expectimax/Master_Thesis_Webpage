from django.contrib import admin

# Register your models here.
from .models import (Experiment, Image, AnswersFormalDelegate, AnswersPhenoDelegate, AnswersIntuitiveDelegate,
                     AnswersSocialDelegate, Visitors, Results, AnswersSocialBase, AnswersFormalBase, AnswersPhenoBase,
                     AnswersIntuitiveBase, FeedbackResultsFormal, FeedbackResultsIntuitive, FeedbackResultsPheno,
                     FeedbackResultsSocial, ExperimentSessionID)

admin.site.register(Experiment)
admin.site.register(Image)
admin.site.register(Visitors)
admin.site.register(Results)
admin.site.register(AnswersFormalDelegate)
admin.site.register(AnswersPhenoDelegate)
admin.site.register(AnswersIntuitiveDelegate)
admin.site.register(AnswersSocialDelegate)
admin.site.register(AnswersSocialBase)
admin.site.register(AnswersFormalBase)
admin.site.register(AnswersPhenoBase)
admin.site.register(AnswersIntuitiveBase)
admin.site.register(FeedbackResultsFormal)
admin.site.register(FeedbackResultsIntuitive)
admin.site.register(FeedbackResultsPheno)
admin.site.register(FeedbackResultsSocial)
admin.site.register(ExperimentSessionID)
