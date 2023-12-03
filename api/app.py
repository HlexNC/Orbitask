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

    # Example request data:
    # {
    #     "openai_key": "sk-your-openai-api-key",
    #     "goals": ["Complete project report", "Attend team meeting", "Review client feedback"]
    # }

    # TODO: Set OpenAI key and implement goal processing logic with OpenAI
    # openai.api_key = openai_key
    # weekly_plan = process_goals_with_openai(goals)

    response = {
        "status": "success",
        "weekly_plan": {
            "Monday": ["Draft initial project report sections"],
            "Tuesday": ["Attend team meeting", "Consolidate meeting notes"],
            "Wednesday": ["Review client feedback", "Adjust report based on feedback"],
            "Thursday": ["Finalize project report"],
            "Friday": ["Submit report", "Prepare for next week's tasks"]
        }
    }

    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)