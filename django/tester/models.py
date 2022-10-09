from django.db import models

# Constants to parametrize field sizes
USERNAME_MAX_LENGTH = 64
SEMESTER_MAX_LENGTH = 8
VERSION_MAX_LENGTH = 8
REPO_URI_MAX_LENGTH = 256

# Model for git user
class User(models.Model):
    # Git username: CEDipEngineering
    username = models.CharField(max_length=USERNAME_MAX_LENGTH, primary_key=True)
    # First Name: Carlos
    first_name = models.CharField(max_length=32)
    # Last Name: Dip
    last_name = models.CharField(max_length=32)

    def __str__(self) -> str:
        return "{} {} ({})".format(self.first_name, self.last_name, self.username)

# Model for every school semester
class Semester(models.Model):
    # Semester identifier string: "2022.2"
    semester = models.CharField(max_length=SEMESTER_MAX_LENGTH, primary_key=True)
    # Language the class will be compiling: "Carbon"
    language_target = models.CharField(max_length=32)
    # Extension for files of said language: ".carbon"
    extension = models.CharField(max_length=16)

    def __str__(self) -> str:
        return "{} ({})".format(self.semester, self.language_target)

# Version Identifier Table
class Version(models.Model):
    # Versions: "v2.3"
    version = models.CharField(max_length=VERSION_MAX_LENGTH, primary_key=True)
    # Should use stdin: False
    use_stdin = models.BooleanField() # False means read from file

    def __str__(self) -> str:
        return "{}".format(self.version)

# Model for compiler project
class Project(models.Model):
    # Git username
    username = models.CharField(max_length=USERNAME_MAX_LENGTH)
    # Semester
    semester = models.CharField(max_length=SEMESTER_MAX_LENGTH)
    # Repository URI: https://github.com/CEDipEngineering/LogComp2022
    repo_uri = models.CharField(max_length=REPO_URI_MAX_LENGTH)
    # Language the student is using to write their compiler: Python
    language = models.CharField(max_length=32)
    # Language must be compiled flag: False
    compile = models.BooleanField()
    # CMDLINE args to run student script: python3 main.py
    run = models.CharField(max_length=1024)

    # Identify twin primary key
    class Meta:
        unique_together = (("semester", "repo_uri"),)

    def __str__(self) -> str:
        return "Project {}\nMade using {}, run with {}".format(self.repo_uri, self.language, self.run)

# Use default auto-gen primary key id
# Many tests, for every repo_uri, every version, every semester.
class TestResult(models.Model):
    # Semester
    semester = models.CharField(max_length=SEMESTER_MAX_LENGTH)
    # Repository URI
    repo_uri = models.CharField(max_length=REPO_URI_MAX_LENGTH)
    # Version
    version = models.CharField(max_length=VERSION_MAX_LENGTH)
    # Timestamp when test was made
    timestamp = models.DateField(auto_now_add=True) # Set timestamp on creation
    # Whether test was successful: "Pass"/"Fail"/"Error"?
    result = models.CharField(max_length=16)
    # Text to be put on issue sent to student Github
    issue_text = models.CharField(max_length=2048)

    def __str__(self) -> str:
        return "{}\n{}\n{}".format(self.repo_uri, self.version, self.result)

# Class to mark every Semester's schedule
class Schedule(models.Model):
    # Version
    version = models.CharField(max_length=VERSION_MAX_LENGTH)
    # Semester
    semester = models.CharField(max_length=SEMESTER_MAX_LENGTH)
    # Deadline for this version, in this semester: "v2.1", "2022.2", "30/09/2022 23:59:59"
    deadline = models.DateField()
    
    # Identify twin primary key
    class Meta:
        unique_together = (("version", "semester"),)

    def __str__(self) -> str:
        return "{} {} due {}".format(self.semester, self.version, self.deadline)