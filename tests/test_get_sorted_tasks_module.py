import pytest
import yaml

from src.get_sorted_tasks import build_exists, get_sorted_tasks_by_build_name


@pytest.fixture()
def read_builds_yaml():
    with open(r"builds\builds.yaml", "r") as stream:
        return yaml.safe_load(stream)


@pytest.fixture()
def read_tasks_yaml():
    with open(r"builds\tasks.yaml", "r") as stream:
        return yaml.safe_load(stream)


class TestBuildExistsFunction:
    def test_build_exists(self, read_builds_yaml):
        # Arrange
        # Act
        # Assert
        assert build_exists(name="reach_wind", builds=read_builds_yaml)

    @pytest.mark.xfail(raises=Exception)
    def test_build_does_not_exist(self, read_builds_yaml):
        build_exists(name="does_not_exist", builds=read_builds_yaml)


class TestGetSortedTasksFunction:
    def test_sorting_works_as_expected(self):

        # Arrange
        builds = {
            "builds": [
                {"name": "first", "tasks": ["1", "4"]},
                {"name": "second", "tasks": ["3", "1", "4"]},
            ]
        }
        tasks = {
            "tasks": [
                {"name": "1", "dependencies": ["2", "3", "6"]},
                {"name": "2", "dependencies": []},
                {"name": "3", "dependencies": ["6"]},
                {"name": "4", "dependencies": ["5"]},
                {"name": "5", "dependencies": []},
                {"name": "6", "dependencies": ["4"]},
            ]
        }
        name = "second"
        expected = ["3", "1", "4"]

        # Act

        result = get_sorted_tasks_by_build_name(name, builds, tasks)

        # Assert
        assert result == expected
