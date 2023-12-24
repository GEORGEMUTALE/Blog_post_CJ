import json
from jinja2 import Environment, FileSystemLoader

def generate_portfolio(data):
    env = Environment(loader=FileSystemLoader("templates"))
    index_template = env.get_template("templates.html")
    projects_template = env.get_template("projects_template.html")
    skills_template = env.get_template("skills_template.html")
    education_template = env.get_template("education_template.html")
    contact_template = env.get_template("contact_template.html")

    with open("output/index.html", "w") as file:
        file.write(index_template.render(
            projects=projects_template.render(projects=data["projects"]),
            skills=skills_template.render(skills=data["skills"]),
            education=education_template.render(education=data["education"]),
            contact=contact_template.render(contact=data["contact"])
        ))

def main():
    with open("data/portfolio_data.json", "r") as file:
        data = json.load(file)

    generate_portfolio(data)
    print("Portfolio generated successfully.")

if __name__ == "__main__":
    main()
