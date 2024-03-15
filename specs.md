# Password Manager
### Team 3
#### Azita Fariborz Saleh, Jake Mitton, Kent Pawson

## Contents
- __[Version Control](#version-control)__
- __[Specifications](#specifications-1)__
- __[Design](#design-1)__
	- [UML Diagrams](#uml-diagrams-1)
		- [Password Manager](#password-manager-1)
		- [Encryption](#encryption)
		- [Database](#database)
		- [User Interface](#user-interface)
- __[Documentation](#documentation-1)__
	- [Code Standards](#code-standards)
		- [Header Comments](#header-comments)
		- [Variable Formatting](#variable-formatting)
		- [Classes](#classes)
		- [Public Methods](#public-methods)
		- [Private Methods](#private-methods)
		- [Inline Commenting](#inline-commenting)
	- [Enforcement](#enforcement)
		

## Version Control
- The responsibility for the upkeep of the project reponsitory is shared between all teams members. In the case of conflict the team will vote with majority rules. 

- The respository can be found at [Github Repo](#https://github.com/kp4ws/password-manager)

- Each team member has their own branch under their name. They should work primarily on this branch, pulling from master often.

- Team members should follow this procedure:
	- Commit and push to your branch regularily
	- When ready to push to master:
                - Post notice in the discord then wait 5 minutes.
		- `git pull origin master`
		- commit and push to your local branch
                - Go to the github website and create a pull request.

## Specifications

## Design
### UML Diagrams
#### Password Manager

#### Encryption

#### Database

#### User Interface

## Documentation
### Code Standards
These standards apply only to Python3 code written for the Password Manager.

All code in this project should be written using Python's built in type-hinting, as well as Docstrings for documentation.

Doctrings are declared using triple backticks: \``` `doctring` \```

#### Header Comments
All python files should have a header file with the primary author's name and a brief description of that file's purpose.

- The formatting should match the following:

    ~~~
    ```
    Primary Author: Alice Smith
    Contributor(s): Bob Smith

    Brief description of the files purpose. If there are files that need to be in the same directory they can be mentioned here. 

	Sources:
	List source URL's here if relevant
    ```
    ~~~

#### Variable Formatting
- _Class Names:_ CapitalCamelCase
- _Class Methods:_ `snake_case`
- _Private Class Methods:_ `_snake_case` with a leading underscore
- _Class Attributes:_ `snake_case`
- _Object Instances:_ `snake_case`
- _Variables:_ `snake_case`
- For any other names not listed here ensure consistency within files.

#### Classes
- Classes should have a header doctring with the following information:
	- Summary of class purpose
	- Public Methods with brief descriptions
	- Attributes with type and brief description if necessary
	- Interface Information

- Class Example:
	~~~Python
	class ClassName:
	```
		Summary...
		METHODS:
			method_one(self, parameters): Brief Description
			...
		ATTRIBUTES:
			class_attribute: attribute type - Details if needed
			...
		INTERFACE INFO:
			Description of any necessary information for subclasses inheriting
			from this class or for classes using this class in composition.
	```
	~~~

#### Public Methods
- Public class methods should have a header doctring with the following information:
	- Brief Description of method purpose
	- Arguments with brief description if neccessary
	- Exceptions Raised
	- Unexpected Side Effects if calling this method
	- Return Type and optional brief description of value

- Default Values for arguments are optional but should be used when they improve code readability.
- In cases where Methods may return difference types (for example string or None) use the Optional special form from the Typing module.
	- Eg:
		~~~Python
		from typing import Optional

		class ClassName:

			def __init__(self):
				pass
			
			def class_method(self, arg1: type) -> Optional[return_type]:
				pass
		~~~

- Header Example:
	~~~Python
	def class_method(self, arguemnt1: type =default_value) -> return_type:
	```
		Brief Description of method purpose...
		:arg argument1: Brief Description
		:except ExceptionType: Condition for raising exception
		:effects Side Effects (optional)
		:return Type and brief description of return value
	```
	~~~

#### Private Methods
- Private class methods should have a header doctring with the following information:
	- Brief Description of method purpose
	- Arguments with brief description if neccessary
	- Exceptions Raised
	- Return Type and optional brief description of value

- In cases where Methods may return difference types (for example string or None) use the Optional special form from the Typing module.
	- Eg:
		~~~Python
		from typing import Optional

		class ClassName:

			def __init__(self):
				pass
			
			def _private_class_method(self, arg1: type) -> Optional[return_type]:
				pass
		~~~

- Header Example:
	~~~Python
	def _private_class_method(self, arguemnt1: type =default_value) -> return_type:
	```
		Brief Description of method purpose...
		:arg argument1: Brief Description
		:except ExceptionType: Condition for raising exception
		:return Type and brief description of return value
	```
	~~~
#### Inline Commenting
- When possible code should be written to be as self-documenting as possible. This means using meaningful naming. In situations where this is not possible inline comments should be used to clarrify code. 
- The standard should be code that is understandable to other teams members who did not work on that section of the program.

### Enforcement
- The code standards outlined above will be checked in code reviews by the team as follows:
	- Azita and Kent will review Jake's code
	- Azita and Jake will review Kent's code
	- Jake and Kent will review Azita's code
- These reviews will be performed withing 48 hours of major commits to the git repository. It is each members responsibility to inform the team via discord when major commits are performed following the Version Control specifications outlined in this document.
