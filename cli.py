import argparse 
from services.manager import ProjectManager
manager = ProjectManager()
parser = argparse.ArgumentParser( description="Project Management CLI" ) 
subparsers = parser.add_subparsers( dest="command" ) 
add_user = subparsers.add_parser( "add-user" ) 
add_user.add_argument( "--name", required=True ) # list-users
subparsers.add_parser( "list-users" ) 
add_project = subparsers.add_parser( "add-project" )
add_project.add_argument( "--user", required=True ) 
add_project.add_argument( "--title", required=True ) 
subparsers.add_parser( "list-projects" ) 
add_task = subparsers.add_parser( "add-task" )
add_task.add_argument( "--project", required=True ) 
add_task.add_argument( "--title", required=True ) 
complete_task = subparsers.add_parser( "complete-task" ) 
complete_task.add_argument( "--project", required=True ) 
complete_task.add_argument( "--task", required=True ) 
user_projects = subparsers.add_parser( "user-projects" ) 
user_projects.add_argument( "--user", required=True ) 
args = parser.parse_args() 
if args.command == "add-user": 
    manager.add_user(args.name) 
elif args.command == "list-users": 
    manager.list_users() 
elif args.command == "add-project":
     manager.add_project( args.user, args.title ) 
elif args.command == "list-projects": 
    manager.list_projects() 
elif args.command == "add-task": 
    manager.add_task( args.project, args.title ) 
elif args.command == "complete-task": 
    manager.complete_task( args.project, args.task ) 
elif args.command == "user-projects": 
    manager.view_user_projects( args.user ) 
else: parser.print_help()