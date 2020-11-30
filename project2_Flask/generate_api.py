from project2_Flask import main_functions
import requests

# Though this was not included in the template, having a separate file for
# URL creation cleans up the project


# Used to add elements to the results.html page
def generate_data_from_api(url_type, search_by, query, list_type):
    # url_type if-else
    if url_type == "reviews":
        url = "https://api.nytimes.com/svc/books/v3/reviews.json?"

        # search_by if-else
        if search_by == "":
            url += "api-key="
        else:
            url += search_by + "=" + query + "&api-key="

    elif url_type == "bestsellers":
        url = "https://api.nytimes.com/svc/books/v3/lists/current/"
        url += list_type + ".json?api-key="

    # Reads API key JSON and adds it to url
    my_key_dict = main_functions.read_from_file("project2_Flask/JSON_Files/API_key.json")
    my_key = my_key_dict["API"]
    url += my_key

    # Generates API information from url, saves it locally to a file, and reads from that file
    response = requests.get(url).json()
    main_functions.save_to_file(response, "project2_Flask/JSON_Files/response.json")
    response_dict = main_functions.read_from_file("project2_Flask/JSON_Files/response.json")

    return response_dict


# Used specifically to make the bestselling-lists list
def generate_names():
    url = "https://api.nytimes.com/svc/books/v3/lists/names.json?api-key="
    my_key_dict = main_functions.read_from_file("project2_Flask/JSON_Files/API_key.json")
    url += my_key_dict["API"]
    response = requests.get(url).json()

    main_functions.save_to_file(response, "project2_Flask/JSON_Files/names.json")
    response_dict = main_functions.read_from_file("project2_Flask/JSON_Files/names.json")
    results = response_dict["results"]

    return results
