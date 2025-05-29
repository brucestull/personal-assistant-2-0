# Database Troubleshooting

- [Heroku 500 Error Debugging - ChatGPT - Private](https://chatgpt.com/c/6837c6dd-b264-8002-82c9-8c3ae99177c8)
- [Git log date filter - ChatGPT - Private](https://chatgpt.com/c/6838463c-8c88-8002-a6e3-38df180cbfd5)
- [Find SHA in Git log - ChatGPT - Private](https://chatgpt.com/c/6838449e-8de4-8002-8732-f00d97d2332b)
- [Makefile Migration Deletion - ChatGPT - Private](https://chatgpt.com/c/68383eb8-9114-8002-8271-30da90c310bc)
- [Open .dump file Windows - ChatGPT - Private](https://chatgpt.com/c/6837dda5-36d8-8002-b052-e01e10eaf11d)
- [Heroku 500 Error Debugging - ChatGPT - Private](https://chatgpt.com/c/6837c6dd-b264-8002-82c9-8c3ae99177c8)
- [Revert to Previous Commit - ChatGPT - Private](https://chatgpt.com/c/6837db59-9e88-8002-ae42-0e6413c053cd)
- [Get commit info - ChatGPT - Private](https://chatgpt.com/c/6838497f-de90-8002-96e8-d94abc15e285)
- [Git log Makefile history - ChatGPT - Private](https://chatgpt.com/c/68384a4d-5bec-8002-9dcb-07c6bf81574d)

## Makefile Migration Deletion

- Makefile created at commit: 23f0ee76b2cef66b0d4f64901ceef41fe2473b54
    - Short SHA: `23f0ee7`

## Git Commands

- `git rev-parse 23f0ee7`
- `git log --oneline --graph --all -30 > notes/database_issue/git_log_30`


## Python Snippets

```python
import subprocess

full_sha_from_git = subprocess.check_output(["git", "rev-parse", short_sha], text=True).strip()
print(f"Full SHA from git: {full_sha_from_git}")
```
