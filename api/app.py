from flask import Flask, request, jsonify, abort

app = Flask(__name__)

@app.route('/api/weekly-planning', methods=['POST'])
def weekly_planning():
    # Extract data from request
    data = request.json
    if not data or 'openai_key' not in data or 'goals' not in data:
        abort(400, description="Missing 'openai_key' or 'goals' in request data")

    openai_key = data.get('openai_key')
    goals = data.get('goals')

    # TODO: Set OpenAI key and implement goal processing logic with OpenAI
    # openai.api_key = openai_key
    # weekly_plan = process_goals_with_openai(goals)

    # Mock response (TODO replace with actual logic)
    weekly_plan = {
        "Monday": ["Task 1", "Task 2"],
        "Tuesday": ["Task 3"]
        # ... other days
    }

    response = {
        "status": "success",
        "weekly_plan": weekly_plan
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)