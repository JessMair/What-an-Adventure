# What An Adventure - A Milestone Project


<img src="images/deployedimage.png" alt="Am I Responsive">


My third milestone project, undertaken as part of the Code Institutes Diploma in Software Development. 
Here is the link for [What An Adventure]()


# Who Is This Game For?

This game has been created for those who enjoy games where there are multiple choices leading to 






Below is a link to the flowchart I had completed 

[]())

[Wireframe page 2]()




# Technologies used
 
- [Github]( https://github.com/) to keep the file 
- [Gitpod]( https://www.gitpod.io/) for version control

## Languages used

- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))



# Resources
- [Code Institute](https://codeinstitute.net/) Course material
- [Code Institute](https://codeinstitute.net/) Slack community 
- [W3Schools]( https://www.w3schools.com/) 
- [PEP8](http://pep8online.com/)
- [Am I Responsive](http://ami.responsivedesign.is/) – Check site and for header image of this README file
- [Stack Overflow](https://stackoverflow.com/)


# Testing

## User Stories Testing 

## Validators

<img src="images/pep8validator" alt="PEP8 Validation">

I ran the code for the application through the PEP8 validator to ensure that it was free of bugs and will run smoothly once deployed. 
The code is completely free of any issues. 

# Version Control 

- GitHub
- Gitpod

Gitpod served as the local repository and IDE. 
GitHUb served as the remote repository. 

The following steps were followed to maintain version control;

- I created a repository on GitHub and named it 'What An Adventure' 
- I then signed in to Gitpod and opened a new workspace via the repository name 'What An Adventure'
- I created the pages, folders and files on GitPod
- I saved my work on GitPod at regular intervals and pushed it to GitHub to keep it safe

This is the process I followed having completing each significant section of code, I typed the following into the terminal:
- git add . (This added the work to git)
- git commit -m "COMMIT MESSAGE" (This committed the work)
- git push (This pushed the work to GitHub)



# Deployment 

## Deployment to Heroku

- Log into Heroku (You will need to create an account if you do not have one)
- Click on the button labelled "New" from teh dashboard. This is located in the right hand corner, just under the header.
- Selcet "Create new app"
- Enter a name for the applocation. This name must be original. Choose the correct region and click "Create App".
- On the project page, select the "settings" tab. 
- Then selcet "config Vars" and enter the following details in the corresponding fields: 
    Key = PORT
    Value = 8000
- Select the "Add" button, this will add the Convig Vars. 
- Scroll to the buildpacks section and selects "Add Buildpacks"
- Add the Python buildpack.
- Add the node.jsbuildpack.
- It is important to ensure that the Python buildpack is listed above the node.js buildpack.
- At the top of the page there is a "Deploy" tab that must be selected. 
- Select the Github deployment method.
- Search for your repository name, then click the "Connect" button to link your repository.
- At the bottom of this page, select the deployment type. This can be automatic or manual. Automatic Deployment will redeploy the project to Heroku every time it is pushed to GitHub. I chose manual. The project is deployed. 




Used technologies and credits

Python Libraries
GSpread enables the Google Sheets savegame system.
Time enables the "p_d" print delay function.
Sys enables the "delete_line" function (and its dependent "pause" function).
GetPass enables the "pause" function.
Other Technologies
GitHub
Google Sheets
Python Tutor
PEP8
Credits
Aniket Navlur and Alper demonstrated how to use "stdout" to delete printed lines.
Mike Hordecki demonstrated how to use "enumerate."
Pedro Lobito provided the "next_available_row" function.
Star Trek: Time Loop by DeannaCarina provided some code direction, as well as giving an example of an excellent story-based Python project.
The Code Institute Slack provided an invaluable database of information and community of support. I am particularly grateful to the msletb-nov-2021 cohort, our facilitator Kasia, and my mentor Darío. From my cohort, special mentions to Rhiannon McNulty and Rachel Rock, who are always ready and willing to provide feedback.
