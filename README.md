# Redo - News Sharing Platform
## Table of Contents
[UX](#ux)
  * [Goal for the Project](#goal-for-the-project)
  * [User Goals](#user-goals)
  * [User Stories](#user-stories)
  * [Site owner Goals](#site-owner-goals)
  * [Design Choices](#design-choices)
    * [Font](#font)
    * [Icons](#icons)
    * [Colours](#colours)
    * [Structure](#structure)
  * [Features](#features)    
  * [Future Plans](#future-plans)      
  * [Tehnologies used](#tehnologies-used)
    * [Languages](#languages)
    * [Tools](#tools)
  * [Testing](#testing)
  * [Deployment](#deployment)
  * [Credits](#credits)
  ## UX
## Goal for the Project
The primary goal of the Redo project is to create a user-friendly and intuitive news sharing platform that empowers users to:

* Share News: Users can easily create accounts and share news articles with the community.
* Discover News: Users can explore a diverse range of news articles shared by other members.
* User Engagement: Foster engagement by allowing users to interact with posts through comments.
* Search Functionality: Provide a convenient search bar to facilitate quick access to posts and user profiles.
* User-Friendly Experience: Design a visually appealing and responsive website for seamless usage across devices.
### User Goals
Users of Redo aim to:

* Post News: Share their own news articles, updates, and stories with the platform's community.
* Discover News: Explore a variety of news articles on topics of interest from different sources.
* Connect with Others: Interact with fellow users by commenting on posts.
* Search Bar: Easily search for specific posts or user profiles using the integrated search bar.
### User Stories
* As a user who wants to share news, I want to create an account, log in, and post my news articles to share them with the community.
* As a user looking to connect, I want to leave comments on posts that resonate with me and follow other users whose content I find valuable.
* As a user in search of specific information, I want to use the search bar to quickly find posts related to particular topics or from specific users.
* As a user interested in current events, I want to scroll through a feed of diverse news articles and click on ones that intrigue me for more details.
### Site owner Goals
* Keep users interested: Make a fun platform where people enjoy spending time and talking to each other.
* Share good stuff: Put up news that's really good and interesting to lots of different people.
* Get more friends: Help the community grow by getting more people to join and take part.
* Make people happy: Keep making the site better based on what people say, so they like using it.
### Design Choices
#### Font
[Open Sans](https://fonts.google.com/specimen/Open+Sans) is a clean and modern font that's perfect for any website. It's easy to read on screens of all sizes, making it ideal for web and mobile use.
#### Icons
I use [Font Awesome](https://fontawesome.com) icons because they're easy to use and look great. After adding them to the site, it became livelier and more attractive. Thanks to them, the website is easier to read. They are easy to understand, so they replace some descriptions.
#### Colours
My project utilizes a dark-themed color scheme inspired by Bootstrap's dark color palette.

![colors](/doc/images/colors.png)


#### Structure
The project is structured into the following main components:

* Home Page: Users are greeted with a feed of the latest news articles posted by the community. The user-friendly interface encourages users to explore and engage.

* User Accounts: Users can create accounts, log in, and personalize their profiles. Profiles include a profile picture, bio, and a list of posts authored by the user.

![profile](/doc/images/profile.png)

* News Feed: The heart of the platform, the news feed displays posts from various users, allowing readers to discover news articles that align with their interests.

![posts](/doc/images/posts.png)

* Post Interaction: Users can interact with posts by leaving comments.

![comment](/doc/images/coments.png)

* Search Functionality: A convenient search bar enables users to find specific posts or profiles efficiently.

![result](/doc/images/searchresult.png)

### Features

Navbar:

* Website features a sleek and responsive navbar that ensures seamless    navigation across different sections. Designed with mobile users in mind, the navbar adapts gracefully to smaller screen sizes. On such devices, the conventional menu transforms into a "hamburger" icon, optimizing screen real estate while retaining easy access to navigation links. This design approach prioritizes both aesthetics and functionality, offering users a consistent browsing experience across devices.

![navbar](/doc/images/navbar.png)

![hamburger](/doc/images/hamburger.png)

Login:

* Login page provides a gateway to access the platform.

![login](/doc/images/login.png)


Create account:

* For new users, we've built a streamlined account creation process. This feature enables anyone to join our community with ease. Simply fill in the required details, and you're all set to explore!

![register](/doc/images/register.png)

Edit Profile:

* Understand the importance of personalization. Once logged in, users can navigate to their profile settings and make modifications. From updating profile pictures to changing personal information.

![edit](/doc/images/editprofile.png)

Post Creation and Sharing:

* Users can create and share news articles, updates, and stories with the community.
* Posts can include text, images, and links, enhancing the storytelling experience.

![create](/doc/images/createpost.png)

Footer:

* At the base of our platform lies the footer, a space where users can find additional information and quick links.

![footer](/doc/images/footer.png)

User Interaction:

* Users can engage with posts through comments.
* Interaction fosters meaningful discussions and community engagement.

Search and Discovery:

* The integrated search bar enables users to find specific posts or profiles quickly.
* Users can search by keywords, usernames, or topics of interest.
Dark Themes:

* Project utilizes a dark-themed color scheme inspired by Bootstrap's dark color palette
### Future Plans
The Redo project is committed to continuous improvement and growth. Future enhancements may include:

* Enhanced User Profiles: Adding additional customization options to user profiles to allow for more personalization.
* Topic Categorization: Implementing a tagging system to categorize posts and enable users to filter content by topic.
* Notification System: Introducing a notification system to alert users about interactions on their posts and updates from followed users.
### Tehnologies used
#### Languages 
* [HTML](https://en.wikipedia.org/wiki/HTML5)
* [CSS](https://en.wikipedia.org/wiki/CSS)
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
* [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) 
#### Frameworks and Libraries
* [Font Awesome](https://fontawesome.com) - Used for icons on the website.
* [Google fonts](https://fonts.google.com) - Used for text font on page.
* [Django](https://www.djangoproject.com/) - Python-based web framework
* [Gunicorn](https://en.wikipedia.org/wiki/Gunicorn) - HTTP server interface.
* [Psycopg](https://wiki.postgresql.org/wiki/Psycopg) Postgres database adaptor.
* [Bootstrap](https://getbootstrap.com/) Bootstrap  was used in this project.
#### Tools
* [Gitpod](https://gitpod.io/workspaces) - Used for building the website.
* [Github](https://github.com/) - Used to deploy the project. 
* [W3C HTML Validation Service](https://validator.w3.org/) - Used to test HTML.
* [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) - Used to test CSS.
* [Devtools](https://developer.chrome.com/docs/devtools/#:~:text=Chrome%20DevTools%20is%20a%20set,you%20can%20open%20Chrome%20DevTools.) - I checked all the time how my code works and if there are any errors in console
* [JSHint](https://jshint.com/) - Used to test my java script if there is any mistakes.
* [Heroku](https://www.heroku.com) - Deployment of website.
### Testing
### Deployment

Local Development

* Go to Github repo [here](https://github.com/EmcioN/Redo) 
press **< CODE >**, and press COPY.
or **FORK** my repo

![clone](/doc/images/clonefork.png)

* Go to your github repositories and create new repo, call it whatever you like. Press Create Repository it will lead you to another page, and press Gitpod it should open workspace for you
* Now you need to download all libraries and frameworks used in this project. Use command : 
```
pip3 install -r requirements.txt
```
* Log in to Heroku or create a new account.
* Click the New button in the top right corner and select Create New App.

![step](/doc/images/step1.png)

* Choose a unique name for your app and select the region you want it to run in, then click Create App.

![step](/doc/images/step2.png)

* Go to the Deploy tab and click on the Settings tab.

![step](/doc/images/step3.png)

* Scroll down to the Buildpack section and click Add Buildpack.

![step](/doc/images/step4.png)

* Select "python" and click Save Changes.
* Repeat step and add "node.js" as well.
* Make sure the Buildpacks are in the correct order by clicking and dragging them if necessary.

![step](/doc/images/step5.png)

* Go back to the top of the page and select the Deploy tab again.

![step](/doc/images/step6.png)

* Choose Github as the deployment method and confirm that you want to connect to your Github account.

![step](/doc/images/step7.png)

* Search for your repository name and click the connect button.
* Scroll to the bottom of the deploy page and select your preferred deployment type.
* You can choose to enable automatic deploys for automatic deployment when you push updates to Github.

![step](/doc/images/step8.png)

* That's it, your site should now be deployed!
### Credits 
#### For help, advice and insperation