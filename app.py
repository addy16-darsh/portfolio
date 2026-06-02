from flask import Flask, render_template

app = Flask(__name__)

# ─────────────────────────── INDEX ───────────────────────────
index_data = {
    "tagline": "Engineer by Profession, Adventurer by Passion, Friend by Choice.",
    "intro_name": "Hi, I'm Balagopal",
    "intro_role": "Python Developer | AI & ML Enthusiast",
    "intro_subtext": "Explore my journey through this portfolio.",
    "portrait": "images/balu.jpg",
    "commands": {
        "about":      "/journey",
        "skills":     "/skills",
        "projects":   "/projects",
        "experience": "/experience",
        "hobbies":    "/hobbies",
        "contact":    "/contact",
        # 'view' opens the résumé PDF in a new tab (handled in JS)
        "view":       "/static/images/balagopal.pdf",
    },
}

# ─────────────────────────── JOURNEY ─────────────────────────
journey_data = {
    "name": "Balagopal M",
    "sections": {
        "intro": (
            "Hi, I'm Balagopal M — a Python developer and AI/ML enthusiast originally from "
            "Mumbai and now based in Kochi, with a foundation in Electronics and Communication "
            "Engineering. I love creating intelligent, user-centric applications that bring the "
            "power of AI and machine learning into real-world use — solving problems, enhancing "
            "efficiency, and creating meaningful impact. My journey in technology began with "
            "curiosity for electronics and coding, which gradually evolved into a passion for "
            "AI and full-stack development. Over time I've explored computer vision, NLP, and "
            "conversational AI, building solutions that balance technical depth with practical "
            "usability. Currently I work at King's Labs Innovation & Technology, developing an "
            "NLP-powered CRM chatbot using Rasa and Django that automates client interactions, "
            "manages data, and streamlines engagement. I've also worked on deepfake detection "
            "and real-time human monitoring, integrating explainability and ethical AI practices "
            "to make systems more transparent and trustworthy."
        ),

        "skills": {
            "Languages":             ["Python", "Dart", "Java", "JavaScript", "SQL", "PHP"],
            "AI / ML & NLP":         ["TensorFlow", "PyTorch", "OpenCV", "YOLOv8", "Rasa"],
            "App & Web Development": ["Flutter", "Django", "Flask", "Firebase"],
            "Tools & Platforms":     ["GitHub", "VS Code", "Android Studio", "Google Colab", "Render"],
        },

        "journey": {
            "current_role": (
                "At King's Labs I design NLP pipelines for intent classification and entity "
                "extraction, and implement backend workflows to automate follow-ups and improve "
                "client communication. Before this I gained hands-on experience through diverse "
                "internships that helped me build a strong foundation across multiple domains:"
            ),
            "past_experience": [
                "Embedded Systems & Robotics (TechMaghi) – Hands-on hardware-software integration.",
                "Full-Stack Development (Unified Mentor) – Building scalable web applications.",
                "Python Programming (CodeAlpha) – Strengthening programming and problem-solving foundations.",
            ],
            "outro": (
                "These experiences shaped my ability to work across domains, from low-level "
                "embedded systems to high-level AI applications."
            ),
        },

        "personality": {
            "intro": "I believe learning never stops, and my passions outside technology play a big role in who I am.",
            "items": [
                (
                    "Cricket – Passionate about cricket since childhood; represented my district in "
                    "U-16 and U-19 tournaments. Playing at this level taught me discipline, leadership, "
                    "resilience, and teamwork — qualities I carry into my professional life."
                ),
                (
                    "Travel – My way of breaking boundaries and exploring perspectives. Each journey "
                    "introduces me to new cultures and stories, broadening my worldview and reminding "
                    "me that creativity often comes from stepping outside comfort zones."
                ),
                (
                    "Photography – More than a hobby; a way of slowing down and observing the world "
                    "closely. I enjoy capturing everyday beauty — from fleeting expressions to "
                    "landscapes — and many of my favourite shots are travel memories that tell a story "
                    "of place, people, and moment."
                ),
            ],
            "outro": "These interests balance my life and bring unique dimensions to my creativity as a developer.",
        },

        "publications": [
            {
                "title": "DeepFake Detection Using CNN Models with Explainable AI Techniques",
                "venue": (
                    "IEEE, 2025 4th International Conference on Advances in Computing, "
                    "Communication, Embedded and Secure Systems (ACCESS)"
                ),
                "description": (
                    "Presents a deepfake detection framework combining XceptionNet, EfficientNet, "
                    "and MesoNet with Grad-CAM explainability. Evaluated on the Celeb-DF v2 dataset, "
                    "the framework shows strong potential for combating misinformation on social media."
                ),
                "doi": "https://doi.org/10.1109/ACCESS65134.2025.11135663",
            }
        ],
    },
}

