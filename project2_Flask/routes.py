from project2_Flask import app
from flask import request, render_template
from project2_Flask import forms, generate_api


# Renders index.html, which links to search.html for convenience
@app.route('/')
def main():
    return render_template("index.html")


# Renders search.html file and imports flask forms
@app.route('/search', methods=['GET', 'POST'])
def search():
    my_form = forms.NewsForm(request.form)

    # if statement for when search.html is requested with POST
    if request.method == "POST":
        url_type = request.form["url_type"]
        search_by = request.form["search_by"]
        query = request.form["query"]
        list_type = request.form["list_type"]
        # POST means user-input; method must take user input
        # Generates requested data using API key

        # Uses flask fields to create a url
        response = generate_api.generate_data_from_api(url_type, search_by, query, list_type)

        # The review and bestseller APIs generate different JSON outputs
        # This makes sure that the program reads those files correctly
        response_result = response["results"]
        if url_type == "bestsellers":
            response_result = response_result["books"]

        return render_template("results.html", response_books=response_result, url_type=url_type,
                               search_by=search_by, query=query, list_type=list_type)

    # else statement for when search.html is requested with GET
    else:
        return render_template("search.html", form=my_form)