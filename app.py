from flask import Flask, render_template

app = Flask(__name__)

# ----------------- INDEX PAGE DATA -----------------
index_data = {
    "tagline": "Engineer by Profession, Adventurer by Passion, Friend by Choice.",
    "intro_name": "Hi I’m Balagopal",
    "intro_role": "Python Developer | AI & ML Enthusiast",
    "intro_subtext": "Explore my journey through this portfolio.",
    "portrait": "images/balu.jpg",
    "resume": "Balagopal_Resume.pdf",
    "commands": {
        "about": "/journey",
        "skills": "/skills",
        "projects": "/projects",
        "experience": "/experience",
        "contact": "/contact",
        "download": "/static/images/balagopal.pdf"
    }
}

# ----------------- JOURNEY PAGE DATA -----------------
journey_data = {
    "name": "Balagopal M",
    "sections": {
        "intro": """Hi, I'm Balagopal M, a Python developer and AI/ML enthusiast from Kochi with a foundation 
                    in Electronics and Communication Engineering. I am passionate about building intelligent, 
                    user-centric applications that leverage AI and machine learning to solve real-world problems, 
                    enhance efficiency, and create meaningful impact. Beyond technology, I am an avid cricket lover, 
                    travel enthusiast, and photography hobbyist.""",

        "summary": """I am a Python developer and AI/ML enthusiast with expertise in designing and developing 
                      full-stack applications and AI systems that address real-world challenges. 
                      My skills span AI, Machine Learning, NLP, with a strong focus on computer vision and 
                      conversational AI. Currently, I am building an NLP-powered CRM chatbot to automate
                      client engagement, and I have also developed systems for deepfake detection and real-time
                      human monitoring. I am passionate about creating technology that is powerful, ethical, explainable, 
                      and secure, blending technical excellence with practical, user-centric solutions.""",

        "skills": {
            "Languages": ["Python", "Dart", "Java", "JavaScript", "SQL", "PHP"],
            "AI/ML & NLP": ["TensorFlow", "PyTorch", "OpenCV", "YOLOv8", "Rasa", "NLTK"],
            "App & Web Development": ["Flutter", "Django", "Flask", "Firebase"],
            "Tools & Platforms": ["GitHub", "VS Code", "Android Studio", "Google Colab", "Render"]
        },

        "journey": {
            "current_role": """At King’s Labs Innovation & Technology, I’m developing a CRM chatbot using Rasa and Django. 
                               I design NLP pipelines for intent classification and entity extraction and build backend 
                               actions to handle client data, track inquiries, and automate follow-ups—enhancing customer 
                               engagement and operational efficiency.""",
            "past_experience": """I’ve gained hands-on experience through internships in Embedded Systems & Robotics (TechMaghi), 
                                  Full-Stack Development (Unified Mentor), and Python Programming (CodeAlpha)."""
        },

        "personality": 
            """I thrive on collaboration, clear communication, and teamwork, believing the best results come from 
                        working together with focus and clarity. I am an avid learner and problem-solver, always seeking
                        personal and professional growth. Beyond technology, I am passionate about sports, travel, and 
                        photography. I have represented my district in U-16 and U-19 cricket tournaments, which strengthened 
                        my discipline, leadership, and resilience. Traveling allows me to explore new cultures and perspectives, 
                        while photography helps me capture and appreciate the beauty in everyday moments, fueling creativity 
                        and inspiration in all areas of life.""",
        "values": {}
    }
}

