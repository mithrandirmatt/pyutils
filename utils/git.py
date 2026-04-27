import subprocess
import sys


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


def is_ahead(repo_path: str) -> bool:
    """Return True if local branch has commits not yet pushed to the remote."""
    result = subprocess.run(
        ["git", "rev-list", "--count", "@{u}..HEAD"],
        cwd=repo_path,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        # No upstream configured -- nothing to push
        return False
    return int(result.stdout.strip() or 0) > 0


def get_remote_url(repo_path: str, remote: str = "origin") -> str:
    result = subprocess.run(
        ["git", "remote", "get-url", remote],
        cwd=repo_path,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip() if result.returncode == 0 else ""

def stage_all(repo_path: str) -> None:
    subprocess.run(["git", "add", "-A"], check=True, cwd=repo_path)


def commit(repo_path: str, message: str) -> None:
    subprocess.run(["git", "commit", "-m", message], check=True, cwd=repo_path)


def push(repo_path: str) -> None:
    url = get_remote_url(repo_path)
    if url.startswith("https://"):
        print(
            f"    [WARNING] skipping push in {repo_path}: remote is HTTPS ({url}).\n"
            f"    Fix with: git remote set-url origin git@github.com:<user>/<repo>.git",
            file=sys.stderr,
        )
        return
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
