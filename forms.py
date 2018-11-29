# forms.py
 
from wtforms import Form, StringField, SelectField, validators
 
class MediaSearchForm(Form):
    choices = [('Title', 'Title'),
               ('Owner', 'Owner'),
               ('Publisher', 'Publisher')]
    select = SelectField('Search for titles:', choices=choices)
    search = StringField('')
    
class TitleForm(Form):
    media_types = [('Physical Copy', 'Physical Copy'),
                   ('PDF', 'PDF'),
                   ('Other', 'Other')]
    title = StringField('Title')
    subject_matter = StringField('Subject Matter')
    publisher = StringField('Publisher')
    media_type = SelectField('Media', choices=media_types)
    file_url = StringField('File Url (optional)', [validators.Optional(), validators.URL(message="File URL must be a valid URL (\"http://www.whatever.com\")")])
    owner = StringField('Owner Name')