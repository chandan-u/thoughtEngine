Design
------

Title: 
~~~~~~
Project Blog -- ThoughtEngine

Expected Features:
~~~~~~~~~~~~~~~~~~

   a. Multiple user login/registration
   b. registration via emailId/ check alternatives such as openId
   c. Need to be able to create and view blogs
   d. enabling blogs to be either private or public
   e. comments -> only registered users can comment / non registered users can send an email
   f. tags ->> learning an efficient way to generate and store tags for blogs
   g. using a jquery plugin to generate the content of the blog....textArea with formatting tools
   i. try to use as simple CSS as possible, we can use the twitter bootstrap too, but try stick to CSS.




Technolgy:
~~~~~~~~~~

# which framework and language?

Python language

web Frameworks associated with python: flask, bottle, django

flask would be the better choice....it has best of both worlds microframework(such as bottle) and all batteries included(such as django) . Also we may need help with email/openid based login/and moreover flask comes with the jinja native template system .



# which db? 

db: we can go for Sql db/ nosql db

this is a simple blog, I think anything is cool.....I am not sure how we evaluate which db to choose. Usually nosql db are used for mainly query based transactions that fails in the case of RDBMS as we need to perform more joins there

Also sql databases are more suitable for quick insertions (transactions ).  And moreover we go for nosql when we think
the data is not structured or semi structured kind of scenarios....hmmm. We have sql when we have structured data.

And more over there is an idea to implement the thought engine, we may have varying structured data as the module progresses in the development. So considering this , we are going for the nosql db.

Versions
~~~~~~~~~~~

There is a reason we have named it as thought engine.... its main idea is to store all our thoughts/thinking any time possible....this could be technical/personal/stupid also we can decide to share/not share these....


version1: The inital version is to build a basic blog...

             a. blog  using flask+mongodb+CSS(interfacing flask and mongo with mostly mongoengine)
             b. single user login for time being 
             c. using jquery plugin to genereate the blog content


version2: The second version is to improvise the blog and then additionaly build the thought engine module. this modules idea is to build a system where we log our thoughts and these are bascially private. And we can see a holitic view of our thoughts with a proper UI. 
             a. improve the login functionality with openId etc..
             b. improve the UI(as needed)
             c. Build the thought engine


FUTURE:
~~~~~~~

The idea of blog is to log anything, techincally/non technical. So we can choose to make these public/private. Usually technical blogs are made public so that others can comment....and personal things are preferred to be private, this could actually act as a diary..

The thought engine usually helps us to log our thoughts, and in feature we can develop modules to perform data analysis to understand the nature of our thoughts(classify them), some times thoughts are linked, one thought leads to others(this is complicated, but we can try understanding how complex really it is...).  This module is to be developed as time progresses and as we obtain new knowlegde.





