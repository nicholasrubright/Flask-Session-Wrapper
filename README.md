# Flask Session

A design for wrapping a flask object into it's own custom object for handling session.

# Design

- Allows session to be accessed through an object instead of the dictionary
- Since we are create a parent object around the Flask object, we can call it from a route meaning the session will always be valid
- Won't have errors by Pylint that the Flask object doesn't have the property
