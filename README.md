# CodeChecker
App to compare, analyze and test C++ programs.
<p align="center">
  <img src=https://github.com/PiotrLezanski/CodeChecker/assets/45331390/f2fb9e90-a42c-4bd2-9f0f-1e5ffab528d5>
</p>

## Functional description

CodeChecker is a powerful application designed to assess the quality and correctness of user’s code. It performs comprehensive code analysis and identifies various types of issues including memory leaks, wrong test outputs, compilation or runtime errors. It can additionally compare two codes in terms of issues or semantic differences.

On the welcome window the user can read brief description of all functionalities and he is given the possibility to change appearance settings, such as size or theme. Additionally the welcome window allows user to upload one or two files with code, which then are stored in the application. Sidebar allows user to switch between different views and try other functionalities.

The views and functionalities are as follows:

- **GetOutput** – app will run users code with provided input and return the output as a preview and with the possibility to download.
- **CheckEfficiency** – user can input his code and a testcase. Additionally, he can choose one or more options of parameters that the program will check, which are: runtime, memory leaks and logs of compilation in general.
- **CompareCode** – given two codes from the user, the program executes both and gets their efficiency parameters. Differences are displayed as an output.
- **TestPass** – the user passes testcases as an input. The application executes the program on these testcases.
- **CodeDifference** – given two codes from the user, the program will check for semantic differences and will return every place, where the codes are different.

CodeChecker provides user-friendly interface, allowing developer to easily configure the analysis parameters and customize the rule sets according to their project requirements.

## Unit testing

CodeChecker uses unit testing with high code coverage to ensure the reliability and robustness of the application. The unit tests cover all the main functionalities and scenarios of the app, such as input validation, output generation, code comparison, efficiency measurement and error handling.

## Used design patterns

CodeChecker applies several design patterns to achieve a modular, maintainable and extensible code base. The main design patterns used are:
- **Model-View-Controller**  – this pattern separates the application into three components: model, view and controller. The model represents the data and business logic of the app, the view displays the data to the user and the controller handles the user input and updates the model and view accordingly. CodeChecker uses this pattern for each functionality or view of the app, such as get output, check efficiency or compare code.
- **Singleton** – this pattern ensures that only one instance of a class is created and provides a global access point to it. CodeChecker uses this pattern for classes that manage resources or settings that are shared across the app, such as file manager.
- **Observer**  – this pattern defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically. CodeChecker uses this pattern for classes that handle user interface events or communication between different views, such as sidebar controller, welcome window controller or output window controller.
- **Factory** – this pattern defines an interface for creating an object of one class, but lets subclasses decide how to create it. CodeChecker uses this pattern for classes that create different types of objects based on some criteria or configuration, such as code analyzer factory, code comparator factory or output generator factory.
