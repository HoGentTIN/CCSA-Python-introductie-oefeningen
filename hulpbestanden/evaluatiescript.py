# Dependencies (pip install...):
#   pytest, pytest-json-report, pytest-timeout, filelock

import os
import sys
import subprocess
import json
import csv
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor, as_completed
from filelock import FileLock
from datetime import datetime

# -------------------- SETTINGS ----------------------
# Zelfevaluatie van de student?
ZELFEVALUATIE = True  # Zet op True om als student zelf je score te berekenen en in de CSV te zetten.
# Debugging output nodig?
VERBOSE = True       # Zet op True voor meer gedetailleerde uitvoer (nuttig bij zelfevaluatie).
# Geef het pad naar de map waaronder zich de student repositories bevinden (wordt enkel gebruikt indien geen zelfevaluatie).
STUDENTS_BASE = Path(r"C:\Users\slam977\OneDrive - Hogeschool Gent\Documenten\CCSA\inzendingen-github-classroom\ccsa-python-oefeningen-v0-submissions")
# Geef het pad naar de map met de referentietests (wordt enkel gebruikt indien geen zelfevaluatie).
REFERENCE_BASE = Path(r"C:\GitHub\hogenttin-classroom-zandbakccsa-ccsa-python-oefeningen-v0-CCSA-Python-oefeningen")
PYTEST_TIMEOUT = 1   # per test; wordt enkel gebruikt voor tests waarvoor geen specifieke timeout gedefinieerd is 
#(wanneer wel een specifieke timeout gedefinieerd is met @pytest.mark.timeout bij de test, wordt die gebruikt).
# Geef het aantal parallelle werkers aan (standaard het aantal CPU-kernen, max 8).
MAX_WORKERS = min(os.cpu_count() or 4, 8)

# ------------ UTILITY: TEST DISCOVERY ---------------
def discover_reference_tests(base_dir: Path):
    """
    Returns a list of (relative_test_path, exercise_name) tuples for all test_*.py files
    in 'reeks_*'/tests subfolders, sorted for reproducibility.
    """
    test_files = []
    for reeks_dir in sorted(base_dir.glob("reeks_*")):
        tests_dir = reeks_dir / "tests"
        if tests_dir.exists():
            for test_f in sorted(tests_dir.glob("test_*.py")):
                ex_name = test_f.stem.replace("test_", "")
                test_files.append((test_f.relative_to(base_dir), ex_name))
    return test_files

# -------------- READ STUDENT INFO ----------------------

