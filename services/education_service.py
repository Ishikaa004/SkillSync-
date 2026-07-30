import re


def extract_required_degree(job_description):

    degrees = [
        "B.Tech",
        "B.E",
        "Bachelor",
        "M.Tech",
        "M.E",
        "MCA",
        "BCA",
        "B.Sc",
        "M.Sc"
    ]

    for degree in degrees:

        pattern = re.escape(degree)

        if re.search(pattern, job_description, re.IGNORECASE):
            return degree

    return "Not Specified"

import re


def extract_candidate_degree(resume_text):

    degrees = [
        "B.Tech",
        "B.E",
        "Bachelor",
        "M.Tech",
        "M.E",
        "MCA",
        "BCA",
        "B.Sc",
        "M.Sc"
    ]

    for degree in degrees:

        pattern = re.escape(degree)

        if re.search(pattern, resume_text, re.IGNORECASE):
            return degree

    return "Not Found"

def compare_degree(required_degree, candidate_degree):

    if required_degree == "Not Specified":

        return {
            "required_degree": required_degree,
            "candidate_degree": candidate_degree,
            "degree_match": None
        }

    return {
        "required_degree": required_degree,
        "candidate_degree": candidate_degree,
        "degree_match": required_degree.lower() == candidate_degree.lower()
    }



    

def extract_required_branch(job_description):

    branches = [
        "Computer Science Engineering",
        "Computer Science",
        "Information Technology",
        "IT",
        "Electronics and Communication",
        "ECE",
        "Electrical Engineering",
        "Mechanical Engineering",
        "Civil Engineering"
    ]

    for branch in branches:

        pattern = re.escape(branch)

        if re.search(pattern, job_description, re.IGNORECASE):
            return branch

def extract_candidate_branch(resume_text):

    branches = [
        "Computer Science Engineering",
        "Computer Science",
        "Information Technology",
        "IT",
        "Electronics and Communication",
        "ECE",
        "Electrical Engineering",
        "Mechanical Engineering",
        "Civil Engineering"
    ]

    for branch in branches:

        pattern = re.escape(branch)

        if re.search(pattern, resume_text, re.IGNORECASE):
            return branch

    return "Not Found"

def compare_branch(required_branch, candidate_branch):

    if (
        required_branch.lower() in candidate_branch.lower()
        or
        candidate_branch.lower() in required_branch.lower()
    ):
        match = True
    else:
        match = False

    return {
        "required_branch": required_branch,
        "candidate_branch": candidate_branch,
        "branch_match": match
    }
