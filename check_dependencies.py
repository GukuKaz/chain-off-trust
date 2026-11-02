from difflib import get_close_matches

approved_packages = [
    "requests",
    "flask",
    "django",
    "numpy",
    "pandas",
]

declared_packages = [
    "requests",
    "flask",
]

suspicious = False

for package in declared_packages:
    if package in approved_packages:
        print(f"OK: {package}")
        continue

    matches = get_close_matches(
        package,
        approved_packages,
        n=1,
        cutoff=0.75
    )

    if matches:
        print(
            f"WARNING: Possible typosquatting: "
            f"{package} resembles {matches[0]}"
        )
        suspicious = True
    else:
        print(f"UNKNOWN: {package}")

if suspicious:
    raise SystemExit(1)