# ─────────────────────────── SKILLS ──────────────────────────
# Structured list for the skills page (category, skills with level %)
skills_data = [
    {
        "category": "Programming Languages",
        "items": [
            {"name": "Python",      "level": 95, "proficiency": "Proficient"},
            {"name": "Java",        "level": 80, "proficiency": "Advanced"},
            {"name": "Dart",        "level": 65, "proficiency": "Intermediate"},
            {"name": "JavaScript",  "level": 75, "proficiency": "Intermediate"},
            {"name": "SQL",         "level": 80, "proficiency": "Advanced"},
            {"name": "PHP",         "level": 60, "proficiency": "Intermediate"},
        ],
    },
    {
        "category": "AI / ML",
        "items": [
            {"name": "TensorFlow",   "level": 85, "proficiency": "Advanced"},
            {"name": "PyTorch",      "level": 70, "proficiency": "Intermediate"},
            {"name": "OpenCV",       "level": 90, "proficiency": "Proficient"},
            {"name": "YOLOv8",       "level": 80, "proficiency": "Advanced"},
            {"name": "Scikit-learn", "level": 80, "proficiency": "Advanced"},
        ],
    },
    {
        "category": "NLP / NLU",
        "items": [
            {"name": "Rasa",  "level": 80, "proficiency": "Advanced"},
            {"name": "NLU",   "level": 65, "proficiency": "Intermediate"},
            {"name": "SpaCy", "level": 40, "proficiency": "Beginner"},
        ],
    },
    {
        "category": "App & Web Development",
        "items": [
            {"name": "Flask",    "level": 90, "proficiency": "Proficient"},
            {"name": "Django",   "level": 70, "proficiency": "Advanced"},
            {"name": "Flutter",  "level": 75, "proficiency": "Intermediate"},
            {"name": "Firebase", "level": 45, "proficiency": "Intermediate"},
        ],
    },
    {
        "category": "Tools & Platforms",
        "items": [
            {"name": "GitHub",          "level": 85, "proficiency": "Advanced"},
            {"name": "VS Code",         "level": 95, "proficiency": "Proficient"},
            {"name": "Android Studio",  "level": 55, "proficiency": "Intermediate"},
            {"name": "Google Colab",    "level": 80, "proficiency": "Advanced"},
            {"name": "Render",          "level": 60, "proficiency": "Intermediate"},
        ],
    },
    {
        "category": "Languages",
        "items": [
            {"name": "English",   "level": 85, "proficiency": "Advanced"},
            {"name": "Hindi",     "level": 85, "proficiency": "Advanced"},
            {"name": "Malayalam", "level": 65, "proficiency": "Intermediate"},
            {"name": "Marathi",   "level": 40, "proficiency": "Beginner"},
        ],
    },
]

