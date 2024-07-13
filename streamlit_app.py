import streamlit as st
import random

def generate_local_questions(employee_info):
    base_questions = [
        f"How has your role as {employee_info['job_title']} evolved over the past year in the {employee_info['department']} department?",
        f"Reflecting on your {employee_info['years_of_service']} years with the company, how have you grown professionally?",
        f"Regarding your key responsibilities ({employee_info['key_responsibilities']}), which areas do you feel you've excelled in this year?",
        f"Let's discuss the goals you set this year: {employee_info['goals_set']}. How would you evaluate your progress on each?",
        f"You mentioned working on {employee_info['major_projects']}. Can you elaborate on your specific contributions to these projects?",
        f"Among your achievements this year ({employee_info['achievements']}), which one are you most proud of and why?",
        f"You've identified {employee_info['areas_for_improvement']} as areas for improvement. What steps have you taken to address these?",
        f"How have you applied the knowledge gained from your training in {employee_info['training_completed']} to your daily work?",
        "How have you collaborated with team members or other departments on key initiatives this year?",
        "What innovative solutions or process improvements have you implemented in your role?",
        "How do you plan to further develop your skills in the coming year?",
        "What are your career aspirations, and how do they align with your current role and the company's goals?",
        "Can you describe a challenging situation you faced this year and how you overcame it?",
        "How have you contributed to the team or department's overall performance and morale?",
        "What additional resources or support would help you perform your job more effectively?"
    ]
    
    additional_questions = [
        "How do you see your role evolving in the next year?",
        "What skills would you like to develop to enhance your performance?",
        "How have you demonstrated leadership in your current role?",
        "What do you consider your biggest professional achievement this year?",
        "How have you adapted to changes in the department or company this year?"
    ]
    
    questions = base_questions + random.sample(additional_questions, 5)
    random.shuffle(questions)
    return questions[:10]

def generate_summary_and_report(employee_info, questions_and_answers):
    summary = f"Annual Performance Review Summary for {employee_info['job_title']}\n\n"
    summary += f"Employee in the {employee_info['department']} department with {employee_info['years_of_service']} years of service.\n\n"
    summary += "Key Highlights:\n"
    summary += f"- Achievements: {employee_info['achievements']}\n"
    summary += f"- Areas for Improvement: {employee_info['areas_for_improvement']}\n"
    summary += f"- Training Completed: {employee_info['training_completed']}\n\n"
    summary += "Overall Performance Summary:\n"
    summary += "Based on the responses provided, the employee has demonstrated [insert overall performance assessment].\n\n"

    report = f"Comprehensive Annual Review Report for {employee_info['job_title']}\n\n"
    report += f"Employee: [Name]\nDepartment: {employee_info['department']}\nYears of Service: {employee_info['years_of_service']}\n\n"
    report += f"Key Responsibilities: {employee_info['key_responsibilities']}\n\n"
    report += "Detailed Review:\n\n"

    for q, a in questions_and_answers:
        report += f"Q: {q}\nA: {a}\n\n"

    report += "\nPerformance Analysis:\n"
    report += "1. Achievements and Successes:\n   [Summarize key achievements based on responses]\n\n"
    report += "2. Areas for Improvement:\n   [Identify areas needing improvement based on responses]\n\n"
    report += "3. Goal Completion:\n   [Assess progress on goals set at the beginning of the year]\n\n"
    report += "4. Skill Development:\n   [Comment on skill growth and application of training]\n\n"
    report += "5. Teamwork and Collaboration:\n   [Evaluate contributions to team dynamics]\n\n"
    report += "\nConclusion and Recommendations:\n"
    report += "[Provide an overall assessment and suggestions for future development]\n\n"
    report += "Prepared by: [Manager's Name]\nDate: [Current Date]"

    return summary, report

def main():
    st.title("Employee Review Question Generator")

    # Employee Information Input
    st.header("Employee Information")
    employee_info = {}
    employee_info['job_title'] = st.text_input("Job Title")
    employee_info['department'] = st.text_input("Department")
    employee_info['years_of_service'] = st.text_input("Years of Service")
    employee_info['key_responsibilities'] = st.text_area("Key Responsibilities")
    employee_info['goals_set'] = st.text_area("Goals Set This Year")
    employee_info['major_projects'] = st.text_area("Major Projects")
    employee_info['achievements'] = st.text_area("Key Achievements")
    employee_info['areas_for_improvement'] = st.text_area("Areas for Improvement")
    employee_info['training_completed'] = st.text_area("Training Completed")

    if st.button("Generate Questions"):
        if all(employee_info.values()):  # Check if all fields are filled
            st.session_state.questions = generate_local_questions(employee_info)
            st.session_state.answers = [""] * len(st.session_state.questions)
        else:
            st.warning("Please fill in all the employee information fields.")

    # Display questions and collect answers
    if 'questions' in st.session_state:
        st.header("Review Questions")
        for i, question in enumerate(st.session_state.questions):
            st.write(f"Q{i+1}: {question}")
            st.session_state.answers[i] = st.text_area(f"Answer {i+1}", st.session_state.answers[i], key=f"answer_{i}")

        if st.button("Generate Summary and Report"):
            questions_and_answers = list(zip(st.session_state.questions, st.session_state.answers))
            summary, report = generate_summary_and_report(employee_info, questions_and_answers)
            
            st.header("Summary")
            st.text_area("Summary", summary, height=300)
            
            st.header("Comprehensive Report")
            st.text_area("Report", report, height=500)

if __name__ == "__main__":
    main()