as was shown in flask routes exc in QA and Earls github excercise 4


This code can be modified to create a method where checks can happen on the text to look out for words.
'
    # def validate_username(self, username):
    #     if username.data.lower() == 'admin':
    #         raise ValidationError("Can't use admin as a username! Try again.")
        
# class checkAdmin:
#     def __init__(self, message=None):
#         if not message:
#             message = 'Please choose another username.'
#         self.message = message

#     def __call__(self, form, field):
#         if field.data.lower() == 'admin':
#             raise ValidationError(self.message)