from apps.portfolio.models.projects import Project, ProjectCategory, ProjectTechnology
from apps.users.models.users import User

USERS_MODELS = [User]
PROJECT_MODELS = [ProjectCategory, ProjectTechnology, Project]

DEBASTIANI_BASE_MODELS = USERS_MODELS + PROJECT_MODELS
