"""
==========================================================
CAREER MENTOR AGENT (CHAINLIT + GEMINI API)
==========================================================

✅ WHAT IT DOES:
- Suggests best career paths for a given field.
- Lists key skills required for that field.
- Gives 3 real-world job roles.

==========================================================
1) PREREQUISITES (RUN THESE IN CMD ONE BY ONE)
==========================================================
# Check Python version (3.9 recommended)
python --version

# Install uv (fast package manager)
pip install uv

# Go to the folder where this file is saved
cd "D:\Agentic Ai\Career Mentor Agent"

# Install requirements using uv
uv pip install chainlit google-generativeai --system

# (If uv gives errors, use pip instead)
pip install chainlit google-generativeai

==========================================================
2) RUN THE AGENT
==========================================================
# Start Chainlit server
chainlit run career_mentor_agent_complete.py -w

# Open the URL shown in the terminal, e.g.:
http://localhost:8000

==========================================================
3) HOW TO USE
==========================================================
Type a field in the chat, for example:
- Artificial Intelligence
- Data Science
- Cybersecurity
- Software Engineering

You will get:
✔ Best career paths
✔ Key skills required
✔ 3 real-world job roles

==========================================================
4) IF PORT 8000 IS BUSY
==========================================================
chainlit run career_mentor_chainlit.py -w --port 8080

Then open:
http://localhost:8080

==========================================================
5) MAKE IT PUBLIC (OPTIONAL)
==========================================================
# Install localtunnel (Node.js required)
npm install -g localtunnel

# After running the agent
npx localtunnel --port 8000

You will get a public URL like:
https://cool-career-agent.loca.lt

==========================================================
6) STOP THE SERVER
==========================================================
Press CTRL + C in terminal.

==========================================================

