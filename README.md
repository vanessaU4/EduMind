# EduMindSolutions - Mental Health Platform

<div align="center">

![EduMindSolutions Logo](frontend/public/favicon.svg)


</div>

## 🌟 Overview

EduMindSolutions is a comprehensive mental health platform designed specifically for youth aged 13-23. The platform provides clinical assessments, peer support, crisis intervention services, and educational resources to support young people's mental health journey.

### Key Features

- 🏥 **Clinical Assessments** - Professional mental health evaluations and tracking
- 👥 **Peer Support Community** - Safe spaces for peer-to-peer support and forums
- 🚨 **Crisis Intervention** - 24/7 crisis support and emergency resources
- 📚 **Educational Content** - Mental health resources, articles, and multimedia content
- 🔒 **HIPAA Compliant** - Secure, privacy-focused healthcare platform
- 📱 **Responsive Design** - Works seamlessly across all devices
- 🎯 **Role-Based Access** - Different interfaces for patients and healthcare professionals

## 🏗️ System Architecture

### Backend (Django REST API)
- **Framework**: Django 5.1.7 + Django REST Framework
- **Authentication**: JWT (JSON Web Tokens)
- **Database**: SQLite (development) / PostgreSQL (production)
- **Security**: HIPAA-compliant data handling and encryption

### Frontend (React TypeScript)
- **Framework**: React 18.3.1 with TypeScript
- **Build Tool**: Vite 7.0.4
- **UI Library**: Radix UI + Tailwind CSS
- **State Management**: Redux Toolkit + React Query
- **Routing**: React Router DOM

### Key Applications

| Application | Purpose | Features |
|-------------|---------|----------|
| **accounts** | User management | Registration, authentication, role-based access |
| **assessments** | Clinical evaluations | Mental health assessments, progress tracking |
| **community** | Peer support | Forums, chat rooms, peer matching |
| **content** | Educational resources | Articles, videos, audio content |
| **crisis** | Emergency support | Crisis hotlines, emergency contacts |
| **wellness** | Health tracking | Mood tracking, wellness goals |

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- Node.js 18+
- Git

### Backend Setup

```bash
# Clone the repository
git clone <repository-url>
cd eduMindSolutions/backend

# Create virtual environment
python -m venv env

# Activate virtual environment
# Windows:
env\Scripts\activate
# Linux/Mac:
source env/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser (optional)
python manage.py createsuperuser

# Start development server
python manage.py runserver
```

### Frontend Setup

```bash
# Navigate to frontend directory
cd ../frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

### Access the Application

- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000/api
- **Admin Panel**: http://localhost:8000/admin

## 🚀 Deployment

Frontend:	React (Vite)
Backend:	Django REST Framework
Database:	PostgreSQL
Containerization:	Docker
Deployment	Vercel
CI/CD: vercel + Github Actions
Monitoring:Vercel Analytics

## 🌍 Live Link

https://edu-mind-solutions.vercel.app

## 🧪 Testing Results
Different testings were done:
Functional Testing 
Testing with Different Data Values
Testing on Different Hardware/Software
<img width="1366" height="768" alt="error handling" src="https://github.com/user-attachments/assets/f39440a3-a082-4c49-aa28-4c8dc10d7fc1" />

<img width="1366" height="768" alt="Empty fields" src="https://github.com/user-attachments/assets/88a5206c-ee0d-4529-ab75-e432d6a87a8c" />
<img wid![App running on a mobile device](https://github.com/user-attachments/assets/e5632aa5-464a-4cf6-b3f4-20f4397da389)
th="1366" height="768" alt="App running on a different browse(Microsoft Edge)" src="https://github.com/user-attachments/assets/527bdd4b-de73-4ead-a778-cf073c760cd0" />
<img width="1366" height="768" alt="invalid email" src="https://github.com/user-attachments/assets/e4c064b2-6e07-4f05-98e3-58b15adaf8d0" />


## 📊 Analysis

The results demonstrated that the project achieved its initial objectives outlined in the proposal.
The primary objective of this project was to design and develop a mobile application that enhances mental health awareness, facilitates early detection, and promotes access to support services among young people in Rwanda, thereby reducing stigma and increasing help-seeking behavior. So it was achieved as we have;
- Successful deployment and integration of all system components.
- Responsive and stable performance across devices.
- All core functionalities work as intended.

## 💬 Discussion

This project demonstrates the importance of iterative development and continuous testing in achieving reliable full-stack deployment.
Through the milestones achieved design, containerization, deployment, and testing the system reflects the real-world software engineering process of planning, automation, and monitoring.
The collaboration and feedback process with the supervisor helped ensure alignment with the original goals and quality standards.

## Recommendations and Future Work
The community is encouraged to use the mental health app to promote awareness, self-care, and peer support while fostering open discussions and early intervention for mental well-being.
For future improvement:
- Add offline mode or caching for better performance in low connectivity areas.
- Optimize container images for faster deployment and reduced resource usage.

## Demo Video

Link to the demo video: https://www.loom.com/share/82fa543a3dc643f399169cc95b59683c

## 📋 API Documentation

### Authentication Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/accounts/register/` | User registration |
| POST | `/api/accounts/login/` | User login |
| POST | `/api/accounts/token/refresh/` | Refresh JWT token |
| GET | `/api/accounts/users/` | List users |

