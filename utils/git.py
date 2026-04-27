import subprocess


def is_git_repo(repo_path: str) -> bool:
    result = subprocess.run(
        ["git", "rev-parse", "--git-dir"],
        cwd=repo_path,
        capture_output=True,
    )
    return result.returncode == 0


def is_dirty(repo_path: str) -> bool:
    """Return True if the repo has any uncommitted changes (tracked or untracked)."""
    result = subprocess.run(
        ["git", "status", "--porcelain"],
        check=True,
        cwd=repo_path,
        capture_output=True,
        text=True,
    )
    return bool(result.stdout.strip())

def stage_all(repo_path: str) -> None:
    subprocess.run(["git", "add", "-A"], check=True, cwd=repo_path)


def commit(repo_path: str, message: str) -> None:
    subprocess.run(["git", "commit", "-m", message], check=True, cwd=repo_path)


def push(repo_path: str) -> None:
    result = subprocess.run(
        ["git", "push"],
        cwd=repo_path,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print(
            f"    [WARNING] push failed in {repo_path}: {result.stderr.strip()}",
            file=sys.stderr,
        )
