# Guuxa Server and Client

You have been given a fully functioning client and server.  It is designed to have the client send a message, and have the server return the exact message.

## Run the program

Before making modifications, run the client and server and make sure they work correctly.

## Instructions

1. Answer the questions in student-README.md.  You should answer them in that file.  You may wish to answer questions 1-5 before you make modifications to the server.

2. Modify the `server.py` to allow the server to accept more than one connection.  It should run until the user terminates the process (e.g. Control+C from the keyboard.)

An example of the output would be, if there are four client connections:

```
» python server.py
Connection by  ('127.0.0.1', 51630)
Connection closed.
Connection by  ('127.0.0.1', 51633)
Connection closed.
Connection by  ('127.0.0.1', 51634)
Connection closed.
```

3. Modify the server so that if the client sends the message `password` it will reply with `enternow` instead of `password`.

4. Commit all your changes (server.py and student-README.md) and push them to Github.  You should not make any changes to client.py

# References

* [Python Network Programming Cookbook](https://subscription.packtpub.com/book/networking_and_servers/9781849513463/1/ch01lvl1sec21/writing-a-simple-echo-client-server-application)
* [Python socket module](https://docs.python.org/3/library/socket.html)
* [Real Python Echo Server and Client](https://realpython.com/python-sockets/#echo-client-and-server)