### Assessment Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/assessments/reviews/` | List assessments/reviews |
| POST | `/api/assessments/reviews/` | Create new assessment |
| GET | `/api/assessments/reviews/stats/` | Assessment statistics |
| GET | `/api/assessments/my-reviews/` | User's assessments |

### Community Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/community/categories/` | Forum categories |
| GET | `/api/community/posts/` | Forum posts |
| POST | `/api/community/posts/` | Create forum post |
| GET | `/api/community/chatrooms/` | Chat rooms |
| GET | `/api/community/peer-support/` | Peer support requests |

### Content Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/content/audio/` | Audio content (meditations, etc.) |
| GET | `/api/content/categories/` | Content categories |
| GET | `/api/content/mental-health-resources/` | Mental health resources |

### Crisis Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/crisis/hotlines/` | Crisis hotlines |
| GET | `/api/crisis/resources/` | Emergency resources |

### Health Monitoring

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/health/` | Basic health check |
| GET | `/health/detailed/` | Detailed system status |

## 🔐 Authentication & Security

### User Roles

- **Patient**: Youth users (13-23) seeking mental health support
- **Professional**: Licensed healthcare providers and counselors
- **Admin**: System administrators

### Security Features

- JWT-based authentication with refresh tokens
- Role-based access control (RBAC)
- HIPAA-compliant data encryption
- Secure session management
- Input validation and sanitization
- CORS protection

### Token Usage

```javascript
// Include JWT token in API requests
headers: {
  'Authorization': 'Bearer ' + accessToken,
  'Content-Type': 'application/json'
}
```

## 🎨 Frontend Features

### User Interface

- **Modern Design**: Clean, accessible interface built with Radix UI
- **Dark/Light Mode**: Theme switching for user preference
- **Responsive Layout**: Mobile-first design approach
- **Accessibility**: WCAG 2.1 AA compliant

### Key Components

- **Dashboard**: Personalized user dashboard with health metrics
- **Assessment Tools**: Interactive mental health assessments
- **Community Forums**: Peer support and discussion spaces
- **Crisis Support**: Quick access to emergency resources
- **Resource Library**: Educational content and tools

### State Management

```typescript
// Redux store structure
interface RootState {
  auth: AuthState;
  assessments: AssessmentState;
  community: CommunityState;
  content: ContentState;
  wellness: WellnessState;
}
```

## 🧪 Testing

### Backend Testing

```bash
cd backend
python manage.py test
```

### Frontend Testing

```bash
cd frontend
npm run test
```

### Integration Testing

```bash
# Run integration tests
docker-compose -f docker-compose.test.yml up --build
```

## 🐳 Docker Deployment

### Development

```bash
# Start all services
docker-compose up --build

# Access services
# Frontend: http://localhost:3000
# Backend: http://localhost:8000
# Database: localhost:5432
```

### Production

```bash
# Build production images
docker-compose -f docker-compose.prod.yml up --build -d

# View logs
docker-compose logs -f
```

## 📊 Monitoring & Analytics

### Health Checks

The platform includes comprehensive health monitoring:

```bash
# Check system health
curl http://localhost:8000/health/

# Detailed health report
curl http://localhost:8000/health/detailed/
```

### Metrics Tracked

- User engagement and session duration
- Assessment completion rates
- Community participation metrics
- Crisis intervention response times
- System performance and uptime

## 🔧 Configuration

### Environment Variables

#### Backend (.env)




```bash
# API configuration
VITE_API_BASE_URL=http://localhost:8000/api


# Feature flags
VITE_ENABLE_CRISIS_CHAT=true
VITE_ENABLE_PEER_MATCHING=true

# Analytics
VITE_ANALYTICS_ID=your-analytics-id
```

## 🆘 Crisis Support

**If you or someone you know is in crisis, please contact:**

- **National Suicide Prevention Lifeline**: 988
- **Crisis Text Line**: Text HOME to 741741
- **Emergency Services**: 911

The platform includes built-in crisis intervention tools and direct connections to professional support services.


## 🙏 Acknowledgments

- Mental health professionals who provided clinical guidance
- Youth advisory board for user experience feedback
- Open source community for foundational technologies
- Healthcare compliance experts for security guidance

---
