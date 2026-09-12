from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


# ======================================================
# HOME
# ======================================================

@app.route("/")
def home():
    return jsonify({
        "message": "Personal Learning Platform Backend API is running"
    })


# ======================================================
# DASHBOARD API
# ======================================================

@app.route("/api/dashboard", methods=["GET"])
def get_dashboard():

    dashboard_data = {
        "learning_goal": "Become a Full Stack Developer",
        "overall_progress": 68,
        "courses_completed": 4,
        "total_courses": 6,
        "current_courses": 2,
        "learning_streak": 12
    }

    return jsonify(dashboard_data)


# ======================================================
# COURSES API
# ======================================================

@app.route("/api/courses", methods=["GET"])
def get_courses():

    courses = [
        {
            "id": 1,
            "title": "JavaScript Fundamentals",
            "difficulty": "Intermediate",
            "description": "Core concepts: variables, functions, DOM, and events.",
            "progress": 72
        },
        {
            "id": 2,
            "title": "Responsive Web Design",
            "difficulty": "Intermediate",
            "description": "Fluid grids, Flexbox, media queries, and Container Queries.",
            "progress": 54
        }
    ]

    return jsonify({
        "courses": courses
    })


# ======================================================
# CONTINUE COURSE API
# ======================================================

@app.route("/api/courses/<int:course_id>/continue", methods=["POST"])
def continue_course(course_id):

    courses = [
        {
            "id": 1,
            "title": "JavaScript Fundamentals",
            "progress": 72
        },
        {
            "id": 2,
            "title": "Responsive Web Design",
            "progress": 54
        }
    ]

    selected_course = None

    for course in courses:
        if course["id"] == course_id:
            selected_course = course
            break

    if selected_course is None:
        return jsonify({
            "success": False,
            "message": "Course not found"
        }), 404

    return jsonify({
        "success": True,
        "message": f"Continuing your learning journey with {selected_course['title']}.",
        "course": selected_course
    })


# ======================================================
# RECOMMENDATIONS API
# ======================================================

@app.route("/api/recommendations", methods=["GET"])
def get_recommendations():

    recommendations = [
        {
            "id": 1,
            "title": "JavaScript Functions",
            "type": "Recommended",
            "description": "Master higher-order functions, closures, and scope to write cleaner code."
        },
        {
            "id": 2,
            "title": "CSS Grid Layout",
            "type": "Skill Gap",
            "description": "Build complex, responsive layouts with ease using CSS Grid."
        },
        {
            "id": 3,
            "title": "Git & GitHub Basics",
            "type": "Next Step",
            "description": "Version control, branching, and collaboration for your projects."
        }
    ]

    return jsonify({
        "recommendations": recommendations
    })


# ======================================================
# START RECOMMENDATION API
# ======================================================

@app.route("/api/recommendations/<int:recommendation_id>/start", methods=["POST"])
def start_recommendation(recommendation_id):

    recommendations = [
        {
            "id": 1,
            "title": "JavaScript Functions"
        },
        {
            "id": 2,
            "title": "CSS Grid Layout"
        },
        {
            "id": 3,
            "title": "Git & GitHub Basics"
        }
    ]

    selected_recommendation = None

    for recommendation in recommendations:
        if recommendation["id"] == recommendation_id:
            selected_recommendation = recommendation
            break

    if selected_recommendation is None:
        return jsonify({
            "success": False,
            "message": "Recommendation not found"
        }), 404

    return jsonify({
        "success": True,
        "message": f"{selected_recommendation['title']} has been added to your learning plan.",
        "recommendation": selected_recommendation
    })


# ======================================================
# SKILLS API
# ======================================================

@app.route("/api/skills", methods=["GET"])
def get_skills():

    skills = [
        {"id": 1, "name": "HTML", "level": "Advanced", "progress": 90},
        {"id": 2, "name": "CSS", "level": "Intermediate", "progress": 72},
        {"id": 3, "name": "JavaScript", "level": "Intermediate", "progress": 65},
        {"id": 4, "name": "Responsive Design", "level": "Intermediate", "progress": 70},
        {"id": 5, "name": "Git", "level": "Beginner", "progress": 45}
    ]

    return jsonify({
        "skills": skills
    })


# ======================================================
# PRACTICE API
# ======================================================

@app.route("/api/practice", methods=["GET"])
def get_practice():

    practice_topics = [
        {
            "id": 1,
            "title": "HTML Basics",
            "description": "Practice semantic structure, forms, and accessibility."
        },
        {
            "id": 2,
            "title": "CSS Layout",
            "description": "Practice Flexbox, Grid, and responsive techniques."
        },
        {
            "id": 3,
            "title": "JavaScript",
            "description": "Practice DOM manipulation, events, and basic algorithms."
        }
    ]

    return jsonify({
        "practice": practice_topics
    })


# ======================================================
# START PRACTICE API
# ======================================================

@app.route("/api/practice/<int:practice_id>/start", methods=["POST"])
def start_practice(practice_id):

    practice_topics = [
        {
            "id": 1,
            "title": "HTML Basics"
        },
        {
            "id": 2,
            "title": "CSS Layout"
        },
        {
            "id": 3,
            "title": "JavaScript"
        }
    ]

    selected_practice = None

    for practice in practice_topics:
        if practice["id"] == practice_id:
            selected_practice = practice
            break

    if selected_practice is None:
        return jsonify({
            "success": False,
            "message": "Practice topic not found"
        }), 404

    return jsonify({
        "success": True,
        "message": f"Starting {selected_practice['title']} practice.",
        "practice": selected_practice
    })


# ======================================================
# ROADMAP API
# ======================================================

@app.route("/api/roadmap", methods=["GET"])
def get_roadmap():

    roadmap = [
        {"id": 1, "title": "HTML", "status": "Completed"},
        {"id": 2, "title": "CSS", "status": "Completed"},
        {"id": 3, "title": "JavaScript", "status": "Current"},
        {"id": 4, "title": "Git & GitHub", "status": "Upcoming"},
        {"id": 5, "title": "Full Stack Basics", "status": "Upcoming"}
    ]

    return jsonify({
        "roadmap": roadmap
    })


# ======================================================
# LEARNING GOAL API
# ======================================================

@app.route("/api/goal", methods=["POST"])
def set_learning_goal():

    data = request.get_json()

    if not data or "goal" not in data:
        return jsonify({
            "success": False,
            "message": "Learning goal is required"
        }), 400

    goal = data["goal"]

    if not isinstance(goal, str) or not goal.strip():
        return jsonify({
            "success": False,
            "message": "Learning goal must be a valid text"
        }), 400

    return jsonify({
        "success": True,
        "message": "Learning goal updated successfully",
        "goal": goal.strip()
    })


# ======================================================
# RUN SERVER
# ======================================================

if __name__ == "__main__":
    app.run(debug=True)