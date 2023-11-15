from typing import Dict


def get_sorted_tasks_by_build_name(name: str, builds: Dict, tasks: Dict):
    """
    The function performs insert_sort over the list of tasks related to the given build
    name. The sort is based on the tasks dependencies.
    :param name: str, Name of the build
    :param builds: dict, contents of builds.yaml in a form of dictionary
    :param tasks: dict, contents of tasks.yaml in a form of dictionary
    :return: List of tasks sorted based on their dependencies
    """
    build_tasks = get_build_tasks(name, builds)

    for i in range(1, len(build_tasks)):
        key_item = build_tasks[i]

        j = i - 1
        preceding_tasks_dependencies = get_tasks_dependencies(build_tasks[j], tasks)

        while j >= 0 and key_item in preceding_tasks_dependencies:
            build_tasks[j + 1] = build_tasks[j]
            j -= 1
            preceding_tasks_dependencies = get_tasks_dependencies(build_tasks[j], tasks)

        build_tasks[j + 1] = key_item

    return build_tasks


def build_exists(name: str, builds: Dict):
    """
    This function checks if the build name, specified in the request exists in yaml file.
    If the name does not exist, it throws an exception to be processed by the endpoint.
    :param name: str, Name of the build
    :param builds: dict, contents of builds.yaml in a form of dictionary
    :return: Exception if build does not exist
    """
    for build in builds.get("builds"):
        if build.get("name") == name:
            return True
    raise Exception(f"No such build exists")


def get_build_tasks(name: str, builds: Dict):
    """
    This function gets the tasks related to a particular build.
    :param name: str, Name of the build
    :param builds: dict, contents of builds.yaml in a form of dictionary
    :return: List of tasks names
    """
    for build in builds.get("builds"):
        if build.get("name") == name:
            return build.get("tasks")


def get_tasks_dependencies(name: str, tasks: Dict):
    """
    This function gets the dependencies for a particular task.
    :param name: str, name of the task
    :param tasks: dict, contents of tasks.yaml in a form of dictionary
    :return: List of tasks dependencies
    """
    for build in tasks.get("tasks"):
        if build.get("name") == name:
            return build.get("dependencies")