def read_student_info(student_dir):
    """
    Reads student number, first name, last name from studentengegevens.txt.
    Returns (nummer, voornaam, familienaam).
    If missing, returns ("", "", "").
    Issues warning if student number is not all digits.
    """
    info_file = student_dir / "hulpbestanden" / "studentengegevens.txt"
    nummer = voornaam = familienaam = ""
    if not info_file.exists():
        print(f"⚠️  WARNING: No studentengegevens.txt found in {student_dir.name}!")
        return nummer, voornaam, familienaam
    try:
        with open(info_file, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line.startswith("Studentennummer:"):
                    nummer = line.split(":", 1)[1].strip()
                elif line.startswith("Voornaam:"):
                    voornaam = line.split(":", 1)[1].strip()
                elif line.startswith("Familienaam:"):
                    familienaam = line.split(":", 1)[1].strip()
        if not nummer.isdigit():
            print(f"⚠️  WARNING: Ongeldig studentnummer ({nummer}) in {student_dir.name}!")
        return nummer, voornaam, familienaam
    except Exception as e:
        print(f"⚠️  WARNING: Fout bij lezen van studentengegevens.txt in {student_dir.name}: {e}")
        return "", "", ""


# -------------- TEST EXECUTION ----------------------
def run_pytest_on_student_exercise(student_repo: Path, test_relpath: Path, ex_name: str, base_tests_dir: Path):
    """
    Runs pytest for a single test file with the student's repo as PYTHONPATH and CWD (current working directory).
    Returns: dict with counts (passed, failed, error, total), binary score, status.
    """
    test_file = base_tests_dir / test_relpath
    env = os.environ.copy() # clone environment variables from current process
    env["PYTHONPATH"] = str(student_repo) # in this subprocess environment, set PYTHONPATH to student's repo (for imports)

    report_file = test_file.parent / f"__tmp_report_{os.getpid()}_{ex_name}.json"
    cmd = [
        sys.executable, "-m", "pytest",
        str(test_file),
        "--json-report", f"--json-report-file={report_file}",
        "--tb=short", "-q",
        "--timeout", str(PYTEST_TIMEOUT), "--timeout-method=thread"
    ]

    debug_info = f"[{student_repo.name} | {ex_name}]"
    passed = failed = error = total = 0
    try:
        result = subprocess.run(
            cmd, env=env, cwd=student_repo, #cwd set to student repo so imports in test files import code under test from there
            capture_output=True, text=True,
            timeout=60
        )
        if VERBOSE:
            print(result.stdout)
        if not report_file.exists() or report_file.stat().st_size == 0:
            if "Timeout" in result.stdout or "Timeout" in result.stderr:
                msg = f"{debug_info} ❌ ERROR: No JSON report due to TIMEOUT."
            else:
                msg = f"{debug_info} ❌ ERROR: No JSON report."
            if VERBOSE:
                print(f"{msg}\n---- pytest stdout ----\n{result.stdout}\n---- pytest stderr ----\n{result.stderr}")
            return {"ex": ex_name, "passed": 0, "failed": 0, "error": 1, "total": 0, "score": 0, "status": "run_error"}
        with open(report_file, encoding="utf-8") as f:
            jsonrep = json.load(f)
        for t in jsonrep.get("tests", []):
            outcome = t.get("outcome", "error")
            total += 1
            if outcome == "passed":
                passed += 1
            elif outcome == "failed":
                failed += 1
            elif outcome == "error":
                error += 1
        status = "OK"
        if total == 0:
            if VERBOSE:
                print(f"{debug_info} ⚠️  WARNING: No tests collected? Check ref test file naming + do imported methods exist?")
                # kan gebeuren als de tests niet gevonden zijn, maar dit kan ook bv. omdat de nodige 
                # methodes niet gedefinieerd zijn (oefening niet gemaakt), dan faalt import bovenaan testfile
            status = "no_tests"
        elif VERBOSE:
            print(f"{debug_info} Pass:{passed} Fail:{failed} Err:{error} Total:{total}")
        score = int(total > 0 and passed == total) # score voor deze oefening: 1 als alle tests geslaagd zijn, anders 0
        return {"ex": ex_name, "passed": passed, "failed": failed, "error": error, "total": total, "score": score, "status": status}
    except Exception as e:
        print(f"{debug_info} ❌ ERROR: {e}")
        return {"ex": ex_name, "passed": 0, "failed": 0, "error": 1, "total": 0, "score": 0, "status": "run_exception"}
    finally:
        try:
            report_file.unlink() # delete temporary report file (if it exists)
        except Exception:
            pass

# -------------- CSV MANAGEMENT -----------------------
def write_result_row(csv_path: Path, lock_path: Path, fieldnames, row):
    """Safely append a row to CSV in a multi-process environment."""
    with FileLock(str(lock_path)):
        file_exists = csv_path.exists()
        with open(csv_path, mode="a", encoding="utf-8", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            if not file_exists:
                writer.writeheader()
            writer.writerow(row)

# ------------ PER-STUDENT GRADE PIPELINE -------------
def grade_one_student(student_dir: Path, test_files, reference_dir: Path, csv_path: Path, lock_path: Path, fieldnames):
    nummer, voornaam, familienaam = read_student_info(student_dir)
    student_results = []
    for test_relpath, ex_name in test_files:
        result = run_pytest_on_student_exercise(student_dir, test_relpath, ex_name, reference_dir)
        student_results.append(result)
    # Compose and write CSV row...
    totalscore = sum(r["score"] for r in student_results)
    maxtotal = len(test_files)
    crashed_count = sum(1 for r in student_results if r["status"] in ("run_error", "run_exception"))
    row = { # samenvatting van de studentengegevens en resultaten in de eerste zeven kolommen
        "naam repository": student_dir.name,
        "studentennummer": nummer,
        "voornaam": voornaam,
        "familienaam": familienaam,
        "totaalscore": totalscore,
        "max. totaalscore": maxtotal,
        "gecrashte runs (# oefn.)": crashed_count
    }
    for res in student_results: # resultaten per oefening toevoegen in verdere kolommen
        ename = res["ex"]
        row[f"passed {ename}"] = res["passed"]
        row[f"failed {ename}"] = res["failed"]
        row[f"error {ename}"] = res["error"]
        row[f"total {ename}"] = res["total"]
        row[f"score {ename}"] = res["score"]
    write_result_row(csv_path, lock_path, fieldnames, row)
    return { # samenvatting voor de console output
    "totaalscore": totalscore,
    "max. totaalscore": maxtotal,
    }


# --------------------- MAIN --------------------------
def main():
    timestamp = datetime.now().strftime("%Y-%m-%d_%H%M")
    out_csv = Path(f"grading_output_{timestamp}.csv")
    lock_file = Path(f"grading_output_{timestamp}.csv.lock")

    if ZELFEVALUATIE:
        STUDENTS_BASE = REFERENCE_BASE = Path(__file__).resolve().parent.parent

    test_files = discover_reference_tests(REFERENCE_BASE)
    if not test_files:
        print("❌ FATAL ERROR: No tests discovered! Is the reference folder path correct?")
        return

    fieldnames = [
        "naam repository", "studentennummer", "voornaam", "familienaam",
        "totaalscore", "max. totaalscore", "gecrashte runs (# oefn.)"
    ]
    for _, ex_name in test_files: # hier enkel naam van de oefening nodig (ex_name)
        fieldnames += [f"passed {ex_name}", f"failed {ex_name}", f"error {ex_name}", f"total {ex_name}", f"score {ex_name}"]

    out_csv.unlink(missing_ok=True) # remove old output file if it exists
    lock_file.unlink(missing_ok=True) # remove old lock file if it exists

    if not ZELFEVALUATIE:
        student_dirs = [p for p in STUDENTS_BASE.iterdir() if p.is_dir()]
    else:
        student_dirs = [STUDENTS_BASE]

    if not student_dirs:
        print("No student dirs found!")
        return

    print("-" * 62)
    print(f"Grading {len(student_dirs)} students on {len(test_files)} exercises in parallel ({MAX_WORKERS} workers)...")
    print("-" * 62)

    with ProcessPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = []
        for i, student_dir in enumerate(student_dirs, 1):
            if not VERBOSE:
                print(f"Grading student {i}/{len(student_dirs)}: {student_dir.name}")
            f = executor.submit(
                grade_one_student,
                student_dir, test_files, REFERENCE_BASE,
                out_csv, lock_file, fieldnames
            )
            futures.append((f, student_dir.name, i))
        finished = 0
        for fut, name, i in futures:
            result = fut.result()
            print(f"Finished grading student {i}/{len(student_dirs)}: {name} (overall score: {result['totaalscore']}/{result['max. totaalscore']})")

    print("\nDONE. Results in", out_csv)


if __name__ == "__main__":
    main()