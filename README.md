<img width="1774" height="912" alt="IQRS" src="https://github.com/user-attachments/assets/a93b29b7-ab40-43e7-b849-fbb4b6e23a4d" />

# 🎓IQRS | UniZulu Course Finder

**__Helping prospective university students make informed decisions about their academic future__**


* IQRS (Intelligent Qualification Recommendation System) is a web-based university program recommendation chatbot designed to help students explore the courses at the University of Zululand (UNIZULU) across all its faculties

* Choosing a university programme can be overwhelming for Grade 12 learners who may not know which qualifications align with their matric results, subject combinations and academic interests

* IQRS aims to simplify this process by allowing students to interact with a chatbot, provide their academic information, and discover programs that they may qualify to pursue

# ✨ Key Features

**Interactive Chatbot**: Allows students to communicate with the system using natural language

**Academic Information Processing**: Designed to interpret matric subjects and their corresponding NSC levels then calculates their APS

**Programme Recommendations**: Matches academic information against stored university programme requirements

**Faculty Coverage**: Includes programmes from all four UNIZULU faculties

**Subject-Based Matching**: Considers subject combinations and minimum achievement requirements

**Bilingual Direction**: Designed with English and isiZulu interaction in mind

**Centralised Programme Information**: Stores programme details and admission requirements in a structured relational database

# My Tech Stack 

1. Python
2. Django
3. MySQL
4. HTML and CSS
5. JavaScript
6. Git and GitHub

# 🏗️ System Architecture

*IQRS follows a client-server architecture*

The application consists of three main components:

## 1. Frontend Layer

Built using HTML, CSS and JavaScript. It provides the chatbot interface through which users submit academic information and receive recommendations.

## 2. Backend Layer

Powered by Python and Django. It handles incoming requests, processes user input, applies recommendation logic and retrieves relevant programme information.

## 3. Database Layer

Powered by MySQL. It stores structured information about:

University faculties.

Academic programmes.

Matric subjects.

Admission requirements.

Programme-specific subject prerequisites.

# 🗄️ Database Design

*One of the central components of IQRS is its relational database*

Rather than relying entirely on hardcoded programme information, the system uses structured database records to organise university programmes and their admission requirements.

The database includes entities such as:

* Faculties

* Programmes

* Subjects

* Requirement Rules

* Requirement Options

This approach makes program information easier to maintain and provides a foundation for scaling the recommendation engine without embedding every admission requirement directly into the application code.

# 📚 What I Learned

Working on IQRS provided practical exposure to several areas of software development, including:

* Backend development using Python and Django.

* Relational database design and MySQL integration.

* Frontend and backend communication using JavaScript and HTTP requests.

* Structuring application logic around database-driven information.

* Translating real-world requirements into software functionality.

* Understanding the challenges of building conversational applications.

  

This IQRS is an academic software engineering project I'm most proud of 


