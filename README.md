# 🎾 Tennis Email Agent

An intelligent AI-powered system that automates tennis match communications for the Toronto Winter League. This agent automatically scrapes match schedules, looks up opponent team captains, and generates personalized reminder emails.

## Features

- **Automated Schedule Scraping**: Extracts match information from tenniscores.com
- **Team Captain Lookup**: Finds opponent team contact information from local database
- **Smart Email Generation**: Creates personalized match reminder emails with venue details
- **Gmail Integration**: Sends draft emails for review and forwarding
- **Home/Away Logic**: Only processes home games, skips away matches
- **Multi-Agent Coordination**: Uses CrewAI for intelligent task orchestration

## Technologies Used

### Core AI Framework
- **[CrewAI](https://github.com/joaomdmoura/crewAI)** - Multi-agent AI framework for task coordination
- **[CrewAI Tools](https://github.com/joaomdmoura/crewai-tools)** - Pre-built tools for web scraping and Gmail integration
- **[OpenAI GPT-4o](https://openai.com/gpt-4)** - Large language model for intelligent reasoning

### Web Scraping & Data Processing
- **[ScrapeElementFromWebsiteTool](https://github.com/joaomdmoura/crewai-tools)** - CSS selector-based web scraping
- **Pydantic** - Data validation and settings management
- **JSON** - Team captain data storage and retrieval

### Email & Authentication
- **[Gmail API](https://developers.google.com/gmail/api)** - Secure email composition and sending
- **[Google OAuth2](https://developers.google.com/identity/protocols/oauth2)** - Authentication flow
- **[google-auth-oauthlib](https://github.com/googleapis/google-auth-library-python-oauthlib)** - OAuth2 client library

### Development Environment
- **Python 3.13** - Modern Python with latest features
- **Jupyter Notebook** - Interactive development and testing
- **Virtual Environment** - Isolated dependency management

## 🏗️ Architecture

The system uses a **multi-agent architecture** with specialized AI agents:

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Scraper       │    │   Captain       │    │   Email         │
│   Agent         │    │   Lookup        │    │   Generator     │
│                 │    │   Agent         │    │   Agent         │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         └───────────────────────┼───────────────────────┘
                                 │
                    ┌─────────────────┐
                    │   Supervisor    │
                    │   Agent         │
                    │   (CrewAI)      │
                    └─────────────────┘
```

### Agent Responsibilities

1. **Scraper Agent**: Extracts match schedules from tenniscores.com using CSS selectors
2. **Captain Lookup Agent**: Finds opponent team contact information from teams.json
3. **Email Generator Agent**: Creates personalized match reminder emails
4. **Gmail Agent**: Handles email composition and sending via Gmail API
5. **Supervisor Agent**: Coordinates all tasks and manages the workflow

##  Workflow

1. **Schedule Check**: Scrapes tenniscores.com for Thornhill Park team schedule
2. **Home/Away Logic**: Determines if the team is playing at home (H) or away (A)
3. **Opponent Lookup**: If home game, identifies opponent team name
4. **Contact Retrieval**: Finds opponent captain's email and name from teams.json
5. **Email Generation**: Creates personalized reminder email with venue details
6. **Draft Creation**: Sends draft email for review and manual forwarding

## Quick Start

### Prerequisites

- Python 3.13+
- Google Cloud Project with Gmail API enabled
- OpenAI API key

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd tennis-email-agent
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install crewai crewai_tools pydantic google_auth_oauthlib
   ```

4. **Set up environment variables**
   ```bash
   export OPENAI_API_KEY="your-openai-api-key"
   export gc_client_id="your-google-client-id"
   export gc_client_secret="your-google-client-secret"
   export gc_refresh_token="your-refresh-token"
   ```

5. **Create credentials.json**
   ```json
   {
     "installed": {
       "client_id": "YOUR_CLIENT_ID",
       "project_id": "YOUR_PROJECT_ID",
       "auth_uri": "https://accounts.google.com/o/oauth2/auth",
       "token_uri": "https://oauth2.googleapis.com/token",
       "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
       "client_secret": "YOUR_CLIENT_SECRET",
       "redirect_uris": ["http://localhost"]
     }
   }
   ```

6. **Run the notebook**
   ```bash
   jupyter notebook tennis-email-agent.ipynb
   ```

## Project Structure

```
tennis-email-agent/
├── tennis-email-agent.ipynb    # Main Jupyter notebook
├── teams.json                   # Team captain contact database
├── refresh_token.py             # OAuth2 token refresh utility
├── requirements.txt             # Python dependencies
├── credentials.json             # Google OAuth2 credentials (not in repo)
├── captain_list.pdf             # Reference document
└── README.md                    # This file
```

## Configuration

### Team Data (teams.json)
```json
[
  {
    "team": "Aces",
    "name": "Julia Passynkova", 
    "email": "julia@email.com"
  },
  {
    "team": "Falcons",
    "name": "Jane Doe",
    "email": "jane@email.com"
  }
]
```

### Environment Variables
- `OPENAI_API_KEY`: Your OpenAI API key for GPT-4o
- `gc_client_id`: Google OAuth2 client ID
- `gc_client_secret`: Google OAuth2 client secret
- `gc_refresh_token`: Gmail API refresh token

## Use Cases

- **Tennis League Management**: Automate match communications
- **Sports Team Coordination**: Streamline opponent contact
- **Event Reminders**: Generate venue-specific instructions
- **Multi-Agent Workflows**: Demonstrate CrewAI capabilities

## Security

- OAuth2 authentication for Gmail API
- Environment variables for sensitive credentials
- Local JSON storage for team data
- No hardcoded secrets in code

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

---

**Built with ❤️ for tennis enthusiasts and AI automation**
