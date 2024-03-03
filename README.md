
<p align="left">
</p>

<h3 align="left">Tools used:</h3>
<p align="left"> <a href="https://aws.amazon.com" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/amazonwebservices/amazonwebservices-original-wordmark.svg" alt="aws" width="40" height="40"/> </a> <a href="https://flask.palletsprojects.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/pocoo_flask/pocoo_flask-icon.svg" alt="flask" width="40" height="40"/> </a> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> </p>


# Github-jira-token-project
Creating a github webhook with the help of python script running in flask such that when a new issue is raised in the github a ticket is created in jira

# GitHub-Jira-Token-Project

This project creates a GitHub webhook using a Python script running in Flask. The webhook is designed to automatically create a Jira ticket when a new issue is raised in the GitHub repository.

## Project Highlights 

- **Boost Productivity:** Say goodbye to manual ticket creation. Our solution streamlines the workflow, saving your team valuable time.
  
- **Flask-Powered Webhook:** The project harnesses the flexibility of Flask, providing a robust foundation for handling GitHub webhook events effortlessly.

- **Smart Configuration:** With clear and concise configuration steps, setting up GitHub and Jira integration becomes a breeze. The README guides you through obtaining and securing necessary tokens, ensuring a smooth setup process.


## How It Works

1. A GitHub webhook is set up to trigger on "issues" events.
2. The Python script listens for incoming webhook payloads.
3. When a new issue is raised on GitHub, the webhook sends a payload to the Flask server.
4. The Flask server processes the payload and uses Jira API to create a corresponding ticket.

## Setup

1. Clone this repository:

    ```bash
    git clone https://github.com/your-username/GitHub-Jira-Token-Project.git
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Configure GitHub and Jira credentials

4. Run the Flask application:

    ```bash
    python app.py
    ```

    The Flask server will be running at ipofinstace:5000.

5. Configure a GitHub and things required 

## Easy Configuration 🛠️

1. **GitHub Token:** Obtain a GitHub personal access token with the required permissions to read issues.
2. **Jira Token:** Acquire a Jira API token, ensuring it has the necessary permissions to create issues.

Update these variables in the code:

```python
API_TOKEN_GITHUB = "YOUR_GITHUB_TOKEN"
API_TOKEN_JIRA = "YOUR_JIRA_TOKEN"
JIRA_PROJECT_KEY = "YOUR_JIRA_PROJECT_KEY"
```

Project screenshots with steps to follow 

Create a api token in jira such that only authorized user can access the jira board

![Screenshot 2024-03-02 144845](https://github.com/jithinkumar900/Github-jira-toke-project/assets/59408287/b39e0818-6f9e-4cf0-b05b-37a34fa93552)

here we see a list of project been already created by the members of the team 

![Screenshot 2024-03-02 145729](https://github.com/jithinkumar900/Github-jira-toke-project/assets/59408287/a1676e9d-3635-4684-b021-41dbe2860d46)

we crated a pyhton script which is used to list the meamber of the project 

![Screenshot 2024-03-02 161823](https://github.com/jithinkumar900/Github-jira-toke-project/assets/59408287/1754ef80-a28e-451e-810a-f177c61578e3)

for issue type we need id of the issue which can be seen from here 

![Screenshot 2024-03-02 162947](https://github.com/jithinkumar900/Github-jira-toke-project/assets/59408287/31cd5367-730e-4b0c-ae2f-33e59f4b648e)
![Screenshot 2024-03-02 162955](https://github.com/jithinkumar900/Github-jira-toke-project/assets/59408287/cdc797da-e405-4d57-8be2-227cac97de04)

and project id from here 

![Screenshot 2024-03-02 163117](https://github.com/jithinkumar900/Github-jira-toke-project/assets/59408287/945ff2bb-9c3e-44a4-b3f3-69201c1589c5)

we created a script which will create a ticket and it can seen in the jira board 

![Screenshot 2024-03-02 163338](https://github.com/jithinkumar900/Github-jira-toke-project/assets/59408287/846c9b78-f53f-4061-9d3b-69706631b9f2)
![Screenshot 2024-03-02 163354](https://github.com/jithinkumar900/Github-jira-toke-project/assets/59408287/aa5411d2-69ab-4813-a15f-47d697cba092)

now we create a instance and then install python and flask for the python script to run which will run the combination of both taking api request from the github and then forwarding the request to the jira board 

  ```bash
   sudo apt update 
   sudo apt install python3 python3-pip python3-venv 
  ```
![Screenshot 2024-03-02 171059](https://github.com/jithinkumar900/Github-jira-toke-project/assets/59408287/5361981d-7fb7-4073-9b14-ceae6caa68e8)
![Screenshot 2024-03-02 173830](https://github.com/jithinkumar900/Github-jira-toke-project/assets/59408287/97ca2a72-42a1-4352-a1ce-ef1dccae2bbc)

now we create a webhook in the github of the format http://publicipofinstance:5000/createJira

![Screenshot 2024-03-02 174011](https://github.com/jithinkumar900/Github-jira-toke-project/assets/59408287/e8a8f486-62b4-41f4-837c-db568da5fb2f)

choose the necessary condition to trigger the webhook and save the webhook 

![Screenshot 2024-03-02 174111](https://github.com/jithinkumar900/Github-jira-toke-project/assets/59408287/f3071dee-b71c-439e-a0dc-0ea4c2e3c1e7)
![Screenshot 2024-03-02 180140](https://github.com/jithinkumar900/Github-jira-toke-project/assets/59408287/42ffb0cb-88de-4de4-abae-eb4e4e41f7be)

now when we comment the command createJira it will crate a jira ticket in jira, we have successfully created a ticket from a comment in github

![Screenshot 2024-03-02 201154](https://github.com/jithinkumar900/Github-jira-toke-project/assets/59408287/1361523e-f112-4d40-ae01-23a5a0810497)

cheers  •ᴗ•









