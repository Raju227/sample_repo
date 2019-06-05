#The mechanism is the following :
# In the nodejsbase directory, issue the command to build nodejsbase image :
# docker build -t nodejsbase:v1 .
#
# In the nodejsbasegit directory, issue the command to add git on top of the nodejsbase image to build the nodejsbasegit (the ssh key must be present in the directory) :
# docker build -t nodejsbasegit:v1 .
#
# In the frontend directory (example : cart ) issue the command to perform the clone of the repo, setup of npm and run the npm tests
# docker build -t nodejscart:v2 .