# ─────────────────────────── PROJECTS ────────────────────────
projects_data = [
    {
        "title": "Deepfake Video Detection System with Explainable AI",
        "video": "videos/deepfake.mp4",
        "details": [
            "Trained and fine-tuned XceptionNet using transfer learning and early stopping, achieving high accuracy in detecting deepfakes.",
            "Integrated Grad-CAM for XAI, enabling heatmap generation to highlight manipulated facial regions.",
            "Evaluated model performance with precision, recall, and F1-score against the Celeb-DF v2 dataset.",
        ],
        "stack": ["Python", "TensorFlow", "Keras", "XceptionNet", "Grad-CAM", "OpenCV", "HTML", "CSS", "JavaScript"],
    },
    {
        "title": "Real vs AI-Generated Image Detection",
        "img": ["images/real.jpg"],
        "details": [
            "Built an image classifier with EfficientNet achieving 97% accuracy across 10 classes.",
            "Improved detection reliability in single-object environments with future scope for multi-object and video deepfake detection.",
        ],
        "stack": ["Python", "EfficientNet", "NumPy", "HTML", "CSS", "JavaScript"],
    },
    {
        "title": "Advanced Fracture and Tumor Detection System",
        "img": ["images/fracture1.jpg", "images/fracture2.jpg", "images/fracture3.jpg"],
        "details": [
            "Collaborated on an ML system to detect fractures and tumors from X-ray scans.",
            "Contributed to data preprocessing, evaluation, and implementation phases using ML workflows.",
        ],
        "stack": ["Python", "Scikit-learn", "NumPy", "Pandas", "OpenCV", "HTML", "CSS", "JavaScript"],
    },
    {
        "title": "Real-Time Fall Monitoring and Alert System",
        "img": ["images/fall.jpg"],
        "details": [
            "Developed a real-time fall detection system using YOLOv8 and posture angle analysis.",
            "Implemented logic to monitor immobility for a configurable duration and integrated Twilio API to send emergency SMS alerts.",
        ],
        "stack": ["Python", "OpenCV", "YOLOv8", "TensorFlow", "NumPy", "Twilio API", "MoveNet", "playsound"],
    },
    {
        "title": "Human Follower System",
        "video": "videos/tracker.mp4",
        "details": [
            "Built a real-time human tracking system integrating YOLOv8 for person detection and MoveNet (TFLite) for pose estimation.",
            "Implemented distance and steering-angle estimation using camera calibration and shoulder keypoints.",
            "Designed smoothing filters, lock/unlock logic, and stability enhancements for robust tracking.",
            "Developed an OpenCV-based UI displaying live telemetry: angle, distance, direction, and proximity warnings.",
        ],
        "stack": ["Python", "OpenCV", "TensorFlow Lite", "YOLOv8", "NumPy"],
    },
    {
        "title": "Executive CRM Chatbot",
        "video": "videos/bot.mp4",
        "details": [
            "Developed and deployed an intelligent CRM chatbot using Rasa and Rasa SDK to handle clients, inquiries, leads, orders, and follow-ups via natural conversation.",
            "Designed extensive NLU training data (intents, entities, stories) to improve intent classification and entity extraction accuracy.",
            "Implemented backend actions in Python with Django and MySQL for client data retrieval, inquiry tracking, and follow-up scheduling.",
        ],
        "stack": ["Python", "Rasa", "Rasa SDK", "Django", "MySQL"],
    },
    {
        "title": "Finance Tracker Application",
        "video": "videos/finance.mp4",
        "details": [
            "Offline finance tracking app enabling users to manage budgets, expenses, and savings with local SQLite storage.",
            "Implemented an alert and notification system for budget overages, with a responsive UI/UX across devices.",
        ],
        "stack": ["Dart", "Flutter", "SQLite", "Android Studio"],
    },
    {
        "title": "LingoDefine – Translator and Dictionary App",
        "video": "videos/translator.mp4",
        "details": [
            "Flutter mobile app for translation and word definition with offline support.",
            "Focused on cross-device UI responsiveness and real-time language switching.",
        ],
        "stack": ["Dart", "Flutter", "Android Studio", "Flutter DevTools"],
    },
    {
        "title": "Hospital Management System",
        "img": ["images/h1.png", "images/h2.png", "images/h3.png"],
        "details": [
            "Multi-role hospital system for doctors, patients, and administrators with secure login.",
            "Focused on session handling, data validation, dynamic form handling, and real-time updates via Firebase.",
        ],
        "stack": ["HTML", "CSS", "JavaScript", "PHP", "SQL", "Firebase", "phpMyAdmin"],
    },
    {
        "title": "Gym Management System",
        "img": ["images/gym1.png", "images/gym2.png", "images/gym3.png", "images/gym4.png"],
        "details": [
            "Responsive web app to handle gym member registrations, schedules, and payments.",
            "Smooth navigation and real-time data updates using Firebase with structured SQL data management.",
        ],
        "stack": ["HTML", "CSS", "JavaScript", "PHP", "SQL", "Firebase", "phpMyAdmin"],
    },
]