# ----------------- EXPERIENCE DATA -----------------
experience_data = [
    {
        "role": "Junior Python Developer",
        "company": "King’s Lab Innovation & Technology",
        "location": "Kochi, Kerala",
        "duration": "Aug 2025 – Present",
        "type": "Full-Time",
        "details": [
            "Developing an NLP-powered CRM chatbot using Rasa and Django.",
            "Designed NLP pipelines for intent classification and entity extraction.",
            "Built backend actions in Python + MySQL for client data retrieval and inquiry tracking.",
            "Learned enterprise-level secure API handling and deployment workflows."
        ]
    },
    {
        "role": "Full-Stack Development Intern",
        "company": "Unified Mentor",
        "location": "Remote",
        "duration": "Jun 2025 – Jul 2025",
        "type": "Internship",
        "details": [
            "Developed Hospital & Gym Management Systems using PHP, SQL, and Firebase.",
            "Worked on authentication, CRUD operations, and database design.",
            "Built responsive UI and improved cross-device accessibility."
        ]
    },
    {
        "role": "Python Programming Intern",
        "company": "CodeAlpha",
        "location": "Remote",
        "duration": "Dec 2024",
        "type": "Internship",
        "details": [
            "Strengthened Python fundamentals through structured projects.",
            "Built small automation scripts for solving real-world problems."
        ]
    },
    {
        "role": "Embedded Systems & Robotics Intern",
        "company": "TechMaghi",
        "location": "Kakkanad, Kerala",
        "duration": "May 2023 – Jun 2023",
        "type": "Internship",
        "details": [
            "Gained exposure to Arduino programming and embedded hardware basics.",
            "Worked on microcontroller projects integrating electronics and coding."
        ]
    },
    {
        "role": "Robotics Intern",
        "company": "Kodachy",
        "location": "Remote",
        "duration": "Feb 2023",
        "type": "Internship",
        "details": [
            "Learned robotics fundamentals including sensors and automation.",
            "Built simple robotics projects remotely with focus on automation."
        ]
    },
    {
        "role": "Social Internship (Project Ganitam – Teaching Team)",
        "company": "Insight for Innovation (Enlite Initiative)",
        "location": "Thrithala, Kerala",
        "duration": "Aug 2022",
        "type": "Internship",
        "details": [
            "Contributed as part of the teaching team delivering sessions to rural students.",
            "Helped improve mathematics problem-solving skills among students.",
            "Learned how to communicate technical knowledge in simple terms."
        ]
    }
]

# ----------------- ROUTES -----------------
@app.route("/")
def index():
    return render_template("index.html", data=index_data)

@app.route("/journey")
def journey_page():
    return render_template("journey.html", data=journey_data)

@app.route("/skills")
def skills_page():
    skills = journey_data['sections']['skills']
    return render_template("skills.html", skills=skills)

