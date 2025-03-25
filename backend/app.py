from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/api/jobs', methods=['GET'])
def get_jobs():
    # Get parameters from the request
    field = request.args.get('field', '')
    geoid = request.args.get('geoid', '')
    page = request.args.get('page', 0)
    sort_by = request.args.get('sortBy', '')
    job_type = request.args.get('jobType', '')
    exp_level = request.args.get('expLevel', '')
    work_type = request.args.get('workType', '')
    filter_by_company = request.args.get('filterByCompany', '')
    
    # Print all parameters received from frontend
    print("\nReceived parameters from frontend:")
    print(f"Field: {field}")
    print(f"Geoid: {geoid}")
    print(f"Page: {page}")
    print(f"Sort By: {sort_by}")
    print(f"Job Type: {job_type}")
    print(f"Experience Level: {exp_level}")
    print(f"Work Type: {work_type}")
    print(f"Filter By Company: {filter_by_company}")
    print("----------------------------------------\n")
    
    # API endpoint and key
    api_key = "Your API key here"
    url = "https://api.scrapingdog.com/linkedinjobs"
    
    # Set up parameters for the API call
    params = {
        "api_key": api_key,
        "field": field,
        "geoid": geoid,
        "page": 1,
        "sortBy": sort_by,
        "jobType": job_type,
        "expLevel": exp_level,
        "workType": work_type,
        "filterByCompany": filter_by_company
    }
    
    # Remove empty parameters
    params = {k: v for k, v in params.items() if v}
    
    try:
        # Make the API call
        response = requests.get(url, params=params)
        
        if response.status_code == 200:
            return jsonify(response.json())
        else:
            return jsonify({
                "error": f"Request failed with status code: {response.status_code}",
                "message": response.text
            }), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)