# ─────────────────────────── EXPERIENCE ──────────────────────
experience_data = [
    {
        "role":     "Junior Python Developer",
        "company":  "King's Lab Innovation & Technology",
        "location": "Kochi, Kerala",
        "duration": "Aug 2025 – Present",
        "type":     "Full-Time",
        "details": [
            "Developing an NLP-powered CRM chatbot using Rasa and Django.",
            "Designed NLP pipelines for intent classification and entity extraction.",
            "Built backend actions in Python + MySQL for client data retrieval and inquiry tracking.",
            "Learned enterprise-level secure API handling and deployment workflows.",
        ],
    },
    {
        "role":     "Full-Stack Development Intern",
        "company":  "Unified Mentor",
        "location": "Remote",
        "duration": "Jun 2025 – Jul 2025",
        "type":     "Internship",
        "details": [
            "Developed Hospital & Gym Management Systems using PHP, SQL, and Firebase.",
            "Worked on authentication, CRUD operations, and database design.",
            "Built responsive UI and improved cross-device accessibility.",
        ],
    },
    {
        "role":     "Python Programming Intern",
        "company":  "CodeAlpha",
        "location": "Remote",
        "duration": "Dec 2024",
        "type":     "Internship",
        "details": [
            "Strengthened Python fundamentals through structured projects.",
            "Built small automation scripts for solving real-world problems.",
        ],
    },
    {
        "role":     "Embedded Systems & Robotics Intern",
        "company":  "TechMaghi",
        "location": "Kakkanad, Kerala",
        "duration": "May 2023 – Jun 2023",
        "type":     "Internship",
        "details": [
            "Gained exposure to Arduino programming and embedded hardware basics.",
            "Worked on microcontroller projects integrating electronics and coding.",
        ],
    },
    {
        "role":     "Robotics Intern",
        "company":  "Kodachy",
        "location": "Remote",
        "duration": "Feb 2023",
        "type":     "Internship",
        "details": [
            "Learned robotics fundamentals including sensors and automation.",
            "Built simple robotics projects with focus on automation.",
        ],
    },
    {
        "role":     "Social Internship – Project Ganitam (Teaching Team)",
        "company":  "Insight for Innovation (Enlite Initiative)",
        "location": "Thrithala, Kerala",
        "duration": "Aug 2022",
        "type":     "Internship",
        "details": [
            "Delivered mathematics sessions to rural students as part of Project Ganitam.",
            "Helped improve problem-solving skills and learned to communicate technical knowledge simply.",
        ],
    },
    {
        "role":     "NSS Volunteer",
        "company":  "Adi Shankara Institute of Engineering and Technology",
        "location": "Kalady, Kerala",
        "duration": "2022 – 2024",
        "type":     "Volunteer",
        "details": [
            "Volunteered in community service programs, cleanliness drives, and blood donation camps.",
            "Developed teamwork, leadership, and social responsibility skills.",
        ],
    },
    {
        "role":     "IEEE Student Branch Member",
        "company":  "IEEE SB, ASIET Kalady",
        "location": "Kalady, Kerala",
        "duration": "2022 – 2024",
        "type":     "Volunteer",
        "details": [
            "Active member of IEEE Student Branch at ASIET.",
            "Participated in Project Expo – IEEE YESS.",
            "Competed in IEEE Xtreme 16.0 (2022) global coding competition.",
        ],
    },
]

# ─────────────────────────── HOBBIES ─────────────────────────
hobbies_data = [
    {
        "title": "Cricket",
        "icon":  "🏏",
        "desc": (
            "Passionate about cricket since childhood; represented my district in U-16 and U-19 "
            "tournaments. The sport taught me discipline, leadership, and resilience under pressure."
        ),
    },
    {
        "title": "Travel",
        "icon":  "✈️",
        "desc": (
            "Travelling is my way of breaking boundaries. Each journey introduces me to new "
            "cultures and stories, broadening my worldview and fuelling creativity."
        ),
    },
    {
        "title": "Photography",
        "icon":  "📷",
        "desc": (
            "Photography lets me slow down and observe the world closely. I enjoy capturing "
            "everyday beauty — from fleeting expressions to landscapes — especially during travels."
        ),
    },
    {
        "title": "Music",
        "icon":  "🎵",
        "desc": (
            "Music is my constant companion — whether coding late at night or unwinding after a "
            "long day. It helps me maintain focus and a positive mindset."
        ),
    },
    {
        "title": "Reading & Learning",
        "icon":  "📚",
        "desc": (
            "I enjoy reading about AI research, psychology, and personal development. Continuous "
            "learning keeps me curious and growing both technically and personally."
        ),
    },
    {
        "title": "Sports & Fitness",
        "icon":  "⚽",
        "desc": (
            "Beyond cricket I stay active through football, badminton, and gym sessions. Physical "
            "fitness keeps my energy and focus sharp for demanding projects."
        ),
    },
]

# ─────────────────────────── CONTACT ─────────────────────────
socials_data = {
    "email":    "baluu1603@gmail.com",
    "linkedin": "https://www.linkedin.com/in/balagopal-m-1b9a7b226",
    "github":   "https://github.com/addy16-darsh",
    "resume":   "/static/images/balagopal.pdf",
}

# ─────────────────────────── ROUTES ──────────────────────────
@app.route("/")
def index():
    return render_template("index.html", data=index_data)

@app.route("/journey")
def journey_page():
    return render_template("journey.html", data=journey_data)

@app.route("/skills")
def skills_page():
    return render_template("skills.html", skills=skills_data)

@app.route("/projects")
def projects_page():
    return render_template("projects.html", projects=projects_data)

@app.route("/experience")
def experience_page():
    return render_template("experience.html", experiences=experience_data)

@app.route("/hobbies")
def hobbies_page():
    return render_template("hobbies.html", hobbies=hobbies_data)

@app.route("/contact")
def contact_page():
    return render_template("contact.html", socials=socials_data)


if __name__ == "__main__":
    app.run(debug=True)
