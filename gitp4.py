import os
from random import randint


def p4_client_path():
    return "/d/s/"


def p4_resolve_path(name):
    return os.path.normpath(p4_client_path() + name)


def strip_crlf(string):
    """ Utility function to remove EOL """
    return ''.join(string.splitlines())


def split_by_space(string):
    """ Returns a string splitted by space as a tuple """
    return tuple(string.split())


def get_commits_since(start_commit_hash, end_commit_hash="HEAD"):
    """
    It returns commit hashes of series of commits which happened between
     the two specified commits.
    """
    command = "git log %s..%s --format=%%h" % \
        (start_commit_hash, end_commit_hash)
    commits = []
    for commit_hash in os.popen(command):
        commits.append(strip_crlf(commit_hash))

    return commits[::-1]


def get_commits_name_status(commit_hash):
    """

    """
    names_status = []
    command = "git diff-tree --no-commit-id --name-status -r %s" % \
        (commit_hash)
    for ns in os.popen(command):
        names_status.append(split_by_space(ns))

    return names_status


def p4_start_changelist():
    cl = randint(5681, 7898)
    print "Starting a change list: %s " % cl
    return cl


def p4_commit_changelist(change_list):
    print "Commiting the changelist: %s" % change_list
    pass


def p4_file_modified(name, change_list):
    command = "p4 edit %s" % p4_resolve_path(name)
    print "Checking out the file %s and copying it over" % name
    print command
    os.popen(command)


def p4_file_added(name, change_list):
    print "Adding the file %s and copying it over" % name
    pass


def p4_file_deleted(name, change_list):
    print "Removing the file %s and copying it over" % name
    pass


def process_by_status(status, name, cl):
    if "M" == status.upper():
        p4_file_modified(name, cl)
    elif "A" == status.upper():
        p4_file_added(name, cl)
    elif "D" == status.upper():
        p4_file_deleted(name, cl)
    else:
        raise Exception("Invalid Status: %s:%s" % (status, name))


def process_commits(start_commit_hash):
    for commit in get_commits_since(start_commit_hash):
        cl = p4_start_changelist()
        for (status, name) in get_commits_name_status(commit):
            process_by_status(status, name, cl)
            print "Had the file: %s , %s" % (status, name)
        p4_commit_changelist(cl)

# print get_commits_since("0817e51")
# print get_commits_name_status("0817e51")
# print get_commits_since("68b8a52")

process_commits("0817e51")