from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, RadioField
from project2_Flask import generate_api


# Creates the user input elements found in search.html through flask, then imports them
class NewsForm(FlaskForm):
    # Returns book reviews or bestsellers list
    url_type = RadioField("url_type", choices=[
        ('reviews', 'Search for Reviews'),
        ('bestsellers', 'Search for Bestsellers')], default='reviews')

    # Search reviews by author's name, book title, or book ISBN
    search_by = SelectField('search_by', choices=[
        ('author', 'Author'),
        ('title', 'Title'),
        ('isbn', 'ISBN')])

    # Building off of the search_by field, allows user to input author/title/ISBN
    query = StringField("query")

    # The following functions read off of an API to generate the next field
    names = generate_api.generate_names()
    names_list = []

    for entry in names:
        names_list.append( (entry["list_name_encoded"], entry["display_name"]) )

    # Creates a list of bestselling categories for user to select
    list_type = SelectField('list_type', choices=names_list)


