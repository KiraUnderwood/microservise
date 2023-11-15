from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_get_tasks_for_existing_build():
    response = client.post(
        "/get_tasks/",
        json={"name": "reach_wind"},
    )
    assert response.status_code == 200
    assert response.json() == {
        "sorted_tasks": [
            "bring_maroon_golems",
            "bring_silver_orcs",
            "build_blue_gorgons",
            "coloring_aqua_golems",
            "coloring_fuchsia_humans",
            "coloring_green_witches",
            "coloring_purple_fairies",
            "coloring_yellow_leprechauns",
            "create_purple_witches",
            "create_silver_gnomes",
            "enable_aqua_goblins",
            "map_gray_leprechauns",
            "map_purple_leprechauns",
            "map_yellow_gnomes",
            "read_fuchsia_orcs",
            "read_gray_humans",
            "read_yellow_gorgons",
            "train_green_centaurs",
            "train_lime_orcs",
            "train_maroon_leprechauns",
            "upgrade_olive_fairies",
            "write_purple_cyclops",
            "write_white_goblins",
        ]
    }


def test_get_tasks_for_non_existing_build():
    response = client.post(
        "/get_tasks/",
        json={"name": "non_existing"},
    )
    assert response.status_code == 404
    assert response.json() == {"detail": "No such build exists"}