@app.route("/projects")
def projects_page():
    projects = [
        {
            "title": "Deepfake Video Detection System With Explainable AI",
            "video": "videos/deepfake.mp4",
            "details": [
                "Trained and fine-tuned XceptionNet using transfer learning and early stopping, achieving high accuracy in detecting deepfakes.",
                "Integrated Grad-CAM for XAI, enabling heatmap generation to highlight manipulated facial regions.",
                "Evaluated model performance with precision, recall, F1-score, achieving reliable detection against Celeb DF V2."
            ],
            "stack": ["Python", "VS Code", "TensorFlow", "Keras", "XceptionNet", "Grad-CAM", "OpenCV", "HTML", "CSS", "JavaScript"]
        },
        {
            "title": "Real Vs AI Generated Image Detection Using Machine Learning",
            "img": ["images/real.jpg"],   # FIXED (was "images")
            "details": [
                "Built an image classifier with EfficientNet achieving 97% accuracy across 10 classes.",
                "Improved detection reliability in single-object environments with future scope for multi-object and video deepfake detection."
            ],
            "stack": ["Python", "VS Code", "EfficientNet", "NumPy", "HTML", "CSS", "JavaScript"]
        },
        {
            "title": "Advanced Fracture And Tumor Detection System",
            "img": [  # FIXED
                "images/fracture1.jpg",
                "images/fracture2.jpg",
                "images/fracture3.jpg"
            ],
            "details": [
                "Collaborated on an ML system to detect fractures and tumors from X-ray scans.",
                "Contributed to data preprocessing, evaluation, and implementation phases using ML workflows."
            ],
            "stack": ["Python", "VS Code", "Scikit-learn", "NumPy", "Pandas", "OpenCV", "HTML", "CSS", "JavaScript"]
        },
        {
            "title": "Real-Time Fall Monitoring and Alert System",
            "img": ["images/fall.jpg"],  # FIXED
            "details": [
                "Developed a real-time fall detection system using YOLOv8 and posture angle analysis.",
                "Implemented logic to monitor immobility for a customizable duration (e.g., 30 seconds) and integrated Twilio API to send emergency SMS alerts."
            ],
            "stack": ["Python", "OpenCV", "YOLOv8", "TensorFlow", "NumPy", "Twilio API", "MovNet", "playsound"]
        },
        {
            "title": "Human Follower System",
            "video": "videos/tracker.mp4",
            "details": [
                "Built a real-time human tracking system by integrating YOLOv8 for person detection and MoveNet (TFLite) for pose estimation.",
                "Implemented distance and steering angle estimation using camera calibration and shoulder keypoints.",
                "Designed smoothing filters, lock/unlock logic, and stability enhancements for robust tracking.",
                "Developed an OpenCV-based UI displaying live telemetry including angle, distance, direction, and proximity warnings."
            ],
            "stack": ["Python", "OpenCV", "TensorFlow Lite", "Ultralytics YOLOv8", "NumPy", "VS Code"]
        },
        {
            "title": "Executive CRM Chatbot",
            "video": "videos/bot.mp4",
            "details": [
                "Developed and deployed an intelligent CRM chatbot using Rasa and Django to handle clients, inquiries, leads, orders, and follow-ups via natural conversations.",
                "Designed and curated extensive NLU training data (intents, entities, stories) to improve intent classification and entity extraction accuracy.",
                "Implemented backend actions in Python with Django and MySQL for case-insensitive queries, client detail retrieval, inquiry tracking, and follow-up scheduling."
            ],
            "stack": ["Python", "Rasa", "Django", "MySQL", "Tailwind", "VS Code"]
        },
        {
            "title": "Finance Tracker Application",
            "video": "videos/finance.mp4",
            "details": [
                "Developed an offline finance tracking application enabling users to manage budgets, expenses, and savings efficiently with local data storage through SQLite.",
                "Implemented an alert and notification system for budget overages, with responsive UI/UX across devices."
            ],
            "stack": ["Dart", "Flutter", "Android Studio", "VS Code", "HTML", "CSS", "JavaScript"]
        },
        {
            "title": "LingoDefine – Flutter-Based Translator and Dictionary App",
            "video": "videos/translator.mp4",
            "details": [
                "Developed a mobile app for translation and word definition with offline support.",
                "Focused on cross-device UI responsiveness and real-time language switching."
            ],
            "stack": ["Dart", "Flutter", "Android Studio", "Flutter DevTools", "HTML"]
        },
        {
            "title": "Hospital Management System",
            "img": [  # FIXED
                "images/h1.png",
                "images/h2.png",
                "images/h3.png"
            ],
            "details": [
                "Engineered a multi-role hospital system for doctors, patients, and administrators with secure login.",
                "Focused on secure session handling, data validation, dynamic form handling, and real-time updates."
            ],
            "stack": ["HTML", "CSS", "JavaScript", "PHP", "SQL", "Firebase", "phpMyAdmin", "VS Code"]
        },
        {
            "title": "Gym Management System",
            "img": [  # FIXED
                "images/gym1.png",
                "images/gym2.png",
                "images/gym3.png",
                "images/gym4.png"
            ],
            "details": [
                "Built a responsive web app to handle gym member registrations, schedules, and payments.",
                "Focused on building a responsive interface with smooth navigation and real-time data updates using Firebase and structured data management with SQL."
            ],
            "stack": ["HTML", "CSS", "JavaScript", "PHP", "SQL", "Firebase", "phpMyAdmin", "VS Code"]
        }
    ]
    return render_template("projects.html", projects=projects)


@app.route("/experience")
def experience_page():
    return render_template("experience.html", experiences=experience_data)

@app.route("/contact")
def contact_page():
    socials = {
        "email": "baluu1603@gmail.com",
        "linkedin": "https://www.linkedin.com/in/balagopal-m-1b9a7b226",
        "github": "https://github.com/yourusername",
        "resume": "/static/Balagopal_Resume.pdf",
    }
    return render_template("contact.html", socials=socials)

if __name__ == "__main__":
    app.run(debug=True)
