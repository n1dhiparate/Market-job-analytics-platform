from flask import Blueprint, render_template
from .services.skill_extraction import get_top_skills
from .services.chart_generator import generate_bar_chart
from flask import request
from .services.skill_extraction import get_top_skills, get_work_type_distribution
from .services.chart_generator import generate_bar_chart, generate_pie_chart


main = Blueprint("main", __name__)

@main.route("/")
def home():
    return render_template("base.html")

@main.route("/dashboard")
def dashboard():

    work_type = request.args.get("work_type")

    # Full dataset stats
    full_skills, full_total = get_top_skills()

    # Filtered stats
    skills, total_jobs = get_top_skills(work_type)

    chart = generate_bar_chart(skills)

    work_type_data = get_work_type_distribution()
    pie_chart = generate_pie_chart(work_type_data)

    top_skill = list(skills.keys())[0] if skills else "N/A"

    # Growth calculation
    growth = 0
    if full_total != 0:
        growth = round(((total_jobs - full_total) / full_total) * 100, 2)

    return render_template(
        "dashboard.html",
        chart=chart,
        pie_chart=pie_chart,
        skills=skills.items(),
        total_jobs=total_jobs,
        unique_skills=len(skills),
        top_skill=top_skill,
        growth=growth,
        selected_work_type=work_type
    )
