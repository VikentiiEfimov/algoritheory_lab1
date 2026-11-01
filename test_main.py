from main import TASKS, run_task


def test_all_tasks_registered():
    assert len(TASKS) == 11
    for i in range(11):
        assert str(i).zfill(2) in TASKS


def test_each_task_runs(capsys):
    for key in TASKS:
        run_task(key)
        captured = capsys.readouterr()
        assert f'=== {key}:' in captured.